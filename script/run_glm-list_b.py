import sys
import os
import json
import time
import re
import copy

import pandas as pd
from tqdm import tqdm
import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import ast
from openai import OpenAI
import requests

os.environ["TOKENIZERS_PARALLELISM"] = "false"

script_dir = os.path.dirname(os.path.abspath(__file__))
cwd = os.path.dirname(script_dir)

os.chdir(cwd)
sys.path.append('tools')

import chat
import parse_data
import sql

question_path = os.path.join(cwd, 'answer_tmp' + os.sep + 'glm_4_plus-market_classifier-v1.0.0.json')

questions = parse_data.read_json(question_path)
# sort the questions by tid
questions = sorted(questions, key=lambda x: int(x['tid'].split('-')[-1]))


##
# api setting
###
llm_api = '1430f2573b273bebdf21c8d68c91d3d6.71llzxJFa9x2Z6ex'
sql_api = "d989596b9e61478bb368eb14e536db69"


client = OpenAI(api_key= llm_api, base_url="https://open.bigmodel.cn/api/paas/v4/")

def fetch_data(data: dict):
    url = "https://comm.chatglm.cn/finglm2/api/query"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {sql_api}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

#######
### Embedding
#####

emb_model = SentenceTransformer('moka-ai/m3e-base')

# 读取 JSON 文件并转换回字典
def load_json_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 递归解析嵌入数据
    def convert_embeddings(obj):
        if isinstance(obj, list) and all(isinstance(x, (int, float)) for x in obj):
            return np.array(obj)
        if isinstance(obj, dict):
            return {key: convert_embeddings(value) for key, value in obj.items()}
        if isinstance(obj, list):
            return [convert_embeddings(item) for item in obj]
        return obj
    
    return convert_embeddings(data)

# 加载 JSON 文件到字典
print("=====Load Embedding=====")
columns_info = load_json_to_dict('data/database-table/columns_emb.json')
print("=====Load Embedding Completed=====")

##
# 计算 embedding
##

def cosine_similarity(vec_a, vec_b):
    return np.dot(vec_a, vec_b) / (np.linalg.norm(vec_a) * np.linalg.norm(vec_b))

def find_top_similar_columns(word, columns_info, emb_model, top_k=20):
    """
    Find the top `top_k` most similar columns to the given word based on cosine similarity.

    Args:
    - word (str): The query word.
    - columns_info (list): list containing column details with embeddings.
    - emb_model (SentenceTransformer): The embedding model.
    - top_k (int): Number of top similar columns to return.

    Returns:
    - List of tuples (column_name, similarity_score, column_description)
    """
    # Encode the input word
    word_embedding = emb_model.encode(word)

    table_similarities = []
    column_similarities = []
    scores1 = []
    scores2 = []

    for col_info in columns_info:
        # Get column name and description
        column_name = col_info['column_name']
        column_description = col_info.get('column_description', '')
        db_name = col_info.get('db_name', '')
        table_name_en = col_info.get('table_name_en', '')
        table_name_zh = col_info.get('table_name_zh', '')


        # Get embeddings (ensure they exist)
        table_name_zh_emb = col_info.get('table_name_zh_emb')
        table_desc_emb = col_info.get('table_desc_emb')
        col_emb = col_info.get('col_emb')
        all_emb = col_info.get('all_emb')

        table_name_similarity = cosine_similarity(word_embedding, table_name_zh_emb) if table_name_zh_emb is not None else 0
        table_desc_similarity = cosine_similarity(word_embedding, table_desc_emb) if table_desc_emb is not None else 0
        col_similarity = cosine_similarity(word_embedding, col_emb) if col_emb is not None else 0
        all_similarity = cosine_similarity(word_embedding, all_emb) if all_emb is not None else 0

        # 四种similarity的计算方法

        table_similarity = 0.5 * table_name_similarity + 0.5 * table_desc_similarity 
        if table_name_en not in [x[2] for x in table_similarities]:
            table_similarities.append((table_similarity, db_name, table_name_en, table_name_zh))

        column_similarities.append((col_similarity, db_name, table_name_en, column_name, column_description))

        score1 = all_similarity
        scores1.append((score1, db_name, table_name_en, column_name, column_description))

        score2 = 0.3 * table_similarity + 0.7 * col_similarity
        scores2.append((score2, db_name, table_name_en, column_name, column_description))


    # Sort by similarity score
    table_similarities = sorted(table_similarities, key=lambda x: x[0], reverse=True)
    column_similarities = sorted(column_similarities, key=lambda x: x[0], reverse=True)
    scores1 = sorted(scores1, key=lambda x: x[0], reverse=True)
    scores2 = sorted(scores2, key=lambda x: x[0], reverse=True)


    # Return top `top_k` results
    return table_similarities[:top_k], column_similarities[:top_k], scores1[:top_k], scores2[:top_k]

def rag_find_tables(query: str) -> str:
    """
    input: query
    output: md format table schema
    """

    available_tables = set()
    rag_results = find_top_similar_columns(query, columns_info, emb_model, top_k=10)
    for i in [0, 1, 2, 3]:
        for result in rag_results[i]:
            # get database.table
            available_tables.add(f'{result[1]}.{result[2]}')

    # read database table
    table_fpath = os.path.join(cwd, 'data', 'database-table', 'database_v4.md')
    df = pd.read_table(table_fpath, sep="|", skiprows=[1], engine='python')
    df = df.iloc[:, 1:-1]  # 去掉多余的边界列
    df = df.fillna('')
    df.columns = [col.strip() for col in df.columns]  # 去掉列名的空格

    # keep the constant databases
    new_df = df[:6].copy()

    # add the available_tables
    for index, row in df.iterrows():
        rname = row['表英文']
        rname= re.sub('\s', '', rname)
        if rname in available_tables:
            new_df = pd.concat([new_df, pd.DataFrame([row])], ignore_index=True)

    # 转换成 Markdown 格式
    markdown_table = new_df.to_markdown(index=False)

    # 去除多余的空格和横线
    markdown_table = '\n'.join(re.sub('  ', '', line) for line in markdown_table.splitlines() if line.strip())
    # 去除多余的 --
    markdown_table = re.sub('\|:-+\|:-+\|:-+\|:-+\|:-+\|', '|---|---|---|---|---|', markdown_table)
    # remove nan
    # markdown_table = re.sub('nan', '', markdown_table)

    return markdown_table

###
# load prompt
###

prompt_dir = os.path.join(cwd, 'prompt')

table_finder_fname = 'table_finder-stage_1-v4.0.0.md'
rewriter_fname = 'rewrite_query-v1.0.0.md'
sql_1_fname = f'sql_generator-stage_1-v2.0.0.md'
sql_2_fname = f'sql_generator-stage_2-v1.0.0.md'
ans_fname = f'answer_generator-v2.0.0.md'

with open(os.path.join(prompt_dir, table_finder_fname), 'r') as f:
    table_finder_prompt_template = ''.join(f.readlines())

with open(os.path.join(prompt_dir, rewriter_fname), 'r') as f:
    rewriter_prompt_template = ''.join(f.readlines())

with open(os.path.join(prompt_dir, sql_1_fname), 'r') as f:
    sql_1_prompt_template = ''.join(f.readlines())

with open(os.path.join(prompt_dir, sql_2_fname), 'r') as f:
    sql_2_prompt_template = ''.join(f.readlines())

with open(os.path.join(prompt_dir, ans_fname), 'r') as f:
    ans_prompt_template = ''.join(f.readlines())

# build sql prompt 

def make_prompt_table_finder(query: str, market: str, ner: dict) -> str:
    """
    ner_res: content from the stage_1
    """

    def parse_database_and_table(query: str) -> dict:
        """
        Parse the given SQL query to return the database and table names in a dictionary.
        
        Args:
        - query (str): The SQL query to parse.
        
        Returns:
        - dict: A dictionary with 'database' and 'table' keys.
        """

        pattern = r'FROM\s+([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)'
        match = re.search(pattern, query, re.IGNORECASE)
        
        if match:
            database = match.group(1)
            table = match.group(2)
            return {'database': database, 'table': table}
        
        return {}

    prompt = table_finder_prompt_template

    prompt = prompt + query


    # replace table schema
    tables = rag_find_tables(query)
    reg_p = re.compile('<Database-Table Schema>')
    prompt = re.sub(reg_p, tables, prompt)

    # ner_result is None
    if not ner['result']:
        return prompt

    ner_content = {}
    # assume there is only one NER result
    ner_content.update(ner['result'][0])
    ner_content['market'] = market

    sql_res = ner['sql']

    cnt = 0
    for k, v in sql_res.items():
        for j in v:
            if not j['result']:
                continue
            else:
                cnt += 1

    if cnt == 1:
        for k, v in sql_res.items():
            for j in v:
                if not j['result']:
                    continue
            
                sql_query = j['query']
                # select database and table via market
                # add database and table
                # tmp_table = parse_database_and_table(sql_query)
                ner_content.update(parse_database_and_table(sql_query))
                # # get market
                # if market in tmp_table['table']: # HK or US
                ner_content['entity_information'] = j['result']
                # else:
    elif cnt == 2:
        for k, v in sql_res.items():
            for j in v:
                if not j['result']:
                    continue
                
                sql_query = j['query']
                tmp_table = parse_database_and_table(sql_query)
                if market in tmp_table['table']: # HK or US
                    ner_content['entity_information'] = j['result']
                    ner_content.update(tmp_table)
                if market == 'cn' and market not in tmp_table['table']:
                    ner_content['entity_information'] = j['result']
                    ner_content.update(tmp_table)      
    else:
        pass              

    # add NER result

    ner_str = f"\n\n### **Name Entity Recognition Result**\n```json\n{json.dumps(ner_content, ensure_ascii=False,indent=2)}\n```"

    prompt += ner_str
    
    return prompt

def make_prompt_sql(query: str, ner: dict, table_finder: dict) -> str:
    
    prompt = sql_1_prompt_template

    # Database-Table Pair(s)
    table_finder_res = table_finder['data_source']
    tables = [i['table'] for i in table_finder_res]
    try:
        del table_finder_res['question']
    except:
        pass
    table_finder_res = json.dumps(table_finder_res, ensure_ascii=False, indent=2)
    reg_p = re.compile('<Database and Table>')
    prompt = re.sub(reg_p, table_finder_res, prompt)
    
    # Table Schema(s)
    table_schema = ''
    for table in tables:
        table_fname = f'{table}-with_instance.md'
        table_dir = os.path.join(cwd, 'data' + os.sep + 'table-column')
        table_fpath = os.path.join(table_dir, table_fname)
        try:
            with open(table_fpath,'r') as f:
                table_schema += ''.join(f.readlines())
                table_schema += '\n\n'
        except:
            print(f"Can't find {table_fname}")
            table_schema = ''
    reg_p = re.compile('<Table-Column Schema>')
    prompt = re.sub(reg_p, table_schema, prompt)

    # NER Result
    if ner['result']:
        ner_res = [i for i in ner['sql'].values() if i][0]
        ner_res = [i['result'] for i in ner_res if i['result']][0][0]
        ner_res = json.dumps(ner_res, ensure_ascii=False, indent=2)
        reg_p = re.compile('<NER Result>')
        prompt = re.sub(reg_p, ner_res, prompt)
    else:
        reg_p = re.compile('\n<NER Result>\n')
        prompt = re.sub(reg_p, '', prompt)
        reg_p = re.compile('\n## NER Result\n')
        prompt = re.sub(reg_p, '', prompt)

    # replace query
    reg_p = re.compile('<Current Query>')
    prompt = re.sub(reg_p, query, prompt)

    # add shots
    prompt += sql_shots(query)

    return prompt

def make_prompt_rewrite(query: str, history: list):

    prompt = rewriter_prompt_template

    # replace query
    reg_p = re.compile('<Current Query>')
    prompt = re.sub(reg_p, query, prompt)

    # replace History
    reg_p = re.compile('<Chat History>')
    history = json.dumps(history, ensure_ascii=False, indent=2)
    prompt = re.sub(reg_p, history, prompt)

    return prompt

def make_prompt_answer(query: str, ner: dict, sql_res: list) -> str:

    prompt = ans_prompt_template

    # SQL Result
    sql_res = json.dumps(sql_res, ensure_ascii=False, indent=2)
    reg_p = re.compile('<SQL Result>')
    prompt = re.sub(reg_p, sql_res, prompt)

    # NER Result
    if ner['result']:
        ner_res = [i for i in ner['sql'].values() if i][0]
        ner_res = [i['result'] for i in ner_res if i['result']][0][0]
        ner_res = json.dumps(ner_res, ensure_ascii=False, indent=2)
        reg_p = re.compile('<NER Result>')
        prompt = re.sub(reg_p, ner_res, prompt)
    else:
        reg_p = re.compile('\n<NER Result>\n')
        prompt = re.sub(reg_p, '', prompt)
        reg_p = re.compile('\n## NER Result\n')
        prompt = re.sub(reg_p, '', prompt)

    # replace query
    reg_p = re.compile('<Current Query>')
    prompt = re.sub(reg_p, query, prompt)

    return prompt


def sql_shots(query: str) -> str:

    way_string_2 = "## **查询参考示例**\n"
    
    if "近一个月最高价" in query:
        way_string_2 += "查询近一个月最高价,你写的sql语句可以优先考虑表中已有字段HighPriceRM  近一月最高价(元)  "
    if "近一个月最低价" in query:
        way_string_2 += "查询近一月最低价(元),你写的sql语句直接调用已有字段LowPriceRM"
    if "行业" in query and ('多少只' in query or '几个' in query or '多少个' in query):
        way_string_2 += """查询某行业某年数量 示例sql语句:SELECT count(*) as 风电零部件_2021
            FROM AStockIndustryDB.LC_ExgIndustry
            where ThirdIndustryName like '%风电零部件%' and year(InfoPublDate)=2021 and IfPerformed = 1;"""
    if '年度报告' in query:
        way_string_2 += """特别重要一定注意，查询最新更新XXXX年年度报告，参考sql条件语句，
                            WHERE date(EndDate) = 'XXXX-12-31'"""

    if '新高' in query:
        way_string_2 += """新高 要用AStockMarketQuotesDB.CS_StockPatterns现有字段
        
        查询今天是2021年01月01日，创近半年新高的股票有几只示。示例sql语句:SELECT count(*)  FROM AStockMarketQuotesDB.CS_StockPatterns
                where  IfHighestHPriceRMSix=1 and date(TradingDay)='2021-01-01;
                判断某日 YY-MM-DD  InnerCode XXXXXX 是否创近一周的新高，查询结果1代表是,IfHighestHPriceRW字段可以根据情况灵活调整  SELECT   InnerCode,TradingDay,IfHighestHPriceRW  FROM AStockMarketQuotesDB.CS_StockPatterns
where  date(TradingDay)='2021-12-20' and InnerCode = '311490'
                
                """
    if '成交额' in query and '平均' in query:
        way_string_2 += """查询这家公司5日内平均成交额是多少。示例sql语句:SELECT count(*)  FROM AStockMarketQuotesDB.CS_StockPatterns
                where  IfHighestHPriceRMSix=1 and date(TradingDay)='2021-01-01"""
    if '半年度报告' in query:
        way_string_2 += """查询XXXX年半年度报告的条件为：year(EndDate) = XXXX and InfoSource='半年度报告'"""

    if '新高' in query:
        way_string_2 += """查询今天是2021年01月01日，创近半年新高的股票有几只示。示例sql语句:SELECT count(*)  FROM AStockMarketQuotesDB.CS_StockPatterns
                where  IfHighestHPriceRMSix=1 and date(TradingDay)='2021-01-01"""
    if '成交额' in query and '平均' in query:
        way_string_2 += """查询这家公司5日内平均成交额是多少。示例sql语句:SELECT count(*)  FROM AStockMarketQuotesDB.CS_StockPatterns
                where  IfHighestHPriceRMSix=1 and date(TradingDay)='2021-01-01"""
        
    if '基金' in query:
        way_string_2 += """如果需要返回基金名，参考以下 sql 语句访问特定的基金名。 SELECT DisclName FROM PublicFundDB.MF_FundProdName
                where  InnerCode=XXX"""

    return way_string_2

###
# set agent
###

def table_finder_agent(query: str, market: str, ner: dict):

    print("====TABLE FINDER AGENT UP====")
    retry_delay = 1
    max_retries = 6
    llm_query = make_prompt_table_finder(query, market, ner)

    history = [{"role": "user", "content": llm_query}]

    retries = 0

    while retries < max_retries:
        should_retry = False
        start_time = time.time()

        # API 调用（增加重试机制）
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    # model="deepseek-chat",
                    model='glm-4-plus',
                    messages=history,
                    stream=False,
                    top_p=0.7,
                    temperature=0.9
                )
                break  # 如果成功，跳出重试循环
            except Exception as e:
                print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    raise  # 如果达到最大重试次数，抛出异常
                time.sleep(retry_delay)  # 等待一段时间后重试

        end_time = time.time()    

        response = json.loads(response.to_json())
        raw_content = response['choices'][0]['message']['content']
        usage = response['usage']
        execution_time = end_time - start_time

        # 第一个 try-except：处理 JSON 解析
        try:
            content = json.loads(raw_content.strip('`json'))
        except Exception as e:
            print(f"Error processing JSON {query} (attempt {retries + 1}/{max_retries}): {e}")
            should_retry = True  # 标记需要重试

        # 如果 JSON 解析成功，继续执行后续逻辑
        if not should_retry:
            print("====TABLE FINDER AGENT COMPLETED====")
            history.append({'role': 'assistant', 'content': content})
            return history
        else:
            retries += 1
            if retries == max_retries:
                print(f"Failed to process question ==={query}=== after {max_retries} attempts.")
                print("====TABLE FINDER AGENT DOWN====")
                return []


def sql_generator_agent(query: str, ner: dict, table_finder: dict):

    print("====SQL GENERATOR AGENT UP====")
    retry_delay = 1
    max_retries = 4
    llm_query = make_prompt_sql(query, ner, table_finder)
    chat_history = [{"role": "user", "content": llm_query}]

    retries = 0

    while retries < max_retries:
        should_retry = False
        start_time = time.time()

        # API 调用（增加重试机制）
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    # model="deepseek-chat",
                    model='glm-4-plus',
                    messages=chat_history,
                    stream=False,
                    top_p=0.7,
                    temperature=0.9
                )
                break  # 如果成功，跳出重试循环
            except Exception as e:
                print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    raise  # 如果达到最大重试次数，抛出异常
                time.sleep(retry_delay)  # 等待一段时间后重试

        end_time = time.time()    

        response = json.loads(response.to_json())
        raw_content = response['choices'][0]['message']['content']
        usage = response['usage']
        execution_time = end_time - start_time

        # 第一个 try-except：处理 JSON 解析
        try:
            content = json.loads(raw_content.strip('`json'))
            chat_history.append({'role': 'assistant', 'content': str(content)})
        except Exception as e:
            print(f"Error processing JSON {query} (attempt {retries + 1}/{max_retries}): {e}")
            should_retry = True  # 标记需要重试

        # 如果 JSON 解析成功，继续执行后续逻辑
        if not should_retry:
            print("====SQL GENERATOR AGENT COMPLETED====")

            print("====SQL QUERYING UP====")

            post_data = {
                'sql': content['sql_query'],
                'limit': 1000
            }

            print(content['sql_query'])

            # 第二个 try-except：处理 fetch_data
            try:
                sql_res = fetch_data(post_data)['data']
                print("====SQL QUERYING COMPLETED====")
            except Exception as e:
                print("====SQL QUERYING DOWN====")
                print(f"Error fetching SQL data {query} (attempt {retries + 1}/{max_retries}): {e}")
                should_retry = True  # 标记需要重试
        
        if should_retry:
            retries += 1
            if retries == max_retries:
                print(f"Failed to process question ==={query}=== after {max_retries} attempts.")
                print("====SQL GENERATOR AGENT DOWN====")
            continue
            
        break

    if not locals().get('sql_res', []):

        sql_res = sql_generator_reflection_agent(chat_history, ner, table_finder)

    return locals().get('sql_res', [])

def rewrite_query_agent(query: str, history: list):
    print("====REWRITER AGENT UP====")

    retry_delay = 1
    max_retries = 6
    llm_query = make_prompt_rewrite(query, history)

    start_time = time.time()

    # API 调用（增加重试机制）
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                # model="deepseek-chat",
                model='glm-4-plus',
                messages=[{"role": "user", "content": llm_query}],
                stream=False,
                top_p=0.7,
                temperature=0.9
            )
            break  # 如果成功，跳出重试循环
        except Exception as e:
            print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                raise  # 如果达到最大重试次数，抛出异常
            time.sleep(retry_delay)  # 等待一段时间后重试

    end_time = time.time()    

    response = json.loads(response.to_json())
    raw_content = response['choices'][0]['message']['content']
    usage = response['usage']
    execution_time = end_time - start_time

    print("====REWRITER AGENT COMPLETED====")

    return raw_content

def answer_generator_agent(query: str, ner: dict, sql_res: list):
    print("====ANSWER GENERATOR UP====")

    retry_delay = 1
    max_retries = 6
    llm_query = make_prompt_answer(query, ner, sql_res)

    start_time = time.time()

    # API 调用（增加重试机制）
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                # model="deepseek-chat",
                model='glm-4-plus',
                messages=[{"role": "user", "content": llm_query}],
                stream=False,
                top_p=0.7,
                temperature=0.9
            )
            break  # 如果成功，跳出重试循环
        except Exception as e:
            print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                raise  # 如果达到最大重试次数，抛出异常
            time.sleep(retry_delay)  # 等待一段时间后重试

    end_time = time.time()    

    response = json.loads(response.to_json())
    raw_content = response['choices'][0]['message']['content']
    usage = response['usage']
    execution_time = end_time - start_time

    print("====ANSWER GENERATOR COMPLETED====")

    return raw_content

def table_finder_reflection_agent(chat_history: list, market: str, ner: dict):
    print("====TABLE REFLECTION AGENT UP====")
    retry_delay = 1
    max_retries = 3
    query = "结果不正确。可能的原因：表找的不全面；表找错了；忽略了表之间的联系。在原本的思考路径中增加一步「反思与修正」（reflection and correct）。"

    history = copy.deepcopy(chat_history)
    history.append({"role": "user", "content": query})

    for i in history:
        i['content'] = str(i['content'])

    retries = 0

    while retries < max_retries:
        should_retry = False
        start_time = time.time()

        # API 调用（增加重试机制）
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    # model="deepseek-chat",
                    model='glm-4-plus',
                    messages=history,
                    stream=False,
                    top_p=0.7,
                    temperature=0.9
                )
                break  # 如果成功，跳出重试循环
            except Exception as e:
                print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    raise  # 如果达到最大重试次数，抛出异常
                time.sleep(retry_delay)  # 等待一段时间后重试

        end_time = time.time()    

        response = json.loads(response.to_json())
        raw_content = response['choices'][0]['message']['content']
        usage = response['usage']
        execution_time = end_time - start_time

        # 第一个 try-except：处理 JSON 解析
        try:
            content = json.loads(raw_content.strip('`json'))
        except Exception as e:
            print(f"Error processing JSON {query} (attempt {retries + 1}/{max_retries}): {e}")
            should_retry = True  # 标记需要重试

        # 如果 JSON 解析成功，继续执行后续逻辑
        if not should_retry:
            print("====TABLE REFLECTION AGENT COMPLETED====")
            history.append({'role': 'assistant', 'content': content})
            return history
        else:
            retries += 1
            if retries == max_retries:
                print(f"Failed to process question ==={query}=== after {max_retries} attempts.")
                print("====TABLE REFLECTION AGENT DOWN====")
                return chat_history
            
def sql_generator_reflection_agent(chat_history: list, ner: dict, table_finder: dict):
    print("====SQL REFLECTION AGENT UP====")

    retry_delay = 1
    max_retries = 3

    query = "结果为空。在原本的思考路径中增加一步「反思与修正」（reflection and correct）。"

    history = copy.deepcopy(chat_history)
    history.append({"role": "user", "content": query})

    retries = 0

    while retries < max_retries:
        should_retry = False
        start_time = time.time()

        if len(history) % 2 == 0:
            history.append({"role": "user", "content": query})

        # API 调用（增加重试机制）
        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    # model="deepseek-chat",
                    model='glm-4-plus',
                    messages=history,
                    stream=False,
                    top_p=0.7,
                    temperature=0.9
                )
                break  # 如果成功，跳出重试循环
            except Exception as e:
                print(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    raise  # 如果达到最大重试次数，抛出异常
                time.sleep(retry_delay)  # 等待一段时间后重试

        end_time = time.time()    

        response = json.loads(response.to_json())
        raw_content = response['choices'][0]['message']['content']
        usage = response['usage']
        execution_time = end_time - start_time

        # 第一个 try-except：处理 JSON 解析
        try:
            content = json.loads(raw_content.strip('`json'))
            history.append({'role': 'assistant', 'content': str(content)})
        except Exception as e:
            print(f"Error processing JSON {query} (attempt {retries + 1}/{max_retries}): {e}")
            should_retry = True  # 标记需要重试

        # 如果 JSON 解析成功，继续执行后续逻辑
        if not should_retry:
            print("====SQL REFLECTION AGENT COMPLETED====")

            print("====SQL QUERYING UP====")

            post_data = {
                'sql': content['sql_query'],
                'limit': 1000
            }

            print(content['sql_query'])

            # 第二个 try-except：处理 fetch_data
            try:
                sql_res = fetch_data(post_data)['data']
                print("====SQL QUERYING COMPLETED====")
                if sql_res:
                    break
            except Exception as e:
                print("====SQL QUERYING DOWN====")
                print(f"Error fetching SQL data {query} (attempt {retries + 1}/{max_retries}): {e}")
                should_retry = True  # 标记需要重试
        
        if should_retry:
            retries += 1
            if retries == max_retries:
                print(f"Failed to process question ==={query}=== after {max_retries} attempts.")
                print("====SQL GENERATOR AGENT DOWN====")
            continue
            
        break

    return locals().get('sql_res', [])
            
def main_workflow(data: dict):
    """
    only for one question team
    """

    market = data['market']['market']
    ner = data['ner']['stage_1']
    chat_history = []
    max_retries = 3
    result = {}
    result['tid'] = data['tid']
    result['team'] = data['team']

    for i in range(len(data['team'])):

        retries = 0

        query = data['team'][i]['question']

        if i >= 1:
            query = rewrite_query_agent(query, chat_history)
            print(query)

        table_finder_history = table_finder_agent(query, market, ner)
        print(table_finder_history[-1]['content'])
        sql_res = sql_generator_agent(query, ner, table_finder_history[-1]['content'])
        print(sql_res)
        answer = answer_generator_agent(query, ner, sql_res)
        print(answer)

        if "信息不足" in answer:
            
            while retries < max_retries:
                table_finder_history = table_finder_reflection_agent(table_finder_history, market, ner)
                print(table_finder_history[-1]['content'])
                sql_res = sql_generator_agent(query, ner, table_finder_history[-1]['content'])
                print(sql_res)
                answer = answer_generator_agent(query, ner, sql_res)
                print(answer)

                retries += 1
                if "信息不足" not in answer:
                        break
            
        chat_history.append({"user": query, "assistant": answer})
        result['team'][i]['answer'] = answer
    
    print("====RESULT B====")
    print(result)
    print("====RESULT E====")
    return result


import concurrent.futures
import queue
import threading
import json
from tqdm import tqdm

def save_result(result_queue, output_file):
    """
    实时保存结果的线程
    """
    while True:
        # 从队列中获取结果
        result = result_queue.get()
        if result is None:
            break  # 如果队列中是 None，表示处理完毕，可以退出

        # 将结果保存到文件
        with open(output_file, "a", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
            f.write(",\n")  # 每个 result 后换行
            f.flush()  # 强制刷新缓冲区，确保实时写入文件

        result_queue.task_done()  # 标记任务完成

def process_data_in_parallel(data_list, num_threads, real_time_output_file="real_time_results.json", final_output_file="final_results.json"):
    """
    使用多线程处理每个 data，并支持实时保存和统一保存
    """
    # 线程安全的队列，用于线程间传递结果
    result_queue = queue.Queue()

    # 启动一个线程来实时保存结果
    save_thread = threading.Thread(target=save_result, args=(result_queue, real_time_output_file))
    save_thread.daemon = True  # 设置为守护线程，主线程退出时会自动退出
    save_thread.start()

    # 用于存储所有结果的列表
    all_results = []

    # 使用 tqdm 创建全局进度条
    with tqdm(total=len(data_list), desc="Processing", unit="task") as pbar:
        # 使用 ThreadPoolExecutor 执行主任务
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            # 提交所有任务
            future_to_data = {executor.submit(main_workflow, data): data for data in data_list}

            # 获取所有任务的结果，并将结果发送到队列中
            for future in concurrent.futures.as_completed(future_to_data):
                try:
                    result = future.result()  # 获取任务返回的结果
                    result_queue.put(result)  # 将结果放入队列，用于实时保存
                    all_results.append(result)  # 将结果添加到列表中，用于统一保存
                except Exception as exc:
                    print(f"Data processing generated an exception: {exc}")
                finally:
                    pbar.update(1)  # 更新进度条

    # 等待队列中的所有任务都处理完成
    result_queue.join()
    # 发送退出信号
    result_queue.put(None)
    # 等待保存线程退出
    save_thread.join()

    # 所有任务完成后，将所有结果统一保存为列表形式的 JSON 文件
    with open(final_output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)

missed = [58, 66, 69, 76, 78, 85, 86, 88, 90, 91, 94, 95, 97, 98, 99, 100]
unsolved = []

for q in questions:
    for i in missed:
        if str(i) == q['tid'].split('-')[-1]:
            unsolved.append(q)
    

# 示例用法
process_data_in_parallel(
    unsolved[:], 
    num_threads=5, 
    real_time_output_file="real_time_results-2.json", 
    final_output_file="final_results-2.json"
)
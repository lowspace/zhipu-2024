import sys
import os
import json
import time
import re
from datetime import datetime

import requests
from tqdm import tqdm
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

script_dir = os.path.dirname(os.path.abspath(__file__))
cwd = os.path.dirname(script_dir)

os.chdir(cwd)
sys.path.append('tools')

import chat
import parse_data
import sql

question_path = os.path.join(cwd, 'answer_tmp', 'stage_3-glm_4_plus-table_finder-v2.7.3.json')

sql_1_fname = f'sql_generator-stage_1-v2.0.0.md'
sql_2_fname = f'sql_generator-stage_2-v1.0.0.md'
ans_fname = f'answer_generator-v1.0.0.md'

model = 'deepseek_v3'
deepseek_api = 'sk-ba0f5eed3bea4fa6be16eb33b139c684'
sql_api = "43d1f290abf2441ea6b52b6e1ef95e79"

questions = parse_data.read_json(question_path)
# sort the questions by tid
questions = sorted(questions, key=lambda x: int(x['tid'].split('-')[-1]))

prompt_dir = os.path.join(cwd, 'prompt')

with open(os.path.join(prompt_dir, sql_1_fname), 'r') as f:
    sql_1_prompt_template = ''.join(f.readlines())

with open(os.path.join(prompt_dir, sql_2_fname), 'r') as f:
    sql_2_prompt_template = ''.join(f.readlines())

with open(os.path.join(prompt_dir, ans_fname), 'r') as f:
    ans_prompt_template = ''.join(f.readlines())


# fetch data
def fetch_data(data: dict):
    url = "https://comm.chatglm.cn/finglm2/api/query"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {sql_api}"
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

# build sql prompt 

def make_prompt_sql_1(data: dict) -> str:
    
    prompt = sql_1_prompt_template

    # Database-Table Pair(s)
    table_finder_res = data['table_finder']['stage_1'][0]['data_source']
    tables = [i['table'] for i in table_finder_res]
    table_finder_res = json.dumps(table_finder_res, ensure_ascii=False, indent=2)
    reg_p = re.compile('<Database and Table>')
    prompt = re.sub(reg_p, table_finder_res, prompt)
    
    # Table Schema(s)
    table_schema = ''
    for table in tables:
        table_fname = f'{table}-with_table_name.md'
        table_dir = os.path.join(cwd, 'data' + os.sep + 'table-column')
        table_fpath = os.path.join(table_dir, table_fname)
        with open(table_fpath,'r') as f:
            table_schema += ''.join(f.readlines())
            table_schema += '\n\n'
    reg_p = re.compile('<Table-Column Schema>')
    prompt = re.sub(reg_p, table_schema, prompt)

    # NER Result
    if data['ner']['stage_1']['result']:
        ner_res = [i for i in data['ner']['stage_1']['sql'].values() if i][0]
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
    query = data['team'][0]['question']
    reg_p = re.compile('<Current Query>')
    prompt = re.sub(reg_p, query, prompt)

    return prompt

def make_prompt_sql_2(data: dict, idx: int) -> str:
    
    prompt = sql_2_prompt_template

    # Database-Table Pair(s)
    table_finder_res = data['table_finder'].get(f'stage_{idx+1}', [])
    if table_finder_res:
        table_finder_res = table_finder_res[0]['data_source']
        tables = [i['table'] for i in table_finder_res]
        table_finder_res = json.dumps(table_finder_res, ensure_ascii=False, indent=2)
        reg_p = re.compile('<Database and Table>')
        prompt = re.sub(reg_p, table_finder_res, prompt)
    else:
        tables = []
        reg_p = re.compile('<Database and Table>')
        prompt = re.sub(reg_p, table_finder_res, prompt)
    
    # Table Schema(s)
    table_schema = ''
    for table in tables:
        table_fname = f'{table}-with_table_name.md'
        table_dir = os.path.join(cwd, 'data' + os.sep + 'table-column')
        table_fpath = os.path.join(table_dir, table_fname)
        with open(table_fpath,'r') as f:
            table_schema += ''.join(f.readlines())
            table_schema += '\n\n'
    reg_p = re.compile('<Table-Column Schema>')
    prompt = re.sub(reg_p, table_schema, prompt)

    # NER Result
    if data['ner']['stage_1']['result']:
        ner_res = [i for i in data['ner']['stage_1']['sql'].values() if i][0]
        ner_res = [i['result'] for i in ner_res if i['result']][0][0]
        ner_res = json.dumps(ner_res, ensure_ascii=False, indent=2)
        reg_p = re.compile('<NER Result>')
        prompt = re.sub(reg_p, ner_res, prompt)
    else:
        reg_p = re.compile('\n<NER Result>\n')
        prompt = re.sub(reg_p, '', prompt)
        reg_p = re.compile('\n## NER Result\n')
        prompt = re.sub(reg_p, '', prompt)

    # Query
    query = data['team'][idx]['question']
    reg_p = re.compile('<Current Query>')
    prompt = re.sub(reg_p, query, prompt)

    # Answers
    history = []
    answers = data['answer_generator']
    for i in range(len(answers)):
        ans = answers[i] # {'stage_n': ans}
        ans = list(ans.values())[0]
        query = data['team'][i]['question']
        history.append({'previous_query': query, "response": ans})
    history = json.dumps(history, ensure_ascii=False, indent=2)
    reg_p = re.compile('<Chat History>')
    prompt = re.sub(reg_p, history, prompt) 

    return prompt

def make_prompt_answer(data: dict, idx: int) -> str:

    prompt = ans_prompt_template

    # SQL Query
    sql_generator = data['sql_generator'].get(f'stage_{idx+1}', [])
    if sql_generator:
        sql_query = sql_generator[0]['sql_query']
        reg_p = re.compile('<SQL Query>')
        prompt = re.sub(reg_p, sql_query, prompt)
    else:
        reg_p = re.compile('\n<SQL Query>\n')
        prompt = re.sub(reg_p, '', prompt)
        reg_p = re.compile('\n## SQL Query\n')
        prompt = re.sub(reg_p, '', prompt)

    # SQL Result
    if sql_generator:
        sql_res = str(sql_generator[0]['sql_res'])
        reg_p = re.compile('<SQL Result>')
        prompt = re.sub(reg_p, sql_res, prompt)
    else:
        reg_p = re.compile('\n<SQL Result>\n')
        prompt = re.sub(reg_p, '', prompt)
        reg_p = re.compile('\n## SQL Result\n')
        prompt = re.sub(reg_p, '', prompt)

    # NER Result
    if data['ner']['stage_1']['result']:
        ner_res = [i for i in data['ner']['stage_1']['sql'].values() if i][0]
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
    query = data['team'][idx]['question']
    reg_p = re.compile('<Current Query>')
    prompt = re.sub(reg_p, query, prompt)

    return prompt

def process_question(question: dict, main_pbar, lock):
    """
    Process a single question and return the result.
    Retry up to 5 times if an error occurs.
    """

    client = OpenAI(api_key= deepseek_api, base_url="https://api.deepseek.com")
    sql_generator_history, answer_generator_history = [], []

    max_retries = 5

    retry_delay = 1  # 重试延迟时间（秒）

    tid = question['tid']
    stage_count = len(question['team'])

    question['sql_generator'] = {}
    question['answer_generator'] = []

    with tqdm(total=stage_count, 
                desc=f"问题 {tid}", 
                position=1,  # 嵌套显示
                leave=False, # 完成后自动清除
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]') as local_pbar:

        for i in tqdm(range(len(question['team']))):
            # sql generator
            retries = 0

            while retries < max_retries:
                should_retry = False  # 标志变量，标记是否需要重试

                if i == 0:
                    llm_sql_query = make_prompt_sql_1(question)
                else:
                    llm_sql_query = make_prompt_sql_2(question, i)

                tmp_sql_generator_history = sql_generator_history.copy()
                tmp_sql_generator_history.append({'role': 'user', 'content': llm_sql_query})

                start_time = time.time()

                # API 调用（增加重试机制）
                for attempt in range(max_retries):
                    try:
                        response = client.chat.completions.create(
                            model="deepseek-chat",
                            messages=tmp_sql_generator_history,
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

                # 第一个 try-except：处理 JSON 解析
                try:
                    content = json.loads(raw_content.strip('`json'))
                    usage = response.get('usage', {})
                    execution_time = end_time - start_time

                    question['sql_generator'][f'stage_{i+1}'] = [content]
                    question['token_usage'][f'sql_generator-stage_{i+1}'] = [usage]
                    question['time_usage'][f'sql_generator-stage_{i+1}'] = [f"{execution_time:.2f}s"]
                except Exception as e:
                    print(f"Error processing JSON {question['team'][i]['id']} (attempt {retries + 1}/{max_retries}): {e}")
                    should_retry = True  # 标记需要重试

                # 如果 JSON 解析成功，继续执行后续逻辑
                if not should_retry:
                    post_question = {
                        'sql': content['sql_query'],
                        'limit': 1000
                    }

                    # 第二个 try-except：处理 fetch_data
                    try:
                        sql_res = fetch_data(post_question)['data']
                        question['sql_generator'][f'stage_{i+1}'][0]['sql_res'] = sql_res
                    except Exception as e:
                        print(f"Error fetching SQL question {question['team'][i]['id']} (attempt {retries + 1}/{max_retries}): {e}")
                        should_retry = True  # 标记需要重试

                # 根据 should_retry 决定是否重试
                if should_retry:
                    retries += 1
                    if retries == max_retries:
                        print(f"Failed to process question {question['team'][i]['id']} after {max_retries} attempts.")
                        question['sql_generator'][f'stage_{i+1}'] = []  # 设置默认值
                    continue  # 跳过本次循环，进入下一次重试

                # 如果成功，跳出重试循环
                break

            # 更新历史记录
            sql_generator_history.extend([
                {'role': 'user', 'content': llm_sql_query},
                {'role': 'assistant', 'content': raw_content}
            ])

            # answer generator（保持不变）
            llm_answer_query = make_prompt_answer(question, i)
            answer_generator_history.append({'role': 'user', 'content': llm_answer_query})

            start_time = time.time()
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=answer_generator_history,
                stream=False,
                top_p=0.7,
                temperature=0.9
            )
            end_time = time.time()

            response = json.loads(response.to_json())
            content = response['choices'][0]['message']['content']
            usage = response.get('usage', {})
            execution_time = end_time - start_time

            question['answer_generator'].append({f'stage_{i+1}': content})
            question['token_usage'][f'answer_generator-stage_{i+1}'] = [usage]
            question['time_usage'][f'answer_generator-stage_{i+1}'] = [f"{execution_time:.2f}s"]

            answer_generator_history.append({'role': 'assistant', 'content': content})

            # 更新进度条（双进度）
            local_pbar.update(1)
            with lock:
                main_pbar.update(1)
                main_pbar.set_postfix_str(f"当前处理：{tid}-阶段{i+1}")

    return question

def main():
    answers = []  # 维护结果列表
    total_stages = sum(len(q['team']) for q in questions[:])
    
    # 带锁的进度条配置
    with tqdm(total=total_stages, 
             desc="总体进度",
             position=0,
             bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as main_pbar:
        
        lock = threading.Lock()
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            # 创建任务映射
            future_to_id = {
                executor.submit(
                    process_question, 
                    question, 
                    main_pbar,
                    lock
                ): question['tid'] for question in questions[:]
            }
            
            # 结果收集
            for future in as_completed(future_to_id):
                tid = future_to_id[future]
                try:
                    result = future.result()
                    answers.append(result)  # 成功时添加结果
                    
                    # 实时保存（可选）
                    with lock:
                        parse_data.write_json(answers, 'temp_results.json')
                        
                except Exception as e:
                    with lock:
                        main_pbar.write(f"错误 {tid}: {str(e)}")
                    # 记录失败任务
                    answers.append({
                        'tid': tid,
                        'error': str(e),
                        'raw_data': future_to_id[future]
                    })

    # Save the results
    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    date = now.strftime("%Y-%m-%d")

    saved_path = os.path.join(cwd, 'answer_tmp' + os.sep + f'answer-{model}-{date}.json')
    parse_data.write_json(answers, saved_path)


if __name__ == "__main__":
    main()
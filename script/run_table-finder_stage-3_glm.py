import sys
import os
import json
import time
import re

from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# 获取当前脚本的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
cwd = os.path.dirname(script_dir)

os.chdir(cwd)
sys.path.append('tools')

# 现在可以正常导入 tools 中的模块
import chat
import parse_data

system_prompt = ""

prompt_dir = os.path.join(cwd, 'prompt')

version = 'v2.7.3'

fname = f'table_finder-stage_1-{version}.md'
prompt_fpath = os.path.join(prompt_dir, fname)

with open(prompt_fpath, 'r') as f:
    prompt_template = ''.join(f.readlines())


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


def make_prompt(query: str, ner: dict) -> str:

    """
    ner_res: content from the stage_1
    """

    prompt = prompt_template + query

    # ner_result is None
    if not ner['result']:
        return prompt

    ner_content = {}
    ner_content.update(ner['result'][0])

    sql_res = ner['sql']

    for k, v in sql_res.items():
        for j in v:
            if not j['result']:
                continue

            sql_query = j['query']
            # add database and table
            ner_content.update(parse_database_and_table(sql_query))
            # get market
            if ner_content['table'] == 'US_SecuMain':
                ner_content['market'] = 'US'
            elif ner_content['table'] == 'HK_SecuMain':
                ner_content['market'] = 'HK'
            else:
                ner_content['market'] = 'CN'
            ner_content['data_from_table'] = j['result']

    # add NER result

    ner_str = f"\n\n### **Name Entity Recognition Result**\n```json\n{json.dumps(ner_content, ensure_ascii=False,indent=2)}\n```"

    prompt += ner_str
    
    return prompt


def process_question(question):
    """
    Process a single question and return the result.
    Retry up to 5 times if an error occurs.
    """
    max_retries = 5
    retries = 0

    while retries < max_retries:
        try:
            res = question
            res['table_finder'] = {}
            history = []
            
            for i in range(len(question['team'])):
                if i == 0:
                    query = make_prompt(question['team'][i]['question'], question['ner']['stage_1'])
                else:
                    query = "基于之前的聊天记录。" + question['team'][i]['question']

                start_time = time.time()
                message = chat.create_message(query, history=history, system_prompt=system_prompt, temperature=0.7, top_p=0.9, response_format='text')
                end_time = time.time()

                execution_time = end_time - start_time
                usage = chat.get_token_usage(message, False)
                content = chat.get_content(message, False)
                history = chat.build_history(history, message=message)

                res['table_finder'][f'stage_{i+1}'] = [json.loads(content.strip('`json'))]
                res['token_usage'][f'table_finder-stage_{i+1}'] = [usage]
                res['time_usage'][f'table_finder-stage_{i+1}'] = [f"{execution_time:.2f}s"]

            return res
        except Exception as e:
            retries += 1
            print(f"Error processing question {question['tid']} (attempt {retries}/{max_retries}): {e}")
            if retries == max_retries:
                print(f"Failed to process question {question['tid']} after {max_retries} attempts.")
                return None
            time.sleep(1)  # Wait for 1 second before retrying


def main():
    question_path = os.path.join(cwd, 'answer_tmp' + os.sep + 'stage_1-glm_4_plus-ner-v2.0.0-sql-HF-Post.json')
    questions = parse_data.read_json(question_path)
    model = 'glm_4_plus'
    answers = []

    # Use ThreadPoolExecutor for multithreading
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers based on your system
        futures = {executor.submit(process_question, question): question for question in questions[:]}

        # Use tqdm to show progress
        for future in tqdm(as_completed(futures), total=len(futures)):
            result = future.result()
            if result is not None:
                answers.append(result)

    # Save the results
    saved_path = os.path.join(cwd, 'answer_tmp' + os.sep + f'stage_3-{model}-table_finder-{version}.json')
    parse_data.write_json(answers, saved_path)


if __name__ == "__main__":
    main()
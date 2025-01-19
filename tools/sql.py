import yaml
import os

import requests


def load_api_key():
    """
    Load the SQL API key from sql_api.yaml located in the src directory.

    Returns:
        str: The SQL API key.

    Raises:
        FileNotFoundError: If the llm_api.yaml file is not found.
        KeyError: If the API key is not present in the yaml file.
    """
    # Get the absolute path to the current script
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the absolute path to the src/sql_api.yaml file
    src_path = os.path.join(current_dir, '..', 'src', 'sql_api.yaml')
    # Normalize the path (resolve .., etc.)
    src_path = os.path.normpath(src_path)

    if not os.path.exists(src_path):
        raise FileNotFoundError(f"The file '{src_path}' does not exist.")

    # Read the YAML file
    with open(src_path, 'r') as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error reading YAML file: {e}")

    # Retrieve the API key
    api_key = config.get('sql_api_key')
    if not api_key:
        raise KeyError("The 'sql_api_key' is missing in the YAML file.")

    return api_key


def init_post() -> dict:

    api_key = load_api_key()
    url = "https://comm.chatglm.cn/finglm2/api/query"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    return {"url": url, "headers": headers}


def get_data_from_sql_query(query: str) -> list:
    """
    General function to send an SQL query, process the response, and return the result.
    Handles common operations for all SQL queries.
    """
    try:
        # Initialize the configuration
        config = init_post()

        # Prepare the data to send
        data = {
            "sql": query,
            "limit": 100000  # Default limit for all queries
        }

        # Send the POST request
        response = requests.post(
            config['url'], headers=config['headers'], json=data)
        response.raise_for_status()  # Raise an exception if the HTTP status code is not 200

        # Parse the response and check if it contains the 'data' field
        response_json = response.json()
        if 'data' not in response_json:
            raise ValueError("The response is missing the 'data' field")

        # Retrieve the 'data' field content
        res = response_json.get('data', [])
        if not res:
            # Print a warning if the 'data' is empty
            # print("Warning: The returned data is empty")
            pass

        # Return the result, or an empty list if no data is found
        return res or []

    except requests.exceptions.RequestException as e:
        # Handle request-related exceptions (e.g., network issues, timeouts, etc.)
        print(f"Request failed: {e}")
        return []  # Return an empty list if the request fails

    except ValueError as e:
        # Handle errors related to data processing (e.g., missing fields in the response)
        print(f"Data processing error: {e}")
        return []  # Return an empty list if there's an issue with the response structure

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []  # Return an empty list in case of any other unexpected errors

def generate_sql_query_ner(data: list, value) -> list:
    """
    Generate SQL query through template.
    
    Args:
        data (list): A list of dictionaries containing database, table, and columns information.
        value (any): The value to compare with the column values in SQL. The type of value can vary (e.g., string, number).
        
    Returns:
        str: The generated SQL query.
    """
    queries = []  # List to store all generated SQL queries
    
    # Helper function to format the value properly for SQL query
    def format_value(val) -> str:
        # If the value is a string, wrap it in single quotes
        if isinstance(val, str):
            return f"'{val}'"
        # If the value is a number (int or float), use it as is
        elif isinstance(val, (int, float)):
            return str(val)
        # If the value is a boolean, convert it to 1 (True) or 0 (False)
        elif isinstance(val, bool):
            return '1' if val else '0'
        # For other types, return the string representation of the value
        return str(val)

    # Iterate over each table's data in the input list
    for i in data:
        # Basic SELECT query for the given database and table
        select_q = f"SELECT * FROM {i['database']}.{i['table']}"
        
        # Generate WHERE clause conditions
        # Join all conditions with IN
        condition_q = f"{format_value(value)} IN ({', '.join([_ for _ in i['columns']])})"
        
        # Combine SELECT query and WHERE conditions to form the full SQL query
        query = f"{select_q} WHERE {condition_q}"
        queries.append(query)
    
    return queries

def get_bio_through_company_code(company_code: str) -> list:
    """
    Get the bio description from the company code
    """

    src_data = [
        {
            "database": "ConstantDB",
            "table": "SecuMain",
            "columns": ["InnerCode", "CompanyCode", "SecuCode", "ISIN", "JSID"]
        },
        {
            "database": "ConstantDB",
            "table": "HK_SecuMain",
            "columns": ["InnerCode", "CompanyCode", "SecuCode", "ISIN", "JSID"]
        },
        {
            "database": "ConstantDB",
            "table": "US_SecuMain",
            "columns": ["InnerCode", "CompanyCode", "SecuCode", "ISIN", "JSID"]
        }
    ]

    company_code = int(company_code)

    queries = generate_sql_query_ner(src_data, company_code)
    results = [get_data_from_sql_query(query) for query in queries]
    query_result_map = [{"query": query, "result": result} for query, result in zip(queries, results)]

    return query_result_map

def get_bio_through_name(name: str) -> list:
    """
    Get the bio description from the company name OR fund name
    """

    src_data = [
        {
            "database": "ConstantDB",
            "table": "SecuMain",
            "columns": ["ChiName", "ChiNameAbbr", "EngName", "EngNameAbbr", "SecuAbbr", "ChiSpelling"]
        },
        {
            "database": "ConstantDB",
            "table": "HK_SecuMain",
            "columns": ["ChiName", "ChiNameAbbr", "EngName", "EngNameAbbr", "SecuAbbr", "ChiSpelling"]
        },
        {
            "database": "ConstantDB",
            "table": "US_SecuMain",
            # SecuCode in US_SecuMain is a name rather a numberic code
            "columns": ["SecuCode", "SecuAbbr", "ChiSpelling", "EngName", "ChiName"]
        },
    ]

    queries = generate_sql_query_ner(src_data, name)
    results = [get_data_from_sql_query(query) for query in queries]
    query_result_map = [{"query": query, "result": result} for query, result in zip(queries, results)]

    return query_result_map

def get_bio_through_fund_company_name(fund_company_name: str) -> list:
    """
    Get the bio description from the company name
    """

    src_data = [
        {
            "database": "InstitutionDB",
            "table": "LC_InstiArchive",
            "columns": ["ChiName", "AbbrChiName", "NameChiSpelling", "EngName", "AbbrEngName"]
        },
    ]

    queries = generate_sql_query_ner(src_data, fund_company_name)
    results = [get_data_from_sql_query(query) for query in queries]
    query_result_map = [{"query": query, "result": result} for query, result in zip(queries, results)]

    return query_result_map

def get_bio_through_industry_name(industry_name: str) -> list:
    
    sql_query = f"SELECT FirstIndustryCode AS 一级行业代码, SecondIndustryCode AS 二级行业代码, ThirdIndustryCode AS 三级行业代码, FourthIndustryCode AS 四级行业代码, FirstIndustryName AS 一级行业名称, SecondIndustryName AS 二级行业名称, ThirdIndustryName AS 三级行业名称, FourthIndustryName AS 四级行业名称 FROM AStockIndustryDB.LC_ExgIndustry WHERE '{industry_name}' IN (FirstIndustryName, SecondIndustryName, ThirdIndustryName, FourthIndustryName)"

    result = get_data_from_sql_query(sql_query)

    return [{"query": sql_query, "result": result}]

def process_ner_res(ner_res: dict) -> list:
    
    ner_res['sql'] = {}

    for i in ner_res['result']:
        for k, v in i.items():
            if k == "代码":
                tmp = get_bio_through_company_code(v)
            elif k == "上市公司名称" or k == "基金名称":
                tmp = get_bio_through_name(v)
            elif k == "基金公司名称":
                tmp = get_bio_through_fund_company_name(v)
            elif k == "行业名称":
                tmp = get_bio_through_industry_name(v)
            else:
                print(f"NER failed:\n Query: {k}\nResult: {v}")

            ner_res['sql'][f'{k}:{v}'] = tmp
    
    return ner_res

def process_sql_generator_res(sql_res: dict) -> list:
    
    sql_res['sql_res'] = get_data_from_sql_query(sql_res['sql_query'])

    return sql_res
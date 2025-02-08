import os
import re

def load_prompt_template(stage='stage_1', agent='table_finder', version='v2.7.1'):
    """
    Load a prompt template from a markdown file located in the prompts directory.

    Args:
        stage (str): The stage of the prompt (e.g., 'stage_1'). Defaults to 'stage_1'.
        agent (str): The agent type (e.g., 'table_finder'). Defaults to 'table_finder'.
        version (str): The version of the prompt template (e.g., 'v2.7.1'). Defaults to 'v2.7.1'.

    Returns:
        str: The content of the prompt template as a string.

    Raises:
        ValueError: If stage, agent, or version is an empty string.
        FileNotFoundError: If the prompt template file is not found.
        IOError: If there is an issue reading the file.
    """
    # Validate input parameters
    if not stage or not agent or not version:
        raise ValueError("stage, agent, and version must be non-empty strings.")

    # Get the absolute path to the current script
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Construct the filename
    fname = f'{agent}-{stage}-{version}.md'

    # Construct the absolute path to the prompt template file
    prompt_fpath = os.path.join(current_dir, '..', 'prompt', fname)
    # Normalize the path (resolve .., etc.)
    prompt_fpath = os.path.normpath(prompt_fpath)

    # Read the prompt template file
    try:
        with open(prompt_fpath, 'r') as f:
            prompt_template = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt template file not found: {prompt_fpath}")
    except IOError as e:
        raise IOError(f"Error reading the prompt template file: {e}")

    return prompt_template


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


def make_prompt(agent='table_finder', stage='stage_1', data=)
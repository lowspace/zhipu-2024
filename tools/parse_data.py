import os
from typing import List, Dict

import json

def read_jsonl(fpath: str) -> list:
    """
    Read a JSON Lines (jsonl) file and return a list of JSON objects.
    
    Parameters:
    fpath (str): The path to the jsonl file.

    Returns:
    list: A list containing JSON objects from the jsonl file.
    """
    data = []
    with open(fpath, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line.strip()))
    return data


def read_json(fpath: str) -> dict:
    """
    Read a JSON file and return a JSON object.
    
    Parameters:
    fpath (str): The path to the JSON file.

    Returns:
    dict: A JSON object parsed from the JSON file.
    """
    with open(fpath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_jsonl(data: List[Dict], fpath: str) -> None:
    """
    Write a list of JSON objects to a JSON Lines (jsonl) file.
    
    Parameters:
    data (List[Dict]): A list of dictionary objects to be written to the jsonl file.
    fpath (str): The path to the jsonl file.
    """
    with open(fpath, 'w', encoding='utf-8') as file:
        for entry in data:
            json_line = json.dumps(entry, ensure_ascii=False)
            file.write(json_line + '\n')

def write_json(data: List[Dict], fpath: str) -> None:
    """
    Write a list of dictionaries to a JSON file.
    
    Parameters:
    data (List[Dict]): A list of dictionary objects to be written to the JSON file.
    fpath (str): The path to the JSON file.
    """
    with open(fpath, 'w', encoding='utf-8') as file:
        # Use json.dump to write the list of dictionaries as a JSON array
        json.dump(data, file, ensure_ascii=False, indent=4)

def find_files_with_suffix(directory, suffix):
    """
    Searches for files with a given suffix in a directory and its subdirectories.
    
    Args:
    directory (str): The directory path to search within.
    suffix (str): The file suffix to search for. It should start with a '.' (e.g., '.txt').
    
    Returns:
    list: A list of full paths to files that end with the given suffix.
    """
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                matched_files.append(os.path.join(root, file))
    return matched_files
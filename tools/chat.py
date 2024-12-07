import json
import os
import yaml
from datetime import datetime

from zhipuai import ZhipuAI

import parse_data

def load_api_key():
    """
    Load the LLM API key from llm_api.yaml located in the src directory.

    Returns:
        str: The LLM API key.
    
    Raises:
        FileNotFoundError: If the llm_api.yaml file is not found.
        KeyError: If the API key is not present in the yaml file.
    """
    # Get the absolute path to the current script
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the absolute path to the src/llm_api.yaml file
    src_path = os.path.join(current_dir, '..', 'src', 'llm_api.yaml')
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
    api_key = config.get('llm_api_key')
    if not api_key:
        raise KeyError("The 'llm_api_key' is missing in the YAML file.")
    
    return api_key

def create_message(new_message, system_prompt = "", history=None, model="glm-4-plus", max_tokens=4096, temperature=0.7, top_p=1, response_format="text"):
    """
    Creates a message using the AnthropicVertex client.

    Parameters:
        new_message (str): The new message content to be added.
        history (list of dict, optional): The conversation history. Each entry is a dict with 'role' and 'content'. Default is None.
        model (str, optional): The model to use. Default is "glm-4-plus".
        max_tokens (int, optional): The maximum number of tokens. Default is 4096.
        temperature (float, optional): The sampling temperature. Default is 0.7.
        top_p (float, optional): The nucleus sampling parameter. Default is 1.
        type (str, optional): The type of the return object. Default is "text", can be "json_object".

    Returns:
        dict: The response from the client.
    """

    api_key = load_api_key()
    client = ZhipuAI(api_key = api_key)

    if history is None:
        if system_prompt is not None:
            history = [{"role": "system", "content": system_prompt}]
        else:
            history = []
    
    # Add the new message to the history
    history.append({"role": "user", "content": new_message})

    message = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        messages=history,
        response_format={'type': response_format}
    )

    return message

def get_content(response, display=False):
    """
    Extracts the content text from the response.

    Parameters:
        response (dict): The response data structure.
        display (bool, optional): Whether to print the result. Default is False.

    Returns:
        str: The content text from the response.
    """
    response = json.loads(response.to_json())
    content_text = response['choices'][0]['message']['content']
    
    if display:
        print(content_text)
    
    return content_text

def get_token_usage(response, display=False):
    """
    Extracts the token usage from the response.

    Parameters:
        response (dict): The response data structure.
        display (bool, optional): Whether to print the result. Default is False.

    Returns:
        dict: The token usage from the response.
    """
    response = json.loads(response.to_json())
    token_usage = response.get('usage', {})
    
    if display:
        print(token_usage)
    
    return token_usage

def build_history(history: list, message=None):
    """
    Builds the conversation history.

    Parameters:
        content (str): The content of the user's message.
        message (dict, optional): The assistant's message response from which to extract content.
        history (list, optional): The current conversation history. Default is None.

    Returns:
        list: The constructed conversation history.

    Raises:
        ValueError: If the message is None or doesn't contain the assistant's response.
    """
    if history is None:
        history = []

    # if system_prompt:
    #     if history[0]['role'] == 'system':
    #         history[0]['content'] = system_prompt
    #     else:
    #         history.insert(0, {"role": "system", "content": system_prompt})

    if message:
        # Extract content from the assistant's message and add it to the history
        assistant_content = get_content(message)
        history.append({"role": "assistant", "content": assistant_content})
    else:
        raise ValueError("Can't find assistant response in this message")

    return history

def save_history(data: list, title: str):
    """
    Saves the conversation history to a JSONL file.

    Parameters:
        data (list): The conversation history to be saved. Each item in the list should be a dictionary representing a conversation turn.
        title (str): The title for the history file. This will be used as part of the filename.

    Returns:
        None
    """
    # Get the current working directory
    cwd = os.getcwd()

    # Define the directory where the history files will be saved
    history_dir = os.path.join(cwd, 'history')

    # Create the history directory if it doesn't exist
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)

    # Create a filename with the given title and the current datetime
    fname = f'{title} {datetime.now().strftime("%Y-%m-%d %H:%M")}.jsonl'

    # Combine the directory and filename to get the full file path
    history_fpath = os.path.join(history_dir, fname)

    # Write the data to the JSONL file
    parse_data.write_jsonl(data, history_fpath)

    return
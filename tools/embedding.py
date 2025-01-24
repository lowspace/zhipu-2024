import json

import numpy as np
from zhipuai import ZhipuAI

import chat

def cosine_similarity(vec1, vec2):
    # Compute the dot product of the vectors
    dot_product = np.dot(vec1, vec2)
    # Compute the magnitude (norm) of each vector
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    # Return the cosine similarity
    return dot_product / (norm_vec1 * norm_vec2)


def compute_embedding(text: str) -> list:
    api_key = chat.load_api_key()
    client = ZhipuAI(api_key=api_key) 
    response = client.embeddings.create(
        model="embedding-3", #填写需要调用的模型编码
        input=[
            text,
        ],
    )
    res = json.loads(response.to_json())['data'][0]['embedding']

    return res
import os

from zhipuai import ZhipuAI
import numpy as np

import chat
import embedding

def match_market_through_embedding(query: str) -> str:
    """ 
    ner.npz =  {"US": us_embedding, "HK": ..., "CN": ....}
    Return US or HK or CN
    """

    # load embedding

    fname = 'ner.npz'

    cwd = os.getcwd()
    # dir_name = os.path.dirname(cwd)
    data_dir = os.path.join(cwd, 'data')
    fpath =  os.path.join(data_dir, 'embedding' + os.sep + fname)

    # compute embedding
    query = embedding.compute_embedding(query)

    embeddings = np.load(fpath)
    res = {}

    for k, v in embeddings.items():
        res[k] = embedding.cosine_similarity(v, query)
    
    # find top 1
    top_1 = sorted(res.items(), key=lambda item: item[1], reverse=True)[0]

    return top_1[0]
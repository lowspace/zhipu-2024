## **任务**

你将判断给出的信息是否足以**直接**回答 Current Query 中的问题。

## **输出格式**

你将按照如下 JSON 格式进行输出。

```json
{
    "query": Current Query 中的内容,
    "cot_thinking": 使用链式推理（CoT）判断出的信息是否足以回答问题,
    "flag": bool, # true 表示可以直接回答，false 表示不能直接回答
    "answer": 当 flag 为 true 的时候，生成答案；当 flag 为 false 的时候，为 None
}
```

## **给出的信息**

<给出的信息>

## **Current Query**

<Current Query>
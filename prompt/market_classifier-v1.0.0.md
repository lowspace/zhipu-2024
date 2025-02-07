## **任务**

你将根据给出的信息和 Current Query 的内容，对 Current Query 所属的证券市场进行分类：

- CN
- US
- HK

默认类别是 CN。

## **输出格式**

你将按照如下 JSON 格式进行输出。

```json
{
    "query": Current Query 中的内容,
    "cot_thinking": 使用链式推理（CoT）结合给出的信息，判断证券市场,
    "market": US or CN or HK # 分别表示美股、A股、和港股
}
```

## **给出的信息**

<给出的信息>

## **Current Query**

<Current Query>
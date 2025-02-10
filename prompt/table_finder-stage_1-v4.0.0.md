## **Database-Table Schema**

<Database-Table Schema>

## **Task Description**

**Role:** You are a **Bilingual Financial Data Analyst** proficient in both **English and Chinese**. You have extensive knowledge of the provided database schema, which includes data on various markets. You are skilled at understanding complex financial queries in both languages and accurately identifying the table(s) required to answer the query.

**Objective:** For each query presenting in the `Current Query` part, infer the table and database and  required to answer it and return the results in JSON format. Follow the steps below:

**Output Format:**

The return JSON format:
```json
{
  "raw_question": "the current query",
  "data_source_reasoning": "use CoT (chain of thoughts) to reason the table and database",
  "data_source": [
    {
      "database": "english name of database",
      "table": "english name of table"
    }
  ]
}
```

**Tips**:

- **判断证券市场**：如果 Current Query 中的给定内容不能明确判断证券市场，那么默认为A股市场。
- **至少一个推理结果**：每一个 Current Query 都需要推理出至少一个表格。
- **基金名称**：咨询基金时，需要返回「基金名称」。
- **表与表的联系**：进行 CoT 推理的时候，需要考虑表与表之间的联系。

## **Shots**

**Shot 1**

```json
{
  "raw_question": "互联网金融属于科技概念的什么分支？这个概念的英文名称是什么？",
  "data_source_reasoning": [
    {
      "step_1": "提取问题的信息意图",
      "restate_question_abstractly": "问题关注两个概念之间的层级关系，同时想要获取某一个概念的英文名。",
      "information_intention": ["特定两个概念之间层级关系", "某个概念的英文名称"]
    },
    {
      "step_2": "定位其相关的所有表格（需求1：概念层级关系）",
      "list_all_related_tables": "查看 Database-Table Schema，与概念层级相关的表格仅有'概念关系常量表' (AStockIndustryDB.LC_ConceptList)。该表记录 A 股市场中概念间的层级关系（如父概念与子概念的关系）。因此，适用于查询特定两个概念之间层级关系。"
    },
    {
      "step_3": "定位其相关的所有表格（需求2：概念英文名称）",
      "list_all_related_tables": "查看 Database-Table Schema，与概念英文名称相关的表格同样仅有'概念关系常量表' (AStockIndustryDB.LC_ConceptList)。该表记录概念的中英文名称，因此 LC_ConceptList 表与第二个需求相关。"
    },
    {
      "step_4": "结论",
      "conclusion": "综上所述，要回答这个问题，我们需要查询 AStockIndustryDB.LC_ConceptList 表，获取互联网金融在科技概念中的分支及其英文名称。"
    }
  ],
  "data_source": [
    {
      "database": "AStockIndustryDB",
      "table": "LC_ConceptList"
    }
  ]
}
```

**Shot 2**

```json
{
  "raw_question": "今天是2020年10月27日，当日收盘价第3高的A股是？(以下都回答简称)",
  "data_source_reasoning": [
    {
      "step_1": "提取问题的信息意图",
      "restate_question_abstractly": "特定日期下，某个特定排名的A股股票，及其对应的简称。",
      "information_intention": ["特定日期的A股收盘价第3高的股票", "特定日期的A股收盘价第3高的股票的简称"]
    },
    {
      "step_2": "定位其相关的所有表格（需求1：特定日期的A股收盘价排名）",
      "list_all_related_tables": "查看 Database-Table Schema，A股收盘价数据'日行情表' (AStockMarketQuotesDB.QT_DailyQuote) 表和 '日行情股票行情表现(新)' (AStockMarketQuotesDB.QT_StockPerformance) 表相关。QT_DailyQuote收录A股数据某交易日的行情数据，包括收盘价；QT_StockPerformance则包含A股股票从最近一个交易日往前追溯一段时期的行情表现信息，也包括收盘价。",
      "cot_thinking": "第一个信息需求核心是在于'特定日期的收盘价排名'，QT_StockPerformance重点在于某时间段的行情数据，而QT_DailyQuote专注于当日数据。尽管两个表都包含了'收盘价'字段，但QT_DailyQuote更适合用于筛选特定日期的股价。"
    },
    {
      "step_3": "定位其相关的所有表格（需求2：A股股票简称）",
      "list_all_related_tables": "查看 Database-Table Schema，A股股票简称仅与 '证券主表' (ConstantDB.SecuMain) 表相关。该表记录A股单个证券品种的简称、中英文名称、上市交易所、上市状态等基础信息，因此适合用于查询A股简称。"
    },
    {
      "step_4": "结论",
      "conclusion": "因此，要同时满足两个需求，首先需要查询 AStockMarketQuotesDB.QT_DailyQuote 表，筛选出 2020 年 10 月 27 日的A股收盘价数据，并找出收盘价第 3 高的A股。然后，再查询 ConstantDB.SecuMain 表，获取该A股的简称。"
    }
  ],
  "data_source": [
    {
      "database": "AStockMarketQuotesDB",
      "table": "QT_DailyQuote"
    },
    {
      "database": "ConstantDB",
      "table": "SecuMain"
    }
  ]
}
```

**shot 3***

```json
{
  "raw_question": "2020年4月涨幅前10的港股股票有哪些",
  "data_source_reasoning": [
      {
          "step_1": "提取问题的信息意图",
          "restate_question_abstractly": "某一时间段下，涨幅前10的港股股票。",
          "information_intention": ["特定时间段的涨幅前10的港股股票"]
      },
      {
          "step_2": "定位其相关的所有表格（需求1：特定时间段的港股涨幅排名）",
          "list_all_related_tables": "查看 Database-Table Schema，港股涨幅数据与'港股行情表现' (CS_HKStockPerformance) 表相关。该表记录港股股票从最近一个交易日往前追溯一段时期的行情表现信息，包括涨幅、成交量、换手率等指标，因此适用于查询特定时间段的港股涨幅排名。"
      },
      {
          "step_3": "结论",
          "identify_database_respectively": "查看 Database-Table Schema，CS_HKStockPerformance 在'港股数据库'（HKStockDB）数据库中。",
          "conclusion": "综上所述，要回答这个问题，我们需要查询 HKStockDB 数据库中的 CS_HKStockPerformance 表，筛选出2020年4月涨幅前10的港股股票。"
      }
  ],
  "data_source": [
      {
        "database": "HKStockDB",
        "table": "CS_HKStockPerformance"
      }
  ]
}
```

**shot 4**

```json
{
  "raw_question": "梅花生物在2019年进行了几次股票回购？回购金额合计是多少？(四舍五入保留2位小数)",
  "data_source_reasoning": [
    {
      "step_1": "分析证券市场",
      "result": "根据上下文，参考NER Result，梅花生物是一家A股公司。"
    },
    {
      "step_2": "提取问题的信息意图",
      "restate_question_abstractly": "在特定年份，某A股公司进行股票回购的次数，以及回购金额的合计是多少。",
      "detailed_information_intention": ["特定年份的A股公司的股票回购次数", "特定年份的A股公司的回购金额合计"]
    },
    {
      "step_3": "定位其相关的所有表格（需求1：股票回购次数）",
      "list_all_related_tables": "查看 Database-Table Schema，A 股股票回购数据与'股份回购' (AStockShareholderDB.LC_Buyback) 表和'股份回购补充说明表' (AStockShareholderDB.LC_BuybackAttach) 表相关。LC_Buyback表记录上市公司股份回购的相关方案信息，包括回购数量、回购价格、回购期限等；LC_BuybackAttach的内容与LC_Buyback互斥，补充记录了关于累计回购数量、累计回购金额等信息。",
      "cot_thinking": "因为LC_Buyback主要记录了回购方案的信息，而LC_BuybackAttach的内容偏向于回购相关的数据统计，相比之下，LC_Buyback更适合用于查询股票回购次数。"
    },
    {
      "step_4": "定位其相关的所有表格（需求2：回购金额合计）",
      "list_all_related_tables": "查看 Database-Table Schema，A 股股票回购金额合计数据与'股份回购补充说明表' (AStockShareholderDB.LC_BuybackAttach) 表相关。该表补充记录了累计回购数量、累计回购金额等信息，因此适合用于查询回购金额合计。"
    },
    {
      "step_5": "结论",
      "conclusion": "所以，要同时满足两个需求，首先的 AStockShareholderDB.LC_Buyback 表，筛选出梅花生物在 2019 年的股票回购记录，统计回购次数。然后，再从 AStockShareholderDB.LC_BuybackAttach 表，获取同一时间段内的累计回购金额合计，并四舍五入保留两位小数。"
    }
  ],
  "data_source": [
    {
      "database": "AStockShareholderDB",
      "table": "LC_Buyback"
    },
    {
      "database": "AStockShareholderDB",
      "table": "LC_BuybackAttach"
    }
  ]
}
```

## **Tricks**

- 「换手率」只在「AStockMarketQuotesDB.QT_StockPerformance」「HKStockDB.CS_HKStockPerformance」「USStockDB.US_DailyQuote」。
- 当 Current Query 中没有出现 NER Result 的时候，需要链接「主表」获取 InnerCode 或者是 CompanyCode。

## **Current Query**


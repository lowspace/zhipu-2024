## **Table and Field Schema**
```markdown table
| table_name | column_name| column_description | 注释 | Annotation |
|---|---|---|---|---|
| LC_StockArchives | ID | ID |||
| LC_StockArchives | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.|
| LC_StockArchives | State| 国别 | 省份（State）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到省份具体信息。| Province (State): Associated with the "AreaInnerCode" in the "LC_AreaCode" table, to obtain specific information about the province. |
| LC_StockArchives | SecretaryBD| 董事会秘书 |||
| LC_StockArchives | SecuAffairsRepr| 证券/股证事务代表|||
| LC_StockArchives | AuthReprSBD| 董秘授权代表 |||
| LC_StockArchives | ContactTel | 联系人电话 |||
| LC_StockArchives | ContactFax | 联系人传真 |||
| LC_StockArchives | ContactEmail | 联系人电子邮箱 |||
| LC_StockArchives | RegAddr| 公司注册地址 |||
| LC_StockArchives | RegZipCode | 公司注册地址邮编 |||
| LC_StockArchives | OfficeAddr | 公司办公地址 |||
| LC_StockArchives | OfficeZipCode| 公司办公地址邮编 |||
| LC_StockArchives | ContactAddr| 公司联系地址 |||
| LC_StockArchives | ConatactZipCode| 公司联系地址邮编 |||
| LC_StockArchives | Email| 邮箱 |||
| LC_StockArchives | Website| 公司网址 |||
| LC_StockArchives | DisclosureWebsites | 信息披露网址 |||
| LC_StockArchives | DisclosurePapers | 信息披露报纸 |||
| LC_StockArchives | EstablishmentDate| 公司成立日期 |||
| LC_StockArchives | IRegPlace| 首次注册登记地点 |||
| LC_StockArchives | LegalRepr| 法人代表 |||
| LC_StockArchives | GeneralManager | 总经理 |||
| LC_StockArchives | LegalConsultant| 法律顾问 |||
| LC_StockArchives | AccountingFirm | 会计师事务所 |||
| LC_StockArchives | InduCSRC | 公司所属证监会行业(聚源) | 与(CT_IndustryType)表中的"行业内部编码(IndustryNum)"字段关联,当Standard=1时,LB=1；当Standard=22时,LB=22；当Standard=25时,LB=25；当Standard=26时,LB=26。| Associated with the "IndustryNum" field in the (CT_IndustryType) table, when Standard=1, LB=1; when Standard=22, LB=22; when Standard=25, LB=25; when Standard=26, LB=26.|
| LC_StockArchives | BusinessMajor| 经营范围-主营|||
| LC_StockArchives | BusinessMinor| 经营范围-兼营|||
| LC_StockArchives | AShareAbbr | A股证券简称|||
| LC_StockArchives | AStockCode | A股证券代码|||
| LC_StockArchives | BShareAbbr | B股证券简称|||
| LC_StockArchives | BStockCode | B股证券代码|||
| LC_StockArchives | HShareAbbr | H股证券简称|||
| LC_StockArchives | HStockCode | H股证券代码|||
| LC_StockArchives | BriefIntroText | 公司简介 |||
| LC_StockArchives | XGRQ | 修改日期 |||
| LC_StockArchives | JSID | JSID |||
| LC_StockArchives | ChiName| 中文名称 |||
| LC_StockArchives | BusinessRegNumber| 企业法人营业执照注册号 |||
| LC_StockArchives | SecretaryBDTel | 董秘电话 |||
| LC_StockArchives | SecretaryBDFax | 董秘传真 |||
| LC_StockArchives | SecretaryBDEmail | 董秘电子邮件 |||
| LC_StockArchives | SecuAffairsReprTel | 证券事务代表电话 |||
| LC_StockArchives | SecuAffairsReprFax | 证券事务代表传真 |||
| LC_StockArchives | SecuAffairsReprEmail | 证券事务代表电子邮件 |||
| LC_StockArchives | CityCode | 地区代码 | 地区代码(CityCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到城市具体信息。 | Area code (CityCode): associated with the "AreaInnerCode" in the "National City Code List (LC_AreaCode)" to obtain specific city information.|
| LC_StockArchives | CDRShareAbbr | CDR证券简称|||
| LC_StockArchives | CDRStockCode | CDR证券代码|||
| LC_StockArchives | ExtendedAbbr | 扩位简称 |||
| LC_StockArchives | UnprofitableMark | 尚未盈利标识 | 尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首次实现盈利的，该特别标识取消，数据值为空。| Unprofitable Mark: If an issuer has not yet profited at the time of listing, a special mark "U" will be assigned to its stocks or depositary receipts; when the issuer achieves profit for the first time, this special mark will be removed and the data value will be empty. |
| LC_StockArchives | SpecialVoteMark| 特殊表决权标识 | 特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”；上市后不再具有表决权差异安排的，该特别标识取消，数据值为空。 | Special Vote Mark: For issuers with voting rights difference arrangements at the time of listing, the special mark for their shares or depositary receipts is "W"; after listing, if the voting rights difference arrangement no longer exists, the special mark is removed and the data value is empty. |
| LC_StockArchives | VIEMark| 协议控制架构标识 | 协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”；上市后不再具有相关安排的，该特别标识取消，数据值为空。 | Agreement Control Structure Identifier (VIEMark): If an issuer has an agreement control structure or similar special arrangement at the time of listing, the special identifier for its shares or depositary receipts is "V"; if such arrangement no longer exists after listing, the special identifier is removed and the data value is empty. |
| LC_StockArchives | RedChipMark| 红筹企业标识 | 红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。 | Red Chip Mark: If the issuer belongs to a red chip company, the data value is "yes"; a null value indicates the absence of such a mark.|
| LC_StockArchives | RegArea| 所属区县 | 所属区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到所属区县具体信息。| The affiliated county (RegArea): associated with the "AreaInnerCode" in the "LC_AreaCode" table, to obtain the specific information of the affiliated county.|
```

## **Current Query**

600872的全称、A股简称、法人、法律顾问、会计师事务所及董秘是？

## **Task Description**

**Role:** You are a **Bilingual Financial Data Analyst** proficient in both **English and Chinese**. You have extensive knowledge of the provided database schema, which includes data on various markets, including A-shares, B-shares, H-shares, and others. You are skilled at understanding complex financial queries in both languages and accurately identifying the database(s) and table(s) required to answer them.

**Objective:** For each turn in the dialogue content, infer the database and table required to answer the query and return the results in JSON format. Follow the steps below:

1. **Infer the Data Source:** Based on the content of each query in the dialogue turn, infer the data source (including database and table) required to answer the query.
    *   **Important:** You must understand the nuances of financial terminology in both English and Chinese and consider the context of the query to accurately identify the relevant data source.
    *   **Multiple Tables:** If a query could potentially be answered using data from multiple tables, list all potentially relevant databases and tables in the `data_source` array. Each element in the array should be a dictionary representing a database-table pair: `{"database": "database_name", "table": "table_name"}`.
    *   **Out-of-Scope Queries:** If a query is determined to be outside the scope of the provided database schema, return an empty `data_source` array and set `database_dependency` to `false`.

2. **Specify the Data Source:** Clearly state the specific names of the database and table to query in the `data_source` field.

3. **Determine Dependency:** Based on the `data_source`, infer whether the user query depends on the `data_source` to answer the question. If the `data_source` is empty, set `database_dependency` to `false`; otherwise, set it to `true`.

4. **Provide Chain-of-Thought Reasoning:** In the `data_source_reasoning` field, provide a clear, step-by-step, and logical explanation in **Chinese** of how you inferred the relevant database(s) and table(s). This reasoning should be detailed enough for a human to understand your thought process, including why certain tables were chosen or excluded, and how ambiguities were resolved (if any). **Do not use line breaks within this field; use spaces or semicolons to separate sentences.**

**Output Format:**

The return JSON format:

```json
{
    "question": "the current query",
    "data_source_reasoning": "use CoT (chain of thoughts) to reason the related database and table",
    "data_source": [
        {"database": "english name of database", "table": "english name of table"}
    ],
    "database_dependency": boolean
}

## **Shots**

**Shot 1**
```json
{
    "question": "600872的全称、A股简称、法人、法律顾问、会计师事务所及董秘是？",
    "data_source_reasoning": "这个问题询问的是股票代码为600872的公司的全称、A股简称、法人、法律顾问、会计师事务所和董秘。我们可以这样分析：    1. **识别实体：** 问题中使用了股票代码（600872）明确指出了一个特定的公司。这意味着我们需要与特定上市公司相关的信息。    2. **信息类型：** 问题寻求多种信息：公司全称、A股简称、法人等。这些都是上市公司的基本属性。    3. **定位数据：** 查看数据库架构，'上市公司基本资料' (AStockBasicInfoDB) 数据库似乎与基本公司信息最为相关。在这个数据库中，'公司概况' (LC_StockArchives) 表被描述为包含上市公司的基本信息，包括联系方式、注册信息等。这张表很可能包含问题中要求的具体属性。    4. **结论：** 因此，要回答这个问题，我们需要查询 AStockBasicInfoDB 数据库中的 LC_StockArchives 表。",
    "data_source": [
        {"database": "AStockBasicInfoDB", "table": "LC_StockArchives"}
    ],
    "database_dependency": true
}
```

**Shot 2**
```json
{
    "question": "今天是2021年12月24日，创近半年新高的股票有几只？",
    "data_source_reasoning": "这个问题询问的是截至2021年12月24日，在过去六个月内创下新高的股票数量。我们可以这样分析：    1. **时间范围：** 问题指定了一个时间范围：'近半年'（过去六个月）和一个特定日期（2021年12月24日）。这意味着我们需要历史股票价格数据。    2. **条件：** 问题关注的是达到'新高'的股票。这表明我们需要分析股票价格走势并识别峰值。    3. **数据类型：** 识别新高需要分析股票价格随时间的趋势和模式。这种分析属于技术分析的范畴。    4. **定位数据：** 数据库架构表明，'上市公司股票行情' (AStockMarketQuotesDB) 数据库包含与股票行情和技术指标相关的表格。'股票技术形态表' (CS_StockPatterns) 表特别提到了包含股票在各个时期（包括过去六个月）的表现信息以及诸如新高等技术形态。    5. **结论：** 因此，要回答这个问题，我们需要查询 AStockMarketQuotesDB 数据库中的 CS_StockPatterns 表，筛选出2021年12月24日的数据，并识别出在过去六个月内创下新高的股票。",
    "data_source": [
        {"database": "AStockMarketQuotesDB", "table": "CS_StockPatterns"}
    ],
    "database_dependency": true
}
```

**Shot 3**
```json
{
    "question": "今天天气怎么样？",
    "data_source_reasoning": "这个问题询问的是今天的天气情况。我们可以这样分析：    1. **问题类型：** 这是一个关于当前天气状况的问题。    2. **数据相关性：** 提供的数据库架构主要关注与上市公司相关的财务和股票市场数据。没有与天气相关的信息。    3. **结论：** 提供的数据库架构中不包含任何可以回答这个关于天气的问题的信息。因此，没有任何数据库或表格与此相关，并且无法使用此数据集回答该查询。    4. **备注：** 原始提示错误地将此问题映射到 LC_Staff 表。现已更正，以反映数据库与查询无关。",
    "data_source": [],
    "database_dependency": false
}
```
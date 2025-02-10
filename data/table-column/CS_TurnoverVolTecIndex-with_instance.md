| table_name| column_name | column_description | 注释 | Annotation| 数据示例|
|---|---|---|---|---|---|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | ID| ID || | 742300729255|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | InnerCode | 证券内部编码 | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。 | The internal code (InnerCode) of securities is associated with the "InnerCode" in the "SecuMain" table, obtaining other detailed information such as the security code and abbreviation of the stock. | 67|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | GilCode | 聚源代码 || | SEC00000001V|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | TradingDay| 交易日期 || | 2019-01-04 12:00:00.000 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | IndexCycle| 指标周期 | 指标周期(IndexCycle)，该字段固定以下常量：0-日，1-周，2-月，3-季，4-半年，5-年 | IndexCycle, this field is fixed with the following constants: 0-Daily, 1-Weekly, 2-Monthly, 3-Quarterly, 4-Half Yearly, 5-Annually| 1 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | SecuMarket| 证券市场 | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。 | The securities market (SecuMarket) is associated with the DM field in the (CT_SystemConst) table, with LB=201 AND DM IN (18,81,83,90), resulting in the specific description of the securities market: 18-Beijing Securities Exchange, 81-Third Board Market, 83-Shanghai Securities Exchange, 90-Shenzhen Securities Exchange. | 90|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA5| 成交额简单移动平均(5日)|| | 98351136.494|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA10 | 成交额简单移动平均(10日) || | 187971378.093 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA20 | 成交额简单移动平均(20日) || | 152531482.8685|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA30 | 成交额简单移动平均(30日) || | 138053975.7207|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA60 | 成交额简单移动平均(60日) || | 152694495.52|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA120| 成交额简单移动平均(120日)|| | 261302718.373 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | AMA250| 成交额简单移动平均(250日)|| | 947896979.881 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA5| 成交量简单移动平均(5日)|| | 18522945.0|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA10 | 成交量简单移动平均(10日) || | 34999875.4|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA20 | 成交量简单移动平均(20日) || | 28799280.5|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA30 | 成交量简单移动平均(30日) || | 26399611.2667 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA60 | 成交量简单移动平均(60日) || | 27270051.8333 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA120| 成交量简单移动平均(120日)|| | 40313785.5167 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMA250| 成交量简单移动平均(250日)|| | 94386022.46 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMACD_EMA12 | 成交量指数平滑异同平均(12日) || | 27042185.6916 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMACD_EMA26 | 成交量指数平滑异同平均(26日) || | 28183154.3655 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMACD_DIFF| 成交量指数平滑异同平均DIFF || | -1140968.6739 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMACD_DEA | 成交量指数平滑异同平均DEA|| | 1786437.2273|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VMACD_MACD| 成交量指数平滑异同平均MACD || | -2927405.9012 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VolumeRatio | 量比 || | 0.4566|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VOSC| VOSC成交量震荡指标 || | 16.3968 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | TAPI_TAPI | TAPI加权指数成交量TAPI || | 7406.6609 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | TAPI_TAPIMA | TAPI加权指数成交量TAPIMA || | 14661.6478|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VSTD| VSTD成交量标准差 || | 23027745.5953 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VROC| VROC量变动速率(%)|| | -61.38|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VR| VR成交量比率(%)|| | 102.4198|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | VRSI| VRSI量相对强弱 || | 1.5755|
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | InsertTime| 发布时间 || | 2023-07-09 04:31:30.907 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | UpdateTime| 更新时间 || | 2023-07-09 04:31:30.907 |
| AStockMarketQuotesDB.CS_TurnoverVolTecIndex | JSID| JSID || | 742300729256|
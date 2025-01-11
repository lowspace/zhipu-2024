| column_name | column_description | 注释 | Annotation|
|---|---|---|---|---|
| ID| ID || |
| InnerCode | 证券内部编码 | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。 | The internal code (InnerCode) of securities is associated with the "InnerCode" in the "SecuMain" table, obtaining other detailed information such as the security code and abbreviation of the stock. |
| GilCode | 聚源代码 || |
| TradingDay| 交易日期 || |
| IndexCycle| 指标周期 | 指标周期(IndexCycle)，该字段固定以下常量：0-日，1-周，2-月，3-季，4-半年，5-年 | IndexCycle, this field is fixed with the following constants: 0-Daily, 1-Weekly, 2-Monthly, 3-Quarterly, 4-Half Yearly, 5-Annually|
| SecuMarket| 证券市场 | 证券市场(SecuMarket)与(CT_SystemConst)表中的DM字段关联，令LB=201 AND DM IN (18,81,83,90)，得到证券市场的具体描述：18-北京证券交易所，81-三板市场，83-上海证券交易所，90-深圳证券交易所。 | The securities market (SecuMarket) is associated with the DM field in the (CT_SystemConst) table, with LB=201 AND DM IN (18,81,83,90), resulting in the specific description of the securities market: 18-Beijing Securities Exchange, 81-Third Board Market, 83-Shanghai Securities Exchange, 90-Shenzhen Securities Exchange. |
| AMA5| 成交额简单移动平均(5日)|| |
| AMA10 | 成交额简单移动平均(10日) || |
| AMA20 | 成交额简单移动平均(20日) || |
| AMA30 | 成交额简单移动平均(30日) || |
| AMA60 | 成交额简单移动平均(60日) || |
| AMA120| 成交额简单移动平均(120日)|| |
| AMA250| 成交额简单移动平均(250日)|| |
| VMA5| 成交量简单移动平均(5日)|| |
| VMA10 | 成交量简单移动平均(10日) || |
| VMA20 | 成交量简单移动平均(20日) || |
| VMA30 | 成交量简单移动平均(30日) || |
| VMA60 | 成交量简单移动平均(60日) || |
| VMA120| 成交量简单移动平均(120日)|| |
| VMA250| 成交量简单移动平均(250日)|| |
| VMACD_EMA12 | 成交量指数平滑异同平均(12日) || |
| VMACD_EMA26 | 成交量指数平滑异同平均(26日) || |
| VMACD_DIFF| 成交量指数平滑异同平均DIFF || |
| VMACD_DEA | 成交量指数平滑异同平均DEA|| |
| VMACD_MACD| 成交量指数平滑异同平均MACD || |
| VolumeRatio | 量比 || |
| VOSC| VOSC成交量震荡指标 || |
| TAPI_TAPI | TAPI加权指数成交量TAPI || |
| TAPI_TAPIMA | TAPI加权指数成交量TAPIMA || |
| VSTD| VSTD成交量标准差 || |
| VROC| VROC量变动速率(%)|| |
| VR| VR成交量比率(%)|| |
| VRSI| VRSI量相对强弱 || |
| InsertTime| 发布时间 || |
| UpdateTime| 更新时间 || |
| JSID| JSID || |
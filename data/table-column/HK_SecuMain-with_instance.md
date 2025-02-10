| table_name | column_name | column_description | 注释 | Annotation | 数据示例 |
|---|---|---|---|---|---|
| ConstantDB.HK_SecuMain | ID| ID ||| 182598377530 |
| ConstantDB.HK_SecuMain | InnerCode | 证券内部编码 ||| 1002504|
| ConstantDB.HK_SecuMain | CompanyCode | 公司代码 ||| 2437 |
| ConstantDB.HK_SecuMain | SecuCode| 证券代码 ||| 00939|
| ConstantDB.HK_SecuMain | ChiName | 中文名称 ||| 中国建设银行股份有限公司 |
| ConstantDB.HK_SecuMain | ChiNameAbbr | 中文名称缩写 ||| null |
| ConstantDB.HK_SecuMain | EngName | 英文名称 ||| China Construction Bank Corpor |
| ConstantDB.HK_SecuMain | EngNameAbbr | 英文名称缩写 ||| CCB|
| ConstantDB.HK_SecuMain | SecuAbbr| 证券简称 ||| 建设银行 |
| ConstantDB.HK_SecuMain | ChiSpelling | 拼音证券简称 ||| JSYH |
| ConstantDB.HK_SecuMain | SecuMarket| 证券市场 | 证券市场(SecuMarket)：与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (72)，得到证券市场的具体描述：72-香港联交所。 | Securities Market (SecuMarket): Associated with the DM field in the (CT_SystemConst) table, with LB = 201 AND DM IN (72), the specific description of the securities market is obtained: 72-Hong Kong Stock Exchange.| 72 |
| ConstantDB.HK_SecuMain | SecuCategory| 证券类别 | 证券类别(SecuCategory)：与(CT_SystemConst)表中的DM字段关联，令LB = 1177 and DM in (3,4,10,20,21,25,51,52,53,55,60,61,62,63,64,65,68,69,71,72,78,81,82)，得到证券类别的具体描述：3-H股，4-大盘，10-其他，20-衍生权证，21-股本权证，25-牛熊证，51-港股，52-合订证券，53-红筹股，55-优先股，60-基金，61-信托基金，62-ETF基金，63-参与证书，64-杠杆及反向产品，65-债务证券，68-界内证，69-美国证券(交易试验计划)，71-普通预托证券，72-优先预托证券，78-临时证券(Temporary)，81-SPAC股份，82-SPAC权证。 | Securities Category (SecuCategory): Associated with the DM field in the (CT_SystemConst) table, let LB = 1177 and DM in (3,4,10,20,21,25,51,52,53,55,60,61,62,63,64,65,68,69,71,72,78,81,82), to obtain the specific description of the securities category: 3-H Share, 4-Large Cap, 10-Other, 20-Derivative Warrant, 21-Equity Warrant, 25-Bull/Bear Certificate, 51-HK Stock, 52-Consolidated Securities, 53-Red Chip Stock, 55-Preferred Stock, 60-Fund, 61-Trust Fund, 62-ETF Fund, 63-Participation Certificate, 64-Leverage and Inverse Products, 65-Debt Securities, 68-In-the-Money Certificate, 69-U.S. Securities (Trading Pilot Program), 71-Ordinary Depositary Receipt, 72-Preferred Depositary Receipt, 78-Temporary Securities (Temporary), 81-SPAC Stock, 82-SPAC Warrant. | 3|
| ConstantDB.HK_SecuMain | ListedDate| 上市日期 ||| 2005-10-27 12:00:00.000|
| ConstantDB.HK_SecuMain | ListedSector| 上市板块 | 上市板块(ListedSector)：与(CT_SystemConst)表中的DM字段关联，令LB = 207 AND DM IN (1,4,6)，得到上市板块的具体描述：1-主板，4-其他，6-创业板。 | Listing Sector: Associated with the DM field in the (CT_SystemConst) table, with LB = 207 AND DM IN (1,4,6), the specific description of the listing sector is obtained: 1-Main Board, 4-Other, 6-Growth Enterprise Market.| 1|
| ConstantDB.HK_SecuMain | ListedState | 上市状态 | 上市状态(ListedState)：与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,5,9)，得到上市状态的具体描述：1-上市，5-终止，9-其他。 | Listing Status (ListedState): Associated with the DM field in the (CT_SystemConst) table, let LB = 1176 AND DM IN (1,5,9), to obtain the specific description of the listing status: 1 - Listed, 5 - Terminated, 9 - Other.| 1|
| ConstantDB.HK_SecuMain | FormerName| 曾用名 ||| null |
| ConstantDB.HK_SecuMain | DelistingDate | 退市日期 ||| null |
| ConstantDB.HK_SecuMain | TradingUnit | 买卖单位(股/手)||| 1000.0 |
| ConstantDB.HK_SecuMain | TraCurrUnit | 交易货币类别 | 交易货币类别（TraCurrUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“交易货币”描述：1000-美元，1100-港元，1160-日本元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。| Transaction currency category (TraCurrUnit): associated with the "code (DM)" in the "System Constants Table (CT_SystemConst)", let LB="1068", to obtain the description of "transaction currency": 1000-USD, 1100-HKD, 1160-JPY, 1320-SGD, 1420-CNY, 3000-EUR, 3030-GBP, 5010-CAD, 6010-AUD. | 1100 |
| ConstantDB.HK_SecuMain | ISIN| ISIN代码 ||| CNE1000002H1 |
| ConstantDB.HK_SecuMain | InsertTime| 发布时间 ||| 2005-10-14 09:46:17.530|
| ConstantDB.HK_SecuMain | XGRQ| 更新时间 ||| 2019-12-08 08:03:38.837|
| ConstantDB.HK_SecuMain | JSID| JSID ||| 629150621771 |
| ConstantDB.HK_SecuMain | ID| ID ||| 182598377530 |
| ConstantDB.HK_SecuMain | InnerCode | 证券内部编码 ||| 1002504|
| ConstantDB.HK_SecuMain | CompanyCode | 公司代码 ||| 2437 |
| ConstantDB.HK_SecuMain | SecuCode| 证券代码 ||| 00939|
| ConstantDB.HK_SecuMain | ChiName | 中文名称 ||| 中国建设银行股份有限公司 |
| ConstantDB.HK_SecuMain | ChiNameAbbr | 中文名称缩写 ||| null |
| ConstantDB.HK_SecuMain | EngName | 英文名称 ||| China Construction Bank Corpor |
| ConstantDB.HK_SecuMain | EngNameAbbr | 英文名称缩写 ||| CCB|
| ConstantDB.HK_SecuMain | SecuAbbr| 证券简称 ||| 建设银行 |
| ConstantDB.HK_SecuMain | ChiSpelling | 拼音证券简称 ||| JSYH |
| ConstantDB.HK_SecuMain | SecuMarket| 证券市场 | 证券市场(SecuMarket)：与(CT_SystemConst)表中的DM字段关联，令LB = 201 AND DM IN (72)，得到证券市场的具体描述：72-香港联交所。 | Securities Market (SecuMarket): Associated with the DM field in the (CT_SystemConst) table, with LB = 201 AND DM IN (72), the specific description of the securities market is obtained: 72-Hong Kong Stock Exchange.| 72 |
| ConstantDB.HK_SecuMain | SecuCategory| 证券类别 | 证券类别(SecuCategory)：与(CT_SystemConst)表中的DM字段关联，令LB = 1177 and DM in (3,4,10,20,21,25,51,52,53,55,60,61,62,63,64,65,68,69,71,72,78,81,82)，得到证券类别的具体描述：3-H股，4-大盘，10-其他，20-衍生权证，21-股本权证，25-牛熊证，51-港股，52-合订证券，53-红筹股，55-优先股，60-基金，61-信托基金，62-ETF基金，63-参与证书，64-杠杆及反向产品，65-债务证券，68-界内证，69-美国证券(交易试验计划)，71-普通预托证券，72-优先预托证券，78-临时证券(Temporary)，81-SPAC股份，82-SPAC权证。 | Securities Category (SecuCategory): Associated with the DM field in the (CT_SystemConst) table, let LB = 1177 and DM in (3,4,10,20,21,25,51,52,53,55,60,61,62,63,64,65,68,69,71,72,78,81,82), to obtain the specific description of the securities category: 3-H Share, 4-Large Cap, 10-Other, 20-Derivative Warrant, 21-Equity Warrant, 25-Bull/Bear Certificate, 51-HK Stock, 52-Consolidated Securities, 53-Red Chip Stock, 55-Preferred Stock, 60-Fund, 61-Trust Fund, 62-ETF Fund, 63-Participation Certificate, 64-Leverage and Inverse Products, 65-Debt Securities, 68-In-the-Money Certificate, 69-U.S. Securities (Trading Pilot Program), 71-Ordinary Depositary Receipt, 72-Preferred Depositary Receipt, 78-Temporary Securities (Temporary), 81-SPAC Stock, 82-SPAC Warrant. | 3|
| ConstantDB.HK_SecuMain | ListedDate| 上市日期 ||| 2005-10-27 12:00:00.000|
| ConstantDB.HK_SecuMain | ListedSector| 上市板块 | 上市板块(ListedSector)：与(CT_SystemConst)表中的DM字段关联，令LB = 207 AND DM IN (1,4,6)，得到上市板块的具体描述：1-主板，4-其他，6-创业板。 | Listing Sector: Associated with the DM field in the (CT_SystemConst) table, with LB = 207 AND DM IN (1,4,6), the specific description of the listing sector is obtained: 1-Main Board, 4-Other, 6-Growth Enterprise Market.| 1|
| ConstantDB.HK_SecuMain | ListedState | 上市状态 | 上市状态(ListedState)：与(CT_SystemConst)表中的DM字段关联，令LB = 1176 AND DM IN (1,5,9)，得到上市状态的具体描述：1-上市，5-终止，9-其他。 | Listing Status (ListedState): Associated with the DM field in the (CT_SystemConst) table, let LB = 1176 AND DM IN (1,5,9), to obtain the specific description of the listing status: 1 - Listed, 5 - Terminated, 9 - Other.| 1|
| ConstantDB.HK_SecuMain | FormerName| 曾用名 ||| null |
| ConstantDB.HK_SecuMain | DelistingDate | 退市日期 ||| null |
| ConstantDB.HK_SecuMain | TradingUnit | 买卖单位(股/手)||| 1000.0 |
| ConstantDB.HK_SecuMain | TraCurrUnit | 交易货币类别 | 交易货币类别（TraCurrUnit）：与“系统常量表（CT_SystemConst）”中的“代码（DM）”关联，令LB=“1068”，得到“交易货币”描述：1000-美元，1100-港元，1160-日本元，1320-新加坡元，1420-人民币元，3000-欧元，3030-英镑，5010-加拿大元，6010-澳大利亚元。| Transaction currency category (TraCurrUnit): associated with the "code (DM)" in the "System Constants Table (CT_SystemConst)", let LB="1068", to obtain the description of "transaction currency": 1000-USD, 1100-HKD, 1160-JPY, 1320-SGD, 1420-CNY, 3000-EUR, 3030-GBP, 5010-CAD, 6010-AUD. | 1100 |
| ConstantDB.HK_SecuMain | ISIN| ISIN代码 ||| CNE1000002H1 |
| ConstantDB.HK_SecuMain | InsertTime| 发布时间 ||| 2005-10-14 09:46:17.530|
| ConstantDB.HK_SecuMain | XGRQ| 更新时间 ||| 2019-12-08 08:03:38.837|
| ConstantDB.HK_SecuMain | JSID| JSID ||| 629150621771 |
| table_name| column_name| column_description | 注释 | Annotation| 数据示例|
|---|---|---|---|---|---|
| AStockIndustryDB.LC_IndustryValuation | ID | ID || | 702068509457|
| AStockIndustryDB.LC_IndustryValuation | IndustryNum| 行业内部编码 || | 60105811|
| AStockIndustryDB.LC_IndustryValuation | TradingDay | 交易日 || | 2021-10-25 12:00:00.000 |
| AStockIndustryDB.LC_IndustryValuation | StatType | 统计类型 | 统计类型(StatType)，该字段固定以下数值型常量：2-整体法不剔除负值 | StatType, this field is fixed with the following numeric constants: 2 - the overall method does not exclude negative values | 2 |
| AStockIndustryDB.LC_IndustryValuation | SectorCode | 统计板块 | 统计板块(SectorCode)，该字段固定以下数值型常量：5-沪、深及北交所市场 | "SectorCode (statistical sector), this field is fixed with the following numeric constants: 5-Shanghai, Shenzhen and Beijing Stock Exchange markets"| 5 |
| AStockIndustryDB.LC_IndustryValuation | Standard | 行业分类标准 | 数值型常量。行业分类标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (24,41)，得到行业分类标准的具体描述：24-申万行业分类2014版，41-申万行业分类2021版。| Numeric constant. The industry classification standard (Standard) is associated with the DM field in the (CT_SystemConst) table, with LB = 1081 AND DM IN (24,41), yielding the specific description of the industry classification standard: 24-Shenwan Industry Classification 2014 Edition, 41-Shenwan Industry Classification 2021 Edition. | 41|
| AStockIndustryDB.LC_IndustryValuation | IndustryCode | 行业代码 | 行业代码（IndustryCode），字符型常量：当Standard=24时，与“系统常量表”的“代码（DM）”关联，“LB=1804”，得到行业名称；当Standard=41时，与“行业类别表”的“行业代码（IndustryCode）”关联，“Standard=41”，得到行业名称 | Industry Code, string constant: When Standard equals 24, it is associated with the "Code (DM)" in the "System Constants Table", "LB=1804" to obtain the industry name; when Standard equals 41, it is associated with the "Industry Code (IndustryCode)" in the "Industry Category Table", "Standard=41" to obtain the industry name. | 740201|
| AStockIndustryDB.LC_IndustryValuation | TotalMV| 总市值(元) || | 134863892169.42 |
| AStockIndustryDB.LC_IndustryValuation | NegotiableMV | A股流通市值(元)|| | 129358349179.86 |
| AStockIndustryDB.LC_IndustryValuation | FreeFloatMV| A股自由流通市值(元)|| | 58139655899.12|
| AStockIndustryDB.LC_IndustryValuation | PE_TTM | 滚动市盈率 || | 14.5732 |
| AStockIndustryDB.LC_IndustryValuation | PE_LYR | 静态市盈率(LYR)|| | 29.9087 |
| AStockIndustryDB.LC_IndustryValuation | PB_LF| 市净率(LF) || | 2.0604|
| AStockIndustryDB.LC_IndustryValuation | DividendRatio| 滚动股息率(%)|| | 0.9597|
| AStockIndustryDB.LC_IndustryValuation | PCF_TTM| 滚动市现率 || | 16.1865 |
| AStockIndustryDB.LC_IndustryValuation | PCF_LYR| 静态市现率(LYR)|| | 27.9572 |
| AStockIndustryDB.LC_IndustryValuation | PS_TTM | 滚动市销率 || | 1.4956|
| AStockIndustryDB.LC_IndustryValuation | PS_LYR | 静态市销率(LYR)|| | 1.8657|
| AStockIndustryDB.LC_IndustryValuation | InsertTime | 发布时间 || | 2022-03-31 06:50:51.230 |
| AStockIndustryDB.LC_IndustryValuation | UpdateTime | 修改时间 || | 2024-08-28 02:41:33.077 |
| AStockIndustryDB.LC_IndustryValuation | JSID | JSID || | 778556320884|
| AStockIndustryDB.LC_IndustryValuation | IndustryName ||| | 焦炭Ⅲ |
| AStockIndustryDB.LC_IndustryValuation | Classification ||| | 3 |
| AStockIndustryDB.LC_IndustryValuation | ListedSecuNum||| | 9 |
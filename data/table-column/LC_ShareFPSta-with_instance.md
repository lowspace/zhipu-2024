| table_name| column_name| column_description | 注释 | Annotation | 数据示例 |
|---|---|---|---|---|---|
| AStockShareholderDB.LC_ShareFPSta | ID | ID ||| 545255016222 |
| AStockShareholderDB.LC_ShareFPSta | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.| 3954 |
| AStockShareholderDB.LC_ShareFPSta | FPCode | 冻结质押编号 | 数值型常量。冻结质押编号(FPCode)：与“股东股权冻结和质押（LC_ShareFP）”中的ID关联，得到股东股权冻结和质押进展情况。 | Numeric constant. Frozen Pledge Code (FPCode): Associated with the ID in "Shareholder Equity Freezing and Pledge (LC_ShareFP)" to obtain the progress of shareholder equity freezing and pledge. | 541903111169 |
| AStockShareholderDB.LC_ShareFPSta | EndDate| 截止日期 ||| 2017-03-04 12:00:00.000|
| AStockShareholderDB.LC_ShareFPSta | InfoSource | 信息来源 ||| 控股股东股权质押的公告 |
| AStockShareholderDB.LC_ShareFPSta | Category | 类别选择 | 数值型常量。类别选择(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1201，得到类别选择的具体描述：1-股权变动，2-股权冻结，3-股权质押，4-股权授权经营，5-股票质押式回购，21-债券增减持。 | Numeric constant. The category selection (Category) is associated with the DM field in the (CT_SystemConst) table, with LB set to 1201, the specific description of the category selection is: 1-Equity Change, 2-Equity Freezing, 3-Equity Pledge, 4-Equity Authorization Operation, 5-Stock Repurchase by Pledge, 21-Bond Increase and Decrease. | 3|
| AStockShareholderDB.LC_ShareFPSta | FPSHName | 股权被冻结质押股东名称 ||| 山东太阳控股集团有限公司 |
| AStockShareholderDB.LC_ShareFPSta | AccuFPShares | 累计冻结质押股数(股) ||| 587200000.0|
| AStockShareholderDB.LC_ShareFPSta | AccuPCTOfPled| 累计占冻结质押方持股数比例 ||| 0.414293 |
| AStockShareholderDB.LC_ShareFPSta | AccuProportion | 累计占总股本比例 ||| 0.2316 |
| AStockShareholderDB.LC_ShareFPSta | UpdateTime | 更新时间 ||| 2023-11-15 03:04:29.283|
| AStockShareholderDB.LC_ShareFPSta | AccuProportionCalc | 累计占总股本比例(计算) | 累计冻结质押股数(股)(计算)（AccuFPSharesCalc）：股东股权冻结和质押LC_ShareFP中该股东未解押的股数之和。 | Cumulative frozen pledged shares (shares) (calculation) (AccuFPSharesCalc): The sum of the number of shares not released by the shareholder in LC_ShareFP due to the shareholder's equity freeze and pledge. | 0.23155896 |
| AStockShareholderDB.LC_ShareFPSta | SHAttribute| 股权被冻结质押股东所属性质 ||| 2|
| AStockShareholderDB.LC_ShareFPSta | SHID | 股权被冻结质押股东ID ||| 72987|
| AStockShareholderDB.LC_ShareFPSta | JSID |||| 753366174567 |
| AStockShareholderDB.LC_ShareFPSta | AccuFPSharesCalc |||| 587200000.0|
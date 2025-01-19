| column_name| column_description | 注释 | Annotation |
|---|---|---|---|---|
| ID | ID |||
| FPCode | 冻结质押编号 | 冻结质押编号(FPCode)：与“股东股权冻结和质押（LC_ShareFP）”中的ID关联，得到股东股权冻结和质押进展情况。 | Frozen Pledge Code (FPCode): Associated with the ID in "Shareholder Equity Freezing and Pledge (LC_ShareFP)" to obtain the progress of shareholder equity freezing and pledge. |
| EndDate| 截止日期 |||
| InfoSource | 信息来源 |||
| Category | 类别选择 | 类别选择(Category)与(CT_SystemConst)表中的DM字段关联，令LB = 1201，得到类别选择的具体描述：1-股权变动，2-股权冻结，3-股权质押，4-股权授权经营，5-股票质押式回购，21-债券增减持。 | The category selection (Category) is associated with the DM field in the (CT_SystemConst) table, with LB set to 1201, the specific description of the category selection is: 1-Equity Change, 2-Equity Freezing, 3-Equity Pledge, 4-Equity Authorization Operation, 5-Stock Repurchase by Pledge, 21-Bond Increase and Decrease. |
| CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| FPSHName | 股权被冻结质押股东名称 |||
| AccuFPShares | 累计冻结质押股数(股) |||
| AccuPCTOfPled| 累计占冻结质押方持股数比例 |||
| AccuProportion | 累计占总股本比例 |||
| UpdateTime | 更新时间 |||
| AccuProportionCalc | 累计占总股本比例(计算) | 累计冻结质押股数(股)(计算)（AccuFPSharesCalc）：股东股权冻结和质押LC_ShareFP中该股东未解押的股数之和。 | Cumulative frozen pledged shares (shares) (calculation) (AccuFPSharesCalc): The sum of the number of shares not released by the shareholder in LC_ShareFP due to the shareholder's equity freeze and pledge. |
| SHAttribute| 股权被冻结质押股东所属性质 |||
| SHID | 股权被冻结质押股东ID |||
| JSID |  |||
| AccuFPSharesCalc |  |||
| table_name | column_name| column_description | 注释 | Annotation|
|---|---|---|---|---|
| LC_NationalStockHoldSt | ID | ID || |
| LC_NationalStockHoldSt | InnerCode| 内部编码 | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。 | Internal Code: Associated with the "InnerCode" in the "SecuMain" table, obtaining the security's trading code, abbreviation, etc. |
| LC_NationalStockHoldSt | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| LC_NationalStockHoldSt | EndDate| 截止日期 || |
| LC_NationalStockHoldSt | SHID | 股东ID | 数值型常量。股东ID（SHID）：与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联 | Numeric constant. Shareholder ID (SHID): associated with the Company Code in the Institutional Basic Information (LC_InstiArchive)|
| LC_NationalStockHoldSt | SHName | 股东名称 || |
| LC_NationalStockHoldSt | HoldAShareSum| 持有A股总数(股)|| |
| LC_NationalStockHoldSt | RestrainedAShare | 有限售A股数 || |
| LC_NationalStockHoldSt | UnstintedAShare| 无限售A股数 || |
| LC_NationalStockHoldSt | PCTOfTotalShares | 占总股本比例(%)|| |
| LC_NationalStockHoldSt | PCTOfFloatShares | 占流通A股比例(%)|| |
| LC_NationalStockHoldSt | HoldASumChange | 持有A股数量增减(股)|| |
| LC_NationalStockHoldSt | HoldASumChangeRate | 持有A股数量增减幅度(%) || |
| LC_NationalStockHoldSt | InsertTime | 发布时间 || |
| LC_NationalStockHoldSt | UpdateTime | 修改时间 || |
| LC_NationalStockHoldSt | JSID | JSID || |
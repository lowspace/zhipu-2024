| table_name | column_name | column_description | 注释 | Annotation | 数据示例|
|---|---|---|---|---|---|
| PublicFundDB.MF_FundProdName | ID| ID ||| 596367161784|
| PublicFundDB.MF_FundProdName | InnerCode | 基金内部编码 | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。 | Fund internal code (InnerCode): associated with the "security internal code (InnerCode)" in the "security main table (SecuMain)", to obtain the fund's trading code, abbreviation, etc.| 202914|
| PublicFundDB.MF_FundProdName | InfoPublDate| 信息发布日期 ||| 2019-02-11 12:00:00.000 |
| PublicFundDB.MF_FundProdName | InfoSource| 信息来源 ||| 上市交易公告书|
| PublicFundDB.MF_FundProdName | InfoType| 信息类别 | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1850，得到信息类别的具体描述：1-证券交易所简称，2-集中申购简称，3-ETF申购赎回简称，4-证监会简称，5-扩位证券简称，6-公告披露简称，8-基金全称。 | The InfoType is associated with the DM field in the CT_SystemConst table, setting LB to 1850 yields the specific description of the InfoType: 1-Stock Exchange Abbreviation, 2-Central Subscription Abbreviation, 3-ETF Subscription and Redemption Abbreviation, 4-CSRC Abbreviation, 5-Extended Security Abbreviation, 6-Announcement Disclosure Abbreviation, 8-Fund Full Name. | 1 |
| PublicFundDB.MF_FundProdName | DisclName | 披露名称 ||| 新经济HK|
| PublicFundDB.MF_FundProdName | EffectiveDate | 生效日期 ||| 2019-02-14 12:00:00.000 |
| PublicFundDB.MF_FundProdName | ExpiryDate| 失效日期 ||| null|
| PublicFundDB.MF_FundProdName | IfEffected| 是否有效 | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。 | Whether "IfEffected" is associated with the "DM" field in the "CT_SystemConst" table, let LB = 999 AND DM IN (1,2), to obtain the specific description of whether it is effective: 1-Yes, 2-No.| 1 |
| PublicFundDB.MF_FundProdName | Remark| 备注 ||| null|
| PublicFundDB.MF_FundProdName | UpdateTime| 更新时间 ||| 2022-06-21 03:28:55.580 |
| PublicFundDB.MF_FundProdName | JSID| JSID ||| 709107373104|
| PublicFundDB.MF_FundProdName | ChiSpelling | 拼音证券简称 ||| XJJHK |
| PublicFundDB.MF_FundProdName | TransCode | 基金转型统一编码 ||| 202914|
| PublicFundDB.MF_FundProdName | InsertTime| 插入时间 ||| 2018-11-24 09:32:41.783 |
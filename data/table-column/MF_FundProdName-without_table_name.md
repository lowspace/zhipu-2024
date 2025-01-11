| column_name | column_description | 注释 | Annotation |
|---|---|---|---|---|
| ID| ID |||
| InnerCode | 基金内部编码 | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。 | Fund internal code (InnerCode): associated with the "security internal code (InnerCode)" in the "security main table (SecuMain)", to obtain the fund's trading code, abbreviation, etc.|
| InfoPublDate| 信息发布日期 |||
| InfoSource| 信息来源 |||
| InfoType| 信息类别 | 信息类别(InfoType)与(CT_SystemConst)表中的DM字段关联，令LB = 1850，得到信息类别的具体描述：1-证券交易所简称，2-集中申购简称，3-ETF申购赎回简称，4-证监会简称，5-扩位证券简称，6-公告披露简称，8-基金全称。 | The InfoType is associated with the DM field in the CT_SystemConst table, setting LB to 1850 yields the specific description of the InfoType: 1-Stock Exchange Abbreviation, 2-Central Subscription Abbreviation, 3-ETF Subscription and Redemption Abbreviation, 4-CSRC Abbreviation, 5-Extended Security Abbreviation, 6-Announcement Disclosure Abbreviation, 8-Fund Full Name. |
| DisclName | 披露名称 |||
| EffectiveDate | 生效日期 |||
| ExpiryDate| 失效日期 |||
| IfEffected| 是否有效 | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。 | Whether "IfEffected" is associated with the "DM" field in the "CT_SystemConst" table, let LB = 999 AND DM IN (1,2), to obtain the specific description of whether it is effective: 1-Yes, 2-No.|
| Remark| 备注 |||
| UpdateTime| 更新时间 |||
| JSID| JSID |||
| ChiSpelling | 拼音证券简称 |||
| TransCode | 基金转型统一编码 |||
| InsertTime| 插入时间 |||
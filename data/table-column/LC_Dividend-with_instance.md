| table_name | column_name | column_description| 注释| Annotation | 数据示例|
|---|---|---|---|---|---|
| LC_Dividend| ID| ID| || 724442297984|
| LC_Dividend| InnerCode | 证券内部编码| 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。| Security Internal Code (InnerCode): Associated with the "Security Main Table (SecuMain)" "Security Internal Code (InnerCode)", to obtain the security's trading code, abbreviation, etc. | 36721 |
| LC_Dividend| EndDate | 日期| || 2021-12-31 12:00:00.000 |
| LC_Dividend| IfDividend| 是否分红| 是否分红(IfDividend)固定以下常量：0-否，1-是，8-对价，24-重整计划，25-特殊分红，26-面值拆分，99-其他分红。| Whether to distribute dividends (IfDividend) fixed the following constants: 0 - No, 1 - Yes, 8 - Consideration, 24 - Restructuring Plan, 25 - Special Dividend, 26 - Par Value Split, 99 - Other Dividends.| 1 |
| LC_Dividend| AdvanceDate | 预案发布日期| || 2022-03-31 12:00:00.000 |
| LC_Dividend| SMDeciPublDate| 股东大会决议公告日期| || 2022-04-23 12:00:00.000 |
| LC_Dividend| EPS | 每股收益(摊薄)(元/股) | || null|
| LC_Dividend| BonusShareRatio | 送股比例(10送X) | || null|
| LC_Dividend| TranAddShareRaio| 转增股比例(10转增X) | || null|
| LC_Dividend| PriceUnit | 期货单位| 派现外币单位（PriceUnit）：与“系统常量表（CT_SystemConst）”中的“常量代码（DM）”关联，令“LB=1068”，得到派现外币单位的具体描述。1000-美元，1100-港元。该字段主要记录B股分红涉及的外币单位，A股分红因通常单位都是人民币，故派现外币单位为NULL。| Distribution currency unit (PriceUnit): associated with "constant code (DM)" in "System Constants Table (CT_SystemConst)", set "LB=1068" to obtain the specific description of the distribution currency unit. 1000-USD, 1100-HKD. This field mainly records the foreign currency unit involved in B-share dividends, as A-share dividends are usually in RMB, the distribution currency unit is NULL. | null|
| LC_Dividend| CashDiviRMB | 派现(含税/人民币元) | || 2.0 |
| LC_Dividend| ActualCashDiviRMB | 实派(税后/人民币元) | || 2.0 |
| LC_Dividend| CashDiviFC| 派现(含税/外币) | || null|
| LC_Dividend| ActualCashDiviFC| 实派(税后/外币) | || null|
| LC_Dividend| RightRegDate| 股权登记日| || 2022-06-07 12:00:00.000 |
| LC_Dividend| ExDiviDate| 除权除息日| || 2022-06-08 12:00:00.000 |
| LC_Dividend| BonusShareListDate| 送转股上市日| || null|
| LC_Dividend| ToAccountDate | 红利到账日| || 2022-06-08 12:00:00.000 |
| LC_Dividend| FinalTradingDay | 最后交易日| || null|
| LC_Dividend| DiviBase| 分红股本基数(股)| || 2740855925.0|
| LC_Dividend| SharesAfterDivi | 送转后总股本(股)| || null|
| LC_Dividend| DiviObject| 分红对象| 分红对象(DiviObject)与(CT_SystemConst)表中的DM字段关联，令LB = 1197 AND DM IN (1,2,3)，得到分红对象的具体描述：1-全体股东，2-发行前股东，3-部分股东。 | The dividend object (DiviObject) is associated with the DM field in the (CT_SystemConst) table, with LB = 1197 AND DM IN (1,2,3), resulting in the specific description of the dividend object: 1 - all shareholders, 2 - shareholders before issuance, 3 - partial shareholders.| 1 |
| LC_Dividend| TotalCashDiviComRMB | 公司合计派现金额(人民币元)| || 548171185.0 |
| LC_Dividend| TotalCashDiviComFC| 公司合计派现金额(外币元)| || null|
| LC_Dividend| CashDiviAShare| A股派现金额(元) | || 548171185.0 |
| LC_Dividend| CashDiviBShareRMB | B股派现金额(人民币元) | || null|
| LC_Dividend| CashDiviBShareFC| B股派现金额(外币元) | || null|
| LC_Dividend| DiviStartDate | 红利发放起始日| || null|
| LC_Dividend| IFSchemeChange| 方案是否变更| 方案是否变更（IFSchemeChange），该字段固定以下常量：1-是；0-否| Whether the scheme changes (IFSchemeChange), this field is fixed with the following constants: 1-yes; 0-no.| 0 |
| LC_Dividend| ChangeStatement | 方案变动说明| || null|
| LC_Dividend| ChangeType| 变动原因| 方案变更类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1013，得到方案变更类型的具体描述：1-总量变更，2-总量不变，3-基数变更，4-基数不变，5-其他。 | The "ChangeType" scheme change type is associated with the "DM" field in the "CT_SystemConst" table, with LB = 1013, the specific description of the scheme change type is obtained: 1-Total amount change, 2-Total amount unchanged, 3-Base change, 4-Base unchanged, 5-Other.| null|
| LC_Dividend| IfDiviBeforeChange| 变更前是否分红| || null|
| LC_Dividend| BonusShareRatioBeforeChange | 变更前送股比例(10送X) | || null|
| LC_Dividend| TranAddShareRatioBeforeChange | 变更前转增股比例(10转增X) | || null|
| LC_Dividend| CashDiviBeforeChangeRMB | 变更前派现(含税/人民币元) | || null|
| LC_Dividend| CashDiviBeforeChangeFC| 变更前派现(含税/外币) | || null|
| LC_Dividend| DiviBaseBeforeChange| 变更前分红股本基数(股)| || null|
| LC_Dividend| Notes | 备注说明| || null|
| LC_Dividend| UndistributeStatement | 利润不分配说明| || null|
| LC_Dividend| DistributeTimes | 利润分配次数| || null|
| LC_Dividend| CeilingNext | 下限| || null|
| LC_Dividend| FloorNext | 上限| || null|
| LC_Dividend| Ceiling | 下限| || null|
| LC_Dividend| Floor | 上限| || null|
| LC_Dividend| MainForm| 主要分配形式| || null|
| LC_Dividend| CashDiviCeiling | 下限| || null|
| LC_Dividend| CashDiviFloor | 上限| || null|
| LC_Dividend| XGRQ| 修改日期| || 2022-12-23 04:02:46.940 |
| LC_Dividend| JSID| JSID| || 725353159074|
| LC_Dividend| DiviEndDate | 红利发放截止日| || null|
| LC_Dividend| DividendImplementDate | 分红实施公告日| || 2022-05-31 12:00:00.000 |
| LC_Dividend| EventProcedure| 事件进程| 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1000,1001,1004,3120,3125,3131,3305)，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，3120-董事会否决，3125-股东大会否决，3131-方案实施，3305-放弃。 | The event process (EventProcedure) is associated with the DM field in the (CT_SystemConst) table, let LB = 1059 AND DM IN (1000,1001,1004,3120,3125,3131,3305), to obtain the specific description of the event process: 1000 - Intention, 1001 - Plan, 1004 - Decision, 3120 - Board Rejection, 3125 - Shareholder Rejection, 3131 - Implementation of Plan, 3305 - Abandonment.| 3131|
| LC_Dividend| EventProcedureDesc| 事件进程描述| || 方案实施|
| LC_Dividend| BonusSHRatioAdjusted| 送股比例(10送X)(计算除权价用) | || null|
| LC_Dividend| TranAddRatioAdjusted| 转增比例(10转增X)(计算除权价用) | || null|
| LC_Dividend| CashDiviRMBAdjusted | 派现(含税10派X元)(计算除权价用) | || 2.0 |
| LC_Dividend| DiviObjectNew | 分红对象(新)| || 1 |
| LC_Dividend| BonusShareArrivalDate | 送转股到账日| || null|
| LC_Dividend| SchemeType| 方案类型| 方案类型(SchemeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1739，得到方案类型的具体描述：10-公司提出方案，20-股东提出方案，99-其它。| The scheme type (SchemeType) is associated with the DM field in the (CT_SystemConst) table, with LB set to 1739, the specific description of the scheme type is obtained: 10 - Company proposed scheme, 20 - Shareholder proposed scheme, 99 - Other.| 10|
| LC_Dividend| ExDiviRefPrice| 除权除息参考价(元)| || 6.95|
| LC_Dividend| DiviIntentPublDate| 分红意向公布日| || null|
| LC_Dividend| DividendBaseDate| 分红派息股本基准日| || 2022-05-31 12:00:00.000 |
| LC_Dividend| ProposalSN| 议案编号| || 1 |
| LC_Dividend| LatestInfoPublDate| 最新信息发布日期| || 2022-05-31 12:00:00.000 |
| LC_Dividend| SchemeStatement | | || null|
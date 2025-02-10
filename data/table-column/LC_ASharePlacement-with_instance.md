| table_name | column_name| column_description | 注释 | Annotation | 数据示例 |
|---|---|---|---|---|---|
| LC_ASharePlacement | ID | ID ||| 605659048983 |
| LC_ASharePlacement | InnerCode| 证券内部编码 ||| 383|
| LC_ASharePlacement | InitialInfoPublDate| 首次信息发布日期 ||| 2019-03-12 12:00:00.000|
| LC_ASharePlacement | PlaYear| 配股年度 ||| 2019-12-31 12:00:00.000|
| LC_ASharePlacement | StockType| 发行股票类型 | 发行股票类型(StockType)与(CT_SystemConst)表中的DM字段关联，令LB = 1177 AND DM IN (1,3)，得到发行股票类型的具体描述：1-A股，3-H股。 | The stock type (StockType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1177 AND DM IN (1,3), resulting in the specific description of the stock type: 1 - A shares, 3 - H shares. | 1|
| LC_ASharePlacement | AdvanceDate| 预案发布日期 ||| 2019-03-12 12:00:00.000|
| LC_ASharePlacement | SMDeciPublDate | 股东大会决议公告日期 ||| 2019-05-22 12:00:00.000|
| LC_ASharePlacement | PricingModel | 定价方式 | 配股价格确定方式(PricingModel)与(CT_SystemConst)表中的DM字段关联，令LB = 1113，得到配股价格确定方式的具体描述：1-设定区间，2-市价折扣。| The method for determining the right issue price (PricingModel) is associated with the DM field in the (CT_SystemConst) table. When LB equals 1113, the specific description of the method for determining the right issue price is obtained: 1 - Set range, 2 - Market discount.| 2|
| LC_ASharePlacement | PricingDescription | 配股价格确定方式说明 ||| 本次配股价格以刊登配股说明书前20个交易日公司股票均价为基数 |
| LC_ASharePlacement | AdvanceValidStartDate| 预案有效期起始日 ||| 2019-05-21 12:00:00.000|
| LC_ASharePlacement | AdvanceValidEndDate| 预案有效期截止日 ||| 2021-05-21 12:00:00.000|
| LC_ASharePlacement | PlaRatioPlanned| 计划配股比例(10配X)||| 3.0|
| LC_ASharePlacement | PlaPriceCeiling| 配股价格上限(最高价)(元) ||| null |
| LC_ASharePlacement | PlaPriceFloor| 配股价格下限(最低价)(元) ||| null |
| LC_ASharePlacement | DeciPublDate | 决案公布日 ||| 2019-05-22 12:00:00.000|
| LC_ASharePlacement | PlaProspectusPublDate| 配股说明书刊登日期 ||| null |
| LC_ASharePlacement | PlaAbbrName| 配股简称 ||| null |
| LC_ASharePlacement | PlaCode| 配股代码 ||| null |
| LC_ASharePlacement | BaseShares | 配股股本基数(股) ||| null |
| LC_ASharePlacement | PlannedPlaVol| 计划配股数量(股) ||| 3185582355.0 |
| LC_ASharePlacement | ActualPlaRatio | 实际配股比例(10配X)||| null |
| LC_ASharePlacement | ActualPlaVol | 实际配股数量(股) ||| null |
| LC_ASharePlacement | PlaObject| 配股对象 ||| 本次配股股权登记日当日收市后在中国证券登记结算有限责任公司深 |
| LC_ASharePlacement | ParValue | 面值(人民币) ||| 1.0|
| LC_ASharePlacement | PlaPrice | 每股配股价格(元) ||| null |
| LC_ASharePlacement | TransferPlaRatio | 转配比(10转配X)||| null |
| LC_ASharePlacement | TransferPlaVol | 转配股(股) ||| null |
| LC_ASharePlacement | TransferFeePerShare| 每股转配费(元) ||| null |
| LC_ASharePlacement | OddLotsTreatment | 零股处理方法 | 零股处理方法(OddLotsTreatment)与(CT_SystemConst)表中的DM字段关联，令LB = 1218，得到零股处理方法的具体描述：1-不足一股不予配售，2-不足一股四舍五入，3-不足一股累计后随机配售，4-不足一股依据精确算法处理。| The Odd Lots Treatment method is associated with the DM field in the CT_SystemConst table, with LB set to 1218, the specific description of the Odd Lots Treatment method is as follows: 1 - No allocation for less than one share, 2 - Round up for less than one share, 3 - Accumulate less than one share and allocate randomly, 4 - Handle less than one share based on precise algorithm. | 4|
| LC_ASharePlacement | PlaProceeds| 实际募集资金(元) ||| null |
| LC_ASharePlacement | PlaCost| 发行费用总额(元) ||| null |
| LC_ASharePlacement | UnderwritingFee| 承销费用(元) ||| null |
| LC_ASharePlacement | CPAFee | 注册会计师费用(元) ||| null |
| LC_ASharePlacement | AssetAppraisalFee| 资产评估费用(元) ||| null |
| LC_ASharePlacement | LandEvaluationFee| 土地评估费用(元) ||| null |
| LC_ASharePlacement | AttorneyFee| 律师费用(元) ||| null |
| LC_ASharePlacement | TotalAgentFee| 中介机构费合计(元) ||| null |
| LC_ASharePlacement | OnlineIssueFee | 上网发行费用(元) ||| null |
| LC_ASharePlacement | ScripFee | 股票登记费用(元) ||| null |
| LC_ASharePlacement | SponsorFee | 上市推荐费用(元) ||| null |
| LC_ASharePlacement | OtherFee | 其他费用(元) ||| null |
| LC_ASharePlacement | PlaNetProceeds | 募集资金净额(元) ||| null |
| LC_ASharePlacement | RightRegDate | 股权登记日 ||| 2019-05-10 12:00:00.000|
| LC_ASharePlacement | ExRightDate| 除权日 ||| null |
| LC_ASharePlacement | PayStartDate | 缴费起始 ||| null |
| LC_ASharePlacement | PayEndDate | 缴费截止 ||| null |
| LC_ASharePlacement | DateToAccount| 募集资金到帐时间 ||| null |
| LC_ASharePlacement | MoneyToAccount | 募集资金到帐金额(元) ||| null |
| LC_ASharePlacement | PlaListDate| 配股上市日 ||| null |
| LC_ASharePlacement | LargeSHSubsStatement | 大股东认配说明 ||| 公司控股股东邯郸钢铁集团有限责任公司及其一致行动人唐山钢铁集 |
| LC_ASharePlacement | SchemeChange | 方案是否变更 | 方案是否变更(SchemeChange)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案是否变更的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，17-重新发行，18-未发行，19-宣布发行不成功。| Whether the scheme changes (SchemeChange) is associated with the DM field in the (CT_SystemConst) table, let LB = 1194, to obtain the specific description of whether the scheme changes: 1 - No, 2 - Yes, 3 - Abandoned or defeated by the shareholders' meeting, 4 - Convertible bonds changed to public offering, 5 - Convertible bonds changed to rights issue, 6 - Public offering changed to rights issue, 7 - Public offering changed to convertible bonds, 8 - Rights issue changed to convertible bonds, 9 - Rights issue changed to public offering, 10 - Not approved, 11 - Change in offering size, 12 - Extend the validity period, 13 - Others, 14 - Issuance unsuccessful after recall, 15 - Delayed and not issued, 16 - Dividend adjustment of exercise price, 17 - Reissue, 18 - Not issued, 19 - Announced issuance unsuccessful. | 3|
| LC_ASharePlacement | ChangeStatement| 方案变动说明 ||| 2020-11-10公告:公司决定终止本次配股事宜;2020 |
| LC_ASharePlacement | UnderwritingMode | 承销方式 | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销，5-限额包销，8-非包销，9-余额包销及代销相结合，10-自销及代销相结合。 | The underwriting mode (UnderwritingMode) is associated with the DM field in the CT_SystemConst table. When LB equals 1017, the specific description of the underwriting mode is obtained: 1-Full underwriting, 2-Balance underwriting, 3-Agent underwriting, 4-Self-underwriting, 5-Quota underwriting, 8-Non-underwriting, 9-Combination of balance underwriting and agent underwriting, 10-Combination of self-underwriting and agent underwriting.| 3|
| LC_ASharePlacement | UnderwriterBoughtVol | 余股包销数量(股) ||| null |
| LC_ASharePlacement | PublicSHSubscriptionEsti | 公众股东预计认配股数(股) ||| 3185582355.0 |
| LC_ASharePlacement | PublicSHSubscriptionActu | 公众股东实际认配股数(股) ||| null |
| LC_ASharePlacement | XGRQ | 修改日期 ||| 2022-09-27 03:35:38.190|
| LC_ASharePlacement | JSID | JSID ||| 717620475990 |
| LC_ASharePlacement | PlannedPlaProceeds | 计划募集资金总额(元) ||| 8000000000.0 |
| LC_ASharePlacement | AdjustedPlaRatioPl | 最新计划配股比例(10配X)||| 3.0|
| LC_ASharePlacement | AdjustedPlaVolPl | 最新计划配股数量(股) ||| 3185582355.0 |
| LC_ASharePlacement | UWSponFee| 1)承销保荐费用合计(元) ||| null |
| LC_ASharePlacement | CPAAppraisalFee| 2)审计验资及评估费用合计(元) ||| null |
| LC_ASharePlacement | CSRCIACApprovalDate| 证监会发审委通过公告日 ||| 2019-12-20 12:00:00.000|
| LC_ASharePlacement | SASACApprovalPublDate| 国资委通过公告日 ||| 2019-05-08 12:00:00.000|
| LC_ASharePlacement | CSRCApprovalPublDate | 证监会批准公告日 ||| 2020-01-18 12:00:00.000|
| LC_ASharePlacement | ExApprovalPublDate | 交易所审核通过日 ||| null |
| LC_ASharePlacement | IssueMethod| 发行方式 | 发行方式(IssueMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2375，得到发行方式的具体描述：1-网上定价，2-无限售流通股网上定价、有限售流通股网下定价，3-其他。 | The issue method (IssueMethod) is associated with the DM field in the (CT_SystemConst) table, setting LB to 2375 yields the specific description of the issue method: 1 - Online pricing, 2 - Online pricing for unrestricted tradable shares, and offline pricing for restricted tradable shares, 3 - Other.| null |
| LC_ASharePlacement | EventProcedureCode | 事件进程 | 事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。 | The event process (EventProcedureCode) is associated with the DM field in the (CT_SystemConst) table, setting LB = 1640, the specific description of the event process is as follows: 1-Intention, 10-Board Resolution, 20-Shareholders' Meeting Approval, 21-SASAC Approval, 22-CSRC Approval, 23-CSRC Approval, 24-Listing Committee Approval, 25-CBRC Approval, 26-CSRC Acceptance, 29-Implementation in Progress, 30-Implementation Completed, 40-SASAC Rejection, 41-Shareholders' Meeting Rejection, 42-CSRC Rejection, 43-CSRC Rejection, 44-Listing Committee Rejection, 45-Board Rejection, 50-Deferred Implementation, 60-Stop Implementation, 61-Terminated Before Issuance, 62-Terminated After Issuance, 70-Suspended Issuance, 80-Registration in Process, 90-Implementation Failed. | 60 |
| LC_ASharePlacement | LatestInfoPublDate | 最新公告日期 ||| 2020-11-10 12:00:00.000|
| LC_ASharePlacement | PlaProspectus| 配股说明 ||| 2019年配股方案停止实施：每10股配3.0000股 |
| LC_ASharePlacement | ResultPulbDate | 配股结果公告日 ||| null |
| LC_ASharePlacement | ListAnnounceDate | 配股上市公告日 ||| null |
| LC_ASharePlacement | PlannedBaseShares| 计划配股股本基数(股) ||| 10618607852.0|
| LC_ASharePlacement | PlaObjectCategory| 配股对象类别 | 配股对象类别(PlaObjectCategory)与(CT_SystemConst)表中的DM字段关联，令LB=1197 and DM in (1,7,10) ，得到配股对象类别的具体描述：1-全体股东，7-无限售股东，10-流通股东。| The "PlaObjectCategory" is associated with the "DM" field in the "CT_SystemConst" table. With LB=1197 and DM in (1,7,10), the specific description of the share allocation object category is obtained: 1-All shareholders, 7-Shareholders without restriction, 10-Circulating shareholders. | 1|
| LC_ASharePlacement | PlaBaseDate| 配股基准日 ||| 2019-05-10 12:00:00.000|
| LC_ASharePlacement | LargeSHHoldSum | 持股5%以上大股东持股数(股) ||| 6072172763.0 |
| LC_ASharePlacement | LargeSHSubscripEsti| 持股5%以上大股东计划认配股数(股) ||| 1821651829.0 |
| LC_ASharePlacement | LargeSHSubscripActu| 持股5%以上大股东实际认配股数(股) ||| null |
| LC_ASharePlacement | NAPSAfterAllotment | 配股完成后预计每股净资产(元) ||| null |
| LC_ASharePlacement | EPSAfterAllotment| 配股完成后预计每股收益(元) ||| null |
| LC_ASharePlacement | InsertTime | 发布时间 ||| 2019-03-11 10:37:29.350|
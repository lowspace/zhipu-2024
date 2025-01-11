| table_name| column_name| column_description | 注释 | Annotation|
|---|---|---|---|---|
| LC_AShareSeasonedNewIssue | ID | ID || |
| LC_AShareSeasonedNewIssue | InnerCode| 证券内部编码 || |
| LC_AShareSeasonedNewIssue | InitialInfoPublDate| 首次信息发布日期 || |
| LC_AShareSeasonedNewIssue | AdvanceDate| 预案发布日期 || |
| LC_AShareSeasonedNewIssue | SMDeciPublDate | 股东大会决议公告日期 || |
| LC_AShareSeasonedNewIssue | AdvanceValidStartDate| 预案有效期起始日 || |
| LC_AShareSeasonedNewIssue | AdvanceValidEndDate| 预案有效期截止日 || |
| LC_AShareSeasonedNewIssue | IntentLetterPublDate | 招股公告日(招股意向书发布日期) || |
| LC_AShareSeasonedNewIssue | ProspectusPublDate | 招股说明书发布日期 || |
| LC_AShareSeasonedNewIssue | StockType| 发行股票类型 || |
| LC_AShareSeasonedNewIssue | PriceIntervalStatement | 发行价区间确定方式说明 || |
| LC_AShareSeasonedNewIssue | PricingModel | 定价方式 || |
| LC_AShareSeasonedNewIssue | RationModel| 发行量定量方式 || |
| LC_AShareSeasonedNewIssue | IssueMethod| 发行方式 || |
| LC_AShareSeasonedNewIssue | IssueObject| 发行对象 || |
| LC_AShareSeasonedNewIssue | IssuePriceCeiling| 发行价上限(最高价)(元) || |
| LC_AShareSeasonedNewIssue | IssuePriceFloor| 发行价下限(元) || |
| LC_AShareSeasonedNewIssue | ReferringPrice | 承销商指导价格(元) || |
| LC_AShareSeasonedNewIssue | IssueVolCeiling| 发行量上限(不多于)(股) || |
| LC_AShareSeasonedNewIssue | IssueVolFloor| 发行量下限(股) || |
| LC_AShareSeasonedNewIssue | OverAllotmentOption| 超额配售权(股) || |
| LC_AShareSeasonedNewIssue | IssueStartDate | 发行日期上限 || |
| LC_AShareSeasonedNewIssue | IssueEndDate | 发行日期下限 || |
| LC_AShareSeasonedNewIssue | UnderwritingStartDate| *承销期上限|| |
| LC_AShareSeasonedNewIssue | UnderwritingEndDate| *承销期下限|| |
| LC_AShareSeasonedNewIssue | IfExRightAShare| A股除权与否| A股除权与否（IfExRightAShare）：固定常量：1->是0->否 | Whether A-share is ex-right (IfExRightAShare): Fixed constant: 1 -> Yes, 0 -> No|
| LC_AShareSeasonedNewIssue | RightRegDate | 股权登记日 || |
| LC_AShareSeasonedNewIssue | ExRightDate| 除权日 || |
| LC_AShareSeasonedNewIssue | SuspendStartDate | 停牌时间起始日 || |
| LC_AShareSeasonedNewIssue | SuspendEndDate | 停牌时间截止日 || |
| LC_AShareSeasonedNewIssue | PrefPlaDateH | 老股东优先配售日期 || |
| LC_AShareSeasonedNewIssue | PrefPlaRatioH| 老股东优先配售比例(10配X)|| |
| LC_AShareSeasonedNewIssue | PrefPlaApplyCodeH| 老股东优先配售申购代码 || |
| LC_AShareSeasonedNewIssue | PrefPlaApplyAbbrNameH| 老股东优先配售申购简称 || |
| LC_AShareSeasonedNewIssue | IssueDateOnline| 上网公开发行日期 || |
| LC_AShareSeasonedNewIssue | ApplyCodeOnline| 上网发行申购代码 || |
| LC_AShareSeasonedNewIssue | ApplyAbbrNameOnline| 上网发行申购简称 || |
| LC_AShareSeasonedNewIssue | ApplyUnitOnline| 上网发行认购单位(股) || |
| LC_AShareSeasonedNewIssue | ApplyMaxOnline | 上网发行申购上限(股) || |
| LC_AShareSeasonedNewIssue | ApplyStartDateLPOffline| 法人网下配售申购日期起始日 || |
| LC_AShareSeasonedNewIssue | ApplyEndDateLPOffline| 法人网下配售申购日期截止日 || |
| LC_AShareSeasonedNewIssue | PayStartDateLPOffline| 法人网下申购缴款开始日 || |
| LC_AShareSeasonedNewIssue | PlaPayEndDateLPOffline | 法人网下申购缴款截止日 || |
| LC_AShareSeasonedNewIssue | ApplyUnitLPOffline | 法人网下配售认购单位(股) || |
| LC_AShareSeasonedNewIssue | ApplyMinLPOffline| 法人网下配售申购下限(股) || |
| LC_AShareSeasonedNewIssue | ApplyMaxLPOffline| 法人网下配售申购上限(股) || |
| LC_AShareSeasonedNewIssue | ValidApplyTimesLPOffline | 法人网下配售有效申购次数限定 | 法人网下配售有效申购次数限定(ValidApplyTimesLPOffline)与(CT_SystemConst)表中的DM字段关联，令LB = 1195，得到法人网下配售有效申购次数限定的具体描述：1-多次申购，2-一次申购。| The valid application times for offline allocation to legal persons (ValidApplyTimesLPOffline) is associated with the DM field in the CT_SystemConst table. When LB equals 1195, the specific description for the valid application times for offline allocation to legal persons is: 1 for multiple applications, 2 for a single application.|
| LC_AShareSeasonedNewIssue | ApplyStartDateF| *基金优先配售申购日期上限|| |
| LC_AShareSeasonedNewIssue | ApplyEndDateF| *基金优先配售申购日期下限|| |
| LC_AShareSeasonedNewIssue | PayStartDateF| *基金优先配售缴款期下限|| |
| LC_AShareSeasonedNewIssue | PayEndDateF| *基金优先配售缴款期上限|| |
| LC_AShareSeasonedNewIssue | PrefAllotmentF | 投资基金配售限额(股) || |
| LC_AShareSeasonedNewIssue | PrefAllotmentSingleF | 单个基金配售限额(股) || |
| LC_AShareSeasonedNewIssue | STAQNETPlaStartDate| STAQ/NET定向配售时间起始日 || |
| LC_AShareSeasonedNewIssue | STAQNETPlaEndDate| STAQ/NET定向配售时间截止日 || |
| LC_AShareSeasonedNewIssue | STAQNETPlaRatio| STAQ/NET定向配售比例(10配X)|| |
| LC_AShareSeasonedNewIssue | QuotationUnitOnline| 网上申购报价单位(元) || |
| LC_AShareSeasonedNewIssue | QuotationUnitOffline | 网下申购报价单位(元) || |
| LC_AShareSeasonedNewIssue | OddLotsTreatment | 零股处理方法 || |
| LC_AShareSeasonedNewIssue | ParValue | 面值(人民币) || |
| LC_AShareSeasonedNewIssue | IssuePrice | 实际发行价(元) || |
| LC_AShareSeasonedNewIssue | StateSharesIssuePrice| *国有股存量发行每股发行价(元)|| |
| LC_AShareSeasonedNewIssue | WeightedPERatio| 发行市盈率(加权平均)(倍) || |
| LC_AShareSeasonedNewIssue | DilutedPERatio | 发行市盈率(全面摊薄)(倍) || |
| LC_AShareSeasonedNewIssue | IssueVol | 发行量(股) || |
| LC_AShareSeasonedNewIssue | StateSharesIssued| *国有股存量发行股数(股)|| |
| LC_AShareSeasonedNewIssue | TotalIssueMV | 发行总市值(元) || |
| LC_AShareSeasonedNewIssue | IssueCost| 发行费用总额(元) || |
| LC_AShareSeasonedNewIssue | UnderwritingFee| 承销费用(元) || |
| LC_AShareSeasonedNewIssue | CPAFee | 注册会计师费用(元) || |
| LC_AShareSeasonedNewIssue | AssetAppraisalFee| 资产评估费用(元) || |
| LC_AShareSeasonedNewIssue | LandEvaluationFee| 土地评估费用(元) || |
| LC_AShareSeasonedNewIssue | AttorneyFee| 律师费用(元) || |
| LC_AShareSeasonedNewIssue | TotalAgentFee| 中介机构费合计(元) || |
| LC_AShareSeasonedNewIssue | OnlineIssueFee | 上网发行费用(元) || |
| LC_AShareSeasonedNewIssue | ScripFee | 股票登记费用(元) || |
| LC_AShareSeasonedNewIssue | SponsorFee | 上市推荐费用(元) || |
| LC_AShareSeasonedNewIssue | OtherFee | 其他费用(元) || |
| LC_AShareSeasonedNewIssue | IssueCostPerShare| 每股发行费用(元/股)|| |
| LC_AShareSeasonedNewIssue | FreezedMoney | 冻结资金(元) || |
| LC_AShareSeasonedNewIssue | SNIProceeds| 增发新股募集资金总额(元) || |
| LC_AShareSeasonedNewIssue | SNINetProceeds | 增发新股募集资金净额(元) || |
| LC_AShareSeasonedNewIssue | StateSharesProceeds| *国有股存量发行收入总额(元)|| |
| LC_AShareSeasonedNewIssue | StateSharesNetProceeds | *国有股存量发行收入净额(元)|| |
| LC_AShareSeasonedNewIssue | MoneyToAccount | 募集资金到帐金额(元) || |
| LC_AShareSeasonedNewIssue | DateToAccount| 募集资金到帐时间 || |
| LC_AShareSeasonedNewIssue | NewShareListDate | 增发股份上市日期 || |
| LC_AShareSeasonedNewIssue | OutstandingShares| 本次上市流通股数(股) || |
| LC_AShareSeasonedNewIssue | PutBackVol | 网上网下回拨股数(股) || |
| LC_AShareSeasonedNewIssue | PrefPlaVolH| 原股东优先配售股数(股) || |
| LC_AShareSeasonedNewIssue | PublicOfferVolOnline | 上网公开发行股数(股) || |
| LC_AShareSeasonedNewIssue | ValidApplyVolOnline| 网上发行有效申购总量(股) || |
| LC_AShareSeasonedNewIssue | ValidApplyNumOnline| 网上发行有效申购户数(户) || |
| LC_AShareSeasonedNewIssue | OverSubsTimesOnline| 网上发行超额认购倍数(倍) || |
| LC_AShareSeasonedNewIssue | LotRateOnline| 网上发行中签率 || |
| LC_AShareSeasonedNewIssue | PlaVolLPOffline| 法人网下配售股数(股) || |
| LC_AShareSeasonedNewIssue | ValidApplyVolLPOffline | 法人网下配售有效申购总量(股) || |
| LC_AShareSeasonedNewIssue | ValidApplyNumLPOffline | 法人网下配售有效申购户数(户) || |
| LC_AShareSeasonedNewIssue | OverSubsTimesLPOffline | 法人网下配售超额认购倍数(倍) || |
| LC_AShareSeasonedNewIssue | LotRateLPOffline | 法人网下配售中签率 || |
| LC_AShareSeasonedNewIssue | PlaVolF| 投资基金配售股数(股) || |
| LC_AShareSeasonedNewIssue | PlaVolSTAQNET| STAQ/NET定向配售股数(股) || |
| LC_AShareSeasonedNewIssue | TailoredPlaVolLP | 法人定向配售股数/战略定向配售(股)|| |
| LC_AShareSeasonedNewIssue | EarningForecastYear| 盈利预测年度 || |
| LC_AShareSeasonedNewIssue | MainIncomeForecast | 主营业务收入预测(元) || |
| LC_AShareSeasonedNewIssue | NetProfitForecast| 净利润预测(元) || |
| LC_AShareSeasonedNewIssue | DilutedEPSForecast | 全面摊薄每股盈利预测(元) || |
| LC_AShareSeasonedNewIssue | UnderwritingMode | 承销方式 | 承销方式(UnderwritingMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1017 AND DM IN (1,2,3,4)，得到承销方式的具体描述：1-全额包销，2-余额包销，3-代销，4-自销。| The underwriting mode (UnderwritingMode) is associated with the DM field in the CT_SystemConst table, with LB = 1017 AND DM IN (1,2,3,4), yielding the specific description of the underwriting mode: 1-Full underwriting, 2-Balance underwriting, 3-Agent selling, 4-Self-selling. |
| LC_AShareSeasonedNewIssue | UnderwriterBoughtVol | 余股包销数量(股) || |
| LC_AShareSeasonedNewIssue | ChangeStatement| 方案变动说明 || |
| LC_AShareSeasonedNewIssue | ChangeType | 变动原因 | 方案变动类型(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1194，得到方案变动类型的具体描述：1-否，2-是，3-放弃或股东大会否决，4-可转债改增发，5-可转债改配股，6-增发改配股，7-增发改可转债，8-配股改可转债，9-配股改增发，10-未核准，11-更改发行规模，12-延长有效期，13-其他，14-回拨后发行未成功，15-推迟未发行，16-分红调整行使价，17-重新发行，18-未发行，19-宣布发行不成功。| The scheme change type (ChangeType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1194, the specific description of the scheme change type is obtained: 1-No, 2-Yes, 3-Abandon or defeated by the shareholders' meeting, 4-Convertible bonds changed to public offering, 5-Convertible bonds changed to rights issue, 6-Increase issue changed to rights issue, 7-Increase issue changed to convertible bonds, 8-Rights issue changed to convertible bonds, 9-Rights issue changed to public offering, 10-Not approved, 11-Change in offering size, 12-Extend the validity period, 13-Other, 14-Issuance unsuccessful after recall, 15-Postponed and not issued, 16-Dividend adjustment of exercise price, 17-Renewed issuance, 18-Not issued, 19-Announced issuance unsuccessful. |
| LC_AShareSeasonedNewIssue | XGRQ | 修改日期 || |
| LC_AShareSeasonedNewIssue | JSID | JSID || |
| LC_AShareSeasonedNewIssue | PERatioBeforeIssue | 发行市盈率(按发行前总股本)(倍) || |
| LC_AShareSeasonedNewIssue | PERatioAfterIssue| 发行市盈率(按发行后总股本预测利润)(倍) || |
| LC_AShareSeasonedNewIssue | PrefPlaVolHMax | 原股东可配售股数(最多)(股) || |
| LC_AShareSeasonedNewIssue | PrefPlaVolHOnline| 原股东网上认购优先配售(股) || |
| LC_AShareSeasonedNewIssue | PrefPlaVolHOffline | 原股东网下认购优先配售(股) || |
| LC_AShareSeasonedNewIssue | ValidApplyHNum | 原股东有效申购户数(户) || |
| LC_AShareSeasonedNewIssue | ValidApplyNumHOnline | 原股东网上认购有效申购户数(户) || |
| LC_AShareSeasonedNewIssue | ValidApplyNumHOffline| 原股东网下认购有效申购户数(户) || |
| LC_AShareSeasonedNewIssue | APlaVolLPOffline | A类法人网下配售股数(股)|| |
| LC_AShareSeasonedNewIssue | AValidApplyVolLPOffline| A类法人网下配售有效申购总量(股)|| |
| LC_AShareSeasonedNewIssue | AValidApplyNumLPOffline| A类法人网下配售有效申购户数(户)|| |
| LC_AShareSeasonedNewIssue | ALotRateLPOffline| A类法人网下配售中签率|| |
| LC_AShareSeasonedNewIssue | BPlaVolLPOffline | B类法人网下配售股数(股)|| |
| LC_AShareSeasonedNewIssue | BValidApplyVolLPOffline| B类法人网下配售有效申购总量(股)|| |
| LC_AShareSeasonedNewIssue | BValidApplyNumLPOffline| B类法人网下配售有效申购户数(户)|| |
| LC_AShareSeasonedNewIssue | BLotRateLPOffline| B类法人网下配售中签率|| |
| LC_AShareSeasonedNewIssue | PlaVolHOffline | 原股东网下配售股数(股) || |
| LC_AShareSeasonedNewIssue | ValidPlaVolHOffline| 原股东网下配售有效申购总量(股) || |
| LC_AShareSeasonedNewIssue | ValidPlaNumHOffline| 原股东网下配售有效申购户数(户) || |
| LC_AShareSeasonedNewIssue | LotRateHOffline| 原股东网下配售中签率 || |
| LC_AShareSeasonedNewIssue | SASACApprovalPublDate| 国资委通过公告日 || |
| LC_AShareSeasonedNewIssue | CSRCApprovalPublDate | 证监会批准公告日 || |
| LC_AShareSeasonedNewIssue | EventProcedureCode | 事件进程 | 事件进程(EventProcedureCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1640，得到事件进程的具体描述：1-意向，10-董事会预案，20-股东大会通过，21-国资委通过，22-发审委通过，23-证监会通过，24-上市委通过，25-银保监会通过，26-证监会受理，29-实施中，30-实施完成，40-国资委否决，41-股东大会否决，42-证监会否决，43-发审委否决，44-上市委否决，45-董事会否决，50-延期实施，60-停止实施，61-发行前终止，62-发行后终止，70-暂缓发行，80-注册中，90-实施失败。 | The event process (EventProcedureCode) is associated with the DM field in the (CT_SystemConst) table, setting LB = 1640, the specific description of the event process is as follows: 1-Intention, 10-Board Resolution, 20-Shareholders' Meeting Approval, 21-SASAC Approval, 22-CSRC Approval, 23-CSRC Approval, 24-Listing Committee Approval, 25-CBRC Approval, 26-CSRC Acceptance, 29-Implementation in Progress, 30-Implementation Completed, 40-SASAC Rejection, 41-Shareholders' Meeting Rejection, 42-CSRC Rejection, 43-CSRC Rejection, 44-Listing Committee Rejection, 45-Board Rejection, 50-Deferred Implementation, 60-Stop Implementation, 61-Terminated Before Issuance, 62-Terminated After Issuance, 70-Suspended Issuance, 80-Registration in Process, 90-Implementation Failed.|
| LC_AShareSeasonedNewIssue | ISOBTypeCode | 发行对象类型 || |
| LC_AShareSeasonedNewIssue | AdjustedIssuePrice | 最新发行价下限(元) || |
| LC_AShareSeasonedNewIssue | PriceAdjustedDate| 最新发行价调整日 || |
| LC_AShareSeasonedNewIssue | SchemeChangePublDate | 方案变动公告日 || |
| LC_AShareSeasonedNewIssue | ListAnnounceDate | 增发新股上市公告日期 || |
| LC_AShareSeasonedNewIssue | ProjInfoSource | 预案信息来源 || |
| LC_AShareSeasonedNewIssue | IssueResultInfoSource| 发行结果信息来源 || |
| LC_AShareSeasonedNewIssue | AdjustedIssueVol | 最新发行量上限(股) || |
| LC_AShareSeasonedNewIssue | PriceVolAdjustedDate | 最新发行价及发行量调整日 || |
| LC_AShareSeasonedNewIssue | IssuePurpose | 发行目的 || |
| LC_AShareSeasonedNewIssue | PricingBaseDate| 定价基准日 || |
| LC_AShareSeasonedNewIssue | PricingBaseDateDesc| 定价基准日描述 || |
| LC_AShareSeasonedNewIssue | IssueType| 增发类别 | 增发类别(IssueType)与(CT_SystemConst)表中的DM字段关联，令LB = 1016 AND DM IN (21,22,23)，得到增发类别的具体描述：21-非公开增发，22-公开增发，23-非公开增发配套融资。 | The "IssueType" is associated with the "DM" field in the "CT_SystemConst" table, with LB = 1016 AND DM IN (21,22,23), yielding the specific description of the issue type: 21-Non-public issuance, 22-Public issuance, 23-Non-public issuance with配套 financing. |
| LC_AShareSeasonedNewIssue | IfEffected | 是否有效 | 是否有效（IfEffected）的具体描述：1-是（代表增发处于正常有效状态），2-否（代表增发处于已终止或否决等无效状态）。 | Specific description of whether it is effective (IfEffected): 1-yes (representing that the issuance is in a normal effective state), 2-no (representing that the issuance is in an invalid state such as terminated or rejected). |
| LC_AShareSeasonedNewIssue | SubscribeMethod| 认购方式 | 认购方式(SubscribeMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。| The subscription method (SubscribeMethod) is associated with the DM field in the (CT_SystemConst) table. Setting LB = 2259, the specific description of the subscription method is obtained: 1-cash, 2-fixed assets, 3-debt, 4-cash and fixed assets, 5-cash and debt, 6-cash, debt and fixed assets, 7-equity, 8-cash and equity, 9-equity and debt, 10-equity and fixed assets, 11-debt and fixed assets, 12-cash, equity and fixed assets, 13-cash, equity and debt, 14-equity, debt and fixed assets, 15-cash, equity, debt and fixed assets, 99-others.|
| LC_AShareSeasonedNewIssue | LargeSHSubMethod | 控股股东认购方式 | 控股股东认购方式(LargeSHSubMethod)与(CT_SystemConst)表中的DM字段关联，令LB = 2259，得到控股股东认购方式的具体描述：1-现金，2-固定资产，3-债权，4-现金及固定资产，5-现金及债权，6-现金、债权及固定资产，7-股权，8-现金及股权，9-股权及债权，10-股权及固定资产，11-债权及固定资产，12-现金、股权及固定资产，13-现金、股权及债权，14-股权、债权及固定资产，15-现金、股权、债权及固定资产，99-其他。 | The method of subscription by the controlling shareholder (LargeSHSubMethod) is associated with the DM field in the (CT_SystemConst) table. Setting LB = 2259, the specific description of the method of subscription by the controlling shareholder is obtained: 1-cash, 2-fixed assets, 3-claims, 4-cash and fixed assets, 5-cash and claims, 6-cash, claims and fixed assets, 7-equity, 8-cash and equity, 9-equity and claims, 10-equity and fixed assets, 11-claims and fixed assets, 12-cash, equity and fixed assets, 13-cash, equity and claims, 14-equity, claims and fixed assets, 15-cash, equity, claims and fixed assets, 99-others. |
| LC_AShareSeasonedNewIssue | LargeSHSubsSum | 控股股东认购数量(股) || |
| LC_AShareSeasonedNewIssue | LargeSHSubsRatio | 控股股东认购比例(%)|| |
| LC_AShareSeasonedNewIssue | PlannedProceeds| 预计募集资金总额(元) || |
| LC_AShareSeasonedNewIssue | CurrencyProceeds | 货币募集资金总额(元) || |
| LC_AShareSeasonedNewIssue | NonCurrencyProceeds| 非货币募集资金总额(元) || |
| LC_AShareSeasonedNewIssue | AssetProceeds| 其中:资产募集资金总额(元)|| |
| LC_AShareSeasonedNewIssue | DebtProceeds | 其中:债权募集资金总额(元)|| |
| LC_AShareSeasonedNewIssue | UWSponFee| 1)承销保荐费用合计(元) || |
| LC_AShareSeasonedNewIssue | CPAAppraisalFee| 2)审计验资及评估费用合计(元) || |
| LC_AShareSeasonedNewIssue | ParValueCurrencyUnit | 每股面值货币单位 || |
| LC_AShareSeasonedNewIssue | AdjustedVolFloor | 最新发行量下限(股) || |
| LC_AShareSeasonedNewIssue | AdjustedPriceCeiling | 最新发行价上限(元) || |
| LC_AShareSeasonedNewIssue | DiscountRatePerShare | 每股发行价折扣率(%)|| |
| LC_AShareSeasonedNewIssue | SubscriptionOfferDate| 认购邀请书发送日 || |
| LC_AShareSeasonedNewIssue | OrgPriceBasePRatio | 预案价格相对基准价格比例(%)|| |
| LC_AShareSeasonedNewIssue | ActPriceBasePRatio | 实施价格相对基准价格比例(%)|| |
| LC_AShareSeasonedNewIssue | AddSubscriptionSDate | 追加认购起始日 || |
| LC_AShareSeasonedNewIssue | AddSubscriptionEDate | 追加认购截止日 || |
| LC_AShareSeasonedNewIssue | VerificationDate | 募集资金验资日 || |
| LC_AShareSeasonedNewIssue | LatestAdvanceDate| 最新预案公布日期 || |
| LC_AShareSeasonedNewIssue | IfSummaryProcedure | 是否简易程序 | 是否简易程序（IfSummaryProcedure）的具体描述：1-是（代表本次增发为简易程序增发）。 | Specific description of the simplified procedure (IfSummaryProcedure): 1-yes (indicating that this issue is a simplified procedure issue).|
| LC_AShareSeasonedNewIssue | InsertTime | 发布时间 || |
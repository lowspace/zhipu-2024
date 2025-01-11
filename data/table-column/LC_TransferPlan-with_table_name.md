| table_name| column_name| column_description | 注释| Annotation |
|---|---|---|---|---|
| LC_TransferPlan | ID | ID  | | |
| LC_TransferPlan | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。| Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.|
| LC_TransferPlan | InitialInfoPublDate| 首次信息发布日期  | | |
| LC_TransferPlan | InfoPublDate | 信息发布日期  | | |
| LC_TransferPlan | InfoSource | 信息来源  | | |
| LC_TransferPlan | PromiseSubject | 承诺主体类型 | 承诺主体类型(PromiseSubject)与(CT_SystemConst)表中的DM字段关联，令LB = 1351 AND DM<>300，得到承诺主体类型的具体描述：100-非流通股东，110-间接控股股东，150-流通股东，500-公司管理层。 | The PromiseSubject type is associated with the DM field in the CT_SystemConst table, with LB = 1351 AND DM<>300, the specific description of the PromiseSubject type is: 100-Non-tradable Shareholder, 110-Indirect Controlling Shareholder, 150-Tradable Shareholder, 500-Corporate Management. |
| LC_TransferPlan | EventType| 承诺事项类型 | 承诺事项类型(EventType)与(CT_SystemConst)表中的DM字段关联，令LB = 1352 AND DM IN (71,72)，得到承诺事项类型的具体描述：71-新股上市股东承诺，72-上市后股东追加承诺。| The commitment item type (EventType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1352 AND DM IN (71,72), resulting in the specific description of the commitment item type: 71 - New Share Listing Shareholder Commitment, 72 - Post-IPO Shareholder Additional Commitment. |
| LC_TransferPlan | IfEffected | 承诺是否有效 | 承诺是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到承诺是否有效的具体描述：1-是，2-否。| Whether the commitment is effective (IfEffected) is associated with the DM field in the (CT_SystemConst) table, let LB = 999 AND DM IN (1,2), to obtain the specific description of whether the commitment is effective: 1-yes, 2-no.|
| LC_TransferPlan | EventProcedure | 事件进程 | 事件进程(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB=2380，得到事件进程的具体描述：1-承诺开始未实施，2-承诺实施完成，3-承诺未实施终止，4-承诺已实施终止，5-承诺到期未实施，6-承诺实施中。 | The event process (EventProcedure) is associated with the DM field in the (CT_SystemConst) table, setting LB=2380 to obtain the specific description of the event process: 1 - Commitment started but not implemented, 2 - Commitment implemented and completed, 3 - Commitment not implemented and terminated, 4 - Commitment implemented and terminated, 5 - Commitment expired and not implemented, 6 - Commitment in progress. |
| LC_TransferPlan | SHSN | 股东序号  | | |
| LC_TransferPlan | SHName | 股东名称  | | |
| LC_TransferPlan | TransferPlanType | 增减持计划类别 | 增减持计划类别(TransferPlanType)与(CT_SystemConst)表中的DM字段关联，令LB = 1306 AND DM IN (124,127,128,201)，得到增减持计划类别的具体描述：124-不减持，127-主动减持计划，128-被动减持计划，201-增持计划。 | The "TransferPlanType" is associated with the "DM" field in the "CT_SystemConst" table. With LB = 1306 AND DM IN (124,127,128,201), the specific description of the transfer plan type is obtained: 124 - No reduction, 127 - Active reduction plan, 128 - Passive reduction plan, 201 - Increase plan.|
| LC_TransferPlan | PromiseBeginDate | 承诺起始日期  | | |
| LC_TransferPlan | PromiseEndDate | 承诺截止日期  | | |
| LC_TransferPlan | PromiseStatment| 承诺说明  | | |
| LC_TransferPlan | IncreaseTime | 增持时间描述  | | |
| LC_TransferPlan | IncreaseTerm | 增持实施期限(月)  | | |
| LC_TransferPlan | IncreasePriceStatement | 增持价格描述  | | |
| LC_TransferPlan | IncreasePriceCeiling | 增持股票触发价格上限(元)  | | |
| LC_TransferPlan | IncreasePriceFloor | 增持股票触发价格下限(元)  | | |
| LC_TransferPlan | IncreaseSize | 增持规模描述  | | |
| LC_TransferPlan | IncreaseShareCeiling | 增持股份数量上限(股/份) | | |
| LC_TransferPlan | IncreaseShareFloor | 增持股份数量下限(股/份) | | |
| LC_TransferPlan | IncreaseRatioCeiling | 增持比例上限-占总股本 | | |
| LC_TransferPlan | IncreaseRatioFloor | 增持比例下限-占总股本 | | |
| LC_TransferPlan | IncreaseFundCeiling| 增持投入资金上限(元)  | | |
| LC_TransferPlan | IncreaseFundFloor| 增持投入资金下限(元)  | | |
| LC_TransferPlan | NotReducePromise | 不减持承诺期限(月)  | | |
| LC_TransferPlan | TradeType| 交易方式 | 交易方式(TradeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1202 AND DM IN (1,8,15,80,98,99)，得到交易方式的具体描述：1-协议转让，8-大宗交易，15-集中竞价，80-司法拍卖，98-多种交易方式，99-其他。| The trade method (TradeType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1202 AND DM IN (1,8,15,80,98,99), resulting in the specific description of the trade method: 1-Protocol Transfer, 8-Bulk Transaction, 15-Centralized Bidding, 80-Judicial Auction, 98-Multiple Trading Methods, 99-Other.|
| LC_TransferPlan | TradeTypeStatment| 交易方式描述  | | |
| LC_TransferPlan | ReduceTime | 减持时间描述  | | |
| LC_TransferPlan | ReduceTerm | 减持实施期限(月)  | | |
| LC_TransferPlan | ReducePriceStatement | 减持价格描述  | | |
| LC_TransferPlan | ReducePriceCeiling | 减持股票触发价格上限(元)  | | |
| LC_TransferPlan | ReducePriceFloor | 减持股票触发价格下限(元)  | | |
| LC_TransferPlan | ReduceSize | 减持规模描述  | | |
| LC_TransferPlan | ReduceShareCeiling | 减持股份数量上限(股/份) | | |
| LC_TransferPlan | ReduceShareFloor | 减持股份数量下限(股/份) | | |
| LC_TransferPlan | ReduceRatioCeiling | 减持比例上限-占总股本 | | |
| LC_TransferPlan | ReduceRatioFloor | 减持比例下限-占总股本 | | |
| LC_TransferPlan | InsertTime | 发布时间  | | |
| LC_TransferPlan | UpdateTime | 更新时间  | | |
| LC_TransferPlan | JSID | JSID  | | |
| table_name | column_name| column_description | 注释 | Annotation | 数据示例 |
|---|---|---|---|---|---|
| AStockShareholderDB.LC_Buyback | ID | ID ||| 599789971529 |
| AStockShareholderDB.LC_Buyback | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.| 224275 |
| AStockShareholderDB.LC_Buyback | FirstPublDate| 首次信息发布日期 ||| 2019-01-03 12:00:00.000|
| AStockShareholderDB.LC_Buyback | InfoSource | 信息来源 ||| 2017年激励计划首次授予回购注销部分限制性股票的公告 |
| AStockShareholderDB.LC_Buyback | ShareType| 股份类别 | 数值型常量。股份类别(ShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得到股份类别的具体描述：1-国家股，2-国有法人股，3-外资法人股，4-其他法人股，5-流通A股，6-B股，7-H股，8-转配股，9-专项资产管理计划转让，10-资产支持证券转让，11-中小企业私募债转让，12-中国存托凭证，13-可转换公司债券。| Numeric constant. The share type (ShareType) is associated with the DM field in the (CT_SystemConst) table, setting LB = 1040, the specific description of the share type is obtained: 1 - State-owned shares, 2 - State-owned legal person shares, 3 - Foreign-funded legal person shares, 4 - Other legal person shares, 5 - Tradable A shares, 6 - B shares, 7 - H shares, 8 - Transferable subscription shares, 9 - Special asset management plan transfer, 10 - Asset-backed securities transfer, 11 - Small and medium-sized enterprise private debt transfer, 12 - Chinese depository receipts, 13 - Convertible corporate bonds. | 5|
| AStockShareholderDB.LC_Buyback | AdvanceDate| 预案发布日期 ||| 2019-01-03 12:00:00.000|
| AStockShareholderDB.LC_Buyback | MeetPassDate | 股东大会通过日期 ||| 2019-01-18 12:00:00.000|
| AStockShareholderDB.LC_Buyback | WriteOffPublDate | 回购并注销股份公告书发布日 ||| 2019-05-28 12:00:00.000|
| AStockShareholderDB.LC_Buyback | ContractDate | 回购协议签署日 ||| null |
| AStockShareholderDB.LC_Buyback | Seller | 股份被回购方 ||| 8名激励对象|
| AStockShareholderDB.LC_Buyback | BuybackSum | 回购股数(股) ||| 14022.0|
| AStockShareholderDB.LC_Buyback | Percentage | 占总股本比例 ||| 9.4e-05|
| AStockShareholderDB.LC_Buyback | PricingStatement | 回购定价方式说明 ||| 本次回购价格为13.02元/股 |
| AStockShareholderDB.LC_Buyback | BuybackPrice | 回购价格(元/股)||| 13.02|
| AStockShareholderDB.LC_Buyback | BuybackMoney | 回购总金额(元) ||| 182566.44|
| AStockShareholderDB.LC_Buyback | StartDate| 起始日期 ||| null |
| AStockShareholderDB.LC_Buyback | EndDate| 日期 ||| null |
| AStockShareholderDB.LC_Buyback | PayMode| 回购支付方式 ||| null |
| AStockShareholderDB.LC_Buyback | ChangeDate | 全称更改日期 ||| 2019-05-28 12:00:00.000|
| AStockShareholderDB.LC_Buyback | PayDate| 回购资金划出日 ||| null |
| AStockShareholderDB.LC_Buyback | ChangeRegDate| 工商变更登记日 ||| 2019-05-28 12:00:00.000|
| AStockShareholderDB.LC_Buyback | XGRQ | 修改日期 ||| 2024-01-08 03:55:53.643|
| AStockShareholderDB.LC_Buyback | JSID | JSID ||| 758044560845 |
| AStockShareholderDB.LC_Buyback | VolumeFloor| 回购数量下限(股) ||| 14022.0|
| AStockShareholderDB.LC_Buyback | VolumeCeiling| 回购数量上限(股) ||| 14022.0|
| AStockShareholderDB.LC_Buyback | PriceFloor | 回购价格下限(元) ||| 13.02|
| AStockShareholderDB.LC_Buyback | PriceCeiling | 回购价格上限(元) ||| 13.02|
| AStockShareholderDB.LC_Buyback | ValueFloor | 拟回购资金总额下限(元) ||| 182566.44|
| AStockShareholderDB.LC_Buyback | ValueCeiling | 拟回购资金总额上限(元) ||| 182566.44|
| AStockShareholderDB.LC_Buyback | MaturityDesc | 待偿期限_指数||| null |
| AStockShareholderDB.LC_Buyback | EventProcedure | 事件进程 | 数值型常量。事件进程代码(EventProcedure)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程代码的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-涉诉，1053-可能涉诉，1055-预估，1303-收到，1305-部分收到，2001-逾期，2003-还款，2005-延期，2007-展期，2501-诉前，2504-诉中，2507-诉后，3001-提前回收，3002-提前部分回收，3003-到期后协议延期，3004-到期回收，3005-到期待回收，3006-到期部分待回收，3007-到期无法回收，3008-到期部分无法回收，3101-改革意向，3103-股改动议取消，3105-董事会改革方案，3108-沟通确认方案，3111-上级部门批准，3115-上级部门驳回，3120-董事会否决，3121-股东大会通过，3125-股东大会否决，3126-有效期内未实施，3131-方案实施，3201-证监会审核通过，3202-证监会审核否决，3203-证监会核准，3204-证监会未核准，3212-方案部分实施，3301-已注册未发行，3302-已发行有额度，3303-已发行无额度，3304-提前终止，3305-放弃，3399-其他。 | Numeric constant. The event procedure code (EventProcedure) is associated with the DM field in the (CT_SystemConst) table. Set LB = 1059, and obtain the specific description of the event procedure code: 1000 - Intent, 1001 - Plan, 1004 - Decision, 1007 - Veto, 1010 - Application, 1013 - Approval, 1016 - Unimplemented Termination, 1019 - In Implementation, 1022 - Implementation Completed, 1025 - Release, 1028 - Expiration, 1041 - Renewal, 1043 - Partial Renewal, 1051 - Involved in Lawsuit, 1053 - Possible Lawsuit, 1055 - Estimate, 1303 - Received, 1305 - Partially Received, 2001 - Overdue, 2003 - Repayment, 2005 - Extension, 2007 - Deferral, 2501 - Pre-litigation, 2504 - During Litigation, 2507 - Post-litigation, 3001 - Early Recovery, 3002 - Early Partial Recovery, 3003 - Post-maturity Agreement Extension, 3004 - Maturity Recovery, 3005 - Maturity Pending Recovery, 3006 - Maturity Partial Pending Recovery, 3007 - Maturity Unable to Recover, 3008 - Maturity Partially Unable to Recover, 3101 - Reform Intent, 3103 - Shareholding Change Proposal Cancellation, 3105 - Board Reform Plan, 3108 - Communication Confirmation Plan, 3111 - Approval by Higher Authority, 3115 - Rejection by Higher Authority, 3120 - Board Veto, 3121 - Shareholders' Meeting Approval, 3125 - Shareholders' Meeting Veto, 3126 - Not Implemented Within Validity Period, 3131 - Plan Implementation, 3201 - CSRC Approval, 3202 - CSRC Rejection, 3203 - CSRC Approval, 3204 - CSRC Non-approval, 3212 - Partial Implementation of Plan, 3301 - Registered but Not Issued, 3302 - Issued with Quota, 3303 - Issued without Quota, 3304 - Early Termination, 3305 - Waiver, 3399 - Other. | 1022 |
| AStockShareholderDB.LC_Buyback | EventProceDesc | 事件进程描述 ||| 实施完成 |
| AStockShareholderDB.LC_Buyback | BuybackModeCode| 股份回购方式代码 | 数值型常量。股份回购方式代码(BuybackModeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1523，得到股份回购方式代码的具体描述：10-集中竞价，20-协议回购，30-其他，40-要约回购。 | Numeric constant. The share buyback method code (BuybackModeCode) is associated with the DM field in the (CT_SystemConst) table. Setting LB = 1523, the specific description of the share buyback method code is obtained: 10 - centralized bidding, 20 - agreement buyback, 30 - others, 40 - tender offer buyback. | 20 |
| AStockShareholderDB.LC_Buyback | BuybackModeDesc| 股份回购方式描述 ||| 协议回购 |
| AStockShareholderDB.LC_Buyback | FundsSourceDesc| 资金总额及来源说明 ||| 回购总金额为182,566.44元,前述资金全部为公司自有资|
| AStockShareholderDB.LC_Buyback | PurposeDesc| 回购目的说明 ||| 因激励对象中1人因个人原因已申报离职,已不符合公司股 |
| AStockShareholderDB.LC_Buyback | InsertTime | 发布时间 ||| 2019-01-03 12:19:31.713|
| AStockShareholderDB.LC_Buyback | BuybackPurpose | 回购目的 | 回购目的(BuybackPurpose)与(CT_SystemConst)表中的DM字段关联，令LB=2560，得到回购目的的具体描述：1-实施股权激励，2-实施员工持股计划，3-实施股权激励或员工持股计划，4-发行可转债，5-未达激励计划条件，6-市值管理，7-资产重组，8-吸收合并，9-业绩补偿，10-大股东资金占用，11-对价购买。| The buyback purpose (BuybackPurpose) is associated with the DM field in the (CT_SystemConst) table. Setting LB=2560, the specific description of the buyback purpose is obtained: 1-Implement equity incentive, 2-Implement employee stock ownership plan, 3-Implement equity incentive or employee stock ownership plan, 4-Issue convertible bonds, 5-Conditions for incentive plan not met, 6-Manage market value, 7-Asset restructuring, 8-Acquisition merger, 9-Performance compensation, 10-Major shareholder's fund occupation, 11-Purchase with consideration.| 5|
| AStockShareholderDB.LC_Buyback | CurrencyUnit | 货币单位 ||| 1420 |
| AStockShareholderDB.LC_Buyback | OverruledDate|||| null |
| table_name | column_name | column_description | 注释| Annotation|
|---|---|---|---|---|
| LC_ESOP| ID| ID | | |
| LC_ESOP| InnerCode | 内部编码 | 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到股票的交易代码、简称等。| Internal Code: Associated with the "InnerCode" in the "SecuMain" table, obtaining the stock's trading code, abbreviation, etc.|
| LC_ESOP| CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。| Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| LC_ESOP| IniInfoPublDate | 首次信息发布日期 | | |
| LC_ESOP| DMAnnounceDate| 董事会公告日期 | | |
| LC_ESOP| SMAnnounceDate| 股东大会公告日期 | | |
| LC_ESOP| Process | 事件进程 | 事件进程(Process)与(CT_SystemConst)表中的DM字段关联，令LB = 1059，得到事件进程的具体描述：1000-意向，1001-预案，1004-决案，1007-否决，1010-申请，1013-批准，1016-未实施终止，1019-实施中，1022-实施完成，1025-解除，1028-到期，1041-续签，1043-部分续签，1051-涉诉，1053-可能涉诉，1055-预估，1303-收到，1305-部分收到，2001-逾期，2003-还款，2005-延期，2007-展期，2501-诉前，2504-诉中，2507-诉后，3001-提前回收，3002-提前部分回收，3003-到期后协议延期，3004-到期回收，3005-到期待回收，3006-到期部分待回收，3007-到期无法回收，3008-到期部分无法回收，3101-改革意向，3103-股改动议取消，3105-董事会改革方案，3108-沟通确认方案，3111-上级部门批准，3115-上级部门驳回，3120-董事会否决，3121-股东大会通过，3125-股东大会否决，3126-有效期内未实施，3131-方案实施，3201-证监会审核通过，3202-证监会审核否决，3203-证监会核准，3204-证监会未核准，3212-方案部分实施，3301-已注册未发行，3302-已发行有额度，3303-已发行无额度，3304-提前终止，3305-放弃，3399-其他。 | The event process is associated with the DM field in the (CT_SystemConst) table, setting LB = 1059, the specific description of the event process is as follows: 1000-Intent, 1001-Plan, 1004-Decision, 1007-Rejection, 1010-Application, 1013-Approval, 1016-Termination Without Implementation, 1019-Implementation in Progress, 1022-Implementation Completed, 1025-Release, 1028-Expiry, 1041-Renewal, 1043-Partial Renewal, 1051-In Litigation, 1053-Potentially In Litigation, 1055-Estimation, 1303-Received, 1305-Partially Received, 2001-Overdue, 2003-Repayment, 2005-Extension, 2007-Deferral, 2501-Pre-litigation, 2504-During Litigation, 2507-Post-litigation, 3001-Advance Recovery, 3002-Partial Advance Recovery, 3003-Extension After Maturity, 3004-Recovery at Maturity, 3005-Awaiting Recovery at Maturity, 3006-Partially Awaiting Recovery at Maturity, 3007-Unable to Recover at Maturity, 3008-Partially Unable to Recover at Maturity, 3101-Reform Intent, 3103-Shares Reform Proposal Canceled, 3105-Board Reform Proposal, 3108-Communication Confirmation Proposal, 3111-Superior Department Approval, 3115-Superior Department Rejection, 3120-Board Rejection, 3121-Shareholders' Meeting Approval, 3125-Shareholders' Meeting Rejection, 3126-Not Implemented Within Validity Period, 3131-Proposal Implementation, 3201-CSRC Approval, 3202-CSRC Rejection, 3203-CSRC Approval, 3204-CSRC Not Approved, 3212-Partial Implementation of Proposal, 3301-Registered but Not Issued, 3302-Issued with Quota, 3303-Issued Without Quota, 3304-Advance Termination, 3305-Abandonment, 3399-Other. |
| LC_ESOP| SerialNumber| 序号 | | |
| LC_ESOP| IfPeriod| 是否分期实施 | 是否分期实施(IfPeriod)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否分期实施的具体描述：1-是，2-否。| Whether to implement in installments (IfPeriod) is associated with the DM field in the (CT_SystemConst) table, with LB = 999 AND DM IN (1,2), to obtain the specific description of whether to implement in installments: 1-Yes, 2-No.|
| LC_ESOP| Period| 数据统计区间 | | |
| LC_ESOP| InitialImpleDay | 首次实施公告日 | | |
| LC_ESOP| ShareSource | 股票来源方式 | | |
| LC_ESOP| ShareCelling| 股票规模上限(万股) | | |
| LC_ESOP| ShareFloor| 股票规模下限(万股) | | |
| LC_ESOP| FundCelling | 资金总额上限(万元) | | |
| LC_ESOP| FundFloor | 资金总额下限(万元) | | |
| LC_ESOP| Duration| 麦考利久期 | | |
| LC_ESOP| LockDuration| 锁定期(月) | | |
| LC_ESOP| ReleaseDuration | 释放期(月) | | |
| LC_ESOP| FundSource| 资金来源 | | |
| LC_ESOP| Participant | 参与单位及人员 | | |
| LC_ESOP| Management| 管理模式 | | |
| LC_ESOP| ManageInsitute| 管理机构 | | |
| LC_ESOP| PlanName| 资产管理计划全称 | | |
| LC_ESOP| UpdateTime| 更新时间 | | |
| LC_ESOP| JSID| JSID | | |
| LC_ESOP| PeriodSituation | 分期情况 | | |
| LC_ESOP| PlanRatio | 资产管理计划杠杆比例 | | |
| LC_ESOP| StockPrice| 购买股票价格 | | |
| LC_ESOP| PartiAmount | 参与人数 | | |
| LC_ESOP| ManagementPartiAmount | 高管参与人数 | | |
| LC_ESOP| ManagementShares| 高管认购的份额 | | |
| LC_ESOP| ManagementRatio | 高管认购的比例 | | |
| LC_ESOP| EmployeePartiAmount | 员工参与人数 | | |
| LC_ESOP| EmployeeShares| 员工认购的份额 | | |
| LC_ESOP| EmployeeRatio | 员工认购的比例 | | |
| LC_ESOP| ImpleEndDate| 持股的完成日 | | |
| LC_ESOP| LockStartDate | 锁定的起始日 | | |
| LC_ESOP| Statement | 计划情况说明 | | |
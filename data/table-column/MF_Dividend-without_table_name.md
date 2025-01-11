| column_name| column_description | 注释| Annotation|
|---|---|---|---|---|
| ID | ID | | |
| TransCode| 基金转型统一编码 | | |
| InnerCode| 基金内部编码 | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。| Fund internal code (InnerCode): associated with the "security internal code (InnerCode)" in the "security main table (SecuMain)", to obtain the fund's trading code, abbreviation, etc. |
| InfoPublDate | 信息发布日期 | | |
| InfoSource | 信息来源 | | |
| DividendImplementDate| 分红实施公告日 | | |
| EndDate| 截止日期 | 截止日期（EndDate）：基金收益分配基准日，同收益分配基准日[ProfitDistDate]字段一致。 | Deadline (EndDate): The benchmark date for the distribution of fund returns, which is the same as the field [ProfitDistDate] for the benchmark date of return distribution. |
| ProfitDistDate | 收益分配基准日 | 收益分配基准日(ProfitDistDate)：基金本次分红依据的可分配利润的截止日期。即，以截止该日期的本基金的可分配利润为准，向基金份额持有人按一定的分红比例实施分红。| Income Distribution Benchmark Date (ProfitDistDate): The cut-off date for the distributable profit of the fund's current dividend distribution. That is, based on the distributable profit of the fund up to and including this date, a dividend is distributed to the fund unit holders at a certain distribution ratio. |
| UnitProfit | 单位基金收益(元) | | |
| UnitRetainedProfit | 单位基金未分配收益(元) | | |
| IfDistributed| 是否分红 | 是否分红（IfDistributed）：该字段固定以下常量：1-是；0-否。 | Whether to distribute (IfDistributed): This field is fixed with the following constants: 1-yes; 0-no. |
| DividendRatioBeforeTax | 派现比例(含税10派X元)| | |
| ActualRatioAfterTax| 实派比例(税后10派X元)| | |
| Dividendsum| 派现金额合计(元) | | |
| ReDate | 权益登记日 | | |
| ExRightDate| 除息日 | | |
| ExRightDateEX| 场内除息日 | | |
| ExecuteDate| 发放日 | | |
| ExecuteDateEX| 场内发放日 | | |
| ReinvestDay| 红利再投资日 | | |
| AccountDay | 红利再投资份额到帐日 | | |
| RedemptionDay| 红利再投资份额可赎回日 | | |
| DistributableProfits | 基准日基金可供分配利润(元) | | |
| AllocationValue| 基准日应分配金额(元) | | |
| SchemeModification | 方案变更说明 | | |
| EventProcedureCode | 事件进程代码 | 事件进程代码(EventProcedureCode)：与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1001,1004,3131)，得到事件进程代码的具体描述：1001-预案，1004-决案，3131-方案实施。 | Event Procedure Code: Associated with the DM field in the (CT_SystemConst) table, let LB = 1059 AND DM IN (1001,1004,3131), to obtain the specific description of the event procedure code: 1001-Plan, 1004-Decision, 3131-Plan Implementation. |
| EventProcedure | 事件进程 | | |
| DistributedRange | 发放范围 | | |
| UnitProfitYTD| 本年单位累计分红(元) | 本年单位累计分红（UnitProfitYTD）：计算公式：∑（Di），其中：Di为年初至今的第i次分红的单位分红金额。 | This year's cumulative dividend (UnitProfitYTD): Calculation formula: ∑(Di), where: Di is the amount of dividend per unit for the i-th dividend from the beginning of the year to date. |
| DividendSumYTD | 本年累计分红总额(元) | | |
| DividendTimesYTD | 本年累计分红次数(次) | | |
| DiviSumSinceInception| 历史累计分红总额(元) | | |
| DiviTimesSinceIncepion | 历史累计分红次数(次) | | |
| XGRQ | 更新日期 | | |
| JSID | JSID | | |
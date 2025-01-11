| table_name | column_name| column_description | 注释| Annotation|
|---|---|---|---|---|
| MF_Dividend| ID | ID | | |
| MF_Dividend| TransCode| 基金转型统一编码 | | |
| MF_Dividend| InnerCode| 基金内部编码 | 基金内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到基金的交易代码、简称等。| Fund internal code (InnerCode): associated with the "security internal code (InnerCode)" in the "security main table (SecuMain)", to obtain the fund's trading code, abbreviation, etc. |
| MF_Dividend| InfoPublDate | 信息发布日期 | | |
| MF_Dividend| InfoSource | 信息来源 | | |
| MF_Dividend| DividendImplementDate| 分红实施公告日 | | |
| MF_Dividend| EndDate| 截止日期 | 截止日期（EndDate）：基金收益分配基准日，同收益分配基准日[ProfitDistDate]字段一致。 | Deadline (EndDate): The benchmark date for the distribution of fund returns, which is the same as the field [ProfitDistDate] for the benchmark date of return distribution. |
| MF_Dividend| ProfitDistDate | 收益分配基准日 | 收益分配基准日(ProfitDistDate)：基金本次分红依据的可分配利润的截止日期。即，以截止该日期的本基金的可分配利润为准，向基金份额持有人按一定的分红比例实施分红。| Income Distribution Benchmark Date (ProfitDistDate): The cut-off date for the distributable profit of the fund's current dividend distribution. That is, based on the distributable profit of the fund up to and including this date, a dividend is distributed to the fund unit holders at a certain distribution ratio. |
| MF_Dividend| UnitProfit | 单位基金收益(元) | | |
| MF_Dividend| UnitRetainedProfit | 单位基金未分配收益(元) | | |
| MF_Dividend| IfDistributed| 是否分红 | 是否分红（IfDistributed）：该字段固定以下常量：1-是；0-否。 | Whether to distribute (IfDistributed): This field is fixed with the following constants: 1-yes; 0-no. |
| MF_Dividend| DividendRatioBeforeTax | 派现比例(含税10派X元)| | |
| MF_Dividend| ActualRatioAfterTax| 实派比例(税后10派X元)| | |
| MF_Dividend| Dividendsum| 派现金额合计(元) | | |
| MF_Dividend| ReDate | 权益登记日 | | |
| MF_Dividend| ExRightDate| 除息日 | | |
| MF_Dividend| ExRightDateEX| 场内除息日 | | |
| MF_Dividend| ExecuteDate| 发放日 | | |
| MF_Dividend| ExecuteDateEX| 场内发放日 | | |
| MF_Dividend| ReinvestDay| 红利再投资日 | | |
| MF_Dividend| AccountDay | 红利再投资份额到帐日 | | |
| MF_Dividend| RedemptionDay| 红利再投资份额可赎回日 | | |
| MF_Dividend| DistributableProfits | 基准日基金可供分配利润(元) | | |
| MF_Dividend| AllocationValue| 基准日应分配金额(元) | | |
| MF_Dividend| SchemeModification | 方案变更说明 | | |
| MF_Dividend| EventProcedureCode | 事件进程代码 | 事件进程代码(EventProcedureCode)：与(CT_SystemConst)表中的DM字段关联，令LB = 1059 AND DM IN (1001,1004,3131)，得到事件进程代码的具体描述：1001-预案，1004-决案，3131-方案实施。 | Event Procedure Code: Associated with the DM field in the (CT_SystemConst) table, let LB = 1059 AND DM IN (1001,1004,3131), to obtain the specific description of the event procedure code: 1001-Plan, 1004-Decision, 3131-Plan Implementation. |
| MF_Dividend| EventProcedure | 事件进程 | | |
| MF_Dividend| DistributedRange | 发放范围 | | |
| MF_Dividend| UnitProfitYTD| 本年单位累计分红(元) | 本年单位累计分红（UnitProfitYTD）：计算公式：∑（Di），其中：Di为年初至今的第i次分红的单位分红金额。 | This year's cumulative dividend (UnitProfitYTD): Calculation formula: ∑(Di), where: Di is the amount of dividend per unit for the i-th dividend from the beginning of the year to date. |
| MF_Dividend| DividendSumYTD | 本年累计分红总额(元) | | |
| MF_Dividend| DividendTimesYTD | 本年累计分红次数(次) | | |
| MF_Dividend| DiviSumSinceInception| 历史累计分红总额(元) | | |
| MF_Dividend| DiviTimesSinceIncepion | 历史累计分红次数(次) | | |
| MF_Dividend| XGRQ | 更新日期 | | |
| MF_Dividend| JSID | JSID | | |
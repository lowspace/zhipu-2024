| table_name| column_name | column_description| 注释 | Annotation |
|---|---|---|---|---|
| LC_IncomeStatementAll | ID| ID|||
| LC_IncomeStatementAll | InfoPublDate| 信息发布日期|||
| LC_IncomeStatementAll | InfoSource| 信息来源|||
| LC_IncomeStatementAll | BulletinType| 公告类别| 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and DM IN (10,20,30,70)，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，70-临时公告。| The BulletinType is associated with the DM field in the CT_SystemConst table, with LB = 1311 and DM IN (10,20,30,70), resulting in the specific description of the bulletin type: 10-Issue and Listing Prospectus, 20-Regular Report, 30-Earnings Flash, 70-Interim Bulletin.|
| LC_IncomeStatementAll | CompanyCode | 公司代码| 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.|
| LC_IncomeStatementAll | EndDate | 日期|||
| LC_IncomeStatementAll | IfAdjusted| 是否调整| 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,4,5)，得到是否调整的具体描述：1-是，2-否，4-否(7-9月)，5-是(7-9月)。| Whether to adjust the association of the DM field in the (IfAdjusted) and (CT_SystemConst) tables, let LB = 1188 AND DM IN (1,2,4,5), to obtain the specific description of whether to adjust: 1-Yes, 2-No, 4-No (July-September), 5-Yes (July-September). |
| LC_IncomeStatementAll | IfMerged| 是否合并| 是否合并（IfMerged），该字段固定以下常量：1-合并报表；2-母公司报表 | Whether to merge (IfMerged), this field is fixed with the following constants: 1-merged report; 2-parent company report|
| LC_IncomeStatementAll | AccountingStandards | 会计准则|||
| LC_IncomeStatementAll | EnterpriseType| 工业企业类型|||
| LC_IncomeStatementAll | TotalOperatingRevenue | 一、营业总收入|||
| LC_IncomeStatementAll | OperatingRevenue| 一、营业收入| 营业总收入（TotalOperatingRevenue）：对非金融类公司（报表格式类型=99），营业总收入=营业收入＋金融类特殊收入项目＋其他业务收入，注：“金融类特殊收入项目”包括：利息收入、手续费及佣金收入、已赚保费、营业收入特殊项目、调整项目| Total Operating Revenue: For non-financial companies (report format type = 99), Total Operating Revenue = Operating Revenue + Special Financial Income Items + Other Operating Income. Note: "Special Financial Income Items" include interest income, fee and commission income, earned premium, special items of operating revenue, and adjustment items.|
| LC_IncomeStatementAll | NetInterestIncome | 利息净收入| 利息净收入（NetInterestIncome）：一般为金融类企业披露科目；本字段优先展示收入模块披露的“利息净收入”，当原文未披露时，且IfComplete=1时，则通过收入模块披露的“其中:利息收入”、“其中:利息支出”计算得出，计算公式=其中:利息收入-其中:利息支出；| Net Interest Income: Generally disclosed by financial companies; this field prioritizes displaying the "Net Interest Income" disclosed in the income module. When the original text does not disclose it and IfComplete=1, it is calculated from the "Interest Income" and "Interest Expense" disclosed in the income module, using the formula = Interest Income - Interest Expense.|
| LC_IncomeStatementAll | InterestIncome| 其中:利息收入(元) | 其中:利息收入（InterestIncome）：一般为金融类企业披露科目| Interest Income: Generally disclosed by financial companies as an accounting item. |
| LC_IncomeStatementAll | InterestExpense | 其中:利息支出(元) | 其中:利息支出（InterestExpense）：一般为金融类企业披露科目；本字段展示收入模块、成本模块披露的“其中：利息支出”合计值； | Where: Interest Expense (InterestExpense): This is generally disclosed by financial companies; this field displays the total "Where: Interest Expense" disclosed in the income module and cost module. |
| LC_IncomeStatementAll | NetCommissionIncome | 手续费及佣金净收入| 手续费及佣金净收入（NetCommissionIncome）：一般为金融类企业披露科目;本字段优先展示收入模块披露的“手续费及佣金净收入”，当原文未披露时，且IfComplete=1时，则通过收入模块披露的“其中:手续费及佣金收入”、“其中:手续费及佣金支出”计算得出，计算公式=其中:手续费及佣金收入-其中:手续费及佣金支出； | Net Commission Income: Generally disclosed by financial companies; this field prioritizes displaying the "Net Commission Income" disclosed in the income module. When the original text does not disclose it and IfComplete=1, it is calculated from the "Where: Commission and Brokerage Income" and "Where: Commission and Brokerage Expenses" disclosed in the income module, using the formula = Where: Commission and Brokerage Income - Where: Commission and Brokerage Expenses.|
| LC_IncomeStatementAll | CommissionIncome| 手续费收入(元)| 其中:手续费及佣金收入（CommissionIncome）：一般为金融类企业披露科目| Where: Commission Income: Generally disclosed by financial companies as an item|
| LC_IncomeStatementAll | CommissionExpense | 手续费支出(元)| 其中:手续费及佣金支出（CommissionExpense）：一般为金融类企业披露科目；本字段展示收入模块、成本模块“其中:手续费及佣金支出”合计值；| Where: Commission Expense: This is generally a disclosed account for financial companies; this field shows the total value of "Commission Expense" from the revenue module and the cost module.|
| LC_IncomeStatementAll | NetProxySecuIncome| 其中:代理买卖证券业务净收入 | 其中:代理买卖证券业务净收入（NetProxySecuIncome）：一般为金融类:证券公司披露科目 | NetProxySecuIncome: Net income from securities trading agency business, usually disclosed by securities companies under the financial category.|
| LC_IncomeStatementAll | NetSubIssueSecuIncome | 其中:证券承销业务净收入 |||
| LC_IncomeStatementAll | NetTrustIncome| 其中:受托客户资产管理业务净收入(元) | 其中:受托客户资产管理业务净收入（NetTrustIncome）：一般为金融类:证券公司披露科目 | Trustee customer asset management business net income (NetTrustIncome): Generally financial: securities companies disclose items |
| LC_IncomeStatementAll | PremiumsEarned| 已赚保费(元)| 已赚保费（PremiumsEarned）：一般为金融类:保险公司披露科目| Premiums Earned: Generally refers to the financial category: disclosed items by insurance companies|
| LC_IncomeStatementAll | PremiumsIncome| 保险业务收入(元)| 其中:保险业务收入（PremiumsIncome）：一般为金融类:保险公司披露科目 | Premiums Income: Generally refers to the financial category: insurance companies disclose the account|
| LC_IncomeStatementAll | ReinsuranceIncome | 其中:分保费收入 | 其中:保险业务收入:分保费收入（ReinsuranceIncome）：一般为金融类:保险公司披露科目 | Where: Insurance Business Income: Premium Income (Reinsurance Income): Generally financial: Insurance companies disclose items |
| LC_IncomeStatementAll | Reinsurance | 减:分出保费(元) | 其中:减:分出保费（Reinsurance）：一般为金融类:保险公司披露科目 | Among them: minus: allocate premium (Reinsurance): usually financial: insurance company discloses the subject|
| LC_IncomeStatementAll | UnearnedPremiumReserve| 未到期责任准备金| 其中:减:提取未到期责任准备金（UnearnedPremiumReserve）：一般为金融类:保险公司披露科目| Among them: minus: extract the unearned premium reserve (Unearned Premium Reserve): generally for financial types: insurance companies disclose items|
| LC_IncomeStatementAll | OtherOperatingRevenue | 其他营业收入|||
| LC_IncomeStatementAll | SpecialItemsOR| ##营业收入特殊项目(元)|||
| LC_IncomeStatementAll | AdjustmentItemsOR | ##营业收入调整项目|||
| LC_IncomeStatementAll | TotalOperatingCost| 二、营业总成本| 营业总成本（TotalOperatingCost）：对非金融类公司（企业性质=99），营业总成本=营业成本＋营业税金及附加＋销售费用＋管理费用合计＋研发费用＋财务费用＋勘探费用＋信用减值损失(成本)＋资产减值损失(成本)＋其他成本＋金融类特殊成本项目（注：“金融类特殊成本项目”：保险手续费及佣金支出、退保金、提取保费准备金、提取期货风险准备金、提取担保业务准备金、提取担保赔偿准备金、赔付支出净额、提取保险责任准备金净额、保单红利支出、分保费用等)＋##营业支出OR营业总成本特殊项目＋##营业支出OR营业总成本调整项目；对金融类公司（企业性质不等于99），营业总成本=营业支出 | Total Operating Cost: For non-financial companies (Enterprise Nature = 99), Total Operating Cost = Operating Cost + Operating Tax and Surcharges + Selling Expenses + Total Management Expenses + R&D Expenses + Financial Expenses + Exploration Expenses + Credit Impairment Loss (Cost) + Asset Impairment Loss (Cost) + Other Costs + Special Costs for Financial Companies (Note: "Special Costs for Financial Companies": Insurance Commission and Handling Fees, Refund Payments, Premium Reserve Extraction, Futures Risk Reserve Extraction, Guarantee Business Reserve Extraction, Guarantee Compensation Reserve Extraction, Net Compensation Payment, Net Reserve Extraction for Insurance Liabilities, Policy Dividend Payments, Reinsurance Expenses, etc.) + ## Operating Expenses OR Total Operating Cost Special Items + ## Operating Expenses OR Total Operating Cost Adjustment Items; For financial companies (Enterprise Nature not equal to 99), Total Operating Cost = Operating Expenses |
| LC_IncomeStatementAll | OperatingPayout | 营业支出(元)|||
| LC_IncomeStatementAll | RefundedPremiums| 退保金| 退保金（RefundedPremiums）：一般为金融类:保险公司披露科目| Refunded Premiums: Generally refers to a financial category: disclosed items by insurance companies|
| LC_IncomeStatementAll | CompensationExpense | 赔付支出| 其中:赔付支出（CompensationExpense）：一般为金融类:保险公司披露科目| Where: Compensation Expense: Generally refers to the financial category: Insurance companies disclose the account title|
| LC_IncomeStatementAll | AmortizationExpense | 减:摊回赔付支出 | 其中:减:摊回赔付支出（AmortizationExpense）：一般为金融类:保险公司披露科目 | Where: Minus: Amortization Expense (AmortizationExpense): Generally refers to the financial category: Insurance companies disclose items |
| LC_IncomeStatementAll | PremiumReserve| 提取保险责任准备金(元)| 其中:提取保险责任准备金（PremiumReserve）：一般为金融类:保险公司披露科目 | Extracting Insurance Liability Reserves (Premium Reserve): Generally refers to the financial category: Insurance companies disclose the account. |
| LC_IncomeStatementAll | AmortizationPremiumReserve| 减:摊回保险责任准备金 | 其中:减:摊回保险责任准备金（AmortizationPremiumReserve）：一般为金融类:保险公司披露科目| Where: Minus: Amortization of Insurance Liability Reserve: Generally refers to the financial category: Insurance companies disclose the account title|
| LC_IncomeStatementAll | PolicyDividendPayout| 保单红利支出| 保单红利支出（PolicyDividendPayout）：一般为金融类:保险公司披露科目| Policy Dividend Payout: Generally refers to a financial category: disclosed items by insurance companies.|
| LC_IncomeStatementAll | ReinsuranceCost | 分保费用(元)| 分保费用（ReinsuranceCost）：一般为金融类:保险公司披露科目 | Reinsurance Cost: Generally refers to a financial category: disclosed items by insurance companies |
| LC_IncomeStatementAll | OperatingAndAdminExpense| 业务及管理费| 其中:业务及管理费（OperatingAndAdminExpense）：一般为金融类企业披露科目| Operating and administrative expenses: Generally disclosed items for financial companies |
| LC_IncomeStatementAll | AmortizationReinsuranceCost | 减:摊回分保费用 | 其中:减:摊回分保费用（AmortizationReinsuranceCost）：一般为金融类:保险公司披露科目 | Amortization of Reinsurance Costs: Generally refers to financial categories: insurance companies disclose items|
| LC_IncomeStatementAll | InsuranceCommissionExpense| 保险手续费及佣金支出| 保险手续费及佣金支出（InsuranceCommissionExpense）：一般为金融类:保险公司披露科目| Insurance Commission Expense: Generally refers to the financial category: insurance company discloses the account. |
| LC_IncomeStatementAll | OtherOperatingCost| 其他业务成本|||
| LC_IncomeStatementAll | OperatingCost | 减:营业成本(元) |||
| LC_IncomeStatementAll | OperatingTaxSurcharges| 营业税金及附加|||
| LC_IncomeStatementAll | OperatingExpense| 营业费用(元)|||
| LC_IncomeStatementAll | AdministrationExpense | 管理费用(元)|||
| LC_IncomeStatementAll | FinancialExpense| 财务费用(元)|||
| LC_IncomeStatementAll | AssetImpairmentLoss | 资产减值损失| 资产减值损失（AssetImpairmentLoss）：根据财政部发布的《关于修订印发2019年度一般企业财务报表格式的通知》格式，“资产减值损失”不隶属于营业总成本部分。因企业披露不一致性，经研究，从2020.07.08披露的2020年半年报开始，字段数值按照原文披露展示，历史报告期维持原有规则。| Asset Impairment Loss: According to the format of the "Notice on Amending and Issuing the Financial Statement Format for General Enterprises in 2019" released by the Ministry of Finance, "Asset Impairment Loss" is not subordinate to the part of total operating costs. Due to the inconsistency of enterprise disclosures, after research, starting from the semi-annual report disclosed on July 8, 2020, the field value will be displayed as per the original disclosure, and the historical reporting period will maintain the original rules.|
| LC_IncomeStatementAll | SpecialItemsTOC | ##营业支出特殊项目(元)|||
| LC_IncomeStatementAll | AdjustmentItemsTOC| ##营业总成本调整项目|||
| LC_IncomeStatementAll | OtherNetRevenue | 三、非经营性净收益| 非经营性净收益（OtherNetRevenue）：聚源计算合计项，仅针对非金融类公司。计算公式=其他收益＋投资净收益＋汇兑收益＋净敞口套期收益+公允价值变动净收益+信用减值损失(利润)+资产减值损失(利润)+资产处置收益+##营业利润特殊项目+##营业利润调整项目 注：对金融类公司，“特别收益/收入”下列示的项目：公允价值变动净收益、净敞口套期收益、其他收益、投资净收益、汇兑收益、资产处置收益属于“营业收入”的子项目 | Non-operating Net Income (Other Net Revenue): Ju Yuan calculation aggregate item, applicable only to non-financial companies. Calculation formula = Other Income + Net Investment Income + Foreign Exchange Gain + Net Fair Value Hedging Gain + Net Change in Fair Value + Credit Impairment Loss (Profit) + Asset Impairment Loss (Profit) + Gain from Disposal of Assets + ## Special Items of Operating Profit + ## Adjustments to Operating Profit. Note: For financial companies, the items listed under "Special Income/Revenue" include Net Change in Fair Value, Net Fair Value Hedging Gain, Other Income, Net Investment Income, Foreign Exchange Gain, and Gain from Disposal of Assets, which are sub-items of "Operating Revenue". |
| LC_IncomeStatementAll | FairValueChangeIncome | 公允价值变动净收益|||
| LC_IncomeStatementAll | InvestIncome| 加:投资净收益(元) |||
| LC_IncomeStatementAll | InvestIncomeAssociates| 其中:对联营合营企业的投资收益 |||
| LC_IncomeStatementAll | ExchangeIncome| 汇兑收益(元)|||
| LC_IncomeStatementAll | OtherItemsEffectingOP | ##加:影响营业利润的其他科目 |||
| LC_IncomeStatementAll | AdjustedItemsEffectingOP| ##加:影响营业利润的调整项目 |||
| LC_IncomeStatementAll | OperatingProfit | 二、营业利润(元)|||
| LC_IncomeStatementAll | NonoperatingIncome| 营业外收入(元)|||
| LC_IncomeStatementAll | NonoperatingExpense | 减：营业外支出(元)|||
| LC_IncomeStatementAll | NonCurrentAssetssDealLoss | 其中:非流动资产处置净损失 |||
| LC_IncomeStatementAll | OtherItemsEffectingTP | ##加:影响利润总额的其他科目 |||
| LC_IncomeStatementAll | AdjustedItemsEffectingTP| ##加:影响利润总额的调整项目 |||
| LC_IncomeStatementAll | TotalProfit | 利润总额(元)|||
| LC_IncomeStatementAll | IncomeTaxCost | 减:所得税(元) |||
| LC_IncomeStatementAll | UncertainedInvestmentLosses | 加:未确认的投资损失 |||
| LC_IncomeStatementAll | OtherItemsEffectingNP | ##加:影响净利润的其他科目 |||
| LC_IncomeStatementAll | AdjustedItemsEffectingNP| ##加:影响净利润的调整项目 |||
| LC_IncomeStatementAll | NetProfit | 四、净利润(元)|||
| LC_IncomeStatementAll | NPParentCompanyOwners | 归属于母公司所有者的净利润|||
| LC_IncomeStatementAll | MinorityProfit| 少数股东损益(元)|||
| LC_IncomeStatementAll | OtherItemsEffectingNPP| ##加:影响母公司净利润的特殊项目 |||
| LC_IncomeStatementAll | AdjustedItemsEffectingNPP | ##加:影响母公司净利润的调整项目 |||
| LC_IncomeStatementAll | OtherCompositeIncome| 其他综合收益|||
| LC_IncomeStatementAll | AdjustedItemsEffectingCI| ##加:影响综合收益总额的调整项目 |||
| LC_IncomeStatementAll | TotalCompositeIncome| 七、综合收益总额|||
| LC_IncomeStatementAll | CIParentCompanyOwners | 归属于母公司所有者的综合收益总额|||
| LC_IncomeStatementAll | CIMinorityOwners| 归属于少数股东的综合收益总额|||
| LC_IncomeStatementAll | AdjustedItemsEffectingPCI | ##加:影响母公司综合收益总额的调整项目 |||
| LC_IncomeStatementAll | BasicEPS| 基本每股收益(元/股) |||
| LC_IncomeStatementAll | DilutedEPS| 稀释每股收益(元/股) |||
| LC_IncomeStatementAll | SpecialFieldRemark| 特殊字段说明|||
| LC_IncomeStatementAll | UpdateTime| 更新时间|||
| LC_IncomeStatementAll | JSID| JSID|||
| LC_IncomeStatementAll | IfComplete| 完整标志| 完整标志(IfComplete)与(CT_SystemConst)表中的DM字段关联，令LB = 1444，得到完整标志的具体描述：1-完整报表，2-简表，3-个别字段修正报表。| The complete flag (IfComplete) is associated with the DM field in the (CT_SystemConst) table, with LB set to 1444, the specific description of the complete flag is: 1-Complete report, 2-Abbreviated report, 3-Individual field correction report.|
| LC_IncomeStatementAll | OCIParentCompanyOwners| 归属于母公司所有者的其他综合收益总额|||
| LC_IncomeStatementAll | OCINotInIncomeStatement | #以后不能重分类进损益表的其他综合收益 |||
| LC_IncomeStatementAll | OCIReMearsure | 1.1重新计量设定收益计划净负债或净资产的变动(元) |||
| LC_IncomeStatementAll | OCIEquityNotInIS| ##权益法下在被投资单位不能重分类进损益表的其他综合收益中享有的份额|||
| LC_IncomeStatementAll | OCIInIncomeStatement| #以后能重分类进损益表的其他综合收益 |||
| LC_IncomeStatementAll | OCIEquityInIS | 2.1权益法下在被投资单位以后将重分类进损益表的其他综合收益中享有的份额(元) |||
| LC_IncomeStatementAll | OCIFairValue| 2.2可供出售金融资产公允价值变动损益(元) |||
| LC_IncomeStatementAll | OCIToMaturityFA | 2.3持有至到期投资重分类为可供出售金融资产损益(元) |||
| LC_IncomeStatementAll | OCICFLoss | 2.4现金流量套期损益的有效部分(元) |||
| LC_IncomeStatementAll | OCIForeignCurrencyFSA | WBCWNCFL|||
| LC_IncomeStatementAll | OCIOthers | 2.6其他(以后能重分类进损益表的其他综合收益)(元) |||
| LC_IncomeStatementAll | OCIMinorityOwners | 归属于少数股东的其他综合收益总额|||
| LC_IncomeStatementAll | OtherRevenue| 其他收益|||
| LC_IncomeStatementAll | AssetDealIncome | 资产处置收益|||
| LC_IncomeStatementAll | OperSustCateg | (一)按经营持续性分类|||
| LC_IncomeStatementAll | OperSustNetP| 持续经营净利润|||
| LC_IncomeStatementAll | DisconOperNetP| 终止经营净利润|||
| LC_IncomeStatementAll | OwnershipCateg| (二)按所有权归属分类|||
| LC_IncomeStatementAll | PreInsurRSRV| 提取保费准备金| 提取保费准备金（PreInsurRSRV）：一般为金融类:保险公司披露科目| Extract Premium Reserve (PreInsurRSRV): Generally for financial types: Insurance companies disclose items|
| LC_IncomeStatementAll | NetClaimIncurred| 赔付支出净额| 赔付支出净额（NetClaimIncurred）：一般为金融类:保险公司披露科目| Net Claim Incurred: Generally refers to financial categories: disclosed items by insurance companies |
| LC_IncomeStatementAll | NetPremiumReserve | 提取保险责任准备金净额| 提取保险责任准备金净额（NetPremiumReserve）：一般为金融类:保险公司披露科目 | Extract the net amount of insurance liability reserves (Net Premium Reserve): usually for financial types: insurance companies disclose items|
| LC_IncomeStatementAll | AmortisedcostIncome | 以摊余成本计量的金融资产终止确认收益|||
| LC_IncomeStatementAll | InfoSourceCode| 信息来源编码|||
| LC_IncomeStatementAll | InsertTime| 发布时间|||
| LC_IncomeStatementAll | SalesRevenue| 其中:主营业务收入 |||
| LC_IncomeStatementAll | OtherOperatingIncome| 其中:其他业务收入 |||
| LC_IncomeStatementAll | GuaranteeIncome | 其中:担保业务收入 | 担保业务收入（GuaranteeIncome）：一般为金融类:担保公司披露科目 | Guarantee Income: Generally refers to the financial category: guarantee companies disclose items |
| LC_IncomeStatementAll | BrokerageIncome | 其中:手续费及佣金收入:经纪业务手续费收入| 其中:手续费及佣金收入:经纪业务手续费收入（BrokerageIncome）：一般为金融类:证券公司披露科目 | Where: Service charges and commission income: Brokerage income (Brokerage Income): Generally financial: Securities companies disclose items|
| LC_IncomeStatementAll | InvestBankIncome| 其中:手续费及佣金收入:投资银行业务手续费收入| 手续费及佣金收入：投资银行业务手续费收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: Investment banking service charge income — Generally financial: disclosed items by securities companies.|
| LC_IncomeStatementAll | AssetManageIncome | 其中:手续费及佣金收入:资产管理业务手续费收入| 手续费及佣金收入：资产管理业务手续费收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: Asset management service charge income — Generally financial: disclosed items by securities companies.|
| LC_IncomeStatementAll | FundManageIncome| 其中:手续费及佣金收入:基金管理业务手续费收入| 手续费及佣金收入：基金管理业务手续费收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: Fund management business service charges income — Generally financial: Securities company disclosure items. |
| LC_IncomeStatementAll | InvestConsultIncome | 其中:手续费及佣金收入:投资咨询业务收入| 手续费及佣金收入：投资咨询业务收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: Investment consulting business income — Generally financial: disclosed items by securities companies. |
| LC_IncomeStatementAll | RiskManageIncome| 其中:手续费及佣金收入:风险管理业务收入| 手续费及佣金收入：风险管理业务收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: income from risk management business — generally financial in nature: disclosed items by securities companies.|
| LC_IncomeStatementAll | InvestManageIncome| 其中:手续费及佣金收入:投资管理业务收入| 手续费及佣金收入：投资管理业务收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: Investment management business income — Generally financial: Disclosed items by securities companies. |
| LC_IncomeStatementAll | OtherAgencyIncome | 其中:手续费及佣金收入:其他代理业务收入| 手续费及佣金收入：其他代理业务收入 — 一般为金融类：证券公司披露科目。| Service charges and commission income: Other agency business income — Generally financial: disclosed items by securities companies.|
| LC_IncomeStatementAll | BrokerageExpense| 其中:手续费及佣金支出:经纪业务手续费支出| 其中:手续费及佣金支出:经纪业务手续费支出（BrokerageExpense）：一般为金融类:证券公司披露科目；本字段展示收入模块、成本模块“其中:手续费及佣金支出:经纪业务手续费支出”合计值；| Where: Commission and brokerage expenses: Brokerage expense (BrokerageExpense): usually financial: disclosed items by securities companies; this field shows the total of the "Where: Commission and brokerage expenses: Brokerage expense" for the income module and cost module. |
| LC_IncomeStatementAll | InvestBankExpense | 其中:手续费及佣金支出:投资银行业务手续费支出| 其中:手续费及佣金支出:投资银行业务手续费支出（InvestBankExpense）：一般为金融类企业披露科目；本字段展示收入模块、成本模块披露的“其中:手续费及佣金支出:投资银行业务手续费”合计值| Where: Commission and fee expenses: Investment banking business fee expenses (InvestBankExpense): usually disclosed by financial companies; this field shows the total of "Where: Commission and fee expenses: Investment banking business fee expenses" disclosed in the income module and cost module. |
| LC_IncomeStatementAll | AssetManageExpense| 其中:手续费及佣金支出:资产管理业务手续费支出| 其中:手续费及佣金支出:资产管理业务手续费支出（AssetManageExpense）：一般为金融类:证券公司披露科目；本字段展示收入模块、成本模块“其中:手续费及佣金支出:资产管理业务手续费”合计值；| Where: Commission and fee expenses: Asset management service fee expenses (AssetManageExpense): usually financial in nature: disclosed items by securities companies; this field shows the total of "Where: Commission and fee expenses: Asset management service fee" for the income module and cost module.|
| LC_IncomeStatementAll | FundManageExpense | 其中:手续费及佣金收入:基金管理业务手续费支出| 手续费及佣金收入：基金管理业务手续费支出 — 一般为金融类：证券公司披露科目。展示收入模块、成本模块“其中:手续费及佣金支出:基金管理业务手续费”合计值。| Service charges and commission income: fund management service charge expenses — usually financial sector: securities company disclosure items. Display the total value of the "service charges and commission expenses: fund management service charge" in the income module and cost module. |
| LC_IncomeStatementAll | InvestConsultExpense| 其中:手续费及佣金支出:投资咨询业务支出| 手续费及佣金支出：投资咨询业务支出 — 一般为金融类：证券公司披露科目。展示收入模块、成本模块“其中:手续费及佣金支出:投资咨询业务支出”合计值。| Transaction fees and commission expenses: Investment consulting business expenses - usually financial: securities company disclosure items. Display the total value of the "income module, cost module: transaction fees and commission expenses: investment consulting business expenses".|
| LC_IncomeStatementAll | RiskManageExpense | 其中:手续费及佣金支出:风险管理业务支出| 手续费及佣金支出：风险管理业务支出 — 一般为金融类：证券公司披露科目。展示收入模块、成本模块“其中:手续费及佣金支出:风险管理业务支出”合计值。| Transaction fees and commission expenses: risk management business expenses - generally financial: securities company disclosure items. Display the total value of the "transaction fees and commission expenses: risk management business expenses" in the income module and cost module. |
| LC_IncomeStatementAll | InvestManageExpense | 其中:手续费及佣金支出:投资管理业务支出| 手续费及佣金支出：投资管理业务支出 — 一般为金融类：证券公司披露科目。展示收入模块、成本模块“其中:手续费及佣金支出:投资管理业务支出”合计值。| Transaction fees and commission expenses: Investment management business expenses - Generally financial: disclosed items by securities companies. Display the total value of the "Transaction fees and commission expenses: Investment management business expenses" in the income module and cost module. |
| LC_IncomeStatementAll | OtherAgencyExpense| 其中:手续费及佣金支出:其他代理业务支出| 手续费及佣金支出：其他代理业务支出 — 一般为金融类：证券公司披露科目。展示收入模块、成本模块“其中:手续费及佣金支出:其他代理业务支出”合计值。| Transaction fees and commission expenses: other agency business expenses - generally financial: securities company disclosure items. Display the total value of the "transaction fees and commission expenses: other agency business expenses" in the income module and cost module. |
| LC_IncomeStatementAll | NetFundMgtIncome| 其中:基金管理业务手续费净收入 |||
| LC_IncomeStatementAll | ExtractFutureRisk | 提取期货风险准备金| 提取期货风险准备金（ExtractFutureRisk）：一般为金融类:期货公司披露科目 | Extract futures risk provision (ExtractFutureRisk): usually for financial types: futures companies disclose items|
| LC_IncomeStatementAll | WithdrawGuaranteeReser| 提取担保业务准备金| 提取担保业务准备金（WithdrawGuaranteeReser）：一般为金融类:担保公司披露科目| Extract Guarantee Business Provision (Withdraw Guarantee Reser): Generally for financial types: Guarantee companies disclose items.|
| LC_IncomeStatementAll | GuarantCompRSRV | 提取担保赔偿准备金| 提取担保赔偿准备金（GuarantCompRSRV）：一般为金融类:担保公司披露科目 | Extract Guarantee Compensation Reserve (GuarantCompRSRV): usually for financial types: guarantee companies disclose items|
| LC_IncomeStatementAll | SalesCost | 其中:主营业务成本 |||
| LC_IncomeStatementAll | OtherOperationalCost| 其中:其他业务成本 |||
| LC_IncomeStatementAll | TotalAdminExpense | 管理费用合计|||
| LC_IncomeStatementAll | ExplorationCost | 勘探费用|||
| LC_IncomeStatementAll | CreditImpairmentP | 信用减值损失(利润)|||
| LC_IncomeStatementAll | AssetImpairmentLossP| 资产减值损失(利润)|||
| LC_IncomeStatementAll | NPCParentCompanyOwners| 其中:归属于母公司普通股股东的净利润 |||
| LC_IncomeStatementAll | NPOtherEqinstruments| 其中:归属于母公司其他权益工具持有者的净利润 |||
| LC_IncomeStatementAll | OtherItemsEffectingCI | ##综合收益总额特殊项目|||
| LC_IncomeStatementAll | CICParentCompanyOwners| 其中:归属于母公司普通股股东的综合收益 |||
| LC_IncomeStatementAll | CIOtherEqinstruments| 其中:归属于母公司其他权益工具持有者的综合收益 |||
| LC_IncomeStatementAll | OthDebtInvesChange| 其他权益工具投资合计|||
| LC_IncomeStatementAll | InterestIncomeFin | 其中:利息收入(财务费用) | 其中:利息收入(财务费用)(InterestIncomeFin)： 1、当原文披露的实际数值为收入项，则统一展示为“负值”； 2、当原文披露的实际数值为减项，则统一展示为“正值”； | Where: Interest Income (Financial Expenses) (InterestIncomeFin): 1. If the actual value disclosed in the original text is an income item, it is uniformly displayed as "negative"; 2. If the actual value disclosed in the original text is a deduction item, it is uniformly displayed as "positive". |
| LC_IncomeStatementAll | CreditImpairmentL | 信用减值损失(成本)| 信用减值损失（CreditImpairmentL）：根据财政部发布的《关于修订印发2019年度一般企业财务报表格式的通知》格式，“信用减值损失”不隶属于营业总成本部分。因企业披露不一致性，经研究，从2020.07.08披露的2020年半年报开始，字段数值按照原文披露展示，历史报告期维持原有规则。| Credit Impairment Loss: According to the format of the "Notice on Amending and Issuing the Financial Statement Format for General Enterprises in 2019" released by the Ministry of Finance, "Credit Impairment Loss" is not subordinate to the part of total operating costs. Due to the inconsistency of enterprise disclosures, after research, starting from the semi-annual report disclosed on July 8, 2020, the field value will be displayed as per the original disclosure, and the historical reporting period will maintain the original rules.|
| LC_IncomeStatementAll | NetOpenHedgeIncome| No description available|||
| LC_IncomeStatementAll | OthEquFVChange| No description available|||
| LC_IncomeStatementAll | FinAssetROtherCI| No description available|||
| LC_IncomeStatementAll | OtherDebtInvestCIP| No description available|||
| LC_IncomeStatementAll | RAndD | No description available|||
| LC_IncomeStatementAll | InterestFinExp| No description available|||
| LC_IncomeStatementAll | CorporateCRChange | No description available|||
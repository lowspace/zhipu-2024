| table_name| column_name | column_description | 注释| Annotation|
|---|---|---|---|---|
| LC_CashFlowStatementAll | ID| ID | | |
| LC_CashFlowStatementAll | InfoPublDate| 信息发布日期 | | |
| LC_CashFlowStatementAll | InfoSource| 信息来源 | | |
| LC_CashFlowStatementAll | BulletinType| 公告类别 | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and DM IN (10,20,30,70)，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，70-临时公告。 | The BulletinType is associated with the DM field in the CT_SystemConst table, with LB = 1311 and DM IN (10,20,30,70), resulting in the specific description of the bulletin type: 10-Issue and Listing Prospectus, 20-Regular Report, 30-Earnings Flash, 70-Interim Bulletin. |
| LC_CashFlowStatementAll | CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。| Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| LC_CashFlowStatementAll | EndDate | 日期 | | |
| LC_CashFlowStatementAll | IfAdjusted| 是否调整 | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,4,5)，得到是否调整的具体描述：1-是，2-否，4-否(7-9月)，5-是(7-9月)。 | Whether to adjust the association of the DM field in the (IfAdjusted) and (CT_SystemConst) tables, let LB = 1188 AND DM IN (1,2,4,5), to obtain the specific description of whether to adjust: 1-Yes, 2-No, 4-No (July-September), 5-Yes (July-September).|
| LC_CashFlowStatementAll | IfMerged| 合并标志 | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到是否合并的具体描述：1-合并，2-母公司。 | Whether to merge the DM field associated with the (IfMerged) and (CT_SystemConst) tables, where LB = 1189 AND DM IN (1,2), to obtain the specific description of whether to merge: 1-merged, 2-parent company.|
| LC_CashFlowStatementAll | AccountingStandards | 会计准则 | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。| Accounting Standards is associated with the DM field in the (CT_SystemConst) table, setting LB = 1455 yields the specific description of the accounting standards: 1 - New Accounting Standards (2007), 9 - Old Accounting Standards. |
| LC_CashFlowStatementAll | EnterpriseType| 工业企业类型 | 报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业)。 本表报表格式类型(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业性质(CompanyType)。 本表企业性质(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业类别(CompanyType)。 | Report format type (EnterpriseType): Associated with the system constant table, LB=1414, DM IN (13-Commercial Bank, 31-Securities Company, 33-Trust Company, 35-Insurance Company, 39-Other Non-Bank Financial Institutions, 99-General Enterprise). The EnterpriseType field in this table is determined by referring to the original text of the announcement on the disclosure form of the financial statements and does not accurately represent the actual nature of the enterprise. If the nature of the enterprise needs to be obtained, it can be done by associating the CompanyCode with the CompanyCode in "Institution Basic Information (LC_InstiArchive)" to get the corresponding CompanyType. The EnterpriseType field in this table is determined by referring to the original text of the announcement on the disclosure form of the financial statements and does not accurately represent the actual nature of the enterprise. If the nature of the enterprise needs to be obtained, it can be done by associating the CompanyCode with the CompanyCode in "Institution Basic Information (LC_InstiArchive)" to get the corresponding Company Category. |
| LC_CashFlowStatementAll | GoodsSaleServiceRenderCash| 销售商品、提供劳务收到的现金(元) | | |
| LC_CashFlowStatementAll | TaxLevyRefund | 收到的税费返还(元) | | |
| LC_CashFlowStatementAll | NetDepositIncrease| 存款增加净额(元) | 客户存款和同业存放款项净增加额（NetDepositIncrease） — 一般为金融类：银行企业披露科目。 | Net increase in customer deposits and interbank placements (Net Deposit Increase) — Generally refers to financial categories: bank enterprise disclosure items. |
| LC_CashFlowStatementAll | NetBorrowingFromCentralBank | 向中央银行借款净增加额 | 向中央银行借款净增加额（NetBorrowingFromCentralBank） — 一般为金融类：银行企业披露科目。| Net increase in borrowing from the central bank (Net Borrowing From Central Bank) — usually a financial category: disclosed items by banking enterprises. |
| LC_CashFlowStatementAll | NetBorrowingFromFinanceCo | 向其他金融企业拆借的资金净额(元) | 向其他金融机构拆入资金净增加额（NetBorrowingFromFinanceCo） — 一般为金融类：银行企业披露科目。| Net increase in funds borrowed from other financial institutions (NetBorrowingFromFinanceCo) — usually a financial category: disclosed items by banking enterprises.|
| LC_CashFlowStatementAll | DrawBackLoansCanceled | 收回已核销贷款 | | |
| LC_CashFlowStatementAll | InterestAndCommissionCashIn | 收取利息、手续费及佣金的现金 | | |
| LC_CashFlowStatementAll | NetDealTradingAssets| 处置交易性金融资产净增加额 | | |
| LC_CashFlowStatementAll | NetBuyBack| 回购业务资金净增加额(元) | | |
| LC_CashFlowStatementAll | NetOriginalInsuranceCash| 收到原保险合同保费取得的现金 | 收到原保险合同保费取得的现金（NetOriginalInsuranceCash） — 一般为金融类：保险公司披露科目。 | Received cash from the original insurance contract premium (Net Original Insurance Cash) — usually financial in nature: disclosed by insurance companies. |
| LC_CashFlowStatementAll | NetReinsuranceCash| 收到再保业务现金净额 | 收到再保业务现金净额（NetReinsuranceCash） — 一般为金融类：保险公司披露科目。 | Received net reinsurance cash (Net Reinsurance Cash) — usually financial: disclosed by insurance companies. |
| LC_CashFlowStatementAll | NetInsurerDepositInvestment | 保户储金及投资款净增加额 | 保户储金及投资款净增加额（NetInsurerDepositInvestment） — 一般为金融类：保险公司披露科目。| Net Increase in Policyholder Deposits and Investment Funds (NetInsurerDepositInvestment) — Generally financial in nature: disclosed item by insurance companies.|
| LC_CashFlowStatementAll | OtherCashInRelatedOperate | 收到的其他与经营活动有关的现金(元) | | |
| LC_CashFlowStatementAll | SpecialItemsOCIF| ##经营活动现金流入特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsOCIF | ##经营活动现金流入调整项目 | | |
| LC_CashFlowStatementAll | SubtotalOperateCashInflow | 经营活动现金流入小计(元) | | |
| LC_CashFlowStatementAll | GoodsServicesCashPaid | 购买商品和劳务所支付的现金(元) | | |
| LC_CashFlowStatementAll | StaffBehalfPaid | 支付给职工以及为职工支付的现金(元) | | |
| LC_CashFlowStatementAll | AllTaxesPaid| 支付的各项税费(元) | | |
| LC_CashFlowStatementAll | NetLoanAndAdvanceIncrease | 客户贷款及垫款净增加额 | 客户贷款及垫款净增加额（NetLoanAndAdvanceIncrease）：一般为金融类:银行企业披露科目| Net Loan and Advance Increase: Generally refers to financial categories: disclosed items by banking enterprises.|
| LC_CashFlowStatementAll | NetDepositInCBAndIB | 存放中央银行和同业款项净增加额 | 存放中央银行和同业款项净增加额（NetDepositInCBAndIB）：一般为金融类:银行企业披露科目| Net increase in deposits with the central bank and interbank placements (NetDepositInCBAndIB): usually financial in nature: bank enterprises disclose the account |
| LC_CashFlowStatementAll | NetLendCapital| 拆出资金净增加额(元) | | |
| LC_CashFlowStatementAll | CommissionCashPaid| 支付手续费及佣金的现金 | | |
| LC_CashFlowStatementAll | OriginalCompensationPaid| 支付原保险合同赔付款项的现金 | 支付原保险合同赔付款项的现金（OriginalCompensationPaid）：一般为金融类:保险公司披露科目 | Cash paid for the original insurance contract compensation (OriginalCompensationPaid): usually financial: insurance companies disclose items|
| LC_CashFlowStatementAll | NetCashForReinsurance | 支付再保业务现金净额 | 支付再保业务现金净额（NetCashForReinsurance）：一般为金融类:保险公司披露科目| Net Cash for Reinsurance: Generally falls under the financial category: disclosed by insurance companies. |
| LC_CashFlowStatementAll | PolicyDividendCashPaid| 支付保单红利的现金 | 支付保单红利的现金（PolicyDividendCashPaid）：一般为金融类:保险公司披露科目 | Cash paid for policy dividends (PolicyDividendCashPaid): usually financial category: insurance company discloses the subject|
| LC_CashFlowStatementAll | OtherOperateCashPaid| 支付的其他与经营活动有关的现金(元) | | |
| LC_CashFlowStatementAll | SpecialItemsOCOF| ##经营活动现金流出特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsOCOF | ##经营活动现金流出调整项目 | | |
| LC_CashFlowStatementAll | SubtotalOperateCashOutflow| 经营活动现金流出小计(元) | | |
| LC_CashFlowStatementAll | AdjustmentItemsNOCF | ##经营活动现金流量净额调整项目 | | |
| LC_CashFlowStatementAll | NetOperateCashFlow| 经营活动产生的现金流量净额(元) | | |
| LC_CashFlowStatementAll | InvestWithdrawalCash| 收回投资所收到的现金(元) | | |
| LC_CashFlowStatementAll | Investproceeds| 取得投资收益收到的现金(元) | | |
| LC_CashFlowStatementAll | FixIntanOtherAssetDispoCash | 处置固定资产、无形资产和其他长期资产而收回的现金净额(元) | | |
| LC_CashFlowStatementAll | NetCashDealSubCompany | 处置子公司及其他营业单位收到的现金净额 | | |
| LC_CashFlowStatementAll | OtherCashFromInvestAct| 收到的其他与投资活动有关的现金(元) | | |
| LC_CashFlowStatementAll | SpecialItemsICIF| ##投资活动现金流入特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsICIF | ##投资活动现金流入调整项目 | | |
| LC_CashFlowStatementAll | SubtotalInvestCashInflow| 投资活动现金流入小计(元) | | |
| LC_CashFlowStatementAll | FixIntanOtherAssetAcquiCash | 购建固定资产、无形资产和其他长期资产所支付的现金(元) | | |
| LC_CashFlowStatementAll | InvestCashPaid| 投资支付的现金(元) | | |
| LC_CashFlowStatementAll | NetCashFromSubCompany | 取得子公司及其他营业单位支付的现金净额 | | |
| LC_CashFlowStatementAll | ImpawnedLoanNetIncrease | 质押贷款净增加额 | | |
| LC_CashFlowStatementAll | OtherCashToInvestAct| 支付的其他与投资活动有关的现金(元) | | |
| LC_CashFlowStatementAll | SpecialItemsICOF| ##投资活动现金流出特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsICOF | ##投资活动现金流出调整项目 | | |
| LC_CashFlowStatementAll | SubtotalInvestCashOutflow | 投资活动现金流出小计(元) | | |
| LC_CashFlowStatementAll | AdjustmentItemsNICF | ##投资活动现金流量净额调整项目 | | |
| LC_CashFlowStatementAll | NetInvestCashFlow | 投资活动产生的现金流量净额(元) | | |
| LC_CashFlowStatementAll | CashFromInvest| 吸收投资收到的现金(元) | | |
| LC_CashFlowStatementAll | CashFromMinoSInvestSub| 其中:子公司吸收少数股东投资收到的现金| | |
| LC_CashFlowStatementAll | CashFromBondsIssue| 发行债券收到的现金 | | |
| LC_CashFlowStatementAll | CashFromBorrowing | 取得借款收到的现金 | | |
| LC_CashFlowStatementAll | OtherFinanceActCash | 收到其他与筹资活动有关的现金 | | |
| LC_CashFlowStatementAll | SpecialItemsFCIF| ##筹资活动现金流入特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsFCIF | ##筹资活动现金流入调整项目 | | |
| LC_CashFlowStatementAll | SubtotalFinanceCashInflow | 筹资活动现金流入小计(元) | | |
| LC_CashFlowStatementAll | BorrowingRepayment| 偿还债务所支付的现金(元) | | |
| LC_CashFlowStatementAll | DividendInterestPayment | 分配股利、利润或偿付利息支付的现金 | | |
| LC_CashFlowStatementAll | ProceedsFromSubToMinoS| 其中:子公司支付给少数股东的股利、利润或偿付的利息| | |
| LC_CashFlowStatementAll | OtherFinanceActPayment| 支付的其他与筹资活动有关的现金(元) | | |
| LC_CashFlowStatementAll | SpecialItemsFCOF| ##筹资活动现金流出特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsFCOF | ##筹资活动现金流出调整项目 | | |
| LC_CashFlowStatementAll | SubtotalFinanceCashOutflow| 筹资活动现金流出小计(元) | | |
| LC_CashFlowStatementAll | AdjustmentItemsNFCF | ##筹资活动流量现金净额调整项目 | | |
| LC_CashFlowStatementAll | NetFinanceCashFlow| 筹资活动产生的现金流量净额(元) | | |
| LC_CashFlowStatementAll | ExchanRateChangeEffect| 汇率变动对现金的影响额(元) | | |
| LC_CashFlowStatementAll | OtherItemsEffectingCE | ##影响现金及现金等价物的其他科目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsCE | ##影响现金及现金等价物的调整项目 | | |
| LC_CashFlowStatementAll | CashEquivalentIncrease| 现金及现金等价物净增加额(元) | | |
| LC_CashFlowStatementAll | BeginPeriodCash | 期初现金及现金等价物余额(元) | | |
| LC_CashFlowStatementAll | OtherItemsEffectingCEI| ##现金及现金等价物净增加额的特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsCEI| ##现金及现金等价物净增加额的调整项目 | | |
| LC_CashFlowStatementAll | EndPeriodCashEquivalent | 现金及现金等价物的期末余额(元) | | |
| LC_CashFlowStatementAll | NetProfit | 四、净利润(元) | | |
| LC_CashFlowStatementAll | MinorityProfit| 少数股东损益(元) | | |
| LC_CashFlowStatementAll | AssetsDepreciationReserves| 加:资产减值准备| | |
| LC_CashFlowStatementAll | FixedAssetDepreciation| 固定资产折旧(元) | | |
| LC_CashFlowStatementAll | IntangibleAssetAmortization | 无形资产摊销(元) | | |
| LC_CashFlowStatementAll | DeferredExpenseAmort| 长期待摊费用的摊销(元) | | |
| LC_CashFlowStatementAll | DeferredExpenseDecreased| 待摊费用的减少(减:增加)(元)| | |
| LC_CashFlowStatementAll | AccruedExpenseAdded | 预提费用的增加(减:减少)(元)| | |
| LC_CashFlowStatementAll | FixIntanOtherAssetDispoLoss | 处理固定资产、无形资产和其他长期资产的损失(减:收益)(元)| | |
| LC_CashFlowStatementAll | FixedAssetScrapLoss | 固定资产报废损失(减:收益)(元)| | |
| LC_CashFlowStatementAll | LossFromFairValueChanges| 公允价值变动损失 | | |
| LC_CashFlowStatementAll | FinancialExpense| 财务费用(元) | | |
| LC_CashFlowStatementAll | InvestLoss| 投资损失(元) | | |
| LC_CashFlowStatementAll | DeferedTaxAssetDecrease | 递延所得税资产减少 | | |
| LC_CashFlowStatementAll | DeferedTaxLiabilityIncrease | 递延所得税负债增加 | | |
| LC_CashFlowStatementAll | InventoryDecrease | 存货的减少(减:增加)(元)| | |
| LC_CashFlowStatementAll | OperateReceivableDecrease | 经营性应收项目的减少(减：增加)(元) | | |
| LC_CashFlowStatementAll | OperatePayableIncrease| 经营性应付项目的增加 | | |
| LC_CashFlowStatementAll | Others| 其他(元) | | |
| LC_CashFlowStatementAll | SpecialItemsNOCF1 | ##(附注)经营活动现金流量净额特殊项目 | | |
| LC_CashFlowStatementAll | AdjustmentItemsNOCF1| ##(附注)经营活动现金流量净额调整项目 | | |
| LC_CashFlowStatementAll | NetOperateCashFlowNotes | (附注)经营活动产生的现金流量净额(元) | | |
| LC_CashFlowStatementAll | ContrastAdjutmentNOCF | ##加:经营流量净额前后对比调整项目| | |
| LC_CashFlowStatementAll | DebtToCaptical| 债务转为资本(元) | | |
| LC_CashFlowStatementAll | CBsExpiringWithin1Y | 一年内到期的可转换公司债券 | | |
| LC_CashFlowStatementAll | FixedAssetsFinanceLeases| 融资租入固定资产 | | |
| LC_CashFlowStatementAll | CashAtEndOfYear | 现金的期末余额(元) | | |
| LC_CashFlowStatementAll | CashAtBeginningOfYear | 减:现金的期初余额| | |
| LC_CashFlowStatementAll | CashEquivalentsAtEndOfYear| 加:现金等价物的期末余额| | |
| LC_CashFlowStatementAll | CashEquivalentsAtBeginning| 减:现金等价物的期初余额| | |
| LC_CashFlowStatementAll | SpecialItemsC | ##(附注)现金特殊项目(元) | | |
| LC_CashFlowStatementAll | AdjustmentItemsC| ##(附注)现金调整项目 | | |
| LC_CashFlowStatementAll | NetIncrInCashAndEquivalents | (附注)现金及现金等价物净增加额 | | |
| LC_CashFlowStatementAll | ContrastAdjutmentNC | ##加:现金净额前后对比调整项目| | |
| LC_CashFlowStatementAll | SpecialFieldRemark| 特殊字段说明 | | |
| LC_CashFlowStatementAll | UpdateTime| 更新时间 | | |
| LC_CashFlowStatementAll | JSID| JSID | | |
| LC_CashFlowStatementAll | IfComplete| 完整标志 | | |
| LC_CashFlowStatementAll | NetIncBorFunds| 拆入资金净增加额 | 拆入资金净增加额（NetIncBorFunds）：一般为金融类企业披露科目| Net Increase in Funds Borrowed (NetIncBorFunds): This item is generally disclosed by financial companies. |
| LC_CashFlowStatementAll | NetCashRecInVTS | 代理买卖证券收到的现金净额 | 代理买卖证券收到的现金净额（NetCashRecInVTS）：一般为金融类:证券公司披露科目| Net Cash Received from Securities Brokerage Transactions (NetCashRecInVTS): Generally pertains to the financial sector: disclosed by securities companies.|
| LC_CashFlowStatementAll | NetCashRecAgeUTS| 代理承销证券收到的现金净额 | 代理承销证券收到的现金净额（NetCashRecAgeUTS）：一般为金融类:证券公司披露科目 | Net cash proceeds from underwriting securities (NetCashRecAgeUTS): usually for financial sector: securities companies disclose the account|
| LC_CashFlowStatementAll | NetIncFinAssTraPurp | 为交易目的而持有的金融资产净增加额 | | |
| LC_CashFlowStatementAll | NetIncCapResBusOper | 返售业务资金净增加额(经营) | | |
| LC_CashFlowStatementAll | NetIncCapResBusInv| 返售业务资金净增加额(投资) | | |
| LC_CashFlowStatementAll | CashRecIssOthEquIns | 发行其他权益工具收到的现金 | | |
| LC_CashFlowStatementAll | NetBuyBackFin | 回购业务资金净增加额(筹资) | 回购业务资金净增加额（NetBuyBack）：一般为金融类企业披露科目| Net Buyback: Generally disclosed by financial companies as an item|
| LC_CashFlowStatementAll | InterestExpense | 利息支出1| | |
| LC_CashFlowStatementAll | IncResFunding | 受限资金的增加 | | |
| LC_CashFlowStatementAll | IncSpeReserves| 专项储备增加 | | |
| LC_CashFlowStatementAll | CreditImpairmentL | 信用减值损失 | | |
| LC_CashFlowStatementAll | DefProceedsAmo| 递延收益摊销 | | |
| LC_CashFlowStatementAll | IncEstLiability | 预计负债的增加(减:减少)| | |
| LC_CashFlowStatementAll | NetDecFinancialAsset| 融出资金净减少额 | 融出资金净减少额（NetDecFinancialAsset）：一般为金融类企业披露科目| Net decrease in funds (NetDecFinancialAsset): usually disclosed by financial companies|
| LC_CashFlowStatementAll | NetCashPaidInVTS| 代理买卖证券支付的现金净额 | | |
| LC_CashFlowStatementAll | UsufructAssetsDA| 使用权资产摊销/折旧| | |
| LC_CashFlowStatementAll | InfoSourceCode| 信息来源编码 | | |
| LC_CashFlowStatementAll | InsertTime| 发布时间 | | |
| LC_CashFlowStatementAll | NetDecLoanAndAdvance| 客户贷款及垫款净减少额 | | |
| LC_CashFlowStatementAll | NetDecreaseInCBAndIB| 存放中央银行和同业款项净减少额 | 拆出资金净减少额（NetDecFundLending）：一般为金融类企业披露科目 | Net decrease in fund lending (NetDecFundLending): usually disclosed by financial companies|
| LC_CashFlowStatementAll | NetDecFundLending | 拆出资金净减少额 | | |
| LC_CashFlowStatementAll | NetDecCapResBusOper | 返售业务资金净减少额(经营) | 返售业务资金净减少额(经营)（NetDecCapResBusOper）：一般为金融类企业披露科目 | Net decrease in funds for the business of reselling (operation) (NetDecCapResBusOper): usually disclosed by financial companies |
| LC_CashFlowStatementAll | NetDecFinAssTraPurp | 为交易目的而持有的金融资产净减少额 | | |
| LC_CashFlowStatementAll | NetIncFinLiaTraPurp | 为交易目的而持有的金融负债净增加额 | | |
| LC_CashFlowStatementAll | BFLAFValOnPLChange| 客户存款和同业存放款项净减少额 | | |
| LC_CashFlowStatementAll | NetDecBorrowFromCB| 向中央银行借款净减少额 | 向中央银行借款净减少额（NetDecBorrowFromCB）：一般为金融类:银行企业披露科目 | Net decrease in borrowings from the central bank (NetDecBorrowFromCB): Generally refers to financial sector: bank enterprises disclose the account title. |
| LC_CashFlowStatementAll | NetDecBorFromFinanceCo| 向其他金融机构拆入资金净减少额 | 向其他金融机构拆入资金净减少额（NetDecBorFromFinanceCo）：一般为金融类:银行企业披露科目 | Net decrease in funds borrowed from other financial institutions (NetDecBorFromFinanceCo): usually for financial sector: bank enterprise disclosure items |
| LC_CashFlowStatementAll | NetDecInsurDPSTInvest | 保户储金及投资款净减少额 | 保户储金及投资款净减少额（NetDecInsurDPSTInvest）：一般为金融类:保险公司披露科目| Net decrease in policyholder deposits and investment amounts (NetDecInsurDPSTInvest): usually financial category: insurance companies disclose items|
| LC_CashFlowStatementAll | NetDecBorrowingCapital| 拆入资金净减少额 | 拆入资金净减少额（NetDecBorrowingCapital）：一般为金融类企业披露科目| Net decrease in funds borrowed (NetDecBorrowingCapital): This item is generally disclosed by financial companies. |
| LC_CashFlowStatementAll | NetDecOfBuyBack | 回购业务资金净减少额 | | |
| LC_CashFlowStatementAll | NetCashPayAgeUTS| 代理承销证券支付的现金净额 | 代理承销证券支付的现金净额（NetCashPayAgeUTS）：一般为金融类:证券公司披露科目 | Net cash paid for underwriting securities (NetCashPayAgeUTS): usually for financial sector: securities companies disclose items |
| LC_CashFlowStatementAll | NetDecDealTradeAssets | 处置交易性金融资产净减少额 | | |
| LC_CashFlowStatementAll | NetDecFinLiaTraPurp | 为交易目的而持有的金融负债净减少额 | | |
| LC_CashFlowStatementAll | OpeAndAdmExpForCash | 以现金支付的业务及管理费 | | |
| LC_CashFlowStatementAll | NetIncFinancialAsset| 融出资金净增加额 | 融出资金净增加额（NetIncFinancialAsset）：一般为金融类企业披露科目| Net Increase in Funds Lent (NetIncFinancialAsset): This is generally a disclosure item for financial companies. |
| LC_CashFlowStatementAll | NetDecBuyBackFin| 回购业务资金净减少额(筹资) | | |
| LC_CashFlowStatementAll | NPParentCompanyOwners | 其中:归属于母公司所有者的净利润| | |
| LC_CashFlowStatementAll | ProductBioAssetsDep | 其中:生产性生物资产折旧| | |
| LC_CashFlowStatementAll | InterestIncome| 利息收入 | | |
| LC_CashFlowStatementAll | LeaseLiaIntExp| 其中:租赁负债利息支出| | |
| LC_CashFlowStatementAll | BondIssueExpense| 其中:发行债券利息支出| | |
| LC_CashFlowStatementAll | ExchangeLoss| 汇兑损失(收益以"-"号填列)| | |
| LC_CashFlowStatementAll | DeferredTaxCredit | 递延税款贷项(减:借项)1 | | |
| LC_CashFlowStatementAll | SharePayment| 股份支付费用 | | |
| LC_CashFlowStatementAll | DecreaseTradeAssets | 交易性金融资产的减少 | | |
| LC_CashFlowStatementAll | DecAvailableSaleAssets| 可供出售金融资产的减少 | | |
| LC_CashFlowStatementAll | DecreaseLoan| 贷款的减少 | | |
| LC_CashFlowStatementAll | InvestPropertyDA| No description available | | |
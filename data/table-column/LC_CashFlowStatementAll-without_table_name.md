| column_name | column_description | 注释| Annotation|
|---|---|---|---|---|
| ID| ID | | |
| InfoPublDate| 信息发布日期 | | |
| InfoSource| 信息来源 | | |
| BulletinType| 公告类别 | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311 and DM IN (10,20,30,70)，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，70-临时公告。 | The BulletinType is associated with the DM field in the CT_SystemConst table, with LB = 1311 and DM IN (10,20,30,70), resulting in the specific description of the bulletin type: 10-Issue and Listing Prospectus, 20-Regular Report, 30-Earnings Flash, 70-Interim Bulletin. |
| CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。| Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| EndDate | 日期 | | |
| IfAdjusted| 是否调整 | 是否调整(IfAdjusted)与(CT_SystemConst)表中的DM字段关联，令LB = 1188 AND DM IN (1,2,4,5)，得到是否调整的具体描述：1-是，2-否，4-否(7-9月)，5-是(7-9月)。 | Whether to adjust the association of the DM field in the (IfAdjusted) and (CT_SystemConst) tables, let LB = 1188 AND DM IN (1,2,4,5), to obtain the specific description of whether to adjust: 1-Yes, 2-No, 4-No (July-September), 5-Yes (July-September).|
| IfMerged| 合并标志 | 是否合并(IfMerged)与(CT_SystemConst)表中的DM字段关联，令LB = 1189 AND DM IN (1,2)，得到是否合并的具体描述：1-合并，2-母公司。 | Whether to merge the DM field associated with the (IfMerged) and (CT_SystemConst) tables, where LB = 1189 AND DM IN (1,2), to obtain the specific description of whether to merge: 1-merged, 2-parent company.|
| AccountingStandards | 会计准则 | 会计准则(AccountingStandards)与(CT_SystemConst)表中的DM字段关联，令LB = 1455，得到会计准则的具体描述：1-新会计准则(2007)，9-旧会计准则。| Accounting Standards is associated with the DM field in the (CT_SystemConst) table, setting LB = 1455 yields the specific description of the accounting standards: 1 - New Accounting Standards (2007), 9 - Old Accounting Standards. |
| EnterpriseType| 工业企业类型 | 报表格式类型(EnterpriseType)：关联系统常量表，LB=1414，DM IN (13-商业银行，31-证券公司，33-信托公司，35-保险公司，39-其他非银行金融机构，99-一般企业)。 本表报表格式类型(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业性质(CompanyType)。 本表企业性质(EnterpriseType)字段是参照公告原文财务报表披露形式判断得出，并不准确代表企业的实际性质，如需获取企业性质，可通过公司代码（CompanyCode）关联“机构基本资料（LC_InstiArchive）”的公司代码（CompanyCode）获取对应的企业类别(CompanyType)。 | Report format type (EnterpriseType): Associated with the system constant table, LB=1414, DM IN (13-Commercial Bank, 31-Securities Company, 33-Trust Company, 35-Insurance Company, 39-Other Non-Bank Financial Institutions, 99-General Enterprise). The EnterpriseType field in this table is determined by referring to the original text of the announcement on the disclosure form of the financial statements and does not accurately represent the actual nature of the enterprise. If the nature of the enterprise needs to be obtained, it can be done by associating the CompanyCode with the CompanyCode in "Institution Basic Information (LC_InstiArchive)" to get the corresponding CompanyType. The EnterpriseType field in this table is determined by referring to the original text of the announcement on the disclosure form of the financial statements and does not accurately represent the actual nature of the enterprise. If the nature of the enterprise needs to be obtained, it can be done by associating the CompanyCode with the CompanyCode in "Institution Basic Information (LC_InstiArchive)" to get the corresponding Company Category. |
| GoodsSaleServiceRenderCash| 销售商品、提供劳务收到的现金(元) | | |
| TaxLevyRefund | 收到的税费返还(元) | | |
| NetDepositIncrease| 存款增加净额(元) | 客户存款和同业存放款项净增加额（NetDepositIncrease） — 一般为金融类：银行企业披露科目。 | Net increase in customer deposits and interbank placements (Net Deposit Increase) — Generally refers to financial categories: bank enterprise disclosure items. |
| NetBorrowingFromCentralBank | 向中央银行借款净增加额 | 向中央银行借款净增加额（NetBorrowingFromCentralBank） — 一般为金融类：银行企业披露科目。| Net increase in borrowing from the central bank (Net Borrowing From Central Bank) — usually a financial category: disclosed items by banking enterprises. |
| NetBorrowingFromFinanceCo | 向其他金融企业拆借的资金净额(元) | 向其他金融机构拆入资金净增加额（NetBorrowingFromFinanceCo） — 一般为金融类：银行企业披露科目。| Net increase in funds borrowed from other financial institutions (NetBorrowingFromFinanceCo) — usually a financial category: disclosed items by banking enterprises.|
| DrawBackLoansCanceled | 收回已核销贷款 | | |
| InterestAndCommissionCashIn | 收取利息、手续费及佣金的现金 | | |
| NetDealTradingAssets| 处置交易性金融资产净增加额 | | |
| NetBuyBack| 回购业务资金净增加额(元) | | |
| NetOriginalInsuranceCash| 收到原保险合同保费取得的现金 | 收到原保险合同保费取得的现金（NetOriginalInsuranceCash） — 一般为金融类：保险公司披露科目。 | Received cash from the original insurance contract premium (Net Original Insurance Cash) — usually financial in nature: disclosed by insurance companies. |
| NetReinsuranceCash| 收到再保业务现金净额 | 收到再保业务现金净额（NetReinsuranceCash） — 一般为金融类：保险公司披露科目。 | Received net reinsurance cash (Net Reinsurance Cash) — usually financial: disclosed by insurance companies. |
| NetInsurerDepositInvestment | 保户储金及投资款净增加额 | 保户储金及投资款净增加额（NetInsurerDepositInvestment） — 一般为金融类：保险公司披露科目。| Net Increase in Policyholder Deposits and Investment Funds (NetInsurerDepositInvestment) — Generally financial in nature: disclosed item by insurance companies.|
| OtherCashInRelatedOperate | 收到的其他与经营活动有关的现金(元) | | |
| SpecialItemsOCIF| ##经营活动现金流入特殊项目 | | |
| AdjustmentItemsOCIF | ##经营活动现金流入调整项目 | | |
| SubtotalOperateCashInflow | 经营活动现金流入小计(元) | | |
| GoodsServicesCashPaid | 购买商品和劳务所支付的现金(元) | | |
| StaffBehalfPaid | 支付给职工以及为职工支付的现金(元) | | |
| AllTaxesPaid| 支付的各项税费(元) | | |
| NetLoanAndAdvanceIncrease | 客户贷款及垫款净增加额 | 客户贷款及垫款净增加额（NetLoanAndAdvanceIncrease）：一般为金融类:银行企业披露科目| Net Loan and Advance Increase: Generally refers to financial categories: disclosed items by banking enterprises.|
| NetDepositInCBAndIB | 存放中央银行和同业款项净增加额 | 存放中央银行和同业款项净增加额（NetDepositInCBAndIB）：一般为金融类:银行企业披露科目| Net increase in deposits with the central bank and interbank placements (NetDepositInCBAndIB): usually financial in nature: bank enterprises disclose the account |
| NetLendCapital| 拆出资金净增加额(元) | | |
| CommissionCashPaid| 支付手续费及佣金的现金 | | |
| OriginalCompensationPaid| 支付原保险合同赔付款项的现金 | 支付原保险合同赔付款项的现金（OriginalCompensationPaid）：一般为金融类:保险公司披露科目 | Cash paid for the original insurance contract compensation (OriginalCompensationPaid): usually financial: insurance companies disclose items|
| NetCashForReinsurance | 支付再保业务现金净额 | 支付再保业务现金净额（NetCashForReinsurance）：一般为金融类:保险公司披露科目| Net Cash for Reinsurance: Generally falls under the financial category: disclosed by insurance companies. |
| PolicyDividendCashPaid| 支付保单红利的现金 | 支付保单红利的现金（PolicyDividendCashPaid）：一般为金融类:保险公司披露科目 | Cash paid for policy dividends (PolicyDividendCashPaid): usually financial category: insurance company discloses the subject|
| OtherOperateCashPaid| 支付的其他与经营活动有关的现金(元) | | |
| SpecialItemsOCOF| ##经营活动现金流出特殊项目 | | |
| AdjustmentItemsOCOF | ##经营活动现金流出调整项目 | | |
| SubtotalOperateCashOutflow| 经营活动现金流出小计(元) | | |
| AdjustmentItemsNOCF | ##经营活动现金流量净额调整项目 | | |
| NetOperateCashFlow| 经营活动产生的现金流量净额(元) | | |
| InvestWithdrawalCash| 收回投资所收到的现金(元) | | |
| Investproceeds| 取得投资收益收到的现金(元) | | |
| FixIntanOtherAssetDispoCash | 处置固定资产、无形资产和其他长期资产而收回的现金净额(元) | | |
| NetCashDealSubCompany | 处置子公司及其他营业单位收到的现金净额 | | |
| OtherCashFromInvestAct| 收到的其他与投资活动有关的现金(元) | | |
| SpecialItemsICIF| ##投资活动现金流入特殊项目 | | |
| AdjustmentItemsICIF | ##投资活动现金流入调整项目 | | |
| SubtotalInvestCashInflow| 投资活动现金流入小计(元) | | |
| FixIntanOtherAssetAcquiCash | 购建固定资产、无形资产和其他长期资产所支付的现金(元) | | |
| InvestCashPaid| 投资支付的现金(元) | | |
| NetCashFromSubCompany | 取得子公司及其他营业单位支付的现金净额 | | |
| ImpawnedLoanNetIncrease | 质押贷款净增加额 | | |
| OtherCashToInvestAct| 支付的其他与投资活动有关的现金(元) | | |
| SpecialItemsICOF| ##投资活动现金流出特殊项目 | | |
| AdjustmentItemsICOF | ##投资活动现金流出调整项目 | | |
| SubtotalInvestCashOutflow | 投资活动现金流出小计(元) | | |
| AdjustmentItemsNICF | ##投资活动现金流量净额调整项目 | | |
| NetInvestCashFlow | 投资活动产生的现金流量净额(元) | | |
| CashFromInvest| 吸收投资收到的现金(元) | | |
| CashFromMinoSInvestSub| 其中:子公司吸收少数股东投资收到的现金| | |
| CashFromBondsIssue| 发行债券收到的现金 | | |
| CashFromBorrowing | 取得借款收到的现金 | | |
| OtherFinanceActCash | 收到其他与筹资活动有关的现金 | | |
| SpecialItemsFCIF| ##筹资活动现金流入特殊项目 | | |
| AdjustmentItemsFCIF | ##筹资活动现金流入调整项目 | | |
| SubtotalFinanceCashInflow | 筹资活动现金流入小计(元) | | |
| BorrowingRepayment| 偿还债务所支付的现金(元) | | |
| DividendInterestPayment | 分配股利、利润或偿付利息支付的现金 | | |
| ProceedsFromSubToMinoS| 其中:子公司支付给少数股东的股利、利润或偿付的利息| | |
| OtherFinanceActPayment| 支付的其他与筹资活动有关的现金(元) | | |
| SpecialItemsFCOF| ##筹资活动现金流出特殊项目 | | |
| AdjustmentItemsFCOF | ##筹资活动现金流出调整项目 | | |
| SubtotalFinanceCashOutflow| 筹资活动现金流出小计(元) | | |
| AdjustmentItemsNFCF | ##筹资活动流量现金净额调整项目 | | |
| NetFinanceCashFlow| 筹资活动产生的现金流量净额(元) | | |
| ExchanRateChangeEffect| 汇率变动对现金的影响额(元) | | |
| OtherItemsEffectingCE | ##影响现金及现金等价物的其他科目 | | |
| AdjustmentItemsCE | ##影响现金及现金等价物的调整项目 | | |
| CashEquivalentIncrease| 现金及现金等价物净增加额(元) | | |
| BeginPeriodCash | 期初现金及现金等价物余额(元) | | |
| OtherItemsEffectingCEI| ##现金及现金等价物净增加额的特殊项目 | | |
| AdjustmentItemsCEI| ##现金及现金等价物净增加额的调整项目 | | |
| EndPeriodCashEquivalent | 现金及现金等价物的期末余额(元) | | |
| NetProfit | 四、净利润(元) | | |
| MinorityProfit| 少数股东损益(元) | | |
| AssetsDepreciationReserves| 加:资产减值准备| | |
| FixedAssetDepreciation| 固定资产折旧(元) | | |
| IntangibleAssetAmortization | 无形资产摊销(元) | | |
| DeferredExpenseAmort| 长期待摊费用的摊销(元) | | |
| DeferredExpenseDecreased| 待摊费用的减少(减:增加)(元)| | |
| AccruedExpenseAdded | 预提费用的增加(减:减少)(元)| | |
| FixIntanOtherAssetDispoLoss | 处理固定资产、无形资产和其他长期资产的损失(减:收益)(元)| | |
| FixedAssetScrapLoss | 固定资产报废损失(减:收益)(元)| | |
| LossFromFairValueChanges| 公允价值变动损失 | | |
| FinancialExpense| 财务费用(元) | | |
| InvestLoss| 投资损失(元) | | |
| DeferedTaxAssetDecrease | 递延所得税资产减少 | | |
| DeferedTaxLiabilityIncrease | 递延所得税负债增加 | | |
| InventoryDecrease | 存货的减少(减:增加)(元)| | |
| OperateReceivableDecrease | 经营性应收项目的减少(减：增加)(元) | | |
| OperatePayableIncrease| 经营性应付项目的增加 | | |
| Others| 其他(元) | | |
| SpecialItemsNOCF1 | ##(附注)经营活动现金流量净额特殊项目 | | |
| AdjustmentItemsNOCF1| ##(附注)经营活动现金流量净额调整项目 | | |
| NetOperateCashFlowNotes | (附注)经营活动产生的现金流量净额(元) | | |
| ContrastAdjutmentNOCF | ##加:经营流量净额前后对比调整项目| | |
| DebtToCaptical| 债务转为资本(元) | | |
| CBsExpiringWithin1Y | 一年内到期的可转换公司债券 | | |
| FixedAssetsFinanceLeases| 融资租入固定资产 | | |
| CashAtEndOfYear | 现金的期末余额(元) | | |
| CashAtBeginningOfYear | 减:现金的期初余额| | |
| CashEquivalentsAtEndOfYear| 加:现金等价物的期末余额| | |
| CashEquivalentsAtBeginning| 减:现金等价物的期初余额| | |
| SpecialItemsC | ##(附注)现金特殊项目(元) | | |
| AdjustmentItemsC| ##(附注)现金调整项目 | | |
| NetIncrInCashAndEquivalents | (附注)现金及现金等价物净增加额 | | |
| ContrastAdjutmentNC | ##加:现金净额前后对比调整项目| | |
| SpecialFieldRemark| 特殊字段说明 | | |
| UpdateTime| 更新时间 | | |
| JSID| JSID | | |
| IfComplete| 完整标志 | | |
| NetIncBorFunds| 拆入资金净增加额 | 拆入资金净增加额（NetIncBorFunds）：一般为金融类企业披露科目| Net Increase in Funds Borrowed (NetIncBorFunds): This item is generally disclosed by financial companies. |
| NetCashRecInVTS | 代理买卖证券收到的现金净额 | 代理买卖证券收到的现金净额（NetCashRecInVTS）：一般为金融类:证券公司披露科目| Net Cash Received from Securities Brokerage Transactions (NetCashRecInVTS): Generally pertains to the financial sector: disclosed by securities companies.|
| NetCashRecAgeUTS| 代理承销证券收到的现金净额 | 代理承销证券收到的现金净额（NetCashRecAgeUTS）：一般为金融类:证券公司披露科目 | Net cash proceeds from underwriting securities (NetCashRecAgeUTS): usually for financial sector: securities companies disclose the account|
| NetIncFinAssTraPurp | 为交易目的而持有的金融资产净增加额 | | |
| NetIncCapResBusOper | 返售业务资金净增加额(经营) | | |
| NetIncCapResBusInv| 返售业务资金净增加额(投资) | | |
| CashRecIssOthEquIns | 发行其他权益工具收到的现金 | | |
| NetBuyBackFin | 回购业务资金净增加额(筹资) | 回购业务资金净增加额（NetBuyBack）：一般为金融类企业披露科目| Net Buyback: Generally disclosed by financial companies as an item|
| InterestExpense | 利息支出1| | |
| IncResFunding | 受限资金的增加 | | |
| IncSpeReserves| 专项储备增加 | | |
| CreditImpairmentL | 信用减值损失 | | |
| DefProceedsAmo| 递延收益摊销 | | |
| IncEstLiability | 预计负债的增加(减:减少)| | |
| NetDecFinancialAsset| 融出资金净减少额 | 融出资金净减少额（NetDecFinancialAsset）：一般为金融类企业披露科目| Net decrease in funds (NetDecFinancialAsset): usually disclosed by financial companies|
| NetCashPaidInVTS| 代理买卖证券支付的现金净额 | | |
| UsufructAssetsDA| 使用权资产摊销/折旧| | |
| InfoSourceCode| 信息来源编码 | | |
| InsertTime| 发布时间 | | |
| NetDecLoanAndAdvance| 客户贷款及垫款净减少额 | | |
| NetDecreaseInCBAndIB| 存放中央银行和同业款项净减少额 | 拆出资金净减少额（NetDecFundLending）：一般为金融类企业披露科目 | Net decrease in fund lending (NetDecFundLending): usually disclosed by financial companies|
| NetDecFundLending | 拆出资金净减少额 | | |
| NetDecCapResBusOper | 返售业务资金净减少额(经营) | 返售业务资金净减少额(经营)（NetDecCapResBusOper）：一般为金融类企业披露科目 | Net decrease in funds for the business of reselling (operation) (NetDecCapResBusOper): usually disclosed by financial companies |
| NetDecFinAssTraPurp | 为交易目的而持有的金融资产净减少额 | | |
| NetIncFinLiaTraPurp | 为交易目的而持有的金融负债净增加额 | | |
| BFLAFValOnPLChange| 客户存款和同业存放款项净减少额 | | |
| NetDecBorrowFromCB| 向中央银行借款净减少额 | 向中央银行借款净减少额（NetDecBorrowFromCB）：一般为金融类:银行企业披露科目 | Net decrease in borrowings from the central bank (NetDecBorrowFromCB): Generally refers to financial sector: bank enterprises disclose the account title. |
| NetDecBorFromFinanceCo| 向其他金融机构拆入资金净减少额 | 向其他金融机构拆入资金净减少额（NetDecBorFromFinanceCo）：一般为金融类:银行企业披露科目 | Net decrease in funds borrowed from other financial institutions (NetDecBorFromFinanceCo): usually for financial sector: bank enterprise disclosure items |
| NetDecInsurDPSTInvest | 保户储金及投资款净减少额 | 保户储金及投资款净减少额（NetDecInsurDPSTInvest）：一般为金融类:保险公司披露科目| Net decrease in policyholder deposits and investment amounts (NetDecInsurDPSTInvest): usually financial category: insurance companies disclose items|
| NetDecBorrowingCapital| 拆入资金净减少额 | 拆入资金净减少额（NetDecBorrowingCapital）：一般为金融类企业披露科目| Net decrease in funds borrowed (NetDecBorrowingCapital): This item is generally disclosed by financial companies. |
| NetDecOfBuyBack | 回购业务资金净减少额 | | |
| NetCashPayAgeUTS| 代理承销证券支付的现金净额 | 代理承销证券支付的现金净额（NetCashPayAgeUTS）：一般为金融类:证券公司披露科目 | Net cash paid for underwriting securities (NetCashPayAgeUTS): usually for financial sector: securities companies disclose items |
| NetDecDealTradeAssets | 处置交易性金融资产净减少额 | | |
| NetDecFinLiaTraPurp | 为交易目的而持有的金融负债净减少额 | | |
| OpeAndAdmExpForCash | 以现金支付的业务及管理费 | | |
| NetIncFinancialAsset| 融出资金净增加额 | 融出资金净增加额（NetIncFinancialAsset）：一般为金融类企业披露科目| Net Increase in Funds Lent (NetIncFinancialAsset): This is generally a disclosure item for financial companies. |
| NetDecBuyBackFin| 回购业务资金净减少额(筹资) | | |
| NPParentCompanyOwners | 其中:归属于母公司所有者的净利润| | |
| ProductBioAssetsDep | 其中:生产性生物资产折旧| | |
| InterestIncome| 利息收入 | | |
| LeaseLiaIntExp| 其中:租赁负债利息支出| | |
| BondIssueExpense| 其中:发行债券利息支出| | |
| ExchangeLoss| 汇兑损失(收益以"-"号填列)| | |
| DeferredTaxCredit | 递延税款贷项(减:借项)1 | | |
| SharePayment| 股份支付费用 | | |
| DecreaseTradeAssets | 交易性金融资产的减少 | | |
| DecAvailableSaleAssets| 可供出售金融资产的减少 | | |
| DecreaseLoan| 贷款的减少 | | |
| InvestPropertyDA| No description available | | |
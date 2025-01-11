| table_name| column_name| column_description| 注释 | Annotation |
|---|---|---|---|---|
| LC_IndFinIndicators | ID | ID|||
| LC_IndFinIndicators | IndustryNum| 行业内部编码| 与(CT_IndustryType)表中的IndustryNum字段关联，令IndustryNum=IndustryNum，得到行业内部编码的具体描述。| Associate with the IndustryNum field in the (CT_IndustryType) table, set IndustryNum=IndustryNum, to obtain the specific description of the industry internal code.|
| LC_IndFinIndicators | IndustryName | 行业名称|||
| LC_IndFinIndicators | Classification | 行业级别|||
| LC_IndFinIndicators | IndustryCode | 行业代码|||
| LC_IndFinIndicators | Standard | 行业划分标准| 行业划分标准(Standard)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 AND DM IN (41)，得到行业划分标准的具体描述：41-申万行业分类2021版。| The industry classification standard (Standard) is associated with the DM field in the (CT_SystemConst) table, with LB = 1081 AND DM IN (41), yielding the specific description of the industry classification standard: 41-Shenwan Industry Classification 2021 Edition.|
| LC_IndFinIndicators | StatType | 统计类型| 统计类型(StatType)，该字段固定以下常量：1-整体法不剔除负值。 | Statistical type (StatType), this field is fixed with the following constants: 1 - the overall method does not exclude negative values.|
| LC_IndFinIndicators | SectorCode | 统计板块| 统计板块(SectorCode)，该字段固定以下常量：5-沪、深及北交所市场。 | Statistics section (SectorCode), this field is fixed with the following constants: 5-Shanghai, Shenzhen and Beijing Stock Exchange markets.|
| LC_IndFinIndicators | InfoPublDate | 信息发布日期|||
| LC_IndFinIndicators | EndDate| 截止日期|||
| LC_IndFinIndicators | DataMark | 数据标志| 数据标志(DataMark)，该字段固定以下常量：1-完整财报期，2-最新财报期，9-财报更正。 | DataMark, this field is fixed with the following constants: 1-Complete financial reporting period, 2-Latest financial reporting period, 9-Financial report correction. |
| LC_IndFinIndicators | ListedSecuNum| 上市证券数量(只)|||
| LC_IndFinIndicators | IndOperatingRevenueTTM | 行业营业收入TTM(万元) | 为行业内公司营业收入TTM总值，行业均值可用该值除以上市证券数量。| For the total value of TTM operating revenue of companies in the industry, the industry average can be obtained by dividing this value by the number of listed securities. |
| LC_IndFinIndicators | IndOperatingRevenue| 行业营业收入(万元)|||
| LC_IndFinIndicators | IndOperatingCost | 行业营业成本(万元)|||
| LC_IndFinIndicators | IndOperatingProfitTTM| 行业营业利润TTM(万元) |||
| LC_IndFinIndicators | IndOperatingProfit | 行业营业利润(万元)|||
| LC_IndFinIndicators | IndNetProfitTTM| 行业净利润TTM(万元) |||
| LC_IndFinIndicators | IndNetProfit | 行业净利润(万元)|||
| LC_IndFinIndicators | IndNPCOwnersTTM| 行业归属母公司的净利润TTM(万元) | 为行业内归属母公司的净利润TTM总值，行业均值可用该值除以上市证券数量。| The total value of net profit attributable to the parent company in the industry TTM, the industry average can be obtained by dividing this value by the number of listed securities.|
| LC_IndFinIndicators | IndNPParentComOwners | 行业归属母公司的净利润(万元)| 采用整体法进行计算：（行业内所有公司当期归母净利润总值-其上期归母净利润总值）/其上期归母净利润总值。（若有公司未披露当期或上期归母净利润，则剔除该样本）。 | Calculate using the overall method: (The total value of the net profit attributable to the parent company of all companies in the industry during the current period - the total value of the net profit attributable to the parent company in the previous period) / the total value of the net profit attributable to the parent company in the previous period. (If a company has not disclosed the net profit attributable to the parent company for the current or previous period, exclude that sample.) |
| LC_IndFinIndicators | IndNetAssets | 行业净资产(万元)|||
| LC_IndFinIndicators | IndTotalAssets | 行业总资产(万元)|||
| LC_IndFinIndicators | IndTotalShares | 行业总股本(万股)|||
| LC_IndFinIndicators | EPSAvg | 每股收益_均值(元) | ∑(个股归母净利润 /个股期末总股本)/证券数。 | The sum of (net profit attributable to shareholders of listed companies / total equity of listed companies at the end of the period) divided by the number of securities.|
| LC_IndFinIndicators | ROEAvg | 净资产收益率_平均(%)| ∑归母净利润*2 / ∑（归母股东权益MRQ+期初归母股东权益）。| Sum of net profit attributable to shareholders * 2 / Sum (equity attributable to shareholders MRQ + beginning equity attributable to shareholders).|
| LC_IndFinIndicators | ROE| 净资产收益率_摊薄(%)| ∑归母净利润 / ∑归母股东权益MRQ。 | Sum of net profit attributable to shareholders / Sum of equity attributable to shareholders MRQ. |
| LC_IndFinIndicators | ROETTM | 净资产收益率_TTM(%) | ∑归母净利润TTM / ∑归母股东权益MRQ。| Sum of net profit attributable to shareholders TTM / Sum of equity attributable to shareholders MRQ. |
| LC_IndFinIndicators | WROECut| 净资产收益率_扣除,平均(%) | ∑扣非归母净利润*2 / ∑（归母股东权益MRQ+期初归母股东权益）。| Sum of non-net profit attributable to shareholders * 2 / Sum (net assets of shareholders MRQ + beginning net assets of shareholders).|
| LC_IndFinIndicators | ROECut | 净资产收益率_扣除,摊薄(%) | ∑扣非归母净利润 / ∑归母股东权益MRQ。 | Sum of non-GAAP net profit attributable to shareholders / Sum of equity attributable to shareholders MRQ.|
| LC_IndFinIndicators | ROAAvg | 总资产净利率_平均(%)| ∑净利润*2 / ∑（总资产+期初总资产）。 | Total net profit * 2 / Sum (total assets + beginning total assets).|
| LC_IndFinIndicators | DilutedROA | 总资产净利率_摊薄(%)| ∑净利润 / ∑期末总资产。| Total net profit / Total total assets at the end of the period.|
| LC_IndFinIndicators | ROATTM | 总资产净利率_TTM(%) | ∑净利润TTM / ∑期末总资产。 | Sum of net profit TTM / Sum of total assets at the end of the period.|
| LC_IndFinIndicators | GrossIncomeRatio | 销售毛利率(%) | ∑毛利润 / ∑营业收入，金融企业不适用。| Gross profit margin / Total operating revenue, not applicable to financial enterprises.|
| LC_IndFinIndicators | GrossIncomeRatioTTM| 销售毛利率_TTM(%) | ∑毛利润TTM / ∑营业收入TTM，金融企业不适用。| Gross Profit TTM / Operating Revenue TTM, not applicable for financial enterprises.|
| LC_IndFinIndicators | NetProfitRatio | 销售净利率(%) | ∑净利润 / ∑营业收入。| Total net profit / Total operating revenue.|
| LC_IndFinIndicators | NetProfitRatioTTM| 销售净利率_TTM(%) | ∑净利润TTM / ∑营业收入TTM。| Sum of net profit TTM / Sum of operating revenue TTM.|
| LC_IndFinIndicators | NetProfitRatioCut| 销售净利率_扣除(%)| ∑扣非净利润 / ∑营业收入。| Sum of non-net profit / Sum of operating revenue.|
| LC_IndFinIndicators | FinExpenseRateTTM| 财务费用/营业收入TTM(%) | ∑财务费用 TTM/ ∑营业收入TTM，金融企业不适用。| The ratio of total financial expenses TTM to total operating revenue TTM, not applicable to financial enterprises. |
| LC_IndFinIndicators | OperatingExpenseRate | 销售费用/营业总收入(%)| ∑销售费用 / ∑营业总收入，金融企业不适用。| The sum of selling expenses divided by the sum of total operating income, not applicable to financial enterprises. |
| LC_IndFinIndicators | OperatExpenseRateTTM | 销售费用/营业总收入_TTM(%)| ∑销售费用TTM / ∑营业总收入TTM，金融企业不适用。| The ratio of total selling expenses TTM to total operating revenue TTM, not applicable to financial enterprises. |
| LC_IndFinIndicators | PeriodCostsRate| 销售期间费用率(%) | ∑销售期间费用 / ∑营业收入，销售期间费用=销售费用+管理费用+财务费用+研发费用，金融企业不适用。| The ratio of total selling period expenses to total operating revenue, where total selling period expenses equals the sum of selling expenses, administrative expenses, financial expenses, and research and development expenses, not applicable to financial enterprises.|
| LC_IndFinIndicators | TOperatingCostToTOR| 营业总成本/营业总收入(%)| ∑营业总成本 / ∑营业总收入，金融企业不适用。| The sum of total operating costs divided by the sum of total operating revenue, not applicable to financial enterprises. |
| LC_IndFinIndicators | ROIC | 投入资本回报率(%) | ∑息税前利润（1-有效税率）2 / ∑（期末全部投入资本+期初全部投入资本），金融企业不适用。| Pre-tax profit (1 - effective tax rate)^2 / ∑ (total investment at the end of the period + total investment at the beginning of the period), not applicable to financial enterprises.|
| LC_IndFinIndicators | CurrentRatio | 流动比率(%) | ∑流动资产 / ∑流动负债，金融企业不适用。| The ratio of total current assets to total current liabilities, not applicable to financial enterprises. |
| LC_IndFinIndicators | QuickRatio | 速动比率(%) | ∑(流动资产-存货)/∑利息费用，金融企业不适用 | The sum of (current assets - inventory) divided by the sum of interest expenses, not applicable to financial enterprises.|
| LC_IndFinIndicators | InterestCover| 利息保障倍数(倍)| ∑息税前利润 / ∑利息费用，金融企业不适用| Pre-tax profit / Interest expenses, not applicable to financial enterprises. |
| LC_IndFinIndicators | NOCFInterestCover| 经营现金流利息保障倍数(倍)| ∑经营活动产生的现金流量净额 / ∑利息费用，金融企业不适用| Net cash flow generated by operating activities / Total interest expenses, not applicable to financial enterprises |
| LC_IndFinIndicators | NPParentCompanyYOY | 归属母公司股东的净利润同比增长(%) | （∑归母净利润-∑上年同期归母净利润） /|∑上年同期归母净利润| | (Σ net profit attributable to shareholders of the parent company - Σ net profit attributable to shareholders of the parent company in the same period of the previous year) / |Σ net profit attributable to shareholders of the parent company in the same period of the previous year||
| LC_IndFinIndicators | GrossProfitYOY | 毛利润同比增长率(%) | （∑毛利润-∑上年同期毛利润） // |∑上年同期毛利润|，金融企业不适用 | (Σ gross profit - Σ gross profit of the same period last year) // |Σ gross profit of the same period last year|, not applicable to financial enterprises |
| LC_IndFinIndicators | InventoryTRate | 存货周转率(次)| ∑营业成本*2 / ∑（存货+期初存货），金融企业不适用 | The sum of operating costs multiplied by 2 divided by the sum of (inventory + beginning inventory), not applicable to financial enterprises. |
| LC_IndFinIndicators | InventoryTDays | 存货周转天数(天)| 周期天数 / 存货周转率，存货周转率=∑营业成本*2 / ∑（存货+期初存货），金融企业不适用 | Number of days in period / Inventory turnover rate, Inventory turnover rate = ∑Operating cost * 2 / ∑(Inventory + Beginning inventory), Not applicable for financial enterprises |
| LC_IndFinIndicators | ARTRate| 应收账款周转率(次)| ∑营业收入*2 / ∑（应收账款+期初应收账款），金融企业不适用 | The sum of operating revenue multiplied by 2 divided by the sum of accounts receivable plus initial accounts receivable, not applicable to financial enterprises.|
| LC_IndFinIndicators | ARTDays| 应收账款周转天数(天)| 周期天数 / 应收账款周转率，应收账款周转率=∑营业收入*2 / ∑（应收账款+期初应收账款），金融企业不适用 | Number of days in the period / Accounts Receivable Turnover Rate, Accounts Receivable Turnover Rate = ∑Operating Revenue * 2 / ∑(Accounts Receivable + Beginning Accounts Receivable), not applicable to financial enterprises.|
| LC_IndFinIndicators | ReceivableTRate| 应收款项周转率(次)| ∑营业收入*2 / ∑（应收款项+期初应收款项），应收款项=应收账款及应收票据+其他应收款合计+应收款项融资，金融企业不适用| Total operating revenue * 2 / Total (accounts receivable + beginning accounts receivable), accounts receivable = accounts receivable and bills receivable + other receivables + accounts receivable financing, not applicable to financial enterprises.|
| LC_IndFinIndicators | TotalAssetTRate| 总资产周转率(次)| ∑营业总收入*2 / ∑（总资产+期初总资产），金融企业用营业收入 | Total operating revenue * 2 / Sum (total assets + beginning total assets), financial enterprises use business revenue|
| LC_IndFinIndicators | NetOperCFToToOperReve| 经营现金净流量/营业总收入(%)| ∑经营现金净流量 / ∑营业总收入，金融企业用营业收入| Net operating cash flow / Total operating revenue, financial enterprises use business revenue|
| LC_IndFinIndicators | DebtAssetsRatio| 资产负债率(%) | ∑期末总负债 / ∑期末总资产| Total liabilities at the end of the period / Total assets at the end of the period |
| LC_IndFinIndicators | NetTangibleAssetsTA| 有形资产净值/总资产(%)| （归母股东权益-（无形资产+开发支出+商誉+长期待摊费用+递延所得税资产）） / 总资产，金融企业不适用 | (Mother company's shareholders' equity - (intangible assets + development expenses + goodwill + long-term deferred expenses + deferred tax assets)) / total assets, not applicable to financial enterprises|
| LC_IndFinIndicators | OutInvestOwnersEquity| 对外投资/所有者权益(%)| ∑（交易性金融资产+可供出售金融资产+持有至到期投资+长期股权投资+债权投资+其他债权投资+其他权益工具投资） / ∑所有者权益合计| The sum of (trading financial assets + available-for-sale financial assets + held-to-maturity investments + long-term equity investments + debt investments + other debt investments + other equity instrument investments) divided by the sum of total owners' equity.|
| LC_IndFinIndicators | AdvanceReceToTOR | 预收账款/营业收入TTM(%) |||
| LC_IndFinIndicators | AccountReceToTOR | 应收账款/营业收入TTM(%) |||
| LC_IndFinIndicators | InsertTime | 发布时间|||
| LC_IndFinIndicators | UpdateTime | 修改时间|||
| LC_IndFinIndicators | JSID | JSID|||
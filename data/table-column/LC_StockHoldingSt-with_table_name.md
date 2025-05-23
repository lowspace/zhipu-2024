| table_name| column_name | column_description| 注释 | Annotation |
|---|---|---|---|---|
| LC_StockHoldingSt | ID| ID|||
| LC_StockHoldingSt | InnerCode | 证券内部编码| 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。 | Security Internal Code (InnerCode): Associated with the "Security Main Table (SecuMain)" "Security Internal Code (InnerCode)", to obtain the security's trading code, abbreviation, etc. |
| LC_StockHoldingSt | CompanyCode | 公司代码| 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.|
| LC_StockHoldingSt | EndDate | 日期|||
| LC_StockHoldingSt | InfoSource| 信息来源| 信息来源(InfoSource)：当InfoSource为“基金定报”时，数据源仅为基金定报；当InfoSource非“基金定报”时，数据源为上市公司定报及基金定报。 | InfoSource: When InfoSource is "Fund Regular Report", the data source is only the Fund Regular Report; when InfoSource is not "Fund Regular Report", the data source is the listed company's regular report and the Fund Regular Report. |
| LC_StockHoldingSt | InstitutionsHoldings| 机构持有无限售流通A股数量合计(股) |||
| LC_StockHoldingSt | FundsHoldings | 公募基金持有无限售流通A股数量(股) | 由于基金披露的持股数中，没有明确给出无限售部分是多少，故该“基金持有无限售流通A股数量”及“基金持有无限售流通A股比例”的值暂时不计算，为空值 | Since the fund's disclosed shareholding does not explicitly state how much of it is non-restricted, the values for "Fund's non-restricted tradable A-share quantity" and "Fund's non-restricted tradable A-share ratio" are temporarily not calculated and are left blank. |
| LC_StockHoldingSt | SecuritiesCorpsHoldings | 券商持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | FinancingProductsHoldings | 券商理财产品持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | QFIIHoldings| QFII持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | InsuranceCorpsHoldings| 保险公司持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | SocialSecurityFundHold| 社保基金持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | EnterpriseAnnuitiesHold | 企业年金持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | TrustCompaniesHoldings| 信托公司持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | FinanceCompaniesHoldings| 财务公司持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | OtherInstitutionHoldings| 其它机构持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | InstitutionsHoldProp| 机构持有无限售流通A股比例合计(%)|||
| LC_StockHoldingSt | FundsHoldProp | 基金持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | SecuritiesCorpsHoldProp | 券商持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | FinancingProductsHoldProp | 券商理财产品持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | QFIIHoldProp| QFII持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | InsuranceCorpsHoldProp| 保险公司持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | SocialSecuFundHoldProp| 社保基金持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | CorpAnnuitiesHoldProp | 企业年金持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | TrustCompaniesHoldProp| 信托公司持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | FinanceCompaniesHoldProp| 财务公司持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | OtherInstitutionHoldProp| 其它机构持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | InstitutionsHoldingsA | 机构持有A股数量合计(股) |||
| LC_StockHoldingSt | FundsHoldingsA| 基金持有A股数量(股) |||
| LC_StockHoldingSt | SecuritiesCorpsHoldingsA| 券商持有A股数量(股) |||
| LC_StockHoldingSt | FinanceProductsHoldingsA| 券商理财产品持有A股数量(股) |||
| LC_StockHoldingSt | QFIIHoldingsA | QFII持有A股数量(股) |||
| LC_StockHoldingSt | InsuranceCorpsHoldingsA | 保险公司持有A股数量(股) |||
| LC_StockHoldingSt | SocialSecurityFundHoldA | 社保基金持有A股数量(股) |||
| LC_StockHoldingSt | EnterpriseAnnuitiesHoldA| 企业年金持有A股数量(股) |||
| LC_StockHoldingSt | TrustCompaniesHoldingsA | 信托公司持有A股数量(股) |||
| LC_StockHoldingSt | FinanceCompHoldingsA| 财务公司持有A股数量(股) |||
| LC_StockHoldingSt | OtherInstiHoldingsA | 其它机构持有A股数量(股) |||
| LC_StockHoldingSt | InstitutionsHoldPropA | 机构持有A股比例合计(%)|||
| LC_StockHoldingSt | FundsHoldPropA| 基金持有A股比例(%)|||
| LC_StockHoldingSt | SecuritiesCorpsHoldPropA| 券商持有A股比例(%)|||
| LC_StockHoldingSt | FinanceProductsHoldPropA| 券商理财产品持有A股比例(%)|||
| LC_StockHoldingSt | QFIIHoldPropA | QFII持有A股比例(%)|||
| LC_StockHoldingSt | InsuranceCorpsHoldPropA | 保险公司持有A股比例(%)|||
| LC_StockHoldingSt | SocialSecuFundHoldPropA | 社保基金持有A股比例(%)|||
| LC_StockHoldingSt | CorpAnnuitiesHoldPropA| 企业年金持有A股比例(%)|||
| LC_StockHoldingSt | TrustCompaniesHoldPropA | 信托公司持有A股比例(%)|||
| LC_StockHoldingSt | FinanceCompHoldPropA| 财务公司持有A股比例(%)|||
| LC_StockHoldingSt | OtherInstiHoldPropA | 其它机构持有A股比例(%)|||
| LC_StockHoldingSt | InstitutionsHoldingsT | 机构持股数量合计(股)|||
| LC_StockHoldingSt | FundsHoldingsT| 基金持股数量(股)|||
| LC_StockHoldingSt | SecuritiesCorpsHoldingsT| 券商持股数量(股)|||
| LC_StockHoldingSt | FinanceProductsHoldingsT| 券商理财产品持股数量(股)|||
| LC_StockHoldingSt | QFIIHoldingsT | QFII持股数量(股)|||
| LC_StockHoldingSt | InsuranceCorpsHoldingsT | 保险公司持股数量(股)|||
| LC_StockHoldingSt | SocialSecurityFundHoldT | 社保基金持股数量(股)|||
| LC_StockHoldingSt | EnterpriseAnnuitiesHoldT| 企业年金持股数量(股)|||
| LC_StockHoldingSt | TrustCompaniesHoldingsT | 信托公司持股数量(股)|||
| LC_StockHoldingSt | FinanceCompHoldingsT| 财务公司持股数量(股)|||
| LC_StockHoldingSt | OtherInstiHoldingsT | 其它机构持股数量(股)|||
| LC_StockHoldingSt | InstitutionsHoldPropT | 机构持股比例合计(%) |||
| LC_StockHoldingSt | FundsHoldPropT| 基金持股比例(%) |||
| LC_StockHoldingSt | SecuritiesCorpsHoldPropT| 券商持股比例(%) |||
| LC_StockHoldingSt | FinanceProductsHoldPropT| 券商理财产品持股比例(%) |||
| LC_StockHoldingSt | QFIIHoldPropT | QFII持股比例(%) |||
| LC_StockHoldingSt | InsuranceCorpsHoldPropT | 保险公司持股比例(%) |||
| LC_StockHoldingSt | SocialSecuFundHoldPropT | 社保基金持股比例(%) |||
| LC_StockHoldingSt | CorpAnnuitiesHoldPropT| 企业年金持股比例(%) |||
| LC_StockHoldingSt | TrustCompaniesHoldPropT | 信托公司持股比例(%) |||
| LC_StockHoldingSt | FinanceCompHoldPropT| 财务公司持股比例(%) |||
| LC_StockHoldingSt | OtherInstiHoldPropT | 其它机构持股比例(%) |||
| LC_StockHoldingSt | Top10StockholdersAmount | 前十大股东持股数量合计(股)|||
| LC_StockHoldingSt | Top10StockholdersProp | 前十大股东持股比例合计(%) |||
| LC_StockHoldingSt | Top10NRStockholdersAmount | 前十大无限售股东持股数量合计(股)|||
| LC_StockHoldingSt | Top10NRHoldersAmountToNRS | 前十大无限售股东持股数占无限售股本比例(%) |||
| LC_StockHoldingSt | Top10NRHoldersAmountToTS| 前十大无限售股东持股数占总股本的比例(%) |||
| LC_StockHoldingSt | NRAFromTop10NRHolders | 前十大无限售股东持有无限售A股数量合计(股) |||
| LC_StockHoldingSt | NRAFromTop10ToNRA | 前十大无限售股东持有无限售A股数占无限售A股比例(%) |||
| LC_StockHoldingSt | UpdateTime| 更新时间|||
| LC_StockHoldingSt | JSID| JSID|||
| LC_StockHoldingSt | InstiHoldTNum | 机构持股户数|||
| LC_StockHoldingSt | InstiHoldANum | 机构持有流通A股户数 |||
| LC_StockHoldingSt | InstiHoldNum| 机构持有无限售流通A股户数 |||
| LC_StockHoldingSt | FundsHoldingsTNum | 基金持股户数|||
| LC_StockHoldingSt | SecuCorpsHoldTNum | 券商持股户数|||
| LC_StockHoldingSt | SecuCorpsHoldANum | 券商持有流通A股户数 |||
| LC_StockHoldingSt | SecuCorpsHoldNum| 券商持有无限售流通A股户数 |||
| LC_StockHoldingSt | FinProductsHoldTNum | 券商理财产品持股户数|||
| LC_StockHoldingSt | FinProductsHoldANum | 券商理财产品持有流通A股户数 |||
| LC_StockHoldingSt | FinProductsHoldNum| 券商理财产品持有无限售流通A股户数 |||
| LC_StockHoldingSt | QFIIHoldTNumber | QFII持股户数|||
| LC_StockHoldingSt | QFIIHoldANum| QFII持有流通A股户数 |||
| LC_StockHoldingSt | QFIIHoldingsNum | QFII持有无限售流通A股户数 |||
| LC_StockHoldingSt | InsurCorpsHoldTNum| 保险公司持股户数|||
| LC_StockHoldingSt | InsurCorpsHoldANum| 保险公司持有流通A股户数 |||
| LC_StockHoldingSt | InsurCorpsHoldNum | 保险公司持有无限售流通A股户数 |||
| LC_StockHoldingSt | SocialSecuFundHoldTN| 社保基金持股户数|||
| LC_StockHoldingSt | SocialSecuFundHoldAN| 社保基金持有流通A股户数 |||
| LC_StockHoldingSt | SocialSecuFundHoldN | 社保基金持有无限售流通A股户数 |||
| LC_StockHoldingSt | EntAnnuitiesHoldTNum| 企业年金持股户数|||
| LC_StockHoldingSt | EntAnnuitiesHoldANum| 企业年金持有流通A股户数 |||
| LC_StockHoldingSt | EntAnnuitiesHoldNum | 企业年金持有无限售流通A股户数 |||
| LC_StockHoldingSt | TrustCoHoldTNum | 信托公司持股户数|||
| LC_StockHoldingSt | TrustCoHoldANum | 信托公司持有流通A股户数 |||
| LC_StockHoldingSt | TrustCoHoldNum| 信托公司持有无限售流通A股户数 |||
| LC_StockHoldingSt | FinanceCoHoldTNum | 财务公司持股户数|||
| LC_StockHoldingSt | FinanceCoHoldANum | 财务公司持有流通A股户数 |||
| LC_StockHoldingSt | FinanceCoHoldNum| 财务公司持有无限售流通A股户数 |||
| LC_StockHoldingSt | OtherInstiHoldTNum| 其他机构持股户数|||
| LC_StockHoldingSt | OtherInstiHoldANum| 其他机构持有流通A股户数 |||
| LC_StockHoldingSt | OtherInstiHoldNum | 其他机构持有无限售流通A股户数 |||
| LC_StockHoldingSt | InsertTime| 发布时间|||
| LC_StockHoldingSt | StatDate| 统计日期|||
| LC_StockHoldingSt | PrivFundHoldings| 私募基金持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | BankHoldings| 银行持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | ForeignInstHoldings | 外资机构持有无限售流通A股数量(股) |||
| LC_StockHoldingSt | PrivFundHoldProp| 私募基金持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | BankHoldProp| 银行持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | ForeignInstHoldProp | 外资机构持有无限售流通A股比例(%)|||
| LC_StockHoldingSt | PrivFundHoldNum | 私募基金持有无限售流通A股户数 |||
| LC_StockHoldingSt | BankHoldNum | 银行持有无限售流通A股户数 |||
| LC_StockHoldingSt | ForeignInstHoldNum| 外资持有无限售流通A股户数 |||
| LC_StockHoldingSt | PrivFundHoldingsA | 私募基金持A股数量(股) |||
| LC_StockHoldingSt | BankHoldingsA | 银行持有A股数量(股) |||
| LC_StockHoldingSt | ForeignInstHoldingsA| 外资机构持A股数量(股) |||
| LC_StockHoldingSt | PrivFundHoldPropA | 私募基金持有A股比例(%)|||
| LC_StockHoldingSt | BankHoldPropA | 银行持有A股比例(%)|||
| LC_StockHoldingSt | ForeignInstHoldPropA| 外资机构持有A股比例(%)|||
| LC_StockHoldingSt | FundsHoldingsANum | 公募基金持有流通A股户数 |||
| LC_StockHoldingSt | PrivFundHoldANum| 私募基金持有流通A股户数 |||
| LC_StockHoldingSt | BankHoldANum| 银行持有流通A股户数 |||
| LC_StockHoldingSt | ForeignInstHoldANum | 外资持有流通A股户数 |||
| LC_StockHoldingSt | PrivFundHoldingsT | 私募基金持股数量(股)|||
| LC_StockHoldingSt | BankHoldingsT | 银行持股数量(股)|||
| LC_StockHoldingSt | ForeignInstHoldingsT| 外资机构持股数量(股)|||
| LC_StockHoldingSt | PrivFundHoldPropT | 私募基金持股比例(%) |||
| LC_StockHoldingSt | BankHoldPropT | 银行持股比例(%) |||
| LC_StockHoldingSt | ForeignInstHoldPropT| 外资机构持股比例(%) |||
| LC_StockHoldingSt | PrivFundHoldTNum| 私募基金持股户数|||
| LC_StockHoldingSt | BankHoldTNum| 银行持股户数|||
| LC_StockHoldingSt | ForeignInstHoldTNum | 外资持股户数|||
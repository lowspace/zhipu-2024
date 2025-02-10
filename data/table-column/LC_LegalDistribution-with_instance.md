| table_name | column_name | column_description | 注释| Annotation| 数据示例 |
|---|---|---|---|---|---|
| LC_LegalDistribution | ID| ID | | | 599707110459 |
| LC_LegalDistribution | InnerCode | 证券内部编码 | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。| Security Internal Code (InnerCode): Associated with the "Security Main Table (SecuMain)" "Security Internal Code (InnerCode)", to obtain the security's trading code, abbreviation, etc.| 587|
| LC_LegalDistribution | InfoPublDate| 信息发布日期 | | | 2019-01-02 12:00:00.000|
| LC_LegalDistribution | InfoSource| 信息来源 | | | 新增股份上市公告书 |
| LC_LegalDistribution | DistributionSum | 配售总股数(股/份/张) | | | 1996073294.0 |
| LC_LegalDistribution | DistributionReason| 配售原因 | 数值型常量。配售原因(DistributionReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1016，得到配售原因的具体描述：1-配股，2-发行新股，3-增发新股，4-可转换债券，5-吸收合并，6-基金发行，7-基金扩募，8-企业债券，9-基金营销，10-金融债券，11-股权分置，12-资产支持证券，13-权证发行，14-信用风险，15-港交所基金发行，16-可交换公司债券，17-优先股发行，18-CDR首发，19-CDR增发，20-CDR配股，21-非公开增发，22-公开增发，23-非公开增发配套融资，99-其他证券发行。 | Numeric constant. The distribution reason (DistributionReason) is associated with the DM field in the (CT_SystemConst) table. Setting LB to 1016, the specific description of the distribution reason is obtained: 1 - Rights issue, 2 - New share issue, 3 - Additional share issue, 4 - Convertible bonds, 5 - Absorption merger, 6 - Fund issue, 7 - Fund expansion, 8 - Corporate bonds, 9 - Fund marketing, 10 - Financial bonds, 11 - Share reform, 12 - Asset-backed securities, 13 - Warrant issue, 14 - Credit risk, 15 - HKEX fund issue, 16 - Exchangeable corporate bonds, 17 - Preferred shares issue, 18 - CDR initial public offering, 19 - CDR additional issue, 20 - CDR rights issue, 21 - Private additional issue, 22 - Public additional issue, 23 - Private additional issue supporting financing, 99 - Other securities issue. | 21 |
| LC_LegalDistribution | SerialNum | 序号 | | | 1|
| LC_LegalDistribution | AquirerName | 获配企业名称 | | | 宁波盈峰资产管理有限公司 |
| LC_LegalDistribution | AquirerCharacter| 获配企业性质 | | | null |
| LC_LegalDistribution | SecuCoBelongedCode| 所属券商编号 | 数值型常量。当获配对象类型(AquirerType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当获配对象类型(AquirerType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。| Numeric constant. When the AquirerType is 2, it is associated with the "CompanyCode" in the "EP_CompanyMain" table to obtain the basic information of the event subject company; when the AquirerType is 3, it is associated with the "InnerCode" in the "SecuMainAll" table to obtain the basic information of the event subject security variety. | 537405 |
| LC_LegalDistribution | SecuCoBelonged| 所属券商名称 | 所属券商名称(SecuCoBelonged)：历史字段，日增数据参考本表“InvestorName[投资者名称(披露)]”| Securities firm name (SecuCoBelonged): Historical field, daily incremental data refers to "InvestorName [Investor Name (disclosed)]" in this table. | 宁波盈峰资产管理 |
| LC_LegalDistribution | SecuCode| 证券代码 | 获配企业证券代码(SecuCode)和证券主表(SecuMain)中的InnerCode关联 | The allocated company's security code (SecuCode) is associated with the InnerCode in the security main table (SecuMain).| null |
| LC_LegalDistribution | AquiredSum| 配售股数(股/份/张) | | | 1017997382.0 |
| LC_LegalDistribution | OwnedPeriod | 持股时间(月) | | | 36 |
| LC_LegalDistribution | DistributeNature| 配售性质 | 数值型常量。配售性质(DistributeNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1220 AND DM IN (1,2,3,4,5,6)，得到配售性质的具体描述：1-一般法人，2-战略投资者，3-基金配售，4-原股东优先配售，5-高管及员工战略配售，6-保荐机构及相关子公司战略配售。 | Numeric constant. The "DistributeNature" is associated with the "DM" field in the "CT_SystemConst" table, where LB = 1220 AND DM IN (1,2,3,4,5,6), resulting in the specific description of the distribution nature: 1-General Corporation, 2-Strategic Investor, 3-Fund Allocation, 4-Original Shareholder Priority Allocation, 5-Executive and Employee Strategic Allocation, 6-Underwriting Institution and Related Subsidiary Strategic Allocation. | 1|
| LC_LegalDistribution | FloatDate | 流通日期 | | | 2022-01-04 12:00:00.000|
| LC_LegalDistribution | Notes | 备注说明 | | | null |
| LC_LegalDistribution | XGRQ| 修改日期 | | | 2021-06-20 03:18:48.280|
| LC_LegalDistribution | JSID| JSID | | | 677517550026 |
| LC_LegalDistribution | IssuePrice| 实际发行价(元) | | | 7.64 |
| LC_LegalDistribution | ValidApplyVol | 有效申购股数(股) | | | null |
| LC_LegalDistribution | RefundAmount| 退款金额(元) | | | null |
| LC_LegalDistribution | InitialInfoPublDate | 首次信息发布日期 | | | 2018-07-18 12:00:00.000|
| LC_LegalDistribution | SecuAccountNumber | 证券账户号码 | | | null |
| LC_LegalDistribution | SupplementAmount| 补款金额 | | | null |
| LC_LegalDistribution | RestrictedSum | 有锁定期配售股数(股) | | | 1017997382.0 |
| LC_LegalDistribution | NonRestrictedSum| 无锁定期配售股数(股) | | | null |
| LC_LegalDistribution | InvestorName| 投资者名称 | | | null |
| LC_LegalDistribution | InvestorType| 投资者类型 | 数值型常量。投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3)，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种。 | Numeric constant. The investor type (InvestorType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1783 and DM in (1,2,3), yielding the specific description of the investor type: 1 - Natural person, 2 - Enterprise, 3 - Securities variety. | null |
| LC_LegalDistribution | InvestorCode| 投资者编号 | 当投资者类型(InvestorType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当投资者类型(InvestorType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。| When InvestorType equals 2, it is associated with the "CompanyCode" in the "EP_CompanyMain" table to obtain the basic information of the event subject company; when InvestorType equals 3, it is associated with the "InnerCode" in the "SecuMainAll" table to obtain the basic information of the event subject security variety. | null |
| LC_LegalDistribution | InsertTime| 发布时间 | | | 2020-12-25 09:03:55.543|
| LC_LegalDistribution | CoreStaffsStraSHVal | 高管、员工参与战略配售股份金额(万元) | | | null |
| LC_LegalDistribution | SponsorStraSharesHVal | 保荐机构及相关子公司参与战略配售股份金额(万元) | | | null |
| LC_LegalDistribution | OtherStraSHVol| 其他参与战略配售计划数量(万股) | | | null |
| LC_LegalDistribution | OtherStraSHVal| 其他参与战略配售计划金额(万元) | | | null |
| LC_LegalDistribution | OtherStraSHRat| 其他计划参与战略配售占比(%)| | | null |
| LC_LegalDistribution | BidderCode| 配售对象代码 | | | null |
| LC_LegalDistribution | AquirerAmount | 获配金额(元) | | | 7777499998.48|
| LC_LegalDistribution | StandardInvestorName| 投资者名称(标准) | | | null |
| LC_LegalDistribution | StandardAquirerName | 获配对象名称(标准) | | | 宁波盈峰资产管理有限公司 |
| LC_LegalDistribution | AquirerType | 获配对象类型 | 数值型常量。获配对象类型(AquirerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到获配对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | Numeric constant. The AquirerType is associated with the DM field in the CT_SystemConst table, setting LB = 1783, the specific description of the AquirerType is obtained: 1 - Natural Person, 2 - Enterprise, 3 - Securities Variety, 99 - Other.| null |
| LC_LegalDistribution | ClassofInvestor | 投资者分类 | 数值型常量。投资者分类(ClassofInvestor)与(CT_SystemConst)表中的DM字段关联，令LB=2465，得到投资者分类的具体描述：1-A类，2-B类，3-C类。 | Numeric constant. The classification of investors (Class of Investor) is associated with the DM field in the (CT_SystemConst) table, setting LB=2465, the specific description of the classification of investors is obtained: 1-Class A, 2-Class B, 3-Class C. | null |
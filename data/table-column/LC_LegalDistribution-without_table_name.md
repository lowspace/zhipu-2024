| column_name | column_description| 注释| Annotation|
|---|---|---|---|---|
| ID| ID| | |
| InnerCode | 证券内部编码| 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。| Security Internal Code (InnerCode): Associated with the "Security Main Table (SecuMain)" "Security Internal Code (InnerCode)", to obtain the security's trading code, abbreviation, etc.|
| InfoPublDate| 信息发布日期| | |
| InfoSource| 信息来源| | |
| DistributionSum | 配售总股数(股/份/张)| | |
| DistributionReason| 配售原因| 配售原因(DistributionReason)与(CT_SystemConst)表中的DM字段关联，令LB = 1016，得到配售原因的具体描述：1-配股，2-发行新股，3-增发新股，4-可转换债券，5-吸收合并，6-基金发行，7-基金扩募，8-企业债券，9-基金营销，10-金融债券，11-股权分置，12-资产支持证券，13-权证发行，14-信用风险，15-港交所基金发行，16-可交换公司债券，17-优先股发行，18-CDR首发，19-CDR增发，20-CDR配股，21-非公开增发，22-公开增发，23-非公开增发配套融资，99-其他证券发行。 | The distribution reason (DistributionReason) is associated with the DM field in the (CT_SystemConst) table. Setting LB to 1016, the specific description of the distribution reason is obtained: 1 - Rights issue, 2 - New share issue, 3 - Additional share issue, 4 - Convertible bonds, 5 - Absorption merger, 6 - Fund issue, 7 - Fund expansion, 8 - Corporate bonds, 9 - Fund marketing, 10 - Financial bonds, 11 - Share reform, 12 - Asset-backed securities, 13 - Warrant issue, 14 - Credit risk, 15 - HKEX fund issue, 16 - Exchangeable corporate bonds, 17 - Preferred shares issue, 18 - CDR initial public offering, 19 - CDR additional issue, 20 - CDR rights issue, 21 - Private additional issue, 22 - Public additional issue, 23 - Private additional issue supporting financing, 99 - Other securities issue. |
| SerialNum | 序号| | |
| AquirerName | 获配企业名称| | |
| AquirerCharacter| 获配企业性质| | |
| SecuCoBelongedCode| 所属券商编号| 当获配对象类型(AquirerType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当获配对象类型(AquirerType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。| When the AquirerType is 2, it is associated with the "CompanyCode" in the "EP_CompanyMain" table to obtain the basic information of the event subject company; when the AquirerType is 3, it is associated with the "InnerCode" in the "SecuMainAll" table to obtain the basic information of the event subject security variety. |
| SecuCoBelonged| 所属券商名称| 所属券商名称(SecuCoBelonged)：历史字段，日增数据参考本表“InvestorName[投资者名称(披露)]”| Securities firm name (SecuCoBelonged): Historical field, daily incremental data refers to "InvestorName [Investor Name (disclosed)]" in this table. |
| SecuCode| 证券代码| 获配企业证券代码(SecuCode)和证券主表(SecuMain)中的InnerCode关联 | The allocated company's security code (SecuCode) is associated with the InnerCode in the security main table (SecuMain).|
| AquiredSum| 配售股数(股/份/张)| | |
| OwnedPeriod | 持股时间(月)| | |
| DistributeNature| 配售性质| 配售性质(DistributeNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1220 AND DM IN (1,2,3,4,5,6)，得到配售性质的具体描述：1-一般法人，2-战略投资者，3-基金配售，4-原股东优先配售，5-高管及员工战略配售，6-保荐机构及相关子公司战略配售。 | The "DistributeNature" is associated with the "DM" field in the "CT_SystemConst" table, where LB = 1220 AND DM IN (1,2,3,4,5,6), resulting in the specific description of the distribution nature: 1-General Corporation, 2-Strategic Investor, 3-Fund Allocation, 4-Original Shareholder Priority Allocation, 5-Executive and Employee Strategic Allocation, 6-Underwriting Institution and Related Subsidiary Strategic Allocation. |
| FloatDate | 流通日期| | |
| Notes | 备注说明| | |
| XGRQ| 修改日期| | |
| JSID| JSID| | |
| IssuePrice| 实际发行价(元)| | |
| ValidApplyVol | 有效申购股数(股)| | |
| RefundAmount| 退款金额(元)| | |
| InitialInfoPublDate | 首次信息发布日期| | |
| SecuAccountNumber | 证券账户号码| | |
| SupplementAmount| 补款金额| | |
| RestrictedSum | 有锁定期配售股数(股)| | |
| NonRestrictedSum| 无锁定期配售股数(股)| | |
| InvestorName| 投资者名称| | |
| InvestorType| 投资者类型| 投资者类型(InvestorType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3)，得到投资者类型的具体描述：1-自然人，2-企业，3-证券品种。 | The investor type (InvestorType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1783 and DM in (1,2,3), yielding the specific description of the investor type: 1 - Natural person, 2 - Enterprise, 3 - Securities variety. |
| InvestorCode| 投资者编号| 当投资者类型(InvestorType)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当投资者类型(InvestorType)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。| When InvestorType equals 2, it is associated with the "CompanyCode" in the "EP_CompanyMain" table to obtain the basic information of the event subject company; when InvestorType equals 3, it is associated with the "InnerCode" in the "SecuMainAll" table to obtain the basic information of the event subject security variety. |
| InsertTime| 发布时间| | |
| CoreStaffsStraSHVal | 其中:高管、员工参与战略配售股份金额(万元) | | |
| SponsorStraSharesHVal | 其中:保荐机构及相关子公司参与战略配售股份金额(万元) | | |
| OtherStraSHVol| 其中:其他参与战略配售计划数量(万股) | | |
| OtherStraSHVal| 其中:其他参与战略配售计划金额(万元) | | |
| OtherStraSHRat| 其中:其他计划参与战略配售占比(%)| | |
| BidderCode| 配售对象代码| | |
| AquirerAmount | 获配金额(元)| | |
| StandardInvestorName| 投资者名称(标准)| | |
| StandardAquirerName | 获配对象名称(标准)| | |
| AquirerType | 获配对象类型| 获配对象类型(AquirerType)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到获配对象类型的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | The AquirerType is associated with the DM field in the CT_SystemConst table, setting LB = 1783, the specific description of the AquirerType is obtained: 1 - Natural Person, 2 - Enterprise, 3 - Securities Variety, 99 - Other.|
| ClassofInvestor | 投资者分类| 投资者分类(ClassofInvestor)与(CT_SystemConst)表中的DM字段关联，令LB=2465，得到投资者分类的具体描述：1-A类，2-B类，3-C类。 | The classification of investors (Class of Investor) is associated with the DM field in the (CT_SystemConst) table, setting LB=2465, the specific description of the classification of investors is obtained: 1-Class A, 2-Class B, 3-Class C. |
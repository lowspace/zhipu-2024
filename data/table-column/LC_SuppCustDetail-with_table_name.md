| table_name| column_name | column_description | 注释| Annotation|
|---|---|---|---|---|
| LC_SuppCustDetail | ID| ID | | |
| LC_SuppCustDetail | InfoPublDate| 信息发布日期 | | |
| LC_SuppCustDetail | CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到A股上市公司的交易代码、简称等。 | Company Code: Associated with the "Company Code" in "SecuMain", obtaining the trading code and abbreviation of A-share listed companies.|
| LC_SuppCustDetail | InfoSource| 信息来源 | | |
| LC_SuppCustDetail | InfoSourceCode| 信息来源编码 | 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM IN (110101,110102,120102,120103,120106,120205,130102,130103,130104,130106,130107,130111)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120106-临时公告:公开转让说明书(更正后)，120205-临时公告:其他，130102-发行上市书:招股说明书(申报稿)，130103-发行上市书:招股意向书，130104-发行上市书:上市公告书，130106-发行上市书:招股说明书，130107-发行上市书:公开转让说明书，130111-发行上市书:其他。 | The InfoSourceCode is associated with the DM field in the CT_SystemConst table, where LB = 2181 AND DM IN (110101,110102,120102,120103,120106,120205,130102,130103,130104,130106,130107,130111), resulting in the specific description of the InfoSourceCode: 110101-Periodic Report: Annual Report, 110102-Periodic Report: Semi-annual Report, 120102-Interim Announcement: Annual Report (Corrected), 120103-Interim Announcement: Semi-annual Report (Corrected), 120106-Interim Announcement: Prospectus for Public Transfer (Corrected), 120205-Interim Announcement: Other, 130102-Issue Prospectus: Prospectus (Application Draft), 130103-Issue Prospectus: Preliminary Prospectus, 130104-Issue Prospectus: Listing Notice, 130106-Issue Prospectus: Prospectus, 130107-Issue Prospectus: Prospectus for Public Transfer, 130111-Issue Prospectus: Other. |
| LC_SuppCustDetail | EndDate | 截止日期 | | |
| LC_SuppCustDetail | RelationType| 关系所属类型 | 关系类型(RelationType)与(CT_SystemConst)表中的DM字段关联，令LB = 1590 AND DM IN (4,6)，得到关系类型的具体描述：4-客户，6-供应商。 | The relation type (RelationType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1590 AND DM IN (4,6), resulting in the specific description of the relation type: 4-Customer, 6-Supplier. |
| LC_SuppCustDetail | SerialNumber| 序号 | 序号(SerialNumber)：999表示前5大客户、前5大供应商的合计值；990表示前5大客户、前5大供应商关联方合计值| Serial Number: 999 indicates the total value of the top 5 customers and the top 5 suppliers; 990 indicates the total value of the related parties of the top 5 customers and the top 5 suppliers. |
| LC_SuppCustDetail | RelatedPartyName| 关联企业名称 | | |
| LC_SuppCustDetail | RelatedPartyCode| 供应商/客户代码| 供应商/客户代码(RelatedPartyCode)：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到所属公司的基础信息。 | Supplier/Customer Code (RelatedPartyCode): Associated with the "Company Code (CompanyCode)" in "Institution Basic Information (LC_InstiArchive)", to obtain the basic information of the affiliated company.|
| LC_SuppCustDetail | RelatedPartyAttribute | 供应商/客户属性| 供应商/客户属性(RelatedPartyAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到供应商/客户属性的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | The supplier/customer attribute (RelatedPartyAttribute) is associated with the DM field in the (CT_SystemConst) table, setting LB to 1783 yields the specific description of the supplier/customer attribute: 1 - Natural person, 2 - Enterprise, 3 - Securities type, 99 - Other.|
| LC_SuppCustDetail | TargetName| 交易标的名称 | | |
| LC_SuppCustDetail | TargetCode| 交易标的代码 | | |
| LC_SuppCustDetail | TradingValue| 交易金额(元) | | |
| LC_SuppCustDetail | Ratio | 占比 | | |
| LC_SuppCustDetail | Remark| 备注 | | |
| LC_SuppCustDetail | InsertTime| 发布时间 | | |
| LC_SuppCustDetail | UpdateTime| 修改时间 | | |
| LC_SuppCustDetail | JSID| JSID | | |
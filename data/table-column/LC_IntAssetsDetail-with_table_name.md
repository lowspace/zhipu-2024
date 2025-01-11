| table_name | column_name | column_description| 注释 | Annotation |
|---|---|---|---|---|
| LC_IntAssetsDetail | ID| ID|||
| LC_IntAssetsDetail | InnerCode | 内部编码| 内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。 | Internal Code: Associated with the "InnerCode" in the "SecuMain" table, obtaining the security's trading code, abbreviation, etc.|
| LC_IntAssetsDetail | CompanyCode | 公司代码| 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.|
| LC_IntAssetsDetail | InfoPublDate| 信息发布日期|||
| LC_IntAssetsDetail | InfoSourceCode| 信息来源编码| 信息来源编码(InfoSourceCode)与(CT_SystemConst)表中的DM字段关联，令LB = 2181 AND DM IN (110101,110102,110103,110104,110105,120102,120103,120104,120105)，得到信息来源编码的具体描述：110101-定期报告:年度报告，110102-定期报告:半年度报告，110103-定期报告:第一季报，110104-定期报告:第三季报，110105-定期报告:审计报告，120102-临时公告:年度报告(更正后)，120103-临时公告:半年度报告(更正后)，120104-临时公告:第一季报(更正后)，120105-临时公告:第三季报(更正后)。 | The InfoSourceCode is associated with the DM field in the CT_SystemConst table, where LB = 2181 AND DM IN (110101,110102,110103,110104,110105,120102,120103,120104,120105), resulting in the specific description of the InfoSourceCode: 110101-Periodic Report: Annual Report, 110102-Periodic Report: Semi-annual Report, 110103-Periodic Report: First Quarter Report, 110104-Periodic Report: Third Quarter Report, 110105-Periodic Report: Audit Report, 120102-Interim Announcement: Annual Report (Corrected), 120103-Interim Announcement: Semi-annual Report (Corrected), 120104-Interim Announcement: First Quarter Report (Corrected), 120105-Interim Announcement: Third Quarter Report (Corrected). |
| LC_IntAssetsDetail | EndDate | 截止日期|||
| LC_IntAssetsDetail | IfMerged| 是否合并| 是否合并（IfMerged）固定常量：1-合并，2-母公司 | Whether to merge (IfMerged) constant: 1-merge, 2-parent company|
| LC_IntAssetsDetail | IfAdjusted| 是否调整| 是否调整(IfAdjusted)固定常量：2-否，1-是 | Whether to adjust (IfAdjusted) constant: 2 - No, 1 - Yes |
| LC_IntAssetsDetail | ExpensedRDInput | 费用化研发投入(元)|||
| LC_IntAssetsDetail | CapitalizedRDInput| 资本化研发投入(元)|||
| LC_IntAssetsDetail | TotalRDInput| 研发投入合计(元)|||
| LC_IntAssetsDetail | RDInputRatio| 研发投入占营业收入比例(%) |||
| LC_IntAssetsDetail | CapitalizedRDInputR | 资本化研发投入占比(%) |||
| LC_IntAssetsDetail | RDStaffNum| 研发人员数量|||
| LC_IntAssetsDetail | RDStaffNumRatio | 研发人员数量占比(%) |||
| LC_IntAssetsDetail | InsertTime| 发布时间|||
| LC_IntAssetsDetail | UpdateTime| 修改时间|||
| LC_IntAssetsDetail | JSID| JSID|||
| LC_IntAssetsDetail | CoreTechnicalStaffNum | 核心技术人员数量|||
| LC_IntAssetsDetail | CoreTechnicalStaffR | 核心技术人员数量占比(%) |||
| LC_IntAssetsDetail | CoreTechnologyOutput| 核心技术营业收入(元)|||
| LC_IntAssetsDetail | CoreTechnologyOutputR | 核心技术营业收入占比(%) |||
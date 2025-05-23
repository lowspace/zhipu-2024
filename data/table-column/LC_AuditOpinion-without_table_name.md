| column_name | column_description | 注释| Annotation|
|---|---|---|---|---|
| ID| ID | | |
| CompanyCode | 公司代码 | | |
| EndDate | 日期 | | |
| InfoSource| 信息来源 | | |
| AccountingFirms | 会计师事务所 | | |
| InstiBelongedCode | 所属机构 | 所属机构（InstiBelongedCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到所属机构的基本信息、联系方式等。 | Affiliation (InstiBelongedCode): Associated with the "Institution Basic Information (LC_InstiArchive)" under the "Company Code (CompanyCode)", to obtain the basic information and contact details of the affiliated institution. |
| CPA | 注册会计师 | | |
| OpinionType | 审计意见类型 | 审计意见类型(OpinionType)与(CT_SystemConst)表中的DM字段关联，令LB = 1051 AND DM IN(1,2,3,,4,5,6,7,10,11)，得到审计意见类型的具体描述：| The audit opinion type (OpinionType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1051 AND DM IN (1,2,3,4,5,6,7,10,11), yielding the specific description of the audit opinion type:|
| OpinionFullText | 审计意见全文 | | |
| XGRQ| 修改日期 | | |
| JSID| JSID | | |
| InfoPublDate| 信息发布日期 | | |
| AuditReportsType| 审计报告类型 | 审计报告类型(AuditReportsType)与(CT_SystemConst)表中的DM字段关联，令LB = 2244 AND DM IN (1,2)，得到审计报告类型的具体描述：1-财务报表审计报告，2-内部控制审计报告。 | The type of audit report (AuditReportsType) is associated with the DM field in the (CT_SystemConst) table, with LB = 2244 AND DM IN (1,2), yielding the specific description of the audit report type: 1-Financial Statement Audit Report, 2-Internal Control Audit Report. |
| InsertTime| 发布时间 | | |
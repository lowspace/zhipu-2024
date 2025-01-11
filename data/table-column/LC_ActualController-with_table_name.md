| table_name| column_name| column_description | 注释 | Annotation |
|---|---|---|---|---|
| LC_ActualController | ID | ID |||
| LC_ActualController | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | 代码（CompanyCode）is associated with the "CompanyCode" in "SecuMain", obtaining the trading code, abbreviation, etc. of the listed company. |
| LC_ActualController | InfoPublDate | 信息发布日期 |||
| LC_ActualController | EndDate| 日期 |||
| LC_ActualController | ControllerCode | 实际控制人代码 | 实际控制人代码（ControllerCode）：与“机构基本资料（LC_InstiArchive）”中的“企业编号（CompanyCode）”关联，得到实际控制人的名称，企业性质等信息。 | Controller Code: Associated with the "Company Code" in "LC_InstiArchive" to obtain information such as the name of the actual controller and the nature of the enterprise. |
| LC_ActualController | ControllerName | 实际控制人 |||
| LC_ActualController | EconomicNature | 经济性质 | 实际控制人经济性质(EconomicNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1581，得到实际控制人经济性质的具体描述：1-中央企业，2-地方国有企业，3-民营企业，4-集体企业，5-大学，6-外资，7-工会，99-其它。 | The economic nature of the actual controller (EconomicNature) is associated with the DM field in the (CT_SystemConst) table, setting LB = 1581, to obtain the specific description of the economic nature of the actual controller: 1-Central Enterprise, 2-Local State-owned Enterprise, 3-Private Enterprise, 4-Collective Enterprise, 5-University, 6-Foreign Capital, 7-Trade Union, 99-Other. |
| LC_ActualController | NationalityCode| 国籍代码 | 国籍代码（NationalityCode）：与“系统常量表”中的“代码（DM）”关联，令“LB=1023”，得到实际控制人的国籍编码。 | Nationality Code: Associated with the "Code (DM)" in the "System Constants Table", setting "LB=1023" yields the actual controller's nationality code.|
| LC_ActualController | NationalityDesc| 国籍描述 |||
| LC_ActualController | PermanentResidency | 永久境外居留权 |||
| LC_ActualController | UpdateTime | 更新时间 |||
| LC_ActualController | JSID | JSID |||
| LC_ActualController | ControllerNature | 实际控制人所属性质 | 实际控制人所属性质(ControllerNature)与(CT_SystemConst)表中的DM字段关联，令LB = 1783，得到实际控制人所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | The nature of the actual controller (ControllerNature) is associated with the DM field in the (CT_SystemConst) table, setting LB = 1783, to obtain the specific description of the nature of the actual controller: 1-natural person, 2-enterprise, 3-security type, 99-others.|
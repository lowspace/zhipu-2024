| table_name | column_name| column_description | 注释 | Annotation|
|---|---|---|---|---|
| US_CompanyInfo | ID | ID || |
| US_CompanyInfo | CompanyCode| 公司代码 || |
| US_CompanyInfo | EngName| 英文名称 || |
| US_CompanyInfo | EngNameAbbr| 英文名称缩写 || |
| US_CompanyInfo | ChiName| 中文名称 || |
| US_CompanyInfo | PEOAddress | 公司地址 || |
| US_CompanyInfo | PEOCity| 城市 || |
| US_CompanyInfo | PEOState | 省份 || |
| US_CompanyInfo | PEOZip | 邮编 || |
| US_CompanyInfo | PEOStatus| 国家 || |
| US_CompanyInfo | PEOTel | 电话 || |
| US_CompanyInfo | BusinessDcrp | 公司简介 || |
| US_CompanyInfo | UpdateTime | 更新时间 || |
| US_CompanyInfo | JSID | JSID || |
| US_CompanyInfo | BriefIntroText | 公司简介 || |
| US_CompanyInfo | EstablishmentDate| 成立日期 || |
| US_CompanyInfo | CompanyType| 公司类型 | 公司类型(CompanyType)与(CT_SystemConst)表中的DM字段关联，令LB = 2261，得到公司类型的具体描述：1-美国联邦存款保险公司(FDIC)的银行分支，2-高等院校，3-融资子公司，4-政府，5-控股公司，6-合营企业，7-非盈利性组织，8-上市公司，9-非上市公司，10-子公司，11-已停止经营解散的实体。 | The company type (CompanyType) is associated with the DM field in the (CT_SystemConst) table, with LB set to 2261, the specific description of the company type is as follows: 1 - Branch of the Federal Deposit Insurance Corporation (FDIC) in the United States, 2 - Higher education institution, 3 - Financing subsidiary, 4 - Government, 5 - Holding company, 6 - Joint venture, 7 - Non-profit organization, 8 - Publicly listed company, 9 - Privately held company, 10 - Subsidiary, 11 - Entity that has ceased operations and been dissolved. |
| US_CompanyInfo | BriefIntroTextEng| 英文公司简介 || |
| US_CompanyInfo | Fax| 传真 || |
| US_CompanyInfo | RegCountry | 注册地国家 | 注册地国家（RegCountry）：与“国家城市代码表(LC_AreaCode)”中的“地区内部编码(AreaInnerCode)”关联，得到注册地国家的相关信息。 | The registered country (RegCountry) is associated with the "AreaInnerCode" in the "LC_AreaCode" table to obtain the relevant information of the registered country. |
| US_CompanyInfo | RegState | 注册地省份/州|| |
| US_CompanyInfo | BusinessDcrpEng| 英文业务简介 || |
| US_CompanyInfo | IfHeadOffice | 是否公司总部 | 是否公司总部(IfHeadOffice)与(CT_SystemConst)表中的DM字段关联，令LB=999 AND DM IN (1,2)，得到是否公司总部的具体描述：1-是，2-否。 | Whether the "IfHeadOffice" field is associated with the "DM" field in the "CT_SystemConst" table, with LB=999 AND DM IN (1,2), to obtain the specific description of whether it is the company headquarters: 1-yes, 2-no. |
| US_CompanyInfo | LinkAddress| 链接地址 || |
| US_CompanyInfo | CountryCode| 国家代码 | 与“国家城市代码表(LC_AreaCode)”中的“地区内部编码(AreaInnerCode)”关联，得到国家的相关信息。 | Associated with the "AreaInnerCode" in the "LC_AreaCode" table to obtain the relevant information of the country. |
| US_CompanyInfo | EstablishmentDatePreci | 成立日期精度 | 成立日期精度(EstablishmentDatePreci)与(CT_SystemConst)表中的DM字段关联，令LB=102 AND DM in (27,28,29)，得到成立日期精度的具体描述：27-年，28-月，29-日。 | The precision of the establishment date (EstablishmentDatePreci) is associated with the DM field in the CT_SystemConst table. When LB=102 and DM is in (27,28,29), the specific description of the precision of the establishment date is obtained: 27 - year, 28 - month, 29 - day.|
| US_CompanyInfo | InsertTime | 发布时间 || |
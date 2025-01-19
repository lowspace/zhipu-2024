| table_name | column_name| column_description | 注释 | Annotation |
|---|---|---|---|---|
| LC_StockArchives | ID | ID |||
| LC_StockArchives | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.|
| LC_StockArchives | State| 省份 | 省份（State）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到省份具体信息。| Province (State): Associated with the "AreaInnerCode" in the "LC_AreaCode" table, to obtain specific information about the province. |
| LC_StockArchives | SecretaryBD| 董事会秘书 |||
| LC_StockArchives | SecuAffairsRepr| 证券/股证事务代表|||
| LC_StockArchives | AuthReprSBD| 董秘授权代表 |||
| LC_StockArchives | ContactTel | 联系人电话 |||
| LC_StockArchives | ContactFax | 联系人传真 |||
| LC_StockArchives | ContactEmail | 联系人电子邮箱 |||
| LC_StockArchives | RegAddr| 公司注册地址 |||
| LC_StockArchives | RegZipCode | 公司注册地址邮编 |||
| LC_StockArchives | OfficeAddr | 公司办公地址 |||
| LC_StockArchives | OfficeZipCode| 公司办公地址邮编 |||
| LC_StockArchives | ContactAddr| 公司联系地址 |||
| LC_StockArchives | ConatactZipCode| 公司联系地址邮编 |||
| LC_StockArchives | Email| 邮箱 |||
| LC_StockArchives | Website| 公司网址 |||
| LC_StockArchives | DisclosureWebsites | 信息披露网址 |||
| LC_StockArchives | DisclosurePapers | 信息披露报纸 |||
| LC_StockArchives | EstablishmentDate| 公司成立日期 |||
| LC_StockArchives | IRegPlace| 首次注册登记地点 |||
| LC_StockArchives | LegalRepr| 法人代表 |||
| LC_StockArchives | GeneralManager | 总经理 |||
| LC_StockArchives | LegalConsultant| 法律顾问 |||
| LC_StockArchives | AccountingFirm | 会计师事务所 |||
| LC_StockArchives | InduCSRC | 公司所属证监会行业(聚源) | 与(CT_IndustryType)表中的"行业内部编码(IndustryNum)"字段关联,当Standard=1时,LB=1；当Standard=22时,LB=22；当Standard=25时,LB=25；当Standard=26时,LB=26。| Associated with the "IndustryNum" field in the (CT_IndustryType) table, when Standard=1, LB=1; when Standard=22, LB=22; when Standard=25, LB=25; when Standard=26, LB=26.|
| LC_StockArchives | BusinessMajor| 经营范围-主营|||
| LC_StockArchives | BusinessMinor| 经营范围-兼营|||
| LC_StockArchives | AShareAbbr | A股证券简称|||
| LC_StockArchives | AStockCode | A股证券代码|||
| LC_StockArchives | BShareAbbr | B股证券简称|||
| LC_StockArchives | BStockCode | B股证券代码|||
| LC_StockArchives | HShareAbbr | H股证券简称|||
| LC_StockArchives | HStockCode | H股证券代码|||
| LC_StockArchives | BriefIntroText | 公司简介 |||
| LC_StockArchives | XGRQ | 修改日期 |||
| LC_StockArchives | JSID | JSID |||
| LC_StockArchives | ChiName| 中文名称 |||
| LC_StockArchives | BusinessRegNumber| 企业法人营业执照注册号 |||
| LC_StockArchives | SecretaryBDTel | 董秘电话 |||
| LC_StockArchives | SecretaryBDFax | 董秘传真 |||
| LC_StockArchives | SecretaryBDEmail | 董秘电子邮件 |||
| LC_StockArchives | SecuAffairsReprTel | 证券事务代表电话 |||
| LC_StockArchives | SecuAffairsReprFax | 证券事务代表传真 |||
| LC_StockArchives | SecuAffairsReprEmail | 证券事务代表电子邮件 |||
| LC_StockArchives | CityCode | 地区代码 | 地区代码(CityCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到城市具体信息。 | Area code (CityCode): associated with the "AreaInnerCode" in the "National City Code List (LC_AreaCode)" to obtain specific city information.|
| LC_StockArchives | CDRShareAbbr | CDR证券简称|||
| LC_StockArchives | CDRStockCode | CDR证券代码|||
| LC_StockArchives | ExtendedAbbr | 扩位简称 |||
| LC_StockArchives | UnprofitableMark | 尚未盈利标识 | 尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首次实现盈利的，该特别标识取消，数据值为空。| Unprofitable Mark: If an issuer has not yet profited at the time of listing, a special mark "U" will be assigned to its stocks or depositary receipts; when the issuer achieves profit for the first time, this special mark will be removed and the data value will be empty. |
| LC_StockArchives | SpecialVoteMark| 特殊表决权标识 | 特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”；上市后不再具有表决权差异安排的，该特别标识取消，数据值为空。 | Special Vote Mark: For issuers with voting rights difference arrangements at the time of listing, the special mark for their shares or depositary receipts is "W"; after listing, if the voting rights difference arrangement no longer exists, the special mark is removed and the data value is empty. |
| LC_StockArchives | VIEMark| 协议控制架构标识 | 协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”；上市后不再具有相关安排的，该特别标识取消，数据值为空。 | Agreement Control Structure Identifier (VIEMark): If an issuer has an agreement control structure or similar special arrangement at the time of listing, the special identifier for its shares or depositary receipts is "V"; if such arrangement no longer exists after listing, the special identifier is removed and the data value is empty. |
| LC_StockArchives | RedChipMark| 红筹企业标识 | 红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。 | Red Chip Mark: If the issuer belongs to a red chip company, the data value is "yes"; a null value indicates the absence of such a mark.|
| LC_StockArchives | RegArea| 所属区县 | 所属区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到所属区县具体信息。| The affiliated county (RegArea): associated with the "AreaInnerCode" in the "LC_AreaCode" table, to obtain the specific information of the affiliated county.|
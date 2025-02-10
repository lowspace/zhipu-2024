| table_name | column_name| column_description | 注释 | Annotation | 数据示例 |
|---|---|---|---|---|---|
| LC_StockArchives | ID | ID ||| 717016908274 |
| LC_StockArchives | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.| 1428 |
| LC_StockArchives | State| 省份 | 省份（State）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到省份具体信息。| Province (State): Associated with the "AreaInnerCode" in the "LC_AreaCode" table, to obtain specific information about the province. | 144200000|
| LC_StockArchives | SecretaryBD| 董事会秘书 ||| 杨力康 |
| LC_StockArchives | SecuAffairsRepr| 证券/股证事务代表||| 凌亦奇 |
| LC_StockArchives | AuthReprSBD| 董秘授权代表 ||| null |
| LC_StockArchives | ContactTel | 联系人电话 ||| 0510-86632358|
| LC_StockArchives | ContactFax | 联系人传真 ||| 0510-86630191-481|
| LC_StockArchives | ContactEmail | 联系人电子邮箱 ||| 600481@shuangliang.com |
| LC_StockArchives | RegAddr| 公司注册地址 ||| 江苏省无锡市江阴市利港镇 |
| LC_StockArchives | RegZipCode | 公司注册地址邮编 ||| 214444 |
| LC_StockArchives | OfficeAddr | 公司办公地址 ||| 江苏省江阴市利港镇西利路88号 |
| LC_StockArchives | OfficeZipCode| 公司办公地址邮编 ||| 214444 |
| LC_StockArchives | ContactAddr| 公司联系地址 ||| 江苏省江阴市利港镇西利路88号 |
| LC_StockArchives | ConatactZipCode| 公司联系地址邮编 ||| 214444 |
| LC_StockArchives | Email| 邮箱 ||| 600481@shuangliang.com |
| LC_StockArchives | Website| 公司网址 ||| http://www.shuangliang.com |
| LC_StockArchives | DisclosureWebsites | 信息披露网址 ||| http://www.sse.com.cn|
| LC_StockArchives | DisclosurePapers | 信息披露报纸 ||| 《证券时报》《中国证券报》 |
| LC_StockArchives | EstablishmentDate| 公司成立日期 ||| 1995-10-05 12:00:00.000|
| LC_StockArchives | IRegPlace| 首次注册登记地点 ||| null |
| LC_StockArchives | LegalRepr| 法人代表 ||| 刘正宇 |
| LC_StockArchives | GeneralManager | 总经理 ||| 刘正宇 |
| LC_StockArchives | LegalConsultant| 法律顾问 ||| 上海市通力律师事务所 |
| LC_StockArchives | AccountingFirm | 会计师事务所 ||| 天衡会计师事务所（特殊普通合伙） |
| LC_StockArchives | InduCSRC | 公司所属证监会行业(聚源) | 与(CT_IndustryType)表中的"行业内部编码(IndustryNum)"字段关联,当Standard=1时,LB=1；当Standard=22时,LB=22；当Standard=25时,LB=25；当Standard=26时,LB=26。| Associated with the "IndustryNum" field in the (CT_IndustryType) table, when Standard=1, LB=1; when Standard=22, LB=22; when Standard=25, LB=25; when Standard=26, LB=26.| 13038|
| LC_StockArchives | BusinessMajor| 经营范围-主营||| 冷热水机组、热泵、空气冷却设备、海水淡化节能设备、污水处理设 |
| LC_StockArchives | BusinessMinor| 经营范围-兼营||| null |
| LC_StockArchives | AShareAbbr | A股证券简称||| 双良节能 |
| LC_StockArchives | AStockCode | A股证券代码||| 600481 |
| LC_StockArchives | BShareAbbr | B股证券简称||| null |
| LC_StockArchives | BStockCode | B股证券代码||| null |
| LC_StockArchives | HShareAbbr | H股证券简称||| null |
| LC_StockArchives | HStockCode | H股证券代码||| null |
| LC_StockArchives | BriefIntroText | 公司简介 ||| 公司以绿色环保为己任,不断开拓创新,致力于成为数字化驱动的全 |
| LC_StockArchives | XGRQ | 修改日期 ||| 2024-08-30 09:29:07.017|
| LC_StockArchives | JSID | JSID ||| 778877872162 |
| LC_StockArchives | ChiName| 中文名称 ||| 双良节能系统股份有限公司 |
| LC_StockArchives | BusinessRegNumber| 企业法人营业执照注册号 ||| 320000400001692|
| LC_StockArchives | SecretaryBDTel | 董秘电话 ||| 0510-86632358|
| LC_StockArchives | SecretaryBDFax | 董秘传真 ||| 0510-86630191-481|
| LC_StockArchives | SecretaryBDEmail | 董秘电子邮件 ||| 600481@shuangliang.com |
| LC_StockArchives | SecuAffairsReprTel | 证券事务代表电话 ||| 0510-86632358|
| LC_StockArchives | SecuAffairsReprFax | 证券事务代表传真 ||| 0510-86630191-481|
| LC_StockArchives | SecuAffairsReprEmail | 证券事务代表电子邮件 ||| lingyq@shuangliang.com |
| LC_StockArchives | CityCode | 地区代码 | 地区代码(CityCode)：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到城市具体信息。 | Area code (CityCode): associated with the "AreaInnerCode" in the "National City Code List (LC_AreaCode)" to obtain specific city information.| 144200113|
| LC_StockArchives | CDRShareAbbr | CDR证券简称||| null |
| LC_StockArchives | CDRStockCode | CDR证券代码||| null |
| LC_StockArchives | ExtendedAbbr | 扩位简称 ||| null |
| LC_StockArchives | UnprofitableMark | 尚未盈利标识 | 尚未盈利标识（UnprofitableMark）：在上市时发行人尚未盈利的，其股票或存托凭证的特别标识为“U”；发行人首次实现盈利的，该特别标识取消，数据值为空。| Unprofitable Mark: If an issuer has not yet profited at the time of listing, a special mark "U" will be assigned to its stocks or depositary receipts; when the issuer achieves profit for the first time, this special mark will be removed and the data value will be empty. | null |
| LC_StockArchives | SpecialVoteMark| 特殊表决权标识 | 特殊表决权标识（SpecialVoteMark）：在上市时发行人具有表决权差异安排的，其股票或存托凭证的特别标识为“W”；上市后不再具有表决权差异安排的，该特别标识取消，数据值为空。 | Special Vote Mark: For issuers with voting rights difference arrangements at the time of listing, the special mark for their shares or depositary receipts is "W"; after listing, if the voting rights difference arrangement no longer exists, the special mark is removed and the data value is empty. | null |
| LC_StockArchives | VIEMark| 协议控制架构标识 | 协议控制架构标识（VIEMark）：在上市时发行人具有协议控制架构或者类似特殊安排的，其股票或存托凭证的特别标识为“V”；上市后不再具有相关安排的，该特别标识取消，数据值为空。 | Agreement Control Structure Identifier (VIEMark): If an issuer has an agreement control structure or similar special arrangement at the time of listing, the special identifier for its shares or depositary receipts is "V"; if such arrangement no longer exists after listing, the special identifier is removed and the data value is empty. | null |
| LC_StockArchives | RedChipMark| 红筹企业标识 | 红筹企业标识（RedChipMark）：发行人属于红筹企业，则数据值=”是“；空值则指无此标识。 | Red Chip Mark: If the issuer belongs to a red chip company, the data value is "yes"; a null value indicates the absence of such a mark.| null |
| LC_StockArchives | RegArea| 所属区县 | 所属区县（RegArea）：与“国家城市代码表（LC_AreaCode）”中的“地区内部编码（AreaInnerCode）”关联，得到所属区县具体信息。| The affiliated county (RegArea): associated with the "AreaInnerCode" in the "LC_AreaCode" table, to obtain the specific information of the affiliated county.| 144200120|
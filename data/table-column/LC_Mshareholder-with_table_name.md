| table_name| column_name| column_description | 注释 | Annotation|
|---|---|---|---|---|
| LC_Mshareholder | ID | ID || |
| LC_Mshareholder | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| LC_Mshareholder | InfoPublDate | 信息发布日期 || |
| LC_Mshareholder | InfoSource | 信息来源 || |
| LC_Mshareholder | MSHName| 股东名称 || |
| LC_Mshareholder | MSHPercentage| 持股比例 || |
| LC_Mshareholder | MSHNumber| 股东地位 || |
| LC_Mshareholder | GetMethod| 股权获取方式 || |
| LC_Mshareholder | LegalRepr| 法人代表 || |
| LC_Mshareholder | RegCapital | 注册资本(元) || |
| LC_Mshareholder | MainBusiness | 主要业务 || |
| LC_Mshareholder | EconomicNature | 经济性质 || |
| LC_Mshareholder | BackgroundIntr | 背景介绍 || |
| LC_Mshareholder | IfExisted| 是否存在 || |
| LC_Mshareholder | XGRQ | 修改日期 || |
| LC_Mshareholder | JSID | JSID || |
| LC_Mshareholder | BulletinType | 公告类别 | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。 | The BulletinType is associated with the DM field in the CT_SystemConst table, with LB set to 1311, the specific description of the BulletinType is: 10-Issue and Listing Prospectus, 20-Regular Reports, 30-Earnings Preview, 50-Bylaws and Regulations, 60-Correction Notice, 70-Interim Notice, 90-Stock Exchange Circular, 91-Stock Exchange Temporary Suspension (Resumption) Notice, 99-Other. |
| LC_Mshareholder | NationalityDesc| 国籍描述 || |
| LC_Mshareholder | PermanentResidency | 永久境外居留权 || |
| LC_Mshareholder | StructureChart | 实际控制人结构图 || |
| LC_Mshareholder | FileType | 报告原文文件格式 || |
| LC_Mshareholder | EndDate| 日期 || |
| LC_Mshareholder | SHAttribute| 股东性质 | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。 | The BulletinType is associated with the DM field in the CT_SystemConst table, with LB set to 1311, the specific description of the BulletinType is: 10-Issue and Listing Prospectus, 20-Regular Reports, 30-Earnings Preview, 50-Bylaws and Regulations, 60-Correction Notice, 70-Interim Notice, 90-Stock Exchange Circular, 91-Stock Exchange Temporary Suspension (Resumption) Notice, 99-Other. |
| LC_Mshareholder | CurrencyUnit | 货币单位 | 货币单位（CurrencyUnit）与（CT_SystemConst）中的DM字段关联，令LB=1068，得到注册资本的货币单位具体描述： 1000-美元 1100-港元 1420-人民币元 3000-欧元| The currency unit (CurrencyUnit) is associated with the DM field in (CT_SystemConst). When LB=1068, the specific description of the registered capital's currency unit is obtained: 1000-USD, 1100-HKD, 1420-CNY, 3000-EUR. |
| LC_Mshareholder | GDID | 股东ID | 股东ID（GDID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。 | Stockholder ID (GDID): When the stockholder attribute (SHAttribute) equals 2, it is associated with the Company Code in the Institutional Basic Information (LC_InstiArchive); when the stockholder attribute (SHAttribute) equals 3, it is associated with the Inner Code in the Financial Product Main Table (SF_PlanMain) or Security Main Table (SecuMain). |
| table_name| column_name| column_description | 注释 | Annotation| 数据示例 |
|---|---|---|---|---|---|
| AStockShareholderDB.LC_Mshareholder | ID | ID || | 314803926078 |
| AStockShareholderDB.LC_Mshareholder | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. | 77931|
| AStockShareholderDB.LC_Mshareholder | InfoPublDate | 信息发布日期 || | 2019-06-06 12:00:00.000|
| AStockShareholderDB.LC_Mshareholder | InfoSource | 信息来源 || | 招股说明书(申报稿) |
| AStockShareholderDB.LC_Mshareholder | MSHName| 股东名称 || | 澳洲联邦银行 |
| AStockShareholderDB.LC_Mshareholder | MSHPercentage| 持股比例 || | 0.1543 |
| AStockShareholderDB.LC_Mshareholder | MSHNumber| 股东地位 || | 1|
| AStockShareholderDB.LC_Mshareholder | GetMethod| 股权获取方式 || | 1|
| AStockShareholderDB.LC_Mshareholder | LegalRepr| 法人代表 || | null |
| AStockShareholderDB.LC_Mshareholder | RegCapital | 注册资本(元) || | null |
| AStockShareholderDB.LC_Mshareholder | MainBusiness | 主要业务 || | 零售、公司以及机构银行业务、基金管理、退休金、寿险、投资及经 |
| AStockShareholderDB.LC_Mshareholder | EconomicNature | 经济性质 || | null |
| AStockShareholderDB.LC_Mshareholder | BackgroundIntr | 背景介绍 || | 澳洲联邦银行成立于1911年,是澳大利亚领先的综合金|
| AStockShareholderDB.LC_Mshareholder | IfExisted| 是否存在 || | 1|
| AStockShareholderDB.LC_Mshareholder | XGRQ | 修改日期 || | 2024-04-26 10:00:47.820|
| AStockShareholderDB.LC_Mshareholder | JSID | JSID || | 767575950072 |
| AStockShareholderDB.LC_Mshareholder | BulletinType | 公告类别 | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。 | The BulletinType is associated with the DM field in the CT_SystemConst table, with LB set to 1311, the specific description of the BulletinType is: 10-Issue and Listing Prospectus, 20-Regular Reports, 30-Earnings Preview, 50-Bylaws and Regulations, 60-Correction Notice, 70-Interim Notice, 90-Stock Exchange Circular, 91-Stock Exchange Temporary Suspension (Resumption) Notice, 99-Other. | 10 |
| AStockShareholderDB.LC_Mshareholder | NationalityDesc| 国籍描述 || | null |
| AStockShareholderDB.LC_Mshareholder | PermanentResidency | 永久境外居留权 || | null |
| AStockShareholderDB.LC_Mshareholder | StructureChart | 实际控制人结构图 || | null |
| AStockShareholderDB.LC_Mshareholder | FileType | 报告原文文件格式 || | null |
| AStockShareholderDB.LC_Mshareholder | EndDate| 日期 || | null |
| AStockShareholderDB.LC_Mshareholder | SHAttribute| 股东性质 | 公告类别(BulletinType)与(CT_SystemConst)表中的DM字段关联，令LB = 1311，得到公告类别的具体描述：10-发行上市书，20-定期报告，30-业绩快报，50-章程制度，60-更正公告，70-临时公告，90-交易所通报，91-交易所临时停(复)牌公告，99-其他。 | The BulletinType is associated with the DM field in the CT_SystemConst table, with LB set to 1311, the specific description of the BulletinType is: 10-Issue and Listing Prospectus, 20-Regular Reports, 30-Earnings Preview, 50-Bylaws and Regulations, 60-Correction Notice, 70-Interim Notice, 90-Stock Exchange Circular, 91-Stock Exchange Temporary Suspension (Resumption) Notice, 99-Other. | 2|
| AStockShareholderDB.LC_Mshareholder | CurrencyUnit | 货币单位 | 货币单位（CurrencyUnit）与（CT_SystemConst）中的DM字段关联，令LB=1068，得到注册资本的货币单位具体描述： 1000-美元 1100-港元 1420-人民币元 3000-欧元| The currency unit (CurrencyUnit) is associated with the DM field in (CT_SystemConst). When LB=1068, the specific description of the registered capital's currency unit is obtained: 1000-USD, 1100-HKD, 1420-CNY, 3000-EUR. | null |
| AStockShareholderDB.LC_Mshareholder | GDID | 股东ID | 股东ID（GDID）：当股东属性（SHAttribute）=2时，与机构基本资料（LC_InstiArchive）中的企业编号（CompanyCode）关联；股东属性（SHAttribute）=3时，与理财产品主表（SF_PlanMain）或证券主表（SecuMain）中的内部编码（InnerCode）关联。 | Stockholder ID (GDID): When the stockholder attribute (SHAttribute) equals 2, it is associated with the Company Code in the Institutional Basic Information (LC_InstiArchive); when the stockholder attribute (SHAttribute) equals 3, it is associated with the Inner Code in the Financial Product Main Table (SF_PlanMain) or Security Main Table (SecuMain). | 14047|
| table_name | column_name| column_description | 注释 | Annotation | 数据示例|
|---|---|---|---|---|---|
| LC_Business| ID | ID ||| 599777135022|
| LC_Business| CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company.| 224275|
| LC_Business| InfoPublDate | 信息发布日期 ||| 2019-01-03 12:00:00.000 |
| LC_Business| InfoSource | 信息来源 ||| 第二届董事会第八次会议决议公告|
| LC_Business| SMDeciPublDate | 股东大会决议公告日期 ||| 2019-01-18 12:00:00.000 |
| LC_Business| IfPassed | 是否否决 | 是否否决(IfPassed)，该字段固定为字符常量："1"-是；"0"-否 | Whether to veto (IfPassed), this field is fixed with the following string constants: "1"-yes; "0"-no.| 0 |
| LC_Business| BusinessMajor| 经营范围-主营||| 生产:半导体设备(测试机、分选机)。服务:半导体设备、光机电|
| LC_Business| BusinessMinor| 经营范围-兼营||| null|
| LC_Business| MainBusiness | 主要业务 ||| 集成电路专用设备的研发、生产和销售,主要产品包括集成电路测试 |
| LC_Business| MainName | 主要产品与业务名称 ||| 测试机和分选机等|
| LC_Business| CSRCInduCategory | 行业代码 | 行业代码（CSRCInduCategory）：当行业类别（IndustryType）=1时，与行业表（CT_Industry）中行业编码（IndustryNum）关联，得到CSRC行业分类标准下的行业名称；当行业类别（IndustryType）=22时，与系统常量表(CT_SystemConst)中的DM字段关联，令LB=1755，得到证监会行业分类2012版分类标准下的行业名称。 | Industry code (CSRCInduCategory): When the industry category (IndustryType) equals 1, it is associated with the industry code (IndustryNum) in the industry table (CT_Industry), and the industry name under the CSRC industry classification standard is obtained; when the industry category (IndustryType) equals 22, it is associated with the DM field in the system constant table (CT_SystemConst), let LB=1755, and the industry name under the CSRC industry classification 2012 version classification standard is obtained. | 13035 |
| LC_Business| InduEngaged| 涉足行业 ||| null|
| LC_Business| ChangeReason | 简称变更原因 ||| null|
| LC_Business| XGRQ | 修改日期 ||| 2024-05-17 01:43:13.797 |
| LC_Business| JSID | JSID ||| 769290274663|
| LC_Business| IndustryType | 行业类别 | 行业类别(IndustryType)与(CT_SystemConst)表中的DM字段关联，令LB = 1081 and DM in (1,22)，得到行业类别的具体描述：1-CSRC行业分类，22-证监会行业分类2012版。| The industry type (IndustryType) is associated with the DM field in the (CT_SystemConst) table, with LB = 1081 and DM in (1,22), yielding the specific description of the industry type: 1-CSRC industry classification, 22-CSRC industry classification 2012 version. | 22|
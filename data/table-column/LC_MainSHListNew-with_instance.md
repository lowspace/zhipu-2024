| table_name | column_name | column_description | 注释| Annotation| 数据示例 |
|---|---|---|---|---|---|
| LC_MainSHListNew | ID| ID | | | 599708421015 |
| LC_MainSHListNew | CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。| Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. | 523|
| LC_MainSHListNew | EndDate | 日期 | | | 2019-01-04 12:00:00.000|
| LC_MainSHListNew | InfoPublDate| 信息发布日期 | | | 2019-01-02 12:00:00.000|
| LC_MainSHListNew | InfoSource| 信息来源 | | | 新增股份上市公告书 |
| LC_MainSHListNew | InfoTypeCode| 信息类别编码 | 数值型常量。信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AND DM IN (1,2,4,5,6)，得到信息类别编码的具体描述：1-前十大股东，2-前十流通股东，4-十大有限售条件股东，5-发行前股东，6-前十大表决权数量股东。 | Numeric constant. The InfoTypeCode is associated with the DM field in the CT_SystemConst table, with LB = 1025 AND DM IN (1,2,4,5,6), the specific description of the InfoTypeCode is: 1 - Top ten shareholders, 2 - Top ten tradable shareholders, 4 - Top ten shareholders with restricted sale conditions, 5 - Shareholders before issuance, 6 - Top ten shareholders by voting rights quantity. | 1|
| LC_MainSHListNew | SHNo| 股东排名 | 股东排名（SHNo），数值型常量：当“信息类别代码（InfoTypeCode）”=1时，“股东排名（SHNo）”表示股东排名；当“信息类别代码（InfoTypeCode）”=2时，“股东排名（SHNo）”表示流通股东排名。| Shareholder Ranking (SHNo), numeric constant: When "Information Type Code (InfoTypeCode)" equals 1, "Shareholder Ranking (SHNo)" indicates the ranking of shareholders; when "Information Type Code (InfoTypeCode)" equals 2, "Shareholder Ranking (SHNo)" indicates the ranking of circulating shareholders. | 1|
| LC_MainSHListNew | SHSerial| 股东序号 | | | 1|
| LC_MainSHListNew | SHList| 股东名称 | 股东名称（SHList）：此字段为股东名称公告原始披露值；如期望获取股东标准名称，可使用股东ID与相关表单关联，具体关联方式详见注4 | Shareholder Name (SHList): This field is the original disclosure value of the shareholder name announcement; if you expect to obtain the standard shareholder name, you can use the shareholder ID to associate with the relevant forms, and the specific association method is detailed in Note 4. | 宁波盈峰资产管理有限公司 |
| LC_MainSHListNew | SHKind| 股东性质 | | | 资产管理公司 |
| LC_MainSHListNew | SHTypeCode| 股东类别编码 | | | 90 |
| LC_MainSHListNew | SHType| 股东类别 | | | 其他股东 |
| LC_MainSHListNew | SecuCoBelongedCode| 所属券商编号 | | | 537405 |
| LC_MainSHListNew | SecuCoBelongedName| 归属机构名称 | | | 宁波盈峰资产管理有限公司 |
| LC_MainSHListNew | SecuCode| 证券代码 | | | null |
| LC_MainSHListNew | SecuAbbr| 证券简称 | | | null |
| LC_MainSHListNew | HoldSum | 持股数(股) | | | 1017997382.0 |
| LC_MainSHListNew | PCTOfTotalShares| 占总股本比例 | 占总股本比例（%）（PCTOfTotalShares）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股)/总股本*100当“信息类别代码（InfoTypeCode）”=2时，无限售股数(股)/总股本*100 | Percentage of Total Shares (PCTOfTotalShares): When "Information Type Code (InfoTypeCode)" equals 1, the number of shares held / total issued shares * 100; when "Information Type Code (InfoTypeCode)" equals 2, the number of unrestricted shares / total issued shares * 100.| 32.18392 |
| LC_MainSHListNew | RestrainedTShare| 其中：有限售股数(股) | | | null |
| LC_MainSHListNew | UnstintedTShare | 其中：无限售股数(股) | | | null |
| LC_MainSHListNew | HoldSumChange | 持股数量增减(股) | | | null |
| LC_MainSHListNew | HoldSumChangeRate | 持股数量增减幅度(%)| | | null |
| LC_MainSHListNew | HoldAShareSum | 持有A股数量(股)| | | 1017997382.0 |
| LC_MainSHListNew | PCTOfFloatShares| 占流通A股比例(%) | | | null |
| LC_MainSHListNew | HoldBShareSum | 持有B股数量(股)| | | null |
| LC_MainSHListNew | HoldHShareSum | 持有H股数量(股)| | | null |
| LC_MainSHListNew | HoldOthterShareSum| 持有其他股数量(股) | | | null |
| LC_MainSHListNew | ShareCharacterStatement | 股本性质描述 | | | 流通A股|
| LC_MainSHListNew | PledgeInvolvedSum | 股权质押涉及股数(股) | | | null |
| LC_MainSHListNew | FreezeInvolvedSum | 股权冻结涉及股数(股) | | | null |
| LC_MainSHListNew | PFStatement | 股权质押冻结情况说明 | | | null |
| LC_MainSHListNew | ConnectionRelation| 股东关联关系 | | | null |
| LC_MainSHListNew | ConnectionStatement | 与其他股东关联关系说明 | | | null |
| LC_MainSHListNew | ActInConcertStatement | 与其他股东同属一致行动人说明 | | | null |
| LC_MainSHListNew | Notes | 备注说明 | | | null |
| LC_MainSHListNew | XGRQ| 修改日期 | | | 2020-11-15 11:07:48.150|
| LC_MainSHListNew | JSID| JSID | | | 658753672337 |
| LC_MainSHListNew | SecuInnerCode | 证券代码 | | | null |
| LC_MainSHListNew | SHKindCode| 股东性质编码 | | | 17 |
| LC_MainSHListNew | GDID| 股东ID | | | 537405 |
| LC_MainSHListNew | SHAttribute | 股东属性 | | | 2|
| LC_MainSHListNew | RestrainedAShare| 有限售A股数(股)| | | null |
| LC_MainSHListNew | UnstintedAShare | 无限售A股数(股)| | | null |
| LC_MainSHListNew | HoldShareASum | 持有A类普通股数量(股)| | | null |
| LC_MainSHListNew | RestrainedShareA| 有限售A类普通股数量(股)| | | null |
| LC_MainSHListNew | UnstintedShareA | 无限售A类普通股数量(股)| | | null |
| LC_MainSHListNew | HoldShareBSum | 持有B类普通股数量(股)| | | null |
| LC_MainSHListNew | RestrainedShareB| 有限售B类普通股数量(股)| | | null |
| LC_MainSHListNew | UnstintedShareB | 无限售B类普通股数量(股)| | | null |
| LC_MainSHListNew | HoldShareCSum | 持有C类普通股数量(股)| | | null |
| LC_MainSHListNew | HoldShareDSum | 持有D类普通股数量(股)| | | null |
| LC_MainSHListNew | HoldOtherComShareSum| 持有其他类普通股数量(股) | | | null |
| LC_MainSHListNew | InsertTime| 发布时间 | | | 2019-01-02 01:40:21.013|
| LC_MainSHListNew | HoldChangeType| 持股变动类型 | | | 4|
| LC_MainSHListNew | PrefShareWithVotRight | 有投票权的优先股数量(股) | | | null |
| LC_MainSHListNew | VotingRightsVol | 表决权总数(票) | | | null |
| LC_MainSHListNew | VotingRightsRatio | 表决权比例(%)| | | null |
| LC_MainSHListNew | SpecialVotingRightsVol| 特别表决权数量(票) | | | null |
| LC_MainSHListNew | PCTOfNRShares | 占无限售股份比例(%)| | | null |
| LC_MainSHListNew | RefinanceLoanShare|| | | null |
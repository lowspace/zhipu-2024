| column_name | column_description | 注释| Annotation|
|---|---|---|---|---|
| ID| ID | | |
| CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。| Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| EndDate | 日期 | | |
| InfoPublDate| 信息发布日期 | | |
| InfoSource| 信息来源 | | |
| InfoTypeCode| 信息类别编码 | 信息类别编码(InfoTypeCode)与(CT_SystemConst)表中的DM字段关联，令LB = 1025 AND DM IN (1,2,4,5,6)，得到信息类别编码的具体描述：1-前十大股东，2-前十流通股东，4-十大有限售条件股东，5-发行前股东，6-前十大表决权数量股东。 | The InfoTypeCode is associated with the DM field in the CT_SystemConst table, with LB = 1025 AND DM IN (1,2,4,5,6), the specific description of the InfoTypeCode is: 1 - Top ten shareholders, 2 - Top ten tradable shareholders, 4 - Top ten shareholders with restricted sale conditions, 5 - Shareholders before issuance, 6 - Top ten shareholders by voting rights quantity. |
| SHNo| 股东排名 | 股东排名（SHNo）：当“信息类别代码（InfoTypeCode）”=1时，“股东排名（SHNo）”表示股东排名；当“信息类别代码（InfoTypeCode）”=2时，“股东排名（SHNo）”表示流通股东排名。| Shareholder Ranking (SHNo): When "Information Type Code (InfoTypeCode)" equals 1, "Shareholder Ranking (SHNo)" indicates the ranking of shareholders; when "Information Type Code (InfoTypeCode)" equals 2, "Shareholder Ranking (SHNo)" indicates the ranking of circulating shareholders. |
| SHSerial| 股东序号 | | |
| SHList| 股东名称 | 股东名称（SHList）：此字段为股东名称公告原始披露值；如期望获取股东标准名称，可使用股东ID与相关表单关联，具体关联方式详见注4 | Shareholder Name (SHList): This field is the original disclosure value of the shareholder name announcement; if you expect to obtain the standard shareholder name, you can use the shareholder ID to associate with the relevant forms, and the specific association method is detailed in Note 4. |
| SHKind| 股东性质 | | |
| SHTypeCode| 股东类别编码 | | |
| SHType| 股东类别 | | |
| SecuCoBelongedCode| 所属券商编号 | | |
| SecuCoBelongedName| 归属机构名称 | | |
| SecuCode| 证券代码 | | |
| SecuAbbr| 证券简称 | | |
| HoldSum | 持股数(股) | | |
| PCTOfTotalShares| 占总股本比例 | 占总股本比例（%）（PCTOfTotalShares）：当“信息类别代码（InfoTypeCode）”=1时，持股数(股)/总股本*100当“信息类别代码（InfoTypeCode）”=2时，无限售股数(股)/总股本*100 | Percentage of Total Shares (PCTOfTotalShares): When "Information Type Code (InfoTypeCode)" equals 1, the number of shares held / total issued shares * 100; when "Information Type Code (InfoTypeCode)" equals 2, the number of unrestricted shares / total issued shares * 100.|
| RestrainedTShare| 其中：有限售股数(股) | | |
| UnstintedTShare | 其中：无限售股数(股) | | |
| HoldSumChange | 持股数量增减(股) | | |
| HoldSumChangeRate | 持股数量增减幅度(%)| | |
| HoldAShareSum | 持有A股数量(股)| | |
| PCTOfFloatShares| 占流通A股比例(%) | | |
| HoldBShareSum | 持有B股数量(股)| | |
| HoldHShareSum | 持有H股数量(股)| | |
| HoldOthterShareSum| 持有其他股数量(股) | | |
| ShareCharacterStatement | 股本性质描述 | | |
| PledgeInvolvedSum | 股权质押涉及股数(股) | | |
| FreezeInvolvedSum | 股权冻结涉及股数(股) | | |
| PFStatement | 股权质押冻结情况说明 | | |
| ConnectionRelation| 股东关联关系 | | |
| ConnectionStatement | 与其他股东关联关系说明 | | |
| ActInConcertStatement | 与其他股东同属一致行动人说明 | | |
| Notes | 备注说明 | | |
| XGRQ| 修改日期 | | |
| JSID| JSID | | |
| SecuInnerCode | 证券代码 | | |
| SHKindCode| 股东性质编码 | | |
| GDID| 股东ID | | |
| SHAttribute | 股东属性 | | |
| RestrainedAShare| 有限售A股数(股) | | |
| UnstintedAShare | 无限售A股数(股) | | |
| HoldShareASum | 持有A类普通股数量(股)| | |
| RestrainedShareA| 有限售A类普通股数量(股) | | |
| UnstintedShareA | 无限售A类普通股数量(股) | | |
| HoldShareBSum | 持有B类普通股数量(股)| | |
| RestrainedShareB| 有限售B类普通股数量(股) | | |
| UnstintedShareB | 无限售B类普通股数量(股) | | |
| HoldShareCSum | 持有C类普通股数量(股)| | |
| HoldShareDSum | 持有D类普通股数量(股)| | |
| HoldOtherComShareSum| 持有其他类普通股数量(股)| | |
| InsertTime| 发布时间 | | |
| HoldChangeType| 持股变动类型 | | |
| PrefShareWithVotRight | 有投票权的优先股数量(股) | | |
| VotingRightsVol | 表决权总数(票) | | |
| VotingRightsRatio | 表决权比例(%)| | |
| SpecialVotingRightsVol| 特别表决权数量(票) | | |
| PCTOfNRShares | 占无限售股份比例(%)| | |
| RefinanceLoanShare|  | | |
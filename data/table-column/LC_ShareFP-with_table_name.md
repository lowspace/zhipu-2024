| table_name | column_name | column_description | 注释 | Annotation|
|---|---|---|---|---|
| LC_ShareFP | ID| ID || |
| LC_ShareFP | CompanyCode | 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| LC_ShareFP | InfoPublDate| 信息发布日期 || |
| LC_ShareFP | InfoSource| 信息来源 || |
| LC_ShareFP | TypeSelect| 类别选择 | 类别选择(TypeSelect)与(CT_SystemConst)表中的DM字段关联，令LB = 1201 AND DM IN (2,3,5)，得到类别选择的具体描述：2-股权冻结，3-股权质押，5-股票质押式回购。| The Category Selection (TypeSelect) is associated with the DM field in the (CT_SystemConst) table, with LB = 1201 AND DM IN (2,3,5), resulting in the specific description of the Category Selection: 2-Equity Freezing, 3-Equity Pledge, 5-Stock Repurchase by Pledge. |
| LC_ShareFP | FPSHName| 股权被冻结质押股东名称 || |
| LC_ShareFP | ReceiverName| 接受股权质押方 || |
| LC_ShareFP | InvolvedSum | 涉及股数(股) || |
| LC_ShareFP | PCTOfPledger| 占冻结质押方持股数比例 || |
| LC_ShareFP | PCTOfTotalShares| 占总股本比例 || |
| LC_ShareFP | FPReason| 股权冻结质押原因 || |
| LC_ShareFP | StartDate | 起始日期 || |
| LC_ShareFP | EndDate | 日期 || |
| LC_ShareFP | Statement | 备注说明 || |
| LC_ShareFP | XGRQ| 修改日期 || |
| LC_ShareFP | JSID| JSID || |
| LC_ShareFP | SHSN| 股权被冻结质押股东序号 || |
| LC_ShareFP | SHAttribute | 股东所属性质 | 股权被冻结质押股东所属性质(SHAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AND DM IN (1,2,3,99)，得到股权被冻结质押股东所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | The equity freeze and pledge attribute of the shareholder (SHAttribute) is associated with the DM field in the (CT_SystemConst) table, where LB = 1783 AND DM IN (1,2,3,99), resulting in the specific description of the equity freeze and pledge attribute of the shareholder: 1 - Individual, 2 - Enterprise, 3 - Securities Type, 99 - Other. |
| LC_ShareFP | SHID| 股权被冻结质押股东ID | 股权被冻结质押股东ID(SHID)：当股权被冻结质押股东所属性质(SHAttribute)=2时，与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联 | When the equity is frozen and pledged, the shareholder ID (SHID): associated with the enterprise code (CompanyCode) in the enterprise code table (EP_CompanyMain) when the nature of the shareholder (SHAttribute) = 2. |
| LC_ShareFP | ReceiverAttribute | 接受股权质押方所属性质 | 接受股权质押方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 AND DM IN (1,2,3,99)，得到接受股权质押方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | The nature of the equity pledge receiver (ReceiverAttribute) is associated with the DM field in the (CT_SystemConst) table, where LB = 1783 AND DM IN (1,2,3,99), resulting in the specific description of the nature of the equity pledge receiver: 1 - Individual, 2 - Enterprise, 3 - Securities Type, 99 - Other. |
| LC_ShareFP | ReceiverID| 接受股权质押方ID | 接受股权质押方ID(ReceiverID)：当接受股权质押方所属性质(ReceiverAttribute)=2时，与企业码表（EP_CompanyMain）中的企业编号（CompanyCode）关联 | Receiver ID (ReceiverID): When the attribute of the party accepting equity pledge (ReceiverAttribute) equals 2, it is associated with the company code (CompanyCode) in the enterprise code table (EP_CompanyMain). |
| LC_ShareFP | EventCode | 事项编码 || |
| LC_ShareFP | EventDate | 事项日期 || |
| LC_ShareFP | UnstintedTShare | 其中:无限售股数(股)|| |
| LC_ShareFP | RestrainedTShare| 其中:有限售股数(股)|| |
| LC_ShareFP | InitialInfoPublDate | No description available || |
| LC_ShareFP | InitialPledgeSum| No description available || |
| LC_ShareFP | EstimateReleaseDate | No description available || |
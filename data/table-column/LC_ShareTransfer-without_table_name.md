| column_name | column_description| 注释 | Annotation|
|---|---|---|---|---|
| ID| ID|| |
| CompanyCode | 公司代码| 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. |
| InfoPublDate| 信息发布日期|| |
| InfoSource| 信息来源|| |
| ContractSignDate| 股权转让协议签署日|| |
| ApprovedDate| 转让批准日期|| |
| TranDate| 股权正式变动日期/过户日期 || |
| TransfererName| 股权出让方名称|| |
| TansfererEcoNature| 股权出让方经济性质|| |
| TranShareType | 出让股权性质| 出让股权性质(TranShareType)与(CT_SystemConst)表中的DM字段关联，令LB = 1040，得到出让股权性质的具体描述：1-国家股，2-国有法人股，3-外资法人股，4-其他法人股，5-流通A股，6-B股，7-H股，8-转配股，9-专项资产管理计划转让，10-资产支持证券转让，11-中小企业私募债转让，12-中国存托凭证，13-可转换公司债券。| The nature of equity transfer (TranShareType) is associated with the DM field in the (CT_SystemConst) table, with LB set to 1040, resulting in the specific description of the nature of equity transfer: 1 - State-owned shares, 2 - State-owned legal person shares, 3 - Foreign-funded legal person shares, 4 - Other legal person shares, 5 - Tradable A shares, 6 - B shares, 7 - H shares, 8 - Transferable subscription shares, 9 - Special asset management plan transfer, 10 - Asset-backed securities transfer, 11 - Small and medium-sized enterprise private debt transfer, 12 - Chinese depository receipts, 13 - Convertible corporate bonds. |
| SumBeforeTran | 出让前持股数量(股)|| |
| PCTBeforeTran | 出让前持股比例|| |
| SumAfterTran| 出让后持股数量(股)|| |
| PCTAfterTran| 出让后持股比例|| |
| ReceiverName| 接受股权质押方|| |
| ReceiverEcoNature | 股权受让方经济性质|| |
| SumAfterRece| 受让后持股数量(股)|| |
| PCTAfterRece| 受让后持股比例|| |
| TranMode| 股权转让方式| 股权转让方式(TranMode)与(CT_SystemConst)表中的DM字段关联，令LB = 1202 AND DM NOT IN ( 8,51,55,57,98)，得到股权转让方式的具体描述：1-协议转让，2-国有股行政划转或变更，3-执行法院裁定，4-以资抵债，5-二级市场买卖，6-其他-股东重组，7-股东更名，9-其他-要约收购，10-以股抵债，11-大宗交易(席位)，12-大宗交易，13-其他-ETF换购，14-其他-行权买入，15-集中竞价，16-定向可转债转让，17-集合竞价，18-连续竞价，19-做市，20-询价转让，21-赠与，22-继承，24-间接方式转让，53-股改后间接股东增持，56-交易所集中交易，59-股权激励，70-国有股转持，71-老股转让，80-司法拍卖，99-其他。 | The transfer method of equity transfer (TranMode) is associated with the DM field in the (CT_SystemConst) table, with LB = 1202 AND DM NOT IN (8,51,55,57,98), resulting in the specific description of the equity transfer method: 1-Protocol transfer, 2-State-owned shares administrative transfer or change, 3-Enforce court ruling, 4-Pay debt with assets, 5-Secondary market trading, 6-Other - Shareholder restructuring, 7-Shareholder name change, 9-Other - Tender offer, 10-Pay debt with shares, 11-Bulk transaction (seat), 12-Bulk transaction, 13-Other - ETF subscription, 14-Other - Exercise purchase, 15-Concentrated bidding, 16-Directed convertible bond transfer, 17-Collective bidding, 18-Continuous bidding, 19-Market making, 20-Inquiry transfer, 21-Gift, 22-Inheritance, 24-Indirect method of transfer, 53-Indirect shareholder increase after share reform, 56-Exchange centralized trading, 59-Equity incentive, 70-State-owned shares transfer holding, 71-Old shares transfer, 80-Judicial auction, 99-Other. |
| InvolvedSum | 涉及股数(股)|| |
| PCTOfTansferer| 占出让方原持股数比例|| |
| PCTOfTotalShares| 占总股本比例|| |
| DealPrice | 交易价格(元/股) || |
| DealTurnover| 交易金额(元)|| |
| ValidCondition| 生效条件|| |
| TranStatement | 事项描述与进展说明|| |
| IfSuspended | 是否终止实施| 是否终止实施（IfSuspended），该字段固定以下常量：1-是；0-否| Whether to terminate the implementation (IfSuspended), this field is fixed with the following constants: 1-Yes; 0-No. |
| SuspendedPublDate | 终止实施公告日期|| |
| XGRQ| 修改日期|| |
| JSID| JSID|| |
| SNBeforeTran| 出让前股东序号|| |
| SNAfterTran | 出让后股东序号|| |
| SNAfterRece | 受让后股东序号|| |
| IfSPBlockTradeCode| 是否专场大宗交易代码| 是否专场大宗交易代码（IfSPBLockTradeCode），该字段固定以下常量：1-是；0-否 | Whether to set up a special bulk transaction code (IfSPBLockTradeCode), this field is fixed with the following constants: 1-yes; 0-no.|
| IfSPBlockTrade| 是否专场大宗交易|| |
| InnerCode | 证券内部编码|| |
| ResSumAfterTran | 出让后有限售股数(股) || |
| NonResSumAfterTran| 出让后无限售股数(股) || |
| ResSumAfterRece | 受让后有限售股数(股) || |
| NonResSumAfterRece| 受让后无限售股数(股) || |
| InitialInfoPublDate | 首次信息发布日期|| |
| TransfererAttribute | 股权出让方所属性质|| |
| TransfererCode| 股权出让方编码|| |
| ReceiverAttribute | 股权受让方所属性质| 股权受让方所属性质(ReceiverAttribute)与(CT_SystemConst)表中的DM字段关联，令LB = 1783 and DM in (1,2,3,99)，得到股权受让方所属性质的具体描述：1-自然人，2-企业，3-证券品种，99-其他。 | The attribute of equity transfer recipient (ReceiverAttribute) is associated with the DM field in the (CT_SystemConst) table, with LB = 1783 and DM in (1,2,3,99), yielding the specific description of the attribute of equity transfer recipient: 1 - Natural Person, 2 - Enterprise, 3 - Securities Variety, 99 - Other. |
| ReceiverCode| 股权受让方编码| 当股权受让方所属性质(ReceiverAttribute)=2时，与“企业码表(EP_CompanyMain)”中的“企业编号(CompanyCode)”关联,得到事件主体企业的基本信息; 当股权受让方所属性质(ReceiverAttribute)=3时,与“证券码表总表(SecuMainAll)”中的“证券内部编码(InnerCode)”关联,得到事件主体证券品种的基本信息。 | When the attribute of equity transfer recipient (ReceiverAttribute) equals 2, it is associated with the "Company Code" in the "Enterprise Code Table (EP_CompanyMain)", and the basic information of the event subject enterprise is obtained; when the attribute of equity transfer recipient (ReceiverAttribute) equals 3, it is associated with the "Inner Code" in the "Securities Code Table (SecuMainAll)", and the basic information of the event subject securities variety is obtained.|
| InsertTime| 发布时间|| |
| SumBeforeRece | 受让前持股数量(股)|| |
| PCTBeforerRece| 受让前持股比例(%) || |
| TranStartDate | 股权变动起始日|| |
| SerialNumber| 序号|| |
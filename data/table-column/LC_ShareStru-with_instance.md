| table_name | column_name| column_description | 注释 | Annotation| 数据示例|
|---|---|---|---|---|---|
| AStockShareholderDB.LC_ShareStru | ID | ID || | 599175654209|
| AStockShareholderDB.LC_ShareStru | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. | 76745 |
| AStockShareholderDB.LC_ShareStru | InfoSource | 信息来源 || | 限售股份上市流通的提示性公告|
| AStockShareholderDB.LC_ShareStru | EndDate| 日期 || | 2019-01-02 12:00:00.000 |
| AStockShareholderDB.LC_ShareStru | NonListedShares| 未流通A股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | PromoterShares | 发起人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | StateShares| 国家股(股) || | null|
| AStockShareholderDB.LC_ShareStru | DLegalPersonShares | 境内法人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | FLegalPersonShares | 外资法人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | OtherPromoterShares| 其它发起人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | RaisedLPShares | 募集法人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | NaturalPersonHoldLPShares| 自然人法人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | StaffShares| 职工股(股) || | null|
| AStockShareholderDB.LC_ShareStru | RightsIssueTransferred | 转配股(股) || | null|
| AStockShareholderDB.LC_ShareStru | PreferredAndOtherShares| 优先股及其他(股) || | null|
| AStockShareholderDB.LC_ShareStru | PreferredShares| 优先股(股) || | null|
| AStockShareholderDB.LC_ShareStru | FloatShare | 流通股本(股) || | 5062400000.0|
| AStockShareholderDB.LC_ShareStru | AFloats| 流通A股(股)|| | 5062400000.0|
| AStockShareholderDB.LC_ShareStru | AFloatListed | 已上市流通A股(包含高管股)(股)|| | 5046400000.0|
| AStockShareholderDB.LC_ShareStru | ManagementShares | 高管股(股) || | null|
| AStockShareholderDB.LC_ShareStru | StategicInvestorShares | 战略投资者配售持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | CommonLPShares | 一般法人配售持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | MutualFundShares | 基金配售持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | AdditionalIssueUnlisted| 增发未上市(股) || | null|
| AStockShareholderDB.LC_ShareStru | RightsIssueUnlisted| 配股未上市(股) || | null|
| AStockShareholderDB.LC_ShareStru | Bshares| B股_旧(股) || | null|
| AStockShareholderDB.LC_ShareStru | Hshares| H股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | Sshares| S股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | Nshares| N股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | OtherFloatShares | 海外上市股(股) || | null|
| AStockShareholderDB.LC_ShareStru | TotalShares| 总股本(股) || | 5062400000.0|
| AStockShareholderDB.LC_ShareStru | ChangeType | 股本变动原因类别 | 数值型常量。股本变动原因类别(ChangeType)与(CT_SystemConst)表中的DM字段关联，令LB = 1022 AND DM NOT IN (43,60,101,102,105,115,116,117,118,119,121,123,127,128,129,131,132,135)，得到股本变动原因类别的具体描述：1-A股发行，2-B股发行，3-A股发行基金配售上市，4-A股发行法人配售上市，6-A股上市，7-B股上市，8-送转股，10-配股除权，11-配股上市，12-转配股上市，17-非公开增发A股上市，18-非公开增发A股，19-定向增发法人股，20-增发A股，21-增发B股，22-增发A股上市，23-增发A股基金配售上市，24-增发A股法人配售上市，25-增发A股原股东配售上市，26-H股增发，27-增发B股上市，28-H股首发上市，29-超额配售H股上市，30-国家股配售，35-股份回购，40-吸收合并，44-以股抵债，45-职工股上市，46-STAQ/NET系统法人股上市，47-外资法人股上市，48-可转换债券转股，49-股权转让，50-面值拆细，51-其他，52-CDR发行，53-CDR上市，54-CDR增发，55-CDR增发上市，56-CDR配股除权，57-CDR配股上市，58-CDR超额配售上市，59-优先股转普通股，71-股权分置方案实施，73-股权分置股份追送，75-股权分置限售流通，77-股权分置增持，78-股权分置股东增持股份上市，79-配股限售流通，80-股权激励限售流通，81-因权证行权流通，82-发行前股份限售流通，83-转债转股限售流通，84-股权激励方案实施，89-延长限售锁定期，90-延长限售锁定期流通，91-B股转H股，100-授予限制性股票，103-员工持股计划，104-员工持股计划限售流通，106-D股增发，107-D股首发上市，108-超额配售D股上市，109-超额配售A股上市，110-GDR基础股票首发上市，111-GDR基础股票增发上市，112-超额配售GDR基础股票上市，113-GDR基础股票生成兑回，114-三板挂牌，130-高管股份减少，134-战略配售股份出借，136-战略配售股份归还，137-高管股份增加，138-股东承诺不减持，139-分红股份上市，140-超额配售B股上市，141-追溯更新，142-承诺不减持到期。 | Numeric constant. The reason category for changes in equity (ChangeType) is associated with the DM field in the CT_SystemConst table, with LB = 1022 AND DM NOT IN (43,60,101,102,105,115,116,117,118,119,121,123,127,128,129,131,132,135), resulting in the specific description of the equity change reason category: 1 - A-share issuance, 2 - B-share issuance, 3 - A-share issuance and fund private placement listing, 4 - A-share issuance and legal person private placement listing, 6 - A-share listing, 7 - B-share listing, 8 - Stock transfer and spin-off, 10 - Rights issue and adjustment, 11 - Rights issue listing, 12 - Spin-off listing, 17 - Non-publicly issued A-share listing, 18 - Non-publicly issued A-share, 19 - Directed private placement of legal person shares, 20 - Additional issuance of A-shares, 21 - Additional issuance of B-shares, 22 - Additional issuance of A-share listing, 23 - Additional issuance of A-share fund private placement listing, 24 - Additional issuance of A-share legal person private placement listing, 25 - Additional issuance of A-share original shareholder private placement listing, 26 - H-share additional issuance, 27 - Additional issuance of B-share listing, 28 - H-share initial public offering, 29 - Excess share placement of H-share listing, 30 - State-owned share placement, 35 - Share repurchase, 40 - Absorption merger, 44 - Debt offset by shares, 45 - Employee share listing, 46 - STAQ/NET system legal person share listing, 47 - Foreign-funded legal person share listing, 48 - Convertible bond conversion to shares, 49 - Share transfer, 50 - Par value splitting, 51 - Others, 52 - CDR issuance, 53 - CDR listing, 54 - CDR additional issuance, 55 - CDR additional issuance listing, 56 - CDR rights issue and adjustment, 57 - CDR rights issue listing, 58 - CDR excess share placement listing, 59 - Preferred shares converted to common shares, 71 - Implementation of equity separation scheme, 73 - Equity separation share follow-up distribution, 75 - Equity separation restricted circulation, 77 - Equity separation share increase, 78 - Equity separation shareholder increase share listing, 79 - Rights issue restricted circulation, 80 - Equity incentive restricted circulation, 81 - Circulation due to warrant exercise, 82 - Pre-issuance share restricted circulation, 83 - Convertible bond conversion to share restricted circulation, 84 - Implementation of equity incentive plan, 89 - Extension of restricted period, 90 - Extension of restricted period circulation, 91 - B-share conversion to H-share, 100 - Granting of restricted stock, 103 - Employee stock ownership plan, 104 - Employee stock ownership plan restricted circulation, 106 - D-share additional issuance, 107 - D-share initial public offering, 108 - Excess share placement of D-share listing, 109 - Excess share placement of A-share listing, 110 - GDR underlying stock initial public offering, 111 - GDR underlying stock additional issuance listing, 112 - Excess share placement of GDR underlying stock listing, 113 - GDR underlying stock creation and redemption, 114 - Third board listing, 130 - Reduction of executive shares, 134 - Strategic placement share lending, 136 - Strategic placement share return, 137 - Increase of executive shares, 138 - Shareholder commitment not to reduce, 139 - Dividend share listing, 140 - Excess share placement of B-share listing, 141 - Retrospective update, 142 - Commitment not to reduce maturity. | 24|
| AStockShareholderDB.LC_ShareStru | ChangeReason | 简称变更原因 || | 252288万股增发A股一般法人配售股份上市 |
| AStockShareholderDB.LC_ShareStru | XGRQ | 修改日期 || | 2023-10-05 12:03:31.517 |
| AStockShareholderDB.LC_ShareStru | JSID | JSID || | 749927668746|
| AStockShareholderDB.LC_ShareStru | SLegalPersonShares | 国有法人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | RaisedSLPShares| 募集国有法人股(股) || | null|
| AStockShareholderDB.LC_ShareStru | OtherAFloatShares| 其他流通股份(股) || | null|
| AStockShareholderDB.LC_ShareStru | RestrictedAFloatShares | 有限售流通A股(股)|| | 16000000.0|
| AStockShareholderDB.LC_ShareStru | RestrinctStaffShares | 有限售流通股中职工股(股) || | null|
| AStockShareholderDB.LC_ShareStru | NonListedBShares | 未流通B股_旧 || | null|
| AStockShareholderDB.LC_ShareStru | InfoPublDate | 信息发布日期 || | 2018-12-27 12:00:00.000 |
| AStockShareholderDB.LC_ShareStru | RestrictedShares | 有限售条件的流通股(股) || | 16000000.0|
| AStockShareholderDB.LC_ShareStru | StateHolding | 国家持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | SLegalPersonHolding| 国有法人持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | OtherDCapitalHolding | 其他内资持股(股) || | 13500000.0|
| AStockShareholderDB.LC_ShareStru | DLegalPersonHolding| 境内法人持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | DNaturalPersonHolding| 境内自然人持股(股) || | 13500000.0|
| AStockShareholderDB.LC_ShareStru | ForeignHolding | 外资持股(股) || | 2500000.0 |
| AStockShareholderDB.LC_ShareStru | FLegalPersonHolding| 境外法人持股(股) || | null|
| AStockShareholderDB.LC_ShareStru | FNaturalPersonHolding| 境外自然人持股(股) || | 2500000.0 |
| AStockShareholderDB.LC_ShareStru | OtherRestrictedShares| 其他有限售(股) || | null|
| AStockShareholderDB.LC_ShareStru | RestrictedBFloatShares | 有限售B股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | PerValue | 每股面值(元) || | 1.0 |
| AStockShareholderDB.LC_ShareStru | Ashares| A股(股)|| | 5062400000.0|
| AStockShareholderDB.LC_ShareStru | NonRestrictedShares| 无限售条件流通A股(股)(披露)|| | 5046400000.0|
| AStockShareholderDB.LC_ShareStru | BsharesTotal | B股总值(股)|| | null|
| AStockShareholderDB.LC_ShareStru | ListedBShares| 流通B股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | NonListedRestrictedBShares | 未流通B股(股)|| | null|
| AStockShareholderDB.LC_ShareStru | ForeignHoldingAshares| 外资持A股(股)|| | 2500000.0 |
| AStockShareholderDB.LC_ShareStru | RestrictedAShares| 有限售条件的流通A股(股)(计算)|| | 16000000.0|
| AStockShareholderDB.LC_ShareStru | OtherFNonListedShares| 其他外资股(股) || | null|
| AStockShareholderDB.LC_ShareStru | NonResiSharesJY| 无限售条件流通A股(股)(计算)|| | 5046400000.0|
| AStockShareholderDB.LC_ShareStru | RestrictAShareP| 有限售条件的流通A股(股)(披露)|| | 16000000.0|
| AStockShareholderDB.LC_ShareStru | SRUnlistedShare| 增发、配股未上市股份(股)(披露) || | null|
| AStockShareholderDB.LC_ShareStru | NonResiBShares | 无限售流通B股|| | null|
| AStockShareholderDB.LC_ShareStru | GDRshares| GDR代表基础股票(股)|| | null|
| AStockShareholderDB.LC_ShareStru | ParValueCurrencyUnit | 每股面值货币单位 || | 1420|
| AStockShareholderDB.LC_ShareStru | InsertTime | 发布时间 || | 2018-12-26 09:41:00.490 |
| AStockShareholderDB.LC_ShareStru | NonRestrictedHShares | 无限售H股|| | null|
| AStockShareholderDB.LC_ShareStru | RestrictedHShares| 有限售H股|| | null|
| AStockShareholderDB.LC_ShareStru | OUnListedShares| 其他未流通股(股) || | null|
| AStockShareholderDB.LC_ShareStru | OtherNonListedShares | 其他未流通股(股) || | null|
| AStockShareholderDB.LC_ShareStru | Dshares||| | null|
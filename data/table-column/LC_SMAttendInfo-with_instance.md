| table_name| column_name| column_description | 注释 | Annotation| 数据示例|
|---|---|---|---|---|---|
| AStockShareholderDB.LC_SMAttendInfo | ID | ID || | 599816366984|
| AStockShareholderDB.LC_SMAttendInfo | CompanyCode| 公司代码 | 公司代码（CompanyCode）：与“证券主表（SecuMain）”中的“公司代码（CompanyCode）”关联，得到上市公司的交易代码、简称等。 | Company Code (CompanyCode): Associated with the "Company Code (CompanyCode)" in "Securities Main Table (SecuMain)", to obtain the trading code, abbreviation, etc. of the listed company. | 273 |
| AStockShareholderDB.LC_SMAttendInfo | InitialInfoPublDate| 首次信息发布日期 || | 2019-01-03 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | LatestInfoPublDate | 最新信息发布日期 || | null|
| AStockShareholderDB.LC_SMAttendInfo | MeetingDate| 股东大会召开日 || | 2019-01-21 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | SHMeetingTime| 股东大会召开时间 || | null|
| AStockShareholderDB.LC_SMAttendInfo | SMRegDate| 股东大会股权登记日 || | 2019-01-16 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | MeetingRegStartDate| 会议登记起始日 || | 2019-01-17 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | MeetingRegEndDate| 会议登记截止日 || | 2019-01-18 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | AnounceDate| 股东大会公告日期 || | 2019-01-22 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | ProposalContent| 议案内容 || | 审议《关于制定<公司董事,监事和高级管理人员薪酬管理办法>的 |
| AStockShareholderDB.LC_SMAttendInfo | CancelDate | 股东大会取消日期 || | null|
| AStockShareholderDB.LC_SMAttendInfo | Address| 股东大会召开地址 || | 肇庆市风华电子工业城1号楼3楼国际会议厅|
| AStockShareholderDB.LC_SMAttendInfo | IfEffected | 是否有效 | 是否有效(IfEffected)与(CT_SystemConst)表中的DM字段关联，令LB = 999 AND DM IN (1,2)，得到是否有效的具体描述：1-是，2-否。 | Whether "IfEffected" is associated with the "DM" field in the "CT_SystemConst" table, let LB = 999 AND DM IN (1,2), to obtain the specific description of whether it is effective: 1-Yes, 2-No. | 1 |
| AStockShareholderDB.LC_SMAttendInfo | SerialNumber | 序号 || | 1 |
| AStockShareholderDB.LC_SMAttendInfo | MeetingType| 股东大会类别 | 股东大会类别(MeetingType)与(CT_SystemConst)表中的DM字段关联，令LB = 1299 AND DM IN (1,3,5)，得到股东大会类别的具体描述：1-年度股东大会，3-临时股东大会，5-出资人组会议。 | The "MeetingType" of the shareholders' meeting is associated with the DM field in the "CT_SystemConst" table, with LB = 1299 AND DM IN (1,3,5), resulting in the specific description of the shareholders' meeting type: 1-Annual General Meeting, 3-Extraordinary General Meeting, 5-Investors' Meeting. | 3 |
| AStockShareholderDB.LC_SMAttendInfo | VotingMeans| 投票表决方式 | 投票表决方式(VotingMeans)与(CT_SystemConst)表中的DM字段关联，令LB = 1300，得到投票表决方式的具体描述：1-网络投票，2-现场投票，3-网络和通讯，5-现场和网络投票，9-通讯表决，15-现场投票和通讯表决，16-现场投票、通讯表决和网络投票。 | The voting means (VotingMeans) is associated with the DM field in the (CT_SystemConst) table, with LB set to 1300, the specific description of the voting means is as follows: 1-Internet voting, 2-Onsite voting, 3-Internet and communication, 5-Onsite and Internet voting, 9-Communication voting, 15-Onsite voting and communication voting, 16-Onsite voting, communication voting, and Internet voting.| 5 |
| AStockShareholderDB.LC_SMAttendInfo | Year | 年度 || | 2019|
| AStockShareholderDB.LC_SMAttendInfo | Series | 届次 || | 1 |
| AStockShareholderDB.LC_SMAttendInfo | NetVotingPlatform| 网络投票通道 | 网络投票通道(NetVotingPlatform)与(CT_SystemConst)表中的DM字段关联，令LB = 2521，得到网络投票通道的具体描述：1-中国证券登记结算有限责任公司网络系统，2-上海证券交易所交易系统，3-深圳证券交易所交易系统，4-互联网投票系统，5-中国证券登记结算有限责任公司网络系统、互联网投票系统，6-上海证券交易所交易系统、互联网投票系统，7-深圳证券交易所交易系统、互联网投票系统，999-其他。 | The NetVotingPlatform is associated with the DM field in the CT_SystemConst table, with LB set to 2521, the specific description of the NetVotingPlatform is as follows: 1-China Securities Registration and Settlement Corporation Network System, 2-Shanghai Stock Exchange Trading System, 3-Shenzhen Stock Exchange Trading System, 4-Internet Voting System, 5-China Securities Registration and Settlement Corporation Network System, Internet Voting System, 6-Shanghai Stock Exchange Trading System, Internet Voting System, 7-Shenzhen Stock Exchange Trading System, Internet Voting System, 999-Other. | 7 |
| AStockShareholderDB.LC_SMAttendInfo | NetVotingCode| 网络投票代码 || | 360636|
| AStockShareholderDB.LC_SMAttendInfo | VotingAbbr | 投票简称 || | 风华投票|
| AStockShareholderDB.LC_SMAttendInfo | NetVotingStartDate | 网络投票起始日 || | 2019-01-20 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | NetVotingEndDate | 网络投票截止日 || | 2019-01-21 12:00:00.000 |
| AStockShareholderDB.LC_SMAttendInfo | Presider | 大会主持人 || | 王广军|
| AStockShareholderDB.LC_SMAttendInfo | PresiderOfficialPost | 主持人职务(多选) || | nan |
| AStockShareholderDB.LC_SMAttendInfo | TestmonyLawOffice| 见证律师事务所 || | 广东东方昆仑律师事务所|
| AStockShareholderDB.LC_SMAttendInfo | LawOfficeCode| 律师事务所企业编号 | 律师事务所企业编号(LawOfficeCode)：与机构基本资料表(LC_InstiArchive)中公司代码(CompanyCode)关联，得到预测机构的具体信息。| Law Office Code: Correlated with the Company Code in the Institutional Basic Information Form (LC_InstiArchive), to obtain specific information of the predicted institution. | null|
| AStockShareholderDB.LC_SMAttendInfo | Lawyer | 经办律师 || | 张吕、谢振声|
| AStockShareholderDB.LC_SMAttendInfo | AttendanceType | 股东出席类别 | 股东出席类别(AttendanceType)与(CT_SystemConst)表中的DM字段关联，令LB = 1301，得到股东出席类别的具体描述：1-总体出席，2-现场投票出席，3-网络投票出席。| Shareholders' attendance type (AttendanceType) is associated with the DM field in the (CT_SystemConst) table, setting LB = 1301, yields the specific description of the shareholders' attendance type: 1 - Overall attendance, 2 - On-site voting attendance, 3 - Online voting attendance. | 1 |
| AStockShareholderDB.LC_SMAttendInfo | AttendanceNumber | 出席总体股东及代表人数(人) || | 285 |
| AStockShareholderDB.LC_SMAttendInfo | ASharesNumber| #A股股东人数(人) || | null|
| AStockShareholderDB.LC_SMAttendInfo | HSharesNumber| #H股股东人数(人) || | null|
| AStockShareholderDB.LC_SMAttendInfo | OtherSharesNumber| #其他基础股票股东人数(人)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareANumber | #A类普通股股东人数 || | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareBNumber | #B类普通股股东人数 || | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareReprensented| 出席总体股东代表股份(股)/(票)|| | 217666984.0 |
| AStockShareholderDB.LC_SMAttendInfo | ASharesReprensented| #A股股东代表股份(股) || | null|
| AStockShareholderDB.LC_SMAttendInfo | HSharesReprensented| #H股股东代表股份(股) || | null|
| AStockShareholderDB.LC_SMAttendInfo | OSharesReprensented| #其他基础股票股东代表股份占比(%) || | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareAReprensented | #A类普通股股东代表股份(票)(以股计) || | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareBReprensented | #B类普通股股东代表股份(票)(以股计) || | null|
| AStockShareholderDB.LC_SMAttendInfo | RatioInTotalShare| 出席总体股东股份占总股份比例(%)|| | 24.314|
| AStockShareholderDB.LC_SMAttendInfo | ASharesRatio | #A股股东代表股份占比(%)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | HSharesRatio | #H股股东代表股份占比(%)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | OtherSharesRatio | #其他基础股票股东代表股份占比(%) || | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareARatio| #A类普通股股东代表股份比例(%)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | ShareBRatio| #B类普通股股东代表股份比例(%)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | MSharesNumber| 出席中小股东及代表人数 || | null|
| AStockShareholderDB.LC_SMAttendInfo | MShareReprensented | 出席中小股东代表股份(股) || | null|
| AStockShareholderDB.LC_SMAttendInfo | MSharesRatio | 出席中小股东股份占总股份比例(%)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | PSharesNumber| 出席优先股股东及代表人数 || | null|
| AStockShareholderDB.LC_SMAttendInfo | PSharesReprensented| 出席优先股股东代表股份(股) || | null|
| AStockShareholderDB.LC_SMAttendInfo | PSharesRatio | 出席优先股股东股份占总股份比例(%)|| | null|
| AStockShareholderDB.LC_SMAttendInfo | InsertTime | 发布时间 || | 2022-11-18 05:56:07.557 |
| AStockShareholderDB.LC_SMAttendInfo | XGRQ | 更新时间 || | 2022-11-25 01:07:08.657 |
| AStockShareholderDB.LC_SMAttendInfo | JSID | JSID || | 722737283681|
| table_name| column_name | column_description | 注释 | Annotation | 数据示例|
|---|---|---|---|---|---|
| InstitutionDB.PS_NewsSecurity | ID| ID ||| 646996772025|
| InstitutionDB.PS_NewsSecurity | RID | RID| RID：与舆情资讯主表（PS_NewsMain）表ID字段关联。 | RID: Associated with the ID field of the Public Opinion Information Main Table (PS_NewsMain).| 606498305893|
| InstitutionDB.PS_NewsSecurity | InnerCode | 证券内部编码 | 证券内部编码(InnerCode)：与证券码表总表（SecuMainAll）中内部编码（InnerCode）关联，获得涉及证券的详细信息。| Security Internal Code (InnerCode): Associated with the internal code (InnerCode) in the master table of security codes (SecuMainAll), to obtain detailed information about the securities involved. | 16764 |
| InstitutionDB.PS_NewsSecurity | CompanyCode | 公司代码 | 公司代码(CompanyCode)：与“企业基本信息（EP_CompanyMain）”中的“企业编号CompanyCode）”关联，得到涉及公司的具体说明。 | Company Code: Associated with "Company Code" in "Enterprise Basic Information (EP_CompanyMain)", to obtain specific descriptions of the involved company.| 170593|
| InstitutionDB.PS_NewsSecurity | EventType | 事件类别 | 事件类别（EventType）：根据事件体系指引表（PS_EventStru）中的事件代码（EventCode）关联，获取涉及事件类别的详细信息。 | Event Category (EventType): Obtain detailed information about the event categories involved by associating with the event code (EventCode) in the event system guidance table (PS_EventStru).| FBT000000094|
| InstitutionDB.PS_NewsSecurity | EventName | 事件名称 ||| 对外投资|
| InstitutionDB.PS_NewsSecurity | EventDate | 事件时间 ||| null|
| InstitutionDB.PS_NewsSecurity | EmotionDirection| 情感方向 | 情感方向（EmotionDirection）：该字段固定以下常量：FCC0000002QA — 负面、FCC0000002QF — 中性、FCC0000002Q9 — 正面。| Emotion Direction (EmotionDirection): This field is fixed with the following constants: FCC0000002QA - Negative, FCC0000002QF - Neutral, FCC0000002Q9 - Positive.| FCC0000002QF|
| InstitutionDB.PS_NewsSecurity | EmotionImportance | 情感重要度 | 情感重要度（EmotionImportance）：该字段固定以下常量：FCC0000002QB — 零星、FCC0000002QC— 一星、FCC0000002QD — 二星、FCC0000002QE — 三星。 | Emotion Importance: This field is fixed with the following constants: FCC0000002QB - Sporadic, FCC0000002QC - One Star, FCC0000002QD - Two Stars, FCC0000002QE - Three Stars.| FCC0000002QE|
| InstitutionDB.PS_NewsSecurity | InsertTime| 发布时间 ||| 2020-06-29 06:44:12.670 |
| InstitutionDB.PS_NewsSecurity | UpdateTime| 更新时间 ||| 2020-06-29 06:44:12.670 |
| InstitutionDB.PS_NewsSecurity | JSID| JSID ||| 646996772026|
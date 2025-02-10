| table_name | column_name | column_description | 注释| Annotation| 数据示例|
|---|---|---|---|---|---|
| PS_EventStru | ID| ID | | | 642623836927|
| PS_EventStru | EventName | 事件名称 | | | 资质荣誉|
| PS_EventStru | EventCode | 事件代码 | 事件代码（EventCode）：与机构舆情表（PS_NewsCompany）的事件类别（EventType）关联，与证券舆情表（PS_NewsSecurity）的事件类别（EventType）关联，与宏观舆情表（PS_NewsMacro）的事件类别（EventType）关联，可得功能表单对应事件名称以及所属父级事件 | Event Code: Associated with the event type (EventType) of the institutional public opinion table (PS_NewsCompany), associated with the event type (EventType) of the securities public opinion table (PS_NewsSecurity), associated with the event type (EventType) of the macro public opinion table (PS_NewsMacro), and can obtain the corresponding event name and parent event to which it belongs in the functional form. | FBT0000000EY|
| PS_EventStru | FEventCode| 父级事件代码 | | | FBT000000089|
| PS_EventStru | EventLevel| 事件级别 | | | 2 |
| PS_EventStru | IfEffected| 是否有效 | 是否有效（IfEffected）：该字段固定以下常量：FCC000000005-是，FCC000000006-否| Whether Effective (IfEffected): This field is fixed with the following constants: FCC000000005-Yes, FCC000000006-No.| FCC000000005|
| PS_EventStru | InsertTime| 发布时间 | | | 2020-05-25 10:47:08.247 |
| PS_EventStru | UpdateTime| 更新时间 | | | 2020-05-25 10:47:08.247 |
| PS_EventStru | JSID| JSID | | | 643718828445|
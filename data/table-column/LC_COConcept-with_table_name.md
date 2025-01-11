| table_name | column_name | column_description | 注释 | Annotation |
|---|---|---|---|---|
| LC_COConcept | ID| ID |||
| LC_COConcept | InnerCode | 证券内部编码 | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。 | Security Internal Code (InnerCode): Associated with the "Security Main Table (SecuMain)" "Security Internal Code (InnerCode)", to obtain the security's trading code, abbreviation, etc. |
| LC_COConcept | ConceptCode | 概念代码 | 概念代码(ConceptCode)：与“概念板块表(LC_ConceptList)”中的“概念代码(ConceptCode)”关联，得到所属概念的信息。 | Concept Code: Associated with the "Concept Code" in the "LC_ConceptList" to obtain information of the所属 concept. |
| LC_COConcept | InDate| 调入日期 |||
| LC_COConcept | OutDate | 调出日期 |||
| LC_COConcept | IndiState | 所属状态 | 所属状态(IndiState)，该字段固定以下常量：1-正常，0-终止。| Belonging status (IndiState), this field is fixed with the following constants: 1-normal, 0-termination. |
| LC_COConcept | Remark| 备注 | 备注(Remark):字段解释了该成分股属于此概念的原因及逻辑。| Remark: The field explains the reason and logic why the component stock belongs to this concept. |
| LC_COConcept | InfoPublDate| 信息发布日期 |||
| LC_COConcept | UpdateTime| 更新时间 |||
| LC_COConcept | JSID| JSID |||
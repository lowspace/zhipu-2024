| table_name| column_name| column_description | 注释| Annotation |
|---|---|---|---|---|
| CS_HKStockPerformance | ID | ID  | | |
| CS_HKStockPerformance | InnerCode | 证券内部编码 | 证券内部编码（InnerCode）：与“证券主表（SecuMain）”中的“证券内部编码（InnerCode）”关联，得到证券的交易代码、简称等。 | Security Internal Code (InnerCode): Associated with the "Security Main Table (SecuMain)" "Security Internal Code (InnerCode)", to obtain the security's trading code, abbreviation, etc. |
| CS_HKStockPerformance | TradingDay | 交易日  | | |
| CS_HKStockPerformance | PrevClosePrice | 昨收盘  | | |
| CS_HKStockPerformance | OpenPrice| 今开盘  | | |
| CS_HKStockPerformance | HighPrice| 最高价  | | |
| CS_HKStockPerformance | LowPrice | 最低价  | | |
| CS_HKStockPerformance | ClosePrice | 收盘价  | | |
| CS_HKStockPerformance | CurrencyUnitCode | 货币代码 | 货币代码(CurrencyUnitCode)与(CT_SystemConst)表中的DM字段关联，令LB=1068 AND DM IN (1000,1100,1420)，得到货币代码的具体描述：1000-美元，1100-港元，1420-人民币元。 | The currency code (CurrencyUnitCode) is associated with the DM field in the (CT_SystemConst) table, with LB=1068 AND DM IN (1000,1100,1420), the specific description of the currency code is: 1000-USD, 1100-HKD, 1420-CNY. |
| CS_HKStockPerformance | TurnoverVolume | 成交量  | | |
| CS_HKStockPerformance | TurnoverValue| 成交金额(元)  | | |
| CS_HKStockPerformance | ChangeOF | 涨跌  | | |
| CS_HKStockPerformance | ChangePCT| 涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCT | 振幅(%) | | |
| CS_HKStockPerformance | TurnoverRate | 换手率(%) | | |
| CS_HKStockPerformance | AvgPrice | 均价  | | |
| CS_HKStockPerformance | TotalMV| 总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMV | 流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueRW| 近一周成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeRW | 近一周成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFRW | 近一周涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTRW| 近一周涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTRW | 近一周振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateRW | 近一周换手率(%) | | |
| CS_HKStockPerformance | AvgPriceRW | 近一周成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceRW| 近一周最高价(元)  | | |
| CS_HKStockPerformance | LowPriceRW | 近一周最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePriceRW| 近一周收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePriceRW | 近一周收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnoverValuePerDayRW| 近一周日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverRatePerDayRW | 近一周日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePerDayRW | 近一周日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPerDayRW| 近一周日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPerDayRW | 近一周日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayRW| 近一周日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPerDayRW | 近一周日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueTW| 本周以来成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeTW | 本周以来成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFTW | 本周以来涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTTW| 本周以来涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTTW | 本周以来振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateTW | 本周以来换手率(%) | | |
| CS_HKStockPerformance | AvgPriceTW | 本周以来成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceTW| 本周以来最高价(元)  | | |
| CS_HKStockPerformance | LowPriceTW | 本周以来最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePriceTW| 本周以来收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePriceTW | 本周以来收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnoverValuePerDayTW| 本周以来日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverRatePerDayTW | 本周以来日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePerDayTW | 本周以来日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPerDayTW| 本周以来日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPerDayTW | 本周以来日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayTW| 本周以来日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPerDayTW | 本周以来日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueRM| 近一月成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeRM | 近一月成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFRM | 近一月涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTRM| 近一月涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTRM | 近一月月振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateRM | 近一月月换手率(%) | | |
| CS_HKStockPerformance | AvgPriceRM | 近一月成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceRM| 近一月最高价(元)  | | |
| CS_HKStockPerformance | LowPriceRM | 近一月最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePriceRM| 近一月收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePriceRM | 近一月收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnoverValuePerDayRM| 近一月日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverRatePerDayRM | 近一月日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePerDayRM | 近一月日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPerDayRM| 近一月日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPerDayRM | 近一月日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayRM| 近一月日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPerDayRM | 近一月日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueTM| 本月以来成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeTM | 本月以来成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFTM | 本月以来涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTTM| 本月以来涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTTM | 本月以来振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateTM | 本月以来换手率(%) | | |
| CS_HKStockPerformance | AvgPriceTM | 本月以来成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceTM| 本月以来最高价(元)  | | |
| CS_HKStockPerformance | LowPriceTM | 本月以来最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePriceTM| 本月以来收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePriceTM | 本月以来收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnoverValuePerDayTM| 本月以来日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverRatePerDayTM | 本月以来日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePerDayTM | 本月以来日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPerDayTM| 本月以来日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPerDayTM | 本月以来日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayTM| 本月以来日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPerDayTM | 本月以来日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueRMThree | 近三个月成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeRMThree| 近三个月成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFRMThree| 近三个月涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTRMThree | 近三个月涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTRMThree| 近三个月振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateRMThree| 近三个月换手率(%) | | |
| CS_HKStockPerformance | AvgPriceRMThree| 近三个月成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceRMThree | 近三个月以来最高价(元)  | | |
| CS_HKStockPerformance | LowPriceRMThree| 近三个月以来最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePRMThree | 近三个月以来收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePRMThree| 近三个月以来收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnValuePDayRMThree | 近三个月日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnRatePDayRMThree| 近三个月日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePDayRMThree| 近三个月日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPDayRMThree | 近三个月日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPDayRMThree| 近三个月日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayRMThree | 近三个月日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPRMThree | 近三个月日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueRMSix | 近六个月成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeRMSix| 近六个月成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFRMSix| 近六个月涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTRMSix | 近六个月涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTRMSix| 近六个月振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateRMSix| 近六个月换手率(%) | | |
| CS_HKStockPerformance | AvgPriceRMSix| 近六个月成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceRMSix | 近六个月以来最高价(元)  | | |
| CS_HKStockPerformance | LowPriceRMSix| 近六个月以来最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePRMSix | 近六个月以来收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePRMSix| 近六个月以来收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnValuePDayRMSix | 近六个月日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnRatePDayRMSix| 近六个月日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePDayRMSix| 近六个月日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPDayRMSix | 近六个月日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPDayRMSix| 近六个月日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayRMSix | 近六个月日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPRMSix | 近六个月日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueRY| 近一年成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeRY | 近一年成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFRY | 近一年涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTRY| 近一年涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTRY | 近一年振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateRY | 近一年换手率(%) | | |
| CS_HKStockPerformance | AvgPriceRY | 近一年成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceRY| 近一年最高价(元)  | | |
| CS_HKStockPerformance | LowPriceRY | 近一年最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePRY| 近一年收盘价最高(元)  | | |
| CS_HKStockPerformance | LowestClosePRY | 近一年收盘价最低(元)  | | |
| CS_HKStockPerformance | TurnoverValuePDayRY| 近一年日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverRatePDayRY | 近一年日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePDayRY | 近一年日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPDayRY| 近一年日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPDayRY | 近一年日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayRY| 近一年日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPRY| 近一年日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | TurnoverValueYTD | 今年以来成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverVolumeYTD| 今年以来成交量(股)  | | |
| CS_HKStockPerformance | ChangeOFYTD| 今年以来涨跌(元)  | | |
| CS_HKStockPerformance | ChangePCTYTD | 今年以来涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTYTD| 今年以来振幅(%) | | |
| CS_HKStockPerformance | TurnoverRateYTD| 今年以来换手率(%) | | |
| CS_HKStockPerformance | AvgPriceYTD| 今年以来成交均价(元)  | | |
| CS_HKStockPerformance | HighPriceYTD | 今年以来最高价(元)  | | |
| CS_HKStockPerformance | LowPriceYTD| 今年以来最低价(元)  | | |
| CS_HKStockPerformance | HighestClosePriceYTD | 今年以来收盘最高价(元)  | | |
| CS_HKStockPerformance | LowestClosePriceYTD| 今年以来收盘最低价(元)  | | |
| CS_HKStockPerformance | TurnoverValuePerDayYTD | 今年以来日均成交金额(元)  | | |
| CS_HKStockPerformance | TurnoverRatePerDayYTD| 今年以来日均换手率(%) | | |
| CS_HKStockPerformance | TurnVolumePDayYTD| 今年以来日均成交量(股)  | | |
| CS_HKStockPerformance | ChangePCTPerDayYTD | 今年以来日均涨跌幅(%) | | |
| CS_HKStockPerformance | RangePCTPerDayYTD| 今年以来日均振幅(%) | | |
| CS_HKStockPerformance | TotalMVPerDayYTD | 今年以来日均总市值(元)  | | |
| CS_HKStockPerformance | NegotiableMVPYTD | 今年以来日均流通市值(不含限售股)(元)  | | |
| CS_HKStockPerformance | HighAdjustedPrice| 上市以来复权最高价(元)  | | |
| CS_HKStockPerformance | HighAdjustedPriceDate| 上市以来复权最高价日期  | | |
| CS_HKStockPerformance | LowAdjustedPrice | 上市以来复权最低价(元)  | | |
| CS_HKStockPerformance | LowAdjustedPriceDate | 上市以来复权最低价日期  | | |
| CS_HKStockPerformance | UpdateTime | 更新时间  | | |
| CS_HKStockPerformance | InsertTime | 发布时间  | | |
| CS_HKStockPerformance | JSID | JSID  | | |
| column_name| column_description | 注释| Annotation |
|---|---|---|---|---|
| ID | ID  | | |
| InnerCode| 证券内部编码 | 证券内部编码（InnerCode）：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。| Security Internal Code (InnerCode): Associated with the "Security Internal Code (InnerCode)" in the "Security Main Table (SecuMain)", to obtain the stock's security code, abbreviation, and other detailed information. |
| TradingDay | 交易日  | | |
| GilCode| 聚源代码  | | |
| SecuMarket | 证券市场  | | |
| IfHighestHPriceRW| 是否创近一周的新高 | 指定日期最高价是否大于指定日期最近N天最高价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the highest price on the specified date is greater than the highest price of the recent N days on the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.|
| IfHighestHPriceRM| 是否创近一月的新高  | | |
| IfHighestHPriceRMThree | 是否创近一季度的新高  | | |
| IfHighestHPriceRMSix | 是否创近半年的新高  | | |
| IfHighestHPriceRY| 是否创近一年的新高  | | |
| IfHighestHPriceSL| 是否创上市以来的新高  | | |
| IfHighestCPriceRW| 是否创近一周的新高收盘价 | 指定日期收盘价是否大于指定日期最近N天收盘价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the closing price on the specified date is higher than the closing price of the nearest N days on the specified date, return 1 if yes, and 2 if no. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing. |
| IfHighestCPriceRM| 是否创近一月的新高收盘价  | | |
| IfHighestCPriceRMThree | 是否创近一季度的新高收盘价  | | |
| IfHighestCPriceRMSix | 是否创近半年的新高收盘价  | | |
| IfHighestCPriceRY| 是否创近一年的新高收盘价  | | |
| IfHighestCPriceSL| 是否创上市以来的新高收盘价  | | |
| IfHighestTVolumeRW | 是否创近一周的新高成交量  | | |
| IfHighestTVolumeRM | 是否创近一月的新高成交量 | 指定日期成交量是否大于指定日期最近N天成交量，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the trading volume on the specified date is greater than that of the nearest N days before the specified date, return 1 if yes, otherwise return 2. N is for the past 1 week, 1 month, 3 months, half a year, 1 year, and since the listing. |
| IfHighestTVRMThree | 是否创近一季度的新高成交量  | | |
| IfHighestTVolumeRMSix| 是否创近半年的新高成交量  | | |
| IfHighestTVolumeRY | 是否创近一年的新高成交量  | | |
| IfHighestTVolumeSL | 是否创上市以来的新高成交量  | | |
| IfHighestTValueRW| 是否创近一周的新高成交金额 | 指定日期成交金额是否大于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。 | Whether the transaction amount on the specified date is greater than that of the nearest N days before the specified date, return 1 if yes, otherwise return 2. N is for the past 1 week, 1 month, 3 months, half a year, 1 year, and since the listing. |
| IfHighestTValueRM| 是否创近一月的新高成交金额  | | |
| IfHighestTValueRMThree | 是否创近一季度的新高成交金额  | | |
| IfHighestTValueRMSix | 是否创近半年的新高成交金额  | | |
| IfHighestTValueRY| 是否创近一年的新高成交金额  | | |
| IfHighestTValueSL| 是否创上市以来的新高成交金额  | | |
| HighestHPTimesSL | 最新交易日创历史新高次数 | 指定日期最近N天内大于指定日期之前的历史交易日最高价的次数。 N: 最新交易日、近1周、近1月、近3月、近半年、近1年 | The number of times the closing price in the last N days is higher than the highest historical trading price before the specified date. N: the most recent trading day, the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year. |
| HighestHPTimesRW | 最近一周创历史新高次数  | | |
| HighestHPTimesRM | 最近一月创历史新高次数  | | |
| HighestHPTimesRMThree| 最近一季度创历史新高次数  | | |
| HighestHPTimesRMSix| 最近半年创历史新高次数  | | |
| HighestHPTimesRY | 最近一年创历史新高次数  | | |
| IfLowestLPriceRW | 是否创近一周的新低 | 指定日期最低价是否小于指定日期最近N天最低价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the lowest price on the specified date is less than the lowest price of the nearest N days on the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.|
| IfLowestLPriceRM | 是否创近一个月的新低  | | |
| IfLowestLPRMThree| 是否创近一季度的新低  | | |
| IfLowestLPriceRMSix| 是否创近半年的新低  | | |
| IfLowestLPriceRY | 是否创近一年的新低  | | |
| IfLowestLPriceSL | 是否创上市以来的新低  | | |
| IfLowestClosePriceRW | 是否创近一周的新低收盘价 | 指定日期收盘价是否小于指定日期最近N天收盘价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the closing price on the specified date is less than the closing price of the nearest N days from the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.|
| IfLowestClosePriceRM | 是否创近一月的新低收盘价  | | |
| IfLowestCPriceRMThree| 是否创近一季度的新低收盘价  | | |
| IfLowestCPriceRMSix| 是否创近半年的新低收盘价  | | |
| IfLowestClosePriceRY | 是否创近一年的新低收盘价  | | |
| IfLowestClosePriceSL | 是否创上市以来的新低收盘价  | | |
| IfLowestTVolumeRW| 是否创近一周的新低成交量 | 指定日期成交量是否小于指定日期最近N天成交量，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the trading volume on the specified date is less than the trading volume of the nearest N days on the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.|
| IfLowestTVolumeRM| 是否创近一月的新低成交量  | | |
| IfLowestTVolumeRMThree | 是否创近一季度的新低成交量  | | |
| IfLowestVolumeRMSix| 是否创近半年的新低成交量  | | |
| IfLowestTVolumeRY| 是否创近一年的新低成交量  | | |
| IfLowestTVolumeSL| 是否创上市以来的新低成交量  | | |
| IfLowestTValueRW | 是否创近一周的新低成交金额 | 指定日期成交金额是否小于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。 | Whether the transaction amount on the specified date is less than the transaction amount of the nearest N days from the specified date, return 1 if yes, otherwise return 2. N is: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing. |
| IfLowestTValueRM | 是否创近一月的新低成交金额  | | |
| IfLowestTValueRMThree| 是否创近一季度的新低成交金额  | | |
| IfLowestTValueRMSix| 是否创近半年的新低成交金额  | | |
| IfLowestTValueRY | 是否创近一年的新低成交金额  | | |
| IfLowestTValueSL | 是否创上市以来的新低成交金额  | | |
| LowestLowPriceTimesSL| 最新交易日创历史新低次数 | 指定日期最近N天内小于指定日期之前的历史交易日最低价的次数， N: 最新交易日、近1周、近1月、近3月、近半年、近1年。 | The number of times the closing price in the last N days is lower than the lowest historical trading price before the specified date, where N is the most recent trading day, the past 1 week, the past 1 month, the past 3 months, the past half year, and the past 1 year. |
| LowestLowPriceTimesRW| 最近一周创历史新低次数  | | |
| LowestLowPriceTimesRM| 最近一个月创历史新低次数  | | |
| LowestLPTimesRMThree | 最近一季度创历史新低次数  | | |
| LowestLPTimesRMSix | 最近半年创历史新低次数  | | |
| LowestLPTimesRY| 最近一年创历史新低次数  | | |
| RisingUpDays | 连涨天数 | 统计个股在指定交易日期往前推连续上涨的天数。| Count the number of consecutive rising days for a specific stock leading up to a given trading date. |
| FallingDownDays| 连跌天数 | 统计个股在指定交易日期往前推连续下跌的天数。| Count the number of consecutive losing days for a specific stock leading up to a given trading date. |
| VolumeRisingUpDays | 连续放量天数 | 统计个股在指定交易日期往前推成交量连续上升的天数。| Count the number of consecutive days with increasing trading volume for a specific stock leading up to a given trading date. |
| VolumeFallingDownDays| 连续缩量天数 | 统计个股在指定交易日期往前推成交量连续下降的天数。| Count the number of consecutive days with decreasing trading volume for a specific stock leading up to a given trading date. |
| BreakingMAverageFive | 向上向下有效突破5日均线| 向上有效突破： 最近N天的收盘价>n日均线，且距今N+1天的收盘价<=n日均线。 向下有效突破： 最近N天的收盘价<n日均线，且距今N+1天的收盘价>=n日均线。 1-向上有效突破, 2-向下有效突破, 0-其他。 均线计算：n日均线=n日收盘价之和/n。 向上向下有效突破字段按照N=3 计算。 | An upward effective breakthrough: The closing price of the recent N days is greater than the N-day moving average, and the closing price of N+1 days ago is less than or equal to the N-day moving average. A downward effective breakthrough: The closing price of the recent N days is less than the N-day moving average, and the closing price of N+1 days ago is greater than or equal to the N-day moving average. 1-Upward effective breakthrough, 2-Downward effective breakthrough, 0-Other. Moving average calculation: N-day moving average = Sum of N-day closing prices / n. The field for upward and downward effective breakthrough is calculated with N=3. |
| BreakingMAverageTen| 向上向下有效突破10日均线  | | |
| BreakingMAverageTwenty | 向上向下有效突破20日均线  | | |
| BreakingMAverageSixty| 向上向下有效突破60日均线  | | |
| RaisingLimitInNDays| N天M板 | N天： 指定交易日往前取到连续三个非涨停的交易日的最后一个交易日的后一个交易日且该交易日涨停作为起始日期，指定交易日作为截至日期，N天即为起始日期到截至日期区间内的天数。 M板：上述N天内的涨停数。| N days: The starting date is the day after the last trading day of the consecutive three non-limit-up trading days before the specified trading day, and the trading day with a limit-up is chosen as the starting date, with the specified trading day as the ending date. N days refer to the number of days from the starting date to the ending date. M board: The number of limit-up days within the aforementioned N days. |
| MAverageArrangements | 均线多空头排列看涨看跌 | 看涨：5日均线>10日均线>20日均线>60日均线，看涨返回1。 看跌：5日均线<10日均线<20日均线<60日均线，看跌返回2。 | Bullish: 5-day MA > 10-day MA > 20-day MA > 60-day MA, return 1 for bullish. Bearish: 5-day MA < 10-day MA < 20-day MA < 60-day MA, return 2 for bearish.|
| InsertTime | 发布时间  | | |
| UpdateTime | 更新时间  | | |
| JSID | JSID  | | |
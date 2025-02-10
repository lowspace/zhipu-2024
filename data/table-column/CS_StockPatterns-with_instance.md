| table_name | column_name| column_description | 注释| Annotation | 数据示例|
|---|---|---|---|---|---|
| CS_StockPatterns | ID | ID | || 738549336899|
| CS_StockPatterns | InnerCode| 证券内部编码 | 证券内部编码（InnerCode）：与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。| Security Internal Code (InnerCode): Associated with the "Security Internal Code (InnerCode)" in the "Security Main Table (SecuMain)", to obtain the stock's security code, abbreviation, and other detailed information. | 352827|
| CS_StockPatterns | TradingDay | 交易日 | || 2021-12-23 12:00:00.000 |
| CS_StockPatterns | GilCode| 聚源代码 | || SEC000007K8R|
| CS_StockPatterns | SecuMarket | 证券市场 | || 83|
| CS_StockPatterns | IfHighestHPriceRW| 是否创近一周的新高 | 指定日期最高价是否大于指定日期最近N天最高价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the highest price on the specified date is greater than the highest price of the recent N days on the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.| 1 |
| CS_StockPatterns | IfHighestHPriceRM| 是否创近一月的新高 | || 1 |
| CS_StockPatterns | IfHighestHPriceRMThree | 是否创近一季度的新高 | || 1 |
| CS_StockPatterns | IfHighestHPriceRMSix | 是否创近半年的新高 | || 1 |
| CS_StockPatterns | IfHighestHPriceRY| 是否创近一年的新高 | || 1 |
| CS_StockPatterns | IfHighestHPriceSL| 是否创上市以来的新高 | || 1 |
| CS_StockPatterns | IfHighestCPriceRW| 是否创近一周的新高收盘价 | 指定日期收盘价是否大于指定日期最近N天收盘价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the closing price on the specified date is higher than the closing price of the nearest N days on the specified date, return 1 if yes, and 2 if no. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing. | 1 |
| CS_StockPatterns | IfHighestCPriceRM| 是否创近一月的新高收盘价 | || 1 |
| CS_StockPatterns | IfHighestCPriceRMThree | 是否创近一季度的新高收盘价 | || 1 |
| CS_StockPatterns | IfHighestCPriceRMSix | 是否创近半年的新高收盘价 | || 1 |
| CS_StockPatterns | IfHighestCPriceRY| 是否创近一年的新高收盘价 | || 1 |
| CS_StockPatterns | IfHighestCPriceSL| 是否创上市以来的新高收盘价 | || 1 |
| CS_StockPatterns | IfHighestTVolumeRW | 是否创近一周的新高成交量 | || 1 |
| CS_StockPatterns | IfHighestTVolumeRM | 是否创近一月的新高成交量 | 指定日期成交量是否大于指定日期最近N天成交量，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the trading volume on the specified date is greater than that of the nearest N days before the specified date, return 1 if yes, otherwise return 2. N is for the past 1 week, 1 month, 3 months, half a year, 1 year, and since the listing. | 1 |
| CS_StockPatterns | IfHighestTVRMThree | 是否创近一季度的新高成交量 | || 1 |
| CS_StockPatterns | IfHighestTVolumeRMSix| 是否创近半年的新高成交量 | || 1 |
| CS_StockPatterns | IfHighestTVolumeRY | 是否创近一年的新高成交量 | || 1 |
| CS_StockPatterns | IfHighestTVolumeSL | 是否创上市以来的新高成交量 | || 1 |
| CS_StockPatterns | IfHighestTValueRW| 是否创近一周的新高成交金额 | 指定日期成交金额是否大于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。 | Whether the transaction amount on the specified date is greater than that of the nearest N days before the specified date, return 1 if yes, otherwise return 2. N is for the past 1 week, 1 month, 3 months, half a year, 1 year, and since the listing. | 1 |
| CS_StockPatterns | IfHighestTValueRM| 是否创近一月的新高成交金额 | || 1 |
| CS_StockPatterns | IfHighestTValueRMThree | 是否创近一季度的新高成交金额 | || 1 |
| CS_StockPatterns | IfHighestTValueRMSix | 是否创近半年的新高成交金额 | || 1 |
| CS_StockPatterns | IfHighestTValueRY| 是否创近一年的新高成交金额 | || 1 |
| CS_StockPatterns | IfHighestTValueSL| 是否创上市以来的新高成交金额 | || 1 |
| CS_StockPatterns | HighestHPTimesSL | 最新交易日创历史新高次数 | 指定日期最近N天内大于指定日期之前的历史交易日最高价的次数。 N: 最新交易日、近1周、近1月、近3月、近半年、近1年 | The number of times the closing price in the last N days is higher than the highest historical trading price before the specified date. N: the most recent trading day, the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year. | 0 |
| CS_StockPatterns | HighestHPTimesRW | 最近一周创历史新高次数 | || 1 |
| CS_StockPatterns | HighestHPTimesRM | 最近一月创历史新高次数 | || 1 |
| CS_StockPatterns | HighestHPTimesRMThree| 最近一季度创历史新高次数 | || 1 |
| CS_StockPatterns | HighestHPTimesRMSix| 最近半年创历史新高次数 | || 1 |
| CS_StockPatterns | HighestHPTimesRY | 最近一年创历史新高次数 | || 1 |
| CS_StockPatterns | IfLowestLPriceRW | 是否创近一周的新低 | 指定日期最低价是否小于指定日期最近N天最低价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the lowest price on the specified date is less than the lowest price of the nearest N days on the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.| 1 |
| CS_StockPatterns | IfLowestLPriceRM | 是否创近一个月的新低 | || 1 |
| CS_StockPatterns | IfLowestLPRMThree| 是否创近一季度的新低 | || 1 |
| CS_StockPatterns | IfLowestLPriceRMSix| 是否创近半年的新低 | || 1 |
| CS_StockPatterns | IfLowestLPriceRY | 是否创近一年的新低 | || 1 |
| CS_StockPatterns | IfLowestLPriceSL | 是否创上市以来的新低 | || 1 |
| CS_StockPatterns | IfLowestClosePriceRW | 是否创近一周的新低收盘价 | 指定日期收盘价是否小于指定日期最近N天收盘价，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the closing price on the specified date is less than the closing price of the nearest N days from the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.| 1 |
| CS_StockPatterns | IfLowestClosePriceRM | 是否创近一月的新低收盘价 | || 1 |
| CS_StockPatterns | IfLowestCPriceRMThree| 是否创近一季度的新低收盘价 | || 1 |
| CS_StockPatterns | IfLowestCPriceRMSix| 是否创近半年的新低收盘价 | || 1 |
| CS_StockPatterns | IfLowestClosePriceRY | 是否创近一年的新低收盘价 | || 1 |
| CS_StockPatterns | IfLowestClosePriceSL | 是否创上市以来的新低收盘价 | || 1 |
| CS_StockPatterns | IfLowestTVolumeRW| 是否创近一周的新低成交量 | 指定日期成交量是否小于指定日期最近N天成交量，是返回1， 否返回2。 N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。| Whether the trading volume on the specified date is less than the trading volume of the nearest N days on the specified date, return 1 if yes, otherwise return 2. N is respectively: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing.| 1 |
| CS_StockPatterns | IfLowestTVolumeRM| 是否创近一月的新低成交量 | || 1 |
| CS_StockPatterns | IfLowestTVolumeRMThree | 是否创近一季度的新低成交量 | || 1 |
| CS_StockPatterns | IfLowestVolumeRMSix| 是否创近半年的新低成交量 | || 1 |
| CS_StockPatterns | IfLowestTVolumeRY| 是否创近一年的新低成交量 | || 1 |
| CS_StockPatterns | IfLowestTVolumeSL| 是否创上市以来的新低成交量 | || 1 |
| CS_StockPatterns | IfLowestTValueRW | 是否创近一周的新低成交金额 | 指定日期成交金额是否小于指定日期最近N天成交金额，是返回1， 否返回2。N分别为：近1周、近1月、近3月、近半年、近1年、上市以来。 | Whether the transaction amount on the specified date is less than the transaction amount of the nearest N days from the specified date, return 1 if yes, otherwise return 2. N is: the past 1 week, the past 1 month, the past 3 months, the past half year, the past 1 year, and since the listing. | 1 |
| CS_StockPatterns | IfLowestTValueRM | 是否创近一月的新低成交金额 | || 1 |
| CS_StockPatterns | IfLowestTValueRMThree| 是否创近一季度的新低成交金额 | || 1 |
| CS_StockPatterns | IfLowestTValueRMSix| 是否创近半年的新低成交金额 | || 1 |
| CS_StockPatterns | IfLowestTValueRY | 是否创近一年的新低成交金额 | || 1 |
| CS_StockPatterns | IfLowestTValueSL | 是否创上市以来的新低成交金额 | || 1 |
| CS_StockPatterns | LowestLowPriceTimesSL| 最新交易日创历史新低次数 | 指定日期最近N天内小于指定日期之前的历史交易日最低价的次数， N: 最新交易日、近1周、近1月、近3月、近半年、近1年。 | The number of times the closing price in the last N days is lower than the lowest historical trading price before the specified date, where N is the most recent trading day, the past 1 week, the past 1 month, the past 3 months, the past half year, and the past 1 year. | 0 |
| CS_StockPatterns | LowestLowPriceTimesRW| 最近一周创历史新低次数 | || 1 |
| CS_StockPatterns | LowestLowPriceTimesRM| 最近一个月创历史新低次数 | || 1 |
| CS_StockPatterns | LowestLPTimesRMThree | 最近一季度创历史新低次数 | || 1 |
| CS_StockPatterns | LowestLPTimesRMSix | 最近半年创历史新低次数 | || 1 |
| CS_StockPatterns | LowestLPTimesRY| 最近一年创历史新低次数 | || 1 |
| CS_StockPatterns | RisingUpDays | 连涨天数 | 统计个股在指定交易日期往前推连续上涨的天数。| Count the number of consecutive rising days for a specific stock leading up to a given trading date. | 0 |
| CS_StockPatterns | FallingDownDays| 连跌天数 | 统计个股在指定交易日期往前推连续下跌的天数。| Count the number of consecutive losing days for a specific stock leading up to a given trading date. | 0 |
| CS_StockPatterns | VolumeRisingUpDays | 连续放量天数 | 统计个股在指定交易日期往前推成交量连续上升的天数。| Count the number of consecutive days with increasing trading volume for a specific stock leading up to a given trading date. | 0 |
| CS_StockPatterns | VolumeFallingDownDays| 连续缩量天数 | 统计个股在指定交易日期往前推成交量连续下降的天数。| Count the number of consecutive days with decreasing trading volume for a specific stock leading up to a given trading date. | 0 |
| CS_StockPatterns | BreakingMAverageFive | 向上向下有效突破5日均线| 向上有效突破： 最近N天的收盘价>n日均线，且距今N+1天的收盘价<=n日均线。 向下有效突破： 最近N天的收盘价<n日均线，且距今N+1天的收盘价>=n日均线。 1-向上有效突破, 2-向下有效突破, 0-其他。 均线计算：n日均线=n日收盘价之和/n。 向上向下有效突破字段按照N=3 计算。 | An upward effective breakthrough: The closing price of the recent N days is greater than the N-day moving average, and the closing price of N+1 days ago is less than or equal to the N-day moving average. A downward effective breakthrough: The closing price of the recent N days is less than the N-day moving average, and the closing price of N+1 days ago is greater than or equal to the N-day moving average. 1-Upward effective breakthrough, 2-Downward effective breakthrough, 0-Other. Moving average calculation: N-day moving average = Sum of N-day closing prices / n. The field for upward and downward effective breakthrough is calculated with N=3. | 0 |
| CS_StockPatterns | BreakingMAverageTen| 向上向下有效突破10日均线 | || 0 |
| CS_StockPatterns | BreakingMAverageTwenty | 向上向下有效突破20日均线 | || 0 |
| CS_StockPatterns | BreakingMAverageSixty| 向上向下有效突破60日均线 | || 0 |
| CS_StockPatterns | RaisingLimitInNDays| N天M板 | N天： 指定交易日往前取到连续三个非涨停的交易日的最后一个交易日的后一个交易日且该交易日涨停作为起始日期，指定交易日作为截至日期，N天即为起始日期到截至日期区间内的天数。 M板：上述N天内的涨停数。| N days: The starting date is the day after the last trading day of the consecutive three non-limit-up trading days before the specified trading day, and the trading day with a limit-up is chosen as the starting date, with the specified trading day as the ending date. N days refer to the number of days from the starting date to the ending date. M board: The number of limit-up days within the aforementioned N days. | null|
| CS_StockPatterns | MAverageArrangements | 均线多空头排列看涨看跌 | 看涨：5日均线>10日均线>20日均线>60日均线，看涨返回1。 看跌：5日均线<10日均线<20日均线<60日均线，看跌返回2。 | Bullish: 5-day MA > 10-day MA > 20-day MA > 60-day MA, return 1 for bullish. Bearish: 5-day MA < 10-day MA < 20-day MA < 60-day MA, return 2 for bearish.| 0 |
| CS_StockPatterns | InsertTime | 发布时间 | || 2023-05-27 01:00:04.040 |
| CS_StockPatterns | UpdateTime | 更新时间 | || 2023-05-27 01:00:04.040 |
| CS_StockPatterns | JSID | JSID | || 738550164953|
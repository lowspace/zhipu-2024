| table_name | column_name| column_description | 注释 | Annotation|
|---|---|---|---|---|
| CS_StockCapFlowIndex | ID | ID || |
| CS_StockCapFlowIndex | InnerCode| 证券内部编码 | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。 | The internal code (InnerCode) of securities is associated with the "InnerCode" in the "SecuMain" table, obtaining other detailed information such as the security code and abbreviation of the stock. |
| CS_StockCapFlowIndex | TradingDay | 交易日期 || |
| CS_StockCapFlowIndex | TimeRange| 成交时间区间 | 成交时间区间(TimeRange)，该字段固定以下常量：1-全盘，2-开盘，3-尾盘| Transaction Time Range (TimeRange), this field is fixed with the following constants: 1-Whole Disk, 2-Opening, 3-End of Disk|
| CS_StockCapFlowIndex | SmallBuyValue| 小单流入额(元) | 小单：单笔成交量区间为[0，2w)或成交金额区间为[0，4w) | Xiao Dan: The volume per transaction ranges from [0, 20,000) or the transaction amount ranges from [0, 40,000). |
| CS_StockCapFlowIndex | SmallSellValue | 小单流出额(元) || |
| CS_StockCapFlowIndex | SmallBuyVolume | 小单流入量(股) || |
| CS_StockCapFlowIndex | SmallSellVolume| 小单流出量(股) || |
| CS_StockCapFlowIndex | SmallBuyNum| 小单流入笔数 || |
| CS_StockCapFlowIndex | SmallSellNum | 小单流出笔数 || |
| CS_StockCapFlowIndex | SmallNetBuyValue | 小单净流入额(元) || |
| CS_StockCapFlowIndex | SmallNetBuyVolume| 小单净流入量(股) || |
| CS_StockCapFlowIndex | SmallBValueRatio | 小单买入率(额) || |
| CS_StockCapFlowIndex | SmallSValueRatio | 小单卖出率(额) || |
| CS_StockCapFlowIndex | SmallBVolumeRatio| 小单买入率(量) || |
| CS_StockCapFlowIndex | SmallSVolumeRatio| 小单卖出率(量) || |
| CS_StockCapFlowIndex | SmallNBValueRatio| 小单净买入率(额) || |
| CS_StockCapFlowIndex | SmallNBVFloatMVRatio | 小单净买入额流通市值比 || |
| CS_StockCapFlowIndex | SmallNBVolumeRatio | 小单净买入率(量) || |
| CS_StockCapFlowIndex | SmallNBVFloatSRatio| 小单净买入量流通股本比 || |
| CS_StockCapFlowIndex | SmallActBuyValue | 小单主动流入额(元) || |
| CS_StockCapFlowIndex | SmallActSellValue| 小单主动流出额(元) || |
| CS_StockCapFlowIndex | SmallActBuyVolume| 小单主动流入量(股) || |
| CS_StockCapFlowIndex | SmallActSellVolume | 小单主动流出量(股) || |
| CS_StockCapFlowIndex | SmallActBuyNum | 小单主动流入笔数 || |
| CS_StockCapFlowIndex | SmallActSellNum| 小单主动流出笔数 || |
| CS_StockCapFlowIndex | SmallNetActBuyValue| 小单净主动流入额(元) || |
| CS_StockCapFlowIndex | SmallNetActBuyVolume | 小单净主动流入量(股) || |
| CS_StockCapFlowIndex | SmallABValueRatio| 小单主动买入率(额) || |
| CS_StockCapFlowIndex | SmallASValueRatio| 小单主动卖出率(额) || |
| CS_StockCapFlowIndex | SmallABVolumeRatio | 小单主动买入率(量) || |
| CS_StockCapFlowIndex | SmallASVolumeRatio | 小单主动卖出率(量) || |
| CS_StockCapFlowIndex | SmallNABValueRatio | 小单净主动买入率(额) || |
| CS_StockCapFlowIndex | SmallNABVFloatMVRatio| 小单净主动买入额流通市值比 || |
| CS_StockCapFlowIndex | SmallNABVolumeRatio| 小单净主动买入率(量) || |
| CS_StockCapFlowIndex | SmallNABVFloatSRatio | 小单净主动买入量流通股本比 || |
| CS_StockCapFlowIndex | MediumBuyValue | 中单流入额(元) | 中单：单笔成交量区间为[2w，10w)或成交金额区间为[4w，20w) | The single transaction volume range is [20,000, 100,000) or the transaction amount range is [40,000, 200,000) |
| CS_StockCapFlowIndex | MediumSellValue| 中单流出额(元) || |
| CS_StockCapFlowIndex | MediumBuyVolume| 中单流入量(股) || |
| CS_StockCapFlowIndex | MediumSellVolume | 中单流出量(股) || |
| CS_StockCapFlowIndex | MediumBuyNum | 中单流入笔数 || |
| CS_StockCapFlowIndex | MediumSellNum| 中单流出笔数 || |
| CS_StockCapFlowIndex | MediumNetBuyValue| 中单净流入额(元) || |
| CS_StockCapFlowIndex | MediumNetBuyVolume | 中单净流入量(股) || |
| CS_StockCapFlowIndex | MediumBValueRatio| 中单买入率(额) || |
| CS_StockCapFlowIndex | MediumSValueRatio| 中单卖出率(额) || |
| CS_StockCapFlowIndex | MediumBVolumeRatio | 中单买入率(量) || |
| CS_StockCapFlowIndex | MediumSVolumeRatio | 中单卖出率(量) || |
| CS_StockCapFlowIndex | MediumNBValueRatio | 中单净买入率(额) || |
| CS_StockCapFlowIndex | MediumNBVFloatMVRatio| 中单净买入额流通市值比 || |
| CS_StockCapFlowIndex | MediumNBVolumeRatio| 中单净买入率(量) || |
| CS_StockCapFlowIndex | MediumNBVFloatSRatio | 中单净买入量流通股本比 || |
| CS_StockCapFlowIndex | MediumActBuyValue| 中单主动流入额(元) || |
| CS_StockCapFlowIndex | MediumActSellValue | 中单主动流出额(元) || |
| CS_StockCapFlowIndex | MediumActBuyVolume | 中单主动流入量(股) || |
| CS_StockCapFlowIndex | MediumActSellVolume| 中单主动流出量(股) || |
| CS_StockCapFlowIndex | MediumActBuyNum| 中单主动流入笔数 || |
| CS_StockCapFlowIndex | MediumActSellNum | 中单主动流出笔数 || |
| CS_StockCapFlowIndex | MediumNetActBuyValue | 中单净主动流入额(元) || |
| CS_StockCapFlowIndex | MediumNetActBuyVolume| 中单净主动流入量(股) || |
| CS_StockCapFlowIndex | MediumABValueRatio | 中单主动买入率(额) || |
| CS_StockCapFlowIndex | MediumASValueRatio | 中单主动卖出率(额) || |
| CS_StockCapFlowIndex | MediumABVolumeRatio| 中单主动买入率(量) || |
| CS_StockCapFlowIndex | MediumASVolumeRatio| 中单主动卖出率(量) || |
| CS_StockCapFlowIndex | MediumNABValueRatio| 中单净主动买入率(额) || |
| CS_StockCapFlowIndex | MediumNABVFloatMVRatio | 中单净主动买入额流通市值比 || |
| CS_StockCapFlowIndex | MediumNABVolumeRatio | 中单净主动买入率(量) || |
| CS_StockCapFlowIndex | MediumNABVFloatSRatio| 中单净主动买入量流通股本比 || |
| CS_StockCapFlowIndex | LargeBuyValue| 大单流入额(元) | 大单：单笔成交量区间为[10w，50w)或成交金额区间为[20w，100w)| Large order: The volume per transaction is in the range of [100,000, 500,000) or the transaction amount is in the range of [200,000, 1,000,000) |
| CS_StockCapFlowIndex | LargeSellValue | 大单流出额(元) || |
| CS_StockCapFlowIndex | LargeBuyVolume | 大单流入量(股) || |
| CS_StockCapFlowIndex | LargeSellVolume| 大单流出量(股) || |
| CS_StockCapFlowIndex | LargeBuyNum| 大单流入笔数 || |
| CS_StockCapFlowIndex | LargeSellNum | 大单流出笔数 || |
| CS_StockCapFlowIndex | LargeNetBuyValue | 大单净流入额(元) || |
| CS_StockCapFlowIndex | LargeNetBuyVolume| 大单净流入量(股) || |
| CS_StockCapFlowIndex | LargeBValueRatio | 大单买入率(额) || |
| CS_StockCapFlowIndex | LargeSValueRatio | 大单卖出率(额) || |
| CS_StockCapFlowIndex | LargeBVolumeRatio| 大单买入率(量) || |
| CS_StockCapFlowIndex | LargeSVolumeRatio| 大单卖出率(量) || |
| CS_StockCapFlowIndex | LargeNBValueRatio| 大单净买入率(额) || |
| CS_StockCapFlowIndex | LargeNBVFloatMVRatio | 大单净买入额流通市值比 || |
| CS_StockCapFlowIndex | LargeNBVolumeRatio | 大单净买入率(量) || |
| CS_StockCapFlowIndex | LargeNBVFloatSRatio| 大单净买入量流通股本比 || |
| CS_StockCapFlowIndex | LargeActBuyValue | 大单主动流入额(元) || |
| CS_StockCapFlowIndex | LargeActSellValue| 大单主动流出额(元) || |
| CS_StockCapFlowIndex | LargeActBuyVolume| 大单主动流入量(股) || |
| CS_StockCapFlowIndex | LargeActSellVolume | 大单主动流出量(股) || |
| CS_StockCapFlowIndex | LargeActBuyNum | 大单主动流入笔数 || |
| CS_StockCapFlowIndex | LargeActSellNum| 大单主动流出笔数 || |
| CS_StockCapFlowIndex | LargeNetActBuyValue| 大单净主动流入额(元) || |
| CS_StockCapFlowIndex | LargeNetActBuyVolume | 大单净主动流入量(股) || |
| CS_StockCapFlowIndex | LargeABValueRatio| 大单主动买入率(额) || |
| CS_StockCapFlowIndex | LargeASValueRatio| 大单主动卖出率(额) || |
| CS_StockCapFlowIndex | LargeABVolumeRatio | 大单主动买入率(量) || |
| CS_StockCapFlowIndex | LargeASVolumeRatio | 大单主动卖出率(量) || |
| CS_StockCapFlowIndex | LargeNABValueRatio | 大单净主动买入率(额) || |
| CS_StockCapFlowIndex | LargeNABVFloatMVRatio| 大单净主动买入额流通市值比 || |
| CS_StockCapFlowIndex | LargeNABVolumeRatio| 大单净主动买入率(量) || |
| CS_StockCapFlowIndex | LargeNABVFloatSRatio | 大单净主动买入量流通股本比 || |
| CS_StockCapFlowIndex | HugeBuyValue | 超大单流入额(元) | 超大单：单笔成交量区间为[50w，+∞)或成交金额区间为[100w，+∞)| Super large order: The volume per transaction is in the range of [500,000, +∞) or the transaction amount is in the range of [1,000,000, +∞).|
| CS_StockCapFlowIndex | HugeSellValue| 超大单流出额(元) || |
| CS_StockCapFlowIndex | HugeBuyVolume| 超大单流入量(股) || |
| CS_StockCapFlowIndex | HugeSellVolume | 超大单流出量(股) || |
| CS_StockCapFlowIndex | HugeBuyNum | 超大单流入笔数 || |
| CS_StockCapFlowIndex | HugeSellNum| 超大单流出笔数 || |
| CS_StockCapFlowIndex | HugeNetBuyValue| 超大单净流入额(元) || |
| CS_StockCapFlowIndex | HugeNetBuyVolume | 超大单净流入量(股) || |
| CS_StockCapFlowIndex | HugeBValueRatio| 超大单买入率(额) || |
| CS_StockCapFlowIndex | HugeSValueRatio| 超大单卖出率(额) || |
| CS_StockCapFlowIndex | HugeBVolumeRatio | 超大单买入率(量) || |
| CS_StockCapFlowIndex | HugeSVolumeRatio | 超大单卖出率(量) || |
| CS_StockCapFlowIndex | HugeNBValueRatio | 超大单净买入率(额) || |
| CS_StockCapFlowIndex | HugeNBVFloatMVRatio| 超大单净买入额流通市值比 || |
| CS_StockCapFlowIndex | HugeNBVolumeRatio| 超大单净买入率(量) || |
| CS_StockCapFlowIndex | HugeNBVFloatSRatio | 超大单净买入量流通股本比 || |
| CS_StockCapFlowIndex | HugeActBuyValue| 超大单主动流入额(元) || |
| CS_StockCapFlowIndex | HugeActSellValue | 超大单主动流出额(元) || |
| CS_StockCapFlowIndex | HugeActBuyVolume | 超大单主动流入量(股) || |
| CS_StockCapFlowIndex | HugeActSellVolume| 超大单主动流出量(股) || |
| CS_StockCapFlowIndex | HugeActBuyNum| 超大单主动流入笔数 || |
| CS_StockCapFlowIndex | HugeActSellNum | 超大单主动流出笔数 || |
| CS_StockCapFlowIndex | HugeNetActBuyValue | 超大单净主动流入额(元) || |
| CS_StockCapFlowIndex | HugeNetActBuyVolume| 超大单净主动流入量(股) || |
| CS_StockCapFlowIndex | HugeABValueRatio | 超大单主动买入率(额) || |
| CS_StockCapFlowIndex | HugeASValueRatio | 超大单主动卖出率(额) || |
| CS_StockCapFlowIndex | HugeABVolumeRatio| 超大单主动买入率(量) || |
| CS_StockCapFlowIndex | HugeASVolumeRatio| 超大单主动卖出率(量) || |
| CS_StockCapFlowIndex | HugeNABValueRatio| 超大单净主动买入率(额) || |
| CS_StockCapFlowIndex | HugeNABVFloatMVRatio | 超大单净主动买入额流通市值比 || |
| CS_StockCapFlowIndex | HugeNABVolumeRatio | 超大单净主动买入率(量) || |
| CS_StockCapFlowIndex | HugeNABVFloatSRatio| 超大单净主动买入量流通股本比 || |
| CS_StockCapFlowIndex | MainBuyValue | 主力流入额(元) | 主力=大单+超大单 | Main force = large orders + super large orders|
| CS_StockCapFlowIndex | MainSellValue| 主力流出额(元) || |
| CS_StockCapFlowIndex | MainBuyVolume| 主力流入量(股) || |
| CS_StockCapFlowIndex | MainSellVolume | 主力流出量(股) || |
| CS_StockCapFlowIndex | MainBuyNum | 主力流入笔数 || |
| CS_StockCapFlowIndex | MainSellNum| 主力流出笔数 || |
| CS_StockCapFlowIndex | MainNetBuyValue| 主力净流入额(元)|| |
| CS_StockCapFlowIndex | MainNetBuyVolume | 主力净流入量(股)|| |
| CS_StockCapFlowIndex | MainBValueRatio| 主力买入率(额) || |
| CS_StockCapFlowIndex | MainSValueRatio| 主力卖出率(额) || |
| CS_StockCapFlowIndex | MainBVolumeRatio | 主力买入率(量) || |
| CS_StockCapFlowIndex | MainSVolumeRatio | 主力卖出率(量) || |
| CS_StockCapFlowIndex | MainNBValueRatio | 主力净买入率(额) || |
| CS_StockCapFlowIndex | MainNBVFloatMVRatio| 主力净买入额流通市值比 || |
| CS_StockCapFlowIndex | MainNBVolumeRatio| 主力净买入率(量) || |
| CS_StockCapFlowIndex | MainNBVFloatSRatio | 主力净买入量流通股本比 || |
| CS_StockCapFlowIndex | MainActBuyValue| 主力主动流入额(元) || |
| CS_StockCapFlowIndex | MainActSellValue | 主力主动流出额(元) || |
| CS_StockCapFlowIndex | MainActBuyVolume | 主力主动流入量(股) || |
| CS_StockCapFlowIndex | MainActSellVolume| 主力主动流出量(股) || |
| CS_StockCapFlowIndex | MainActBuyNum| 主力主动流入笔数 || |
| CS_StockCapFlowIndex | MainActSellNum | 主力主动流出笔数 || |
| CS_StockCapFlowIndex | MainNetActBuyValue | 主力净主动流入额(元) || |
| CS_StockCapFlowIndex | MainNetActBuyVolume| 主力净主动流入量(股) || |
| CS_StockCapFlowIndex | MainABValueRatio | 主力主动买入率(额) || |
| CS_StockCapFlowIndex | MainASValueRatio | 主力主动卖出率(额) || |
| CS_StockCapFlowIndex | MainABVolumeRatio| 主力主动买入率(量) || |
| CS_StockCapFlowIndex | MainASVolumeRatio| 主力主动卖出率(量) || |
| CS_StockCapFlowIndex | MainNABValueRatio| 主力净主动买入率(额) || |
| CS_StockCapFlowIndex | MainNABVFloatMVRatio | 主力净主动买入额流通市值比 || |
| CS_StockCapFlowIndex | MainNABVolumeRatio | 主力净主动买入率(量) || |
| CS_StockCapFlowIndex | MainNABVFloatSRatio| 主力净主动买入量流通股本比 || |
| CS_StockCapFlowIndex | TotalBuyValue| 全单流入额(元) | 全单=小单+中单+大单+超大单 | Total order = small order + medium order + large order + extra-large order|
| CS_StockCapFlowIndex | TotalSellValue | 全单流出额(元) || |
| CS_StockCapFlowIndex | TotalBuyVolume | 全单流入量(股) || |
| CS_StockCapFlowIndex | TotalSellVolume| 全单流出量(股) || |
| CS_StockCapFlowIndex | TotalBuyNum| 全单流入笔数 || |
| CS_StockCapFlowIndex | TotalSellNum | 全单流出笔数 || |
| CS_StockCapFlowIndex | TotalNetBuyValue | 全单净流入额(元) || |
| CS_StockCapFlowIndex | TotalNetBuyVolume| 全单净流入量(股) || |
| CS_StockCapFlowIndex | TotalBValueRatio | 全单买入率(额) || |
| CS_StockCapFlowIndex | TotalSValueRatio | 全单卖出率(额) || |
| CS_StockCapFlowIndex | TotalBVolumeRatio| 全单买入率(量) || |
| CS_StockCapFlowIndex | TotalSVolumeRatio| 全单卖出率(量) || |
| CS_StockCapFlowIndex | TotalNBValueRatio| 全单净买入率(额) || |
| CS_StockCapFlowIndex | TotalNBVFloatMVRatio | 全单净买入额流通市值比 || |
| CS_StockCapFlowIndex | TotalNBVolumeRatio | 全单净买入率(量) || |
| CS_StockCapFlowIndex | TotalNBVFloatSRatio| 全单净买入量流通股本比 || |
| CS_StockCapFlowIndex | TotalActBuyValue | 全单主动流入额(元) || |
| CS_StockCapFlowIndex | TotalActSellValue| 全单主动流出额(元) || |
| CS_StockCapFlowIndex | TotalActBuyVolume| 全单主动流入量(股) || |
| CS_StockCapFlowIndex | TotalActSellVolume | 全单主动流出量(股) || |
| CS_StockCapFlowIndex | TotalActBuyNum | 全单主动流入笔数 || |
| CS_StockCapFlowIndex | TotalActSellNum| 全单主动流出笔数 || |
| CS_StockCapFlowIndex | TotalNetActBuyValue| 全单净主动流入额(元) || |
| CS_StockCapFlowIndex | TotalNetActBuyVolume | 全单净主动流入量(股) || |
| CS_StockCapFlowIndex | TotalABValueRatio| 全单主动买入率(额) || |
| CS_StockCapFlowIndex | TotalASValueRatio| 全单主动卖出率(额) || |
| CS_StockCapFlowIndex | TotalABVolumeRatio | 全单主动买入率(量) || |
| CS_StockCapFlowIndex | TotalASVolumeRatio | 全单主动卖出率(量) || |
| CS_StockCapFlowIndex | TotalNABValueRatio | 全单净主动买入率(额) || |
| CS_StockCapFlowIndex | TotalNABVFloatMVRatio| 全单净主动买入额流通市值比 || |
| CS_StockCapFlowIndex | TotalNABVolumeRatio| 全单净主动买入率(量) || |
| CS_StockCapFlowIndex | TotalNABVFloatSRatio | 全单净主动买入量流通股本比 || |
| CS_StockCapFlowIndex | InsertTime | 发布时间 || |
| CS_StockCapFlowIndex | UpdateTime | 更新时间 || |
| CS_StockCapFlowIndex | JSID | JSID || |
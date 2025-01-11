| column_name| column_description | 注释 | Annotation|
|---|---|---|---|---|
| ID | ID || |
| InnerCode| 证券内部编码 | 证券内部编码（InnerCode）与“证券主表(SecuMain)”中的“证券内部编码(InnerCode)”关联，得到股票的证券代码、简称等其他详细信息。 | The internal code (InnerCode) of securities is associated with the "InnerCode" in the "SecuMain" table, obtaining other detailed information such as the security code and abbreviation of the stock. |
| TradingDay | 交易日期 || |
| TimeRange| 成交时间区间 | 成交时间区间(TimeRange)，该字段固定以下常量：1-全盘，2-开盘，3-尾盘| Transaction Time Range (TimeRange), this field is fixed with the following constants: 1-Whole Disk, 2-Opening, 3-End of Disk|
| SmallBuyValue| 小单流入额(元) | 小单：单笔成交量区间为[0，2w)或成交金额区间为[0，4w) | Xiao Dan: The volume per transaction ranges from [0, 20,000) or the transaction amount ranges from [0, 40,000). |
| SmallSellValue | 小单流出额(元) || |
| SmallBuyVolume | 小单流入量(股) || |
| SmallSellVolume| 小单流出量(股) || |
| SmallBuyNum| 小单流入笔数 || |
| SmallSellNum | 小单流出笔数 || |
| SmallNetBuyValue | 小单净流入额(元) || |
| SmallNetBuyVolume| 小单净流入量(股) || |
| SmallBValueRatio | 小单买入率(额) || |
| SmallSValueRatio | 小单卖出率(额) || |
| SmallBVolumeRatio| 小单买入率(量) || |
| SmallSVolumeRatio| 小单卖出率(量) || |
| SmallNBValueRatio| 小单净买入率(额) || |
| SmallNBVFloatMVRatio | 小单净买入额流通市值比 || |
| SmallNBVolumeRatio | 小单净买入率(量) || |
| SmallNBVFloatSRatio| 小单净买入量流通股本比 || |
| SmallActBuyValue | 小单主动流入额(元) || |
| SmallActSellValue| 小单主动流出额(元) || |
| SmallActBuyVolume| 小单主动流入量(股) || |
| SmallActSellVolume | 小单主动流出量(股) || |
| SmallActBuyNum | 小单主动流入笔数 || |
| SmallActSellNum| 小单主动流出笔数 || |
| SmallNetActBuyValue| 小单净主动流入额(元) || |
| SmallNetActBuyVolume | 小单净主动流入量(股) || |
| SmallABValueRatio| 小单主动买入率(额) || |
| SmallASValueRatio| 小单主动卖出率(额) || |
| SmallABVolumeRatio | 小单主动买入率(量) || |
| SmallASVolumeRatio | 小单主动卖出率(量) || |
| SmallNABValueRatio | 小单净主动买入率(额) || |
| SmallNABVFloatMVRatio| 小单净主动买入额流通市值比 || |
| SmallNABVolumeRatio| 小单净主动买入率(量) || |
| SmallNABVFloatSRatio | 小单净主动买入量流通股本比 || |
| MediumBuyValue | 中单流入额(元) | 中单：单笔成交量区间为[2w，10w)或成交金额区间为[4w，20w) | The single transaction volume range is [20,000, 100,000) or the transaction amount range is [40,000, 200,000) |
| MediumSellValue| 中单流出额(元) || |
| MediumBuyVolume| 中单流入量(股) || |
| MediumSellVolume | 中单流出量(股) || |
| MediumBuyNum | 中单流入笔数 || |
| MediumSellNum| 中单流出笔数 || |
| MediumNetBuyValue| 中单净流入额(元) || |
| MediumNetBuyVolume | 中单净流入量(股) || |
| MediumBValueRatio| 中单买入率(额) || |
| MediumSValueRatio| 中单卖出率(额) || |
| MediumBVolumeRatio | 中单买入率(量) || |
| MediumSVolumeRatio | 中单卖出率(量) || |
| MediumNBValueRatio | 中单净买入率(额) || |
| MediumNBVFloatMVRatio| 中单净买入额流通市值比 || |
| MediumNBVolumeRatio| 中单净买入率(量) || |
| MediumNBVFloatSRatio | 中单净买入量流通股本比 || |
| MediumActBuyValue| 中单主动流入额(元) || |
| MediumActSellValue | 中单主动流出额(元) || |
| MediumActBuyVolume | 中单主动流入量(股) || |
| MediumActSellVolume| 中单主动流出量(股) || |
| MediumActBuyNum| 中单主动流入笔数 || |
| MediumActSellNum | 中单主动流出笔数 || |
| MediumNetActBuyValue | 中单净主动流入额(元) || |
| MediumNetActBuyVolume| 中单净主动流入量(股) || |
| MediumABValueRatio | 中单主动买入率(额) || |
| MediumASValueRatio | 中单主动卖出率(额) || |
| MediumABVolumeRatio| 中单主动买入率(量) || |
| MediumASVolumeRatio| 中单主动卖出率(量) || |
| MediumNABValueRatio| 中单净主动买入率(额) || |
| MediumNABVFloatMVRatio | 中单净主动买入额流通市值比 || |
| MediumNABVolumeRatio | 中单净主动买入率(量) || |
| MediumNABVFloatSRatio| 中单净主动买入量流通股本比 || |
| LargeBuyValue| 大单流入额(元) | 大单：单笔成交量区间为[10w，50w)或成交金额区间为[20w，100w)| Large order: The volume per transaction is in the range of [100,000, 500,000) or the transaction amount is in the range of [200,000, 1,000,000) |
| LargeSellValue | 大单流出额(元) || |
| LargeBuyVolume | 大单流入量(股) || |
| LargeSellVolume| 大单流出量(股) || |
| LargeBuyNum| 大单流入笔数 || |
| LargeSellNum | 大单流出笔数 || |
| LargeNetBuyValue | 大单净流入额(元) || |
| LargeNetBuyVolume| 大单净流入量(股) || |
| LargeBValueRatio | 大单买入率(额) || |
| LargeSValueRatio | 大单卖出率(额) || |
| LargeBVolumeRatio| 大单买入率(量) || |
| LargeSVolumeRatio| 大单卖出率(量) || |
| LargeNBValueRatio| 大单净买入率(额) || |
| LargeNBVFloatMVRatio | 大单净买入额流通市值比 || |
| LargeNBVolumeRatio | 大单净买入率(量) || |
| LargeNBVFloatSRatio| 大单净买入量流通股本比 || |
| LargeActBuyValue | 大单主动流入额(元) || |
| LargeActSellValue| 大单主动流出额(元) || |
| LargeActBuyVolume| 大单主动流入量(股) || |
| LargeActSellVolume | 大单主动流出量(股) || |
| LargeActBuyNum | 大单主动流入笔数 || |
| LargeActSellNum| 大单主动流出笔数 || |
| LargeNetActBuyValue| 大单净主动流入额(元) || |
| LargeNetActBuyVolume | 大单净主动流入量(股) || |
| LargeABValueRatio| 大单主动买入率(额) || |
| LargeASValueRatio| 大单主动卖出率(额) || |
| LargeABVolumeRatio | 大单主动买入率(量) || |
| LargeASVolumeRatio | 大单主动卖出率(量) || |
| LargeNABValueRatio | 大单净主动买入率(额) || |
| LargeNABVFloatMVRatio| 大单净主动买入额流通市值比 || |
| LargeNABVolumeRatio| 大单净主动买入率(量) || |
| LargeNABVFloatSRatio | 大单净主动买入量流通股本比 || |
| HugeBuyValue | 超大单流入额(元) | 超大单：单笔成交量区间为[50w，+∞)或成交金额区间为[100w，+∞)| Super large order: The volume per transaction is in the range of [500,000, +∞) or the transaction amount is in the range of [1,000,000, +∞).|
| HugeSellValue| 超大单流出额(元) || |
| HugeBuyVolume| 超大单流入量(股) || |
| HugeSellVolume | 超大单流出量(股) || |
| HugeBuyNum | 超大单流入笔数 || |
| HugeSellNum| 超大单流出笔数 || |
| HugeNetBuyValue| 超大单净流入额(元) || |
| HugeNetBuyVolume | 超大单净流入量(股) || |
| HugeBValueRatio| 超大单买入率(额) || |
| HugeSValueRatio| 超大单卖出率(额) || |
| HugeBVolumeRatio | 超大单买入率(量) || |
| HugeSVolumeRatio | 超大单卖出率(量) || |
| HugeNBValueRatio | 超大单净买入率(额) || |
| HugeNBVFloatMVRatio| 超大单净买入额流通市值比 || |
| HugeNBVolumeRatio| 超大单净买入率(量) || |
| HugeNBVFloatSRatio | 超大单净买入量流通股本比 || |
| HugeActBuyValue| 超大单主动流入额(元) || |
| HugeActSellValue | 超大单主动流出额(元) || |
| HugeActBuyVolume | 超大单主动流入量(股) || |
| HugeActSellVolume| 超大单主动流出量(股) || |
| HugeActBuyNum| 超大单主动流入笔数 || |
| HugeActSellNum | 超大单主动流出笔数 || |
| HugeNetActBuyValue | 超大单净主动流入额(元) || |
| HugeNetActBuyVolume| 超大单净主动流入量(股) || |
| HugeABValueRatio | 超大单主动买入率(额) || |
| HugeASValueRatio | 超大单主动卖出率(额) || |
| HugeABVolumeRatio| 超大单主动买入率(量) || |
| HugeASVolumeRatio| 超大单主动卖出率(量) || |
| HugeNABValueRatio| 超大单净主动买入率(额) || |
| HugeNABVFloatMVRatio | 超大单净主动买入额流通市值比 || |
| HugeNABVolumeRatio | 超大单净主动买入率(量) || |
| HugeNABVFloatSRatio| 超大单净主动买入量流通股本比 || |
| MainBuyValue | 主力流入额(元) | 主力=大单+超大单 | Main force = large orders + super large orders|
| MainSellValue| 主力流出额(元) || |
| MainBuyVolume| 主力流入量(股) || |
| MainSellVolume | 主力流出量(股) || |
| MainBuyNum | 主力流入笔数 || |
| MainSellNum| 主力流出笔数 || |
| MainNetBuyValue| 主力净流入额(元)1|| |
| MainNetBuyVolume | 主力净流入量(股)1|| |
| MainBValueRatio| 主力买入率(额) || |
| MainSValueRatio| 主力卖出率(额) || |
| MainBVolumeRatio | 主力买入率(量) || |
| MainSVolumeRatio | 主力卖出率(量) || |
| MainNBValueRatio | 主力净买入率(额) || |
| MainNBVFloatMVRatio| 主力净买入额流通市值比 || |
| MainNBVolumeRatio| 主力净买入率(量) || |
| MainNBVFloatSRatio | 主力净买入量流通股本比 || |
| MainActBuyValue| 主力主动流入额(元) || |
| MainActSellValue | 主力主动流出额(元) || |
| MainActBuyVolume | 主力主动流入量(股) || |
| MainActSellVolume| 主力主动流出量(股) || |
| MainActBuyNum| 主力主动流入笔数 || |
| MainActSellNum | 主力主动流出笔数 || |
| MainNetActBuyValue | 主力净主动流入额(元) || |
| MainNetActBuyVolume| 主力净主动流入量(股) || |
| MainABValueRatio | 主力主动买入率(额) || |
| MainASValueRatio | 主力主动卖出率(额) || |
| MainABVolumeRatio| 主力主动买入率(量) || |
| MainASVolumeRatio| 主力主动卖出率(量) || |
| MainNABValueRatio| 主力净主动买入率(额) || |
| MainNABVFloatMVRatio | 主力净主动买入额流通市值比 || |
| MainNABVolumeRatio | 主力净主动买入率(量) || |
| MainNABVFloatSRatio| 主力净主动买入量流通股本比 || |
| TotalBuyValue| 全单流入额(元) | 全单=小单+中单+大单+超大单 | Total order = small order + medium order + large order + extra-large order|
| TotalSellValue | 全单流出额(元) || |
| TotalBuyVolume | 全单流入量(股) || |
| TotalSellVolume| 全单流出量(股) || |
| TotalBuyNum| 全单流入笔数 || |
| TotalSellNum | 全单流出笔数 || |
| TotalNetBuyValue | 全单净流入额(元) || |
| TotalNetBuyVolume| 全单净流入量(股) || |
| TotalBValueRatio | 全单买入率(额) || |
| TotalSValueRatio | 全单卖出率(额) || |
| TotalBVolumeRatio| 全单买入率(量) || |
| TotalSVolumeRatio| 全单卖出率(量) || |
| TotalNBValueRatio| 全单净买入率(额) || |
| TotalNBVFloatMVRatio | 全单净买入额流通市值比 || |
| TotalNBVolumeRatio | 全单净买入率(量) || |
| TotalNBVFloatSRatio| 全单净买入量流通股本比 || |
| TotalActBuyValue | 全单主动流入额(元) || |
| TotalActSellValue| 全单主动流出额(元) || |
| TotalActBuyVolume| 全单主动流入量(股) || |
| TotalActSellVolume | 全单主动流出量(股) || |
| TotalActBuyNum | 全单主动流入笔数 || |
| TotalActSellNum| 全单主动流出笔数 || |
| TotalNetActBuyValue| 全单净主动流入额(元) || |
| TotalNetActBuyVolume | 全单净主动流入量(股) || |
| TotalABValueRatio| 全单主动买入率(额) || |
| TotalASValueRatio| 全单主动卖出率(额) || |
| TotalABVolumeRatio | 全单主动买入率(量) || |
| TotalASVolumeRatio | 全单主动卖出率(量) || |
| TotalNABValueRatio | 全单净主动买入率(额) || |
| TotalNABVFloatMVRatio| 全单净主动买入额流通市值比 || |
| TotalNABVolumeRatio| 全单净主动买入率(量) || |
| TotalNABVFloatSRatio | 全单净主动买入量流通股本比 || |
| InsertTime | 发布时间 || |
| UpdateTime | 更新时间 || |
| JSID | JSID || |
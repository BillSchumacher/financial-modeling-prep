ETF_HOLDING_DATES_ENDPOINT = "v4/etf-holdings/portfolio-date"
# The FMP ETF Holding Dates endpoint provides a list of the dates on which ETF holdings are updated. For example, an investor may want to know when an ETF's holdings are updated in order to make sure that they are still aligned with their investment goals.

# Query Params:
# symbol: string
# cik (optional): string

# Response:
"""
[
	{
		"date": "2023-03-31"
	},
	{
		"date": "2022-12-31"
	}
]
"""

ETF_HOLDINGS_ENDPOINT = "v4/etf-holdings"
# The FMP ETF Holdings endpoint provides a list of all the securities that are held by an ETF. For example, an investor may want to know which ETF has the highest exposure to a particular industry or sector.

# Query Params:
# cik: string
# symbol: string
# date (optional): string

# Response:
"""
[
	{
		"cik": "0000036405",
		"acceptanceTime": "2023-05-26 15:28:00",
		"date": "2023-03-31",
		"symbol": "NXPI",
		"name": "NXP Semiconductors NV",
		"lei": "724500M9BY5293JDF951",
		"title": "NXP SEMICONDUCTO",
		"cusip": "N6596X109",
		"isin": "NL0009538784",
		"balance": 6046657,
		"units": "NS",
		"cur_cd": "USD",
		"valUsd": 1127550364.08,
		"pctVal": 0.03930805710834702,
		"payoffProfile": "Long",
		"assetCat": "EC",
		"issuerCat": "CORP",
		"invCountry": "US",
		"isRestrictedSec": "N",
		"fairValLevel": "1",
		"isCashCollateral": "N",
		"isNonCashCollateral": "N",
		"isLoanByFund": "N"
	}
]
"""

ETF_HOLDER_ENDPOINT = "v3/etf-holder/{symbol}"
# The FMP ETF Holder endpoint provides a list of all the institutional investors that own shares of an ETF. For example, an investor may want to know which institutions are buying or selling shares of a particular ETF.

# Path Params:
# symbol: string


# Response:
"""
[
	{
		"asset": "AAPL",
		"name": "Apple Inc.",
		"isin": "US0378331005",
		"cusip": "037833100",
		"sharesNumber": 163400200,
		"weightPercentage": 6.71,
		"marketValue": 24766568314,
		"updated": "2023-02-16"
	}
]
"""


ETF_INFORMATION_ENDPOINT = "v4/etf-info"
# The FMP ETF Information endpoint provides basic information about an ETF, such as its ticker symbol, name, expense ratio, and asset under management. For example, an investor may want to compare the expense ratios of different ETFs to find the one that is most cost-effective.

# Query Params:
# symbol: string

# Response:
"""
[
	{
		"symbol": "SPY",
		"assetClass": "Equity",
		"aum": 375825060000,
		"avgVolume": 81144062,
		"cusip": "",
		"description": "The Trust seeks to achieve its investment objective by holding a portfolio of the common stocks that are included in the index (the Portfolio), with the weight of each stock in the Portfolio substantially corresponding to the weight of such stock in the index.",
		"domicile": "US",
		"etfCompany": "SPDR",
		"expenseRatio": 0.0945,
		"inceptionDate": "1993-01-22",
		"isin": "",
		"name": "SPDR S&P 500 ETF Trust",
		"nav": 375825.06,
		"navCurrency": "USD",
		"sectorsList": [
			{
				"exposure": "2.53%",
				"industry": "Real Estate"
			}
		],
		"website": "https://www.ssga.com/us/en/institutional/etfs/funds/spdr-sp-500-etf-trust-spy",
		"holdingsCount": 503
	}
]
"""

ETF_SECTOR_WEIGHTING_ENDPOINT = "v3/etf-sector-weightings/{symbol}"
# The FMP ETF Sector Weighting endpoint provides a breakdown of the percentage of an ETF's assets that are invested in each sector. For example, an investor may want to invest in an ETF that has a high exposure to the technology sector if they believe that the technology sector is poised for growth.

# Path Params:
# symbol: string

# Response:
"""
[
	{
		"sector": "Technology",
		"weightPercentage": "90.11%"
	}
]
"""

ETF_COUNTRY_WEIGHTING_ENDPOINT = "v3/etf-country-weightings/{symbol}"
# The FMP ETF Country Weighting endpoint provides a breakdown of the percentage of an ETF's assets that are invested in each country. For example, an investor may want to invest in an ETF that has a high exposure to China if they believe that the Chinese economy is poised for growth.

# Path Params:
# symbol: string

# Response:
"""
[
	{
		"country": "United States",
		"weightPercentage": "96.54%"
	}
]
"""

ETF_SECTOR_EXPOSURE_ENDPOINT = "v3/etf-stock-exposure/{symbol}"
# The FMP ETF Sector Exposure endpoint provides a measure of how much of an ETF's performance is attributable to each sector. For example, an investor may want to invest in an ETF that has a high exposure to the technology sector if they believe that the technology sector is likely to outperform the overall market.

# Path Params:
# symbol: string

# Response:
"""
[
	{
		"etfSymbol": "QDVE.DE",
		"assetExposure": "AAPL",
		"sharesNumber": 5128516,
		"weightPercentage": 27,
		"marketValue": 798715081.84
	}
]
"""
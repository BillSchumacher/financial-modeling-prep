INSIDER_TRADES_RSS_ENDPOINT = "v4/insider-trading-rss-feed"
# Provides an RSS feed of insider trades, updated in real-time.

# Query Parameters
# page: int (optional) - The page number to retrieve

# Response:
"""
[
	{
		"title": "4 - Atlantic Union Bankshares Corp (0000883948) (Issuer)",
		"fillingDate": "2022-10-05 13:43:47",
		"symbol": "AUB",
		"link": "https://www.sec.gov/Archives/edgar/data/883948/000141588922010327/0001415889-22-010327-index.htm",
		"reportingCik": "0001745407",
		"issuerCik": "0000883948"
	}
]
"""

INSIDER_TRADES_SEARCH_ENDPOINT = "v4/insider-trading"
# Allows users to search for insider trades by company name, ticker symbol, or insider name.

# Query Parameters
# symbol: str (optional) - The ticker symbol of the company
# reportingCik: str (optional) - The CIK of the reporting owner
# companyCik: str (optional) - The CIK of the company
# page: int (optional) - The page number to retrieve

# Response:
"""
[
	{
		"symbol": "AAPL",
		"filingDate": "2022-10-04 22:05:07",
		"transactionDate": "2022-10-03",
		"reportingCik": "0001767094",
		"transactionType": "S-Sale",
		"securitiesOwned": 270196,
		"securitiesTransacted": 42393,
		"companyCik": "0000320193",
		"reportingName": "O'BRIEN DEIRDRE",
		"typeOfOwner": "officer: Senior Vice President",
		"link": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000097/0000320193-22-000097-index.htm",
		"securityName": "Common Stock",
		"price": 141.09,
		"formType": "4",
		"acquistionOrDisposition": "D"
	}
]
"""

TRANSACTION_TYPES_ENDPOINT = "v4/insider-trading-transaction-type"
# Provides a list of all insider transaction types, such as purchases, sales, and gifts.

# Response:
"""
[
	"J-Other",
	"P-Purchase",
	"W-Will",
	"I-Discretionary",
	"Z-Trust",
	"F-InKind"
]
"""

INSIDERS_BY_SYMBOL_ENDPOINT = "v4/insider-roaster"
# Provides a list of all insiders for a given company.

# Query Parameters
# symbol: str (required) - The ticker symbol of the company

# Response:
"""
[
	{
		"typeOfOwner": "officer: SVP, GC and Secretary",
		"transactionDate": "2022-10-03",
		"owner": "Adams Katherine L."
	}
]
"""

INSIDER_TRADE_STATISTICS_ENDPOINT = "v4/insider-roaster-statistics"
# Provides statistics on insider trading activity, such as the total number of insider trades, the average value of insider trades, and the most popular insider stocks.

# Query Parameters
# symbol: str (required) - The ticker symbol of the company

# Response:
"""
[
	{
		"symbol": "AAPL",
		"cik": "0000320193",
		"year": 2022,
		"quarter": 4,
		"purchases": 6,
		"sales": 30,
		"buySellRatio": 0.2,
		"totalBought": 1492148,
		"totalSold": 2810029,
		"averageBought": 248691.3333,
		"averageSold": 93667.6333,
		"pPurchases": 0,
		"sSales": 15
	}
]
"""

CIK_MAPPER_ENDPOINT = "v4/mapper-cik-name"
# Converts a CIK number to a company name.

# Query Parameters
# page: int (optional) - The page number to retrieve
# name: str (optional) - The name of the company or person

# Response:
"""
[
	{
		"reportingCik": "0001453356",
		"reportingName": "10X Fund, L.P."
	}
]
"""

CIK_MAPPER_BY_SYMBOL_ENDPOINT = "v4/mapper-cik-company/{symbol}"
# Provides a list of all CIK numbers and corresponding company names.

# Path Params:
# symbol: str (required) - The ticker symbol of the company

# Response:
"""
[
	{
		"symbol": "MSFT",
		"companyCik": "0000789019"
	}
]
"""

FAIL_TO_DELIVER_ENDPOINT = "v4/fail-to-deliver"
# Provides a list of all fail to deliver data.

# Query Parameters
# symbol: str (required?) - The ticker symbol of the company
# page: int (optional) - The page number to retrieve

# Response:
"""
[
	{
		"symbol": "GE",
		"date": "2023-09-27",
		"price": 109.93,
		"quantity": 3320,
		"cusip": "369604301",
		"name": "GEN ELEC CO COM NEW (NY)"
	}
]
"""

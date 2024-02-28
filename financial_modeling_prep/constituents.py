SP500_CONSTITUENTS_ENDPOINT = "v3/sp500_constituent"
# Provides a list of all companies that are included in the S&P 500 index.

# Query Params:
# datatype: string - json, csv

# Response:
"""
[
	{
		"symbol": "VLTO",
		"name": "Veralto",
		"sector": "Industrials",
		"subSector": "",
		"headQuarter": "Waltham, Massachusetts",
		"dateFirstAdded": "2023-10-02",
		"cik": "0001967680",
		"founded": "2023"
	}
]
"""

HISTORICAL_SP500_CONSTITUENTS_ENDPOINT = "v3/historical/sp500_constituent"
# Provides historical data for all companies that are included in the S&P 500 index.

# Response:
"""
[
	{
		"dateAdded": "October 3, 2023",
		"addedSecurity": "",
		"removedTicker": "DXC",
		"removedSecurity": "DXC Technology",
		"date": "2023-10-03",
		"symbol": "DXC",
		"reason": "Market capitalization change."
	}
]
"""

NASDAQ_CONSTITUENTS_ENDPOINT = "v3/nasdaq_constituent"
# Provides a list of all companies that are included in the NASDAQ index.

# Query Params:
# datatype: string - json, csv

# Response:
"""
[
	{
		"symbol": "AAPL",
		"name": "Apple Inc.",
		"sector": "Technology",
		"subSector": "Technology",
		"headQuarter": "Cupertino, CA",
		"dateFirstAdded": null,
		"cik": "0000320193",
		"founded": "1976-04-01"
	}
]
"""

HISTORICAL_NASDAQ_CONSTITUENTS_ENDPOINT = "v3/historical/nasdaq_constituent"
# Provides historical data for all companies that are included in the NASDAQ index.

# Response:
"""
[
	{
		"dateAdded": "December 21, 2020",
		"addedSecurity": "Okta Inc",
		"removedTicker": "",
		"removedSecurity": null,
		"date": "2020-12-21",
		"symbol": "OKTA",
		"reason": "Market capitalization change"
	}
]
"""

DOW_JONES_CONSTITUENTS_ENDPOINT = "v3/dowjones_constituent"
# Provides a list of all companies that are included in the Dow Jones index.

# Query Params:
# datatype: string - json, csv

# Response:
"""
[
	{
		"symbol": "AMGN",
		"name": "Amgen Inc.",
		"sector": "Healthcare",
		"subSector": "Healthcare",
		"headQuarter": "Thousand Oaks, CA",
		"dateFirstAdded": "2020-08-31",
		"cik": "0000318154",
		"founded": "1980-04-08"
	}
]
"""

HISTORICAL_DOW_JONES_CONSTITUENTS_ENDPOINT = "v3/historical/dowjones_constituent"
# Provides historical data for all companies that are included in the Dow Jones index.

# Response:
"""
[
	{
		"dateAdded": "August 31, 2020",
		"addedSecurity": "Salesforce.Com Inc",
		"removedTicker": "",
		"removedSecurity": "",
		"date": "2020-08-31",
		"symbol": "CRM",
		"reason": "Market capitalization change."
	}
]
"""
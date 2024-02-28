GENERAL_SEARCH_ENDPOINT = "v3/search"
# Search over 70,000 symbols by symbol name or company name, including cryptocurrencies, forex, stocks, etf and other financial instruments.
# Query params
# query: string - The search query (Symbol)
# limit: int - The number of results to return
# exchange: string - The exchange to search

# Response
"""
[
	{
		"symbol": "PRAA",
		"name": "PRA Group, Inc.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	},
	{
		"symbol": "PAAS",
		"name": "Pan American Silver Corp.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	}
]
"""

TICKER_SEARCH_ENDPOINT = "v3/search-ticker"
# Find ticker symbols and exchanges for both equity securities and exchange-traded funds (ETFs) by searching with the company name or ticker symbol.

# Query params
# query: string - The search query (Company Name or Ticker Symbol)
# limit: int - The number of results to return
# exchange: string - The exchange to search

# Response
"""
[
	{
		"symbol": "PRAA",
		"name": "PRA Group, Inc.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	},
	{
		"symbol": "PAAS",
		"name": "Pan American Silver Corp.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	}
]
"""

NAME_SEARCH_ENDPOINT = "v3/search-name"
# Find ticker symbols and exchange information for equity securities and exchange-traded funds (ETFs) by searching with the company name.
# Query params
# query: string - The search query (Company Name)
# limit: int - The number of results to return
# exchange: string - The exchange to search

# Response
"""
[
	{
		"symbol": "PRAA",
		"name": "PRA Group, Inc.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	},
	{
		"symbol": "PAAS",
		"name": "Pan American Silver Corp.",
		"currency": "USD",
		"stockExchange": "NasdaqGS",
		"exchangeShortName": "NASDAQ"
	}
]
"""

CIK_NAME_SEARCH_ENDPOINT = "v3/cik-search/{company_name}"
# Discover CIK numbers for SEC-registered entities with our CIK Name Search.
# Path Params
# company_name: string - The company name to search

# Response
"""
[
	{
		"name": "BERKSHIRE BANCORP INC.",
		"cik": "0000000000"
	},
	{
		"name": "BERKSHIRE FOCUS FUND",
		"cik": "0000000000"
	},
	{
		"name": "BERKSHIRE GREY, INC.",
		"cik": "0001824734"
	}
]
"""

CIK_SEARCH_ENDPOINT = "v3/cik/{cik_number}"
# Quickly find registered company names linked to SEC-registered entities using their CIK Number with our CIK Search..
# Path params
# cik_number: string - The CIK number to search

# Response
"""
[
	{
		"name": "BERKSHIRE HATHAWAY INC.",
		"cik": "0001067983"
	}
]
"""

CUSIP_SEARCH_ENDPOINT = "v3/cusip/{cusip_number}"
# Access information about financial instruments and securities by simply entering their unique CUSIP (Committee on Uniform Securities Identification Procedures) numbers with our CUSIP Search..
# Path params
# cusip_number: string - The CUSIP number to search

# Response
"""
[
	{
		"company": "AAON, INC.",
		"ticker": "AAON",
		"cusip": "000360206"
	}
]
"""
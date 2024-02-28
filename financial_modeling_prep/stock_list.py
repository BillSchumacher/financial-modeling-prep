

STOCK_LIST_ENDPOINT = "v3/stock/list"
# Find symbols for traded and non-traded stocks with our Symbol List. This comprehensive list includes over 25,000 stocks, making it the perfect resource for investors and traders of all levels.

# Response
"""
[
	{
		"symbol": "PWP",
		"exchange": "NASDAQ Global Select",
		"exchangeShortName": "NASDAQ",
		"price": "8.13",
		"name": "Perella Weinberg Partners"
	}
]
"""

ETF_LIST_ENDPOINT = "v3/etf/list"
# Our Exchange Traded Fund Search makes it easy to find the symbol for any ETF you're looking for. Simply enter the ETF's name and we'll return the symbol, name, and price.

# Response
"""
[
	{
		"symbol": "SPPR.F",
		"exchange": "Frankfurt",
		"exchangeShortName": "EURONEXT",
		"price": 26.541,
		"name": "SPDR Bloomberg SASB Euro Corporate ESG UCITS ETF"
	}
]
"""

FINANCIAL_STATEMENT_SYMBOLS_LIST_ENDPOINT = "v3/financial-statement-symbol-lists"
# Discover all companies with financial statements available on our API. Our comprehensive list covers major exchanges such as the NYSE and NASDAQ, as well as international exchanges. This list is regularly updated, so you can always find the information you need.

# Response
"""
[
	"GOGN",
	"SNCM.TA",
	"000540.SZ",
	"603931.SS",
	"JMG.L",
	"ERM.L",
	"LVCLY",
	"SBFMW",
	"JGLE.JK",
	"SMWN.DE",
	"CYBN",
	"0440.HK"
]
"""

TRADEABLE_SEARCH_ENDPOINT = "v3/available-traded/list"
# Discover all actively traded stocks with our Tradable Search feature. This comprehensive list includes over 70,000 stocks, with symbol, name, price, and exchange information for each company.

# Response
"""
[
	{
		"symbol": "0Y9S.L",
		"name": "Check Point Software Technologies Ltd.",
		"exchange": "London Stock Exchange",
		"exchangeShortName": "LSE",
		"price": 116.96
	}
]
"""

COMMITMENT_OF_TRADERS_REPORT_ENDPOINT = "v4/commitment_of_traders_report/list"
# The Commitment of Traders Report is a weekly report from the Commodity Futures Trading Commission (CFTC) that provides insights into the positions of market participants in various markets. Our Commitment of Traders Report tool makes it easy to access and analyze this valuable data, helping you to make more informed trading decisions.

# Response
"""
[
	{
		"trading_symbol": "NG",
		"short_name": "Natural Gas (NG)"
	}
]
"""

CIK_LIST_ENDPOINT = "v3/cik_list"
# Our CIK List provides a comprehensive database of CIK numbers for SEC-registered entities. A CIK number is a unique identifier assigned to each SEC-registered entity, and it is required for many financial transactions. Our CIK List is a valuable resource for businesses and individuals who need to quickly and easily find CIK numbers.

# Response
"""
[
	{
		"cik": "0000002230",
		"name": "ADAMS DIVERSIFIED EQUITY FUND, INC."
	}
]
"""

EURONEXT_SYMBOLS_ENDPOINT = "v3/symbol/available-euronext"
# Find all symbols for stocks traded on Euronext exchanges with our comprehensive list. Euronext is one of the largest exchanges in Europe, and our list includes stocks from a wide range of industries.

# Response
"""
[
	{
		"symbol": "533.SI",
		"name": "ABR Holdings Limited",
		"currency": "SGD",
		"stockExchange": "SES",
		"exchangeShortName": "EURONEXT"
	}
]
"""

SYMBOL_CHANGES_ENDPOINT = "v4/symbol_change"
# Stay up-to-date on the latest symbol changes with our easy-to-use tool. Track symbol changes due to mergers, acquisitions, stock splits, and name changes.

# Response
"""
[
	{
		"date": "2023-03-01",
		"name": "Zevra Therapeutics, Inc. Common Stock",
		"oldSymbol": "KMPH",
		"newSymbol": "ZVRA"
	}
]
"""

EXCHANGE_SYMBOLS_ENDPOINT = "v3/exchange/{exchange}"
# Our Exchange Symbols list includes all symbols for supported exchanges. This list includes exchanges from all over the world, making it a valuable resource for investors and traders who want to trade stocks on different exchanges.
# Path params
# exchange: string - The exchange to search

# Response
"""
[
	{
		"symbol": "SRDX",
		"name": "Surmodics, Inc.",
		"price": 22.1,
		"changesPercentage": 0.7752,
		"change": 0.17,
		"dayLow": 21.76,
		"dayHigh": 22.3,
		"yearHigh": 45.85,
		"yearLow": 21.61,
		"marketCap": 312162500,
		"priceAvg50": 30.0696,
		"priceAvg200": 33.5478,
		"exchange": "NASDAQ",
		"volume": 51517,
		"avgVolume": 72111,
		"open": 21.76,
		"previousClose": 21.93,
		"eps": -2.23,
		"pe": -9.91,
		"earningsAnnouncement": "2023-04-25T12:30:00.000+0000",
		"sharesOutstanding": 14125000,
		"timestamp": 1677789927
	}
]
"""


AVAILABLE_INDEXES_ENDPOINT = "v3/symbol/available-indexes"
# The FMP Available Indexes endpoint provides a list of all available indexes. The list includes the index's symbol, name, and exchange.

# Response
"""
[
	{
		"symbol": "XU100.IS",
		"name": "BIST 100",
		"currency": "TRY",
		"stockExchange": "Istanbul",
		"exchangeShortName": "INDEX"
	}
]
"""
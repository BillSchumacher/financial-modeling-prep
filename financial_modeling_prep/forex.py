FOREX_LIST_ENDPOINT = "v3/symbol/available-forex-currency-pairs"
# Provides a list of all currency pairs that are traded on the forex market.

# Response:
"""
[
	{
		"symbol": "MYREUR",
		"name": "MYR/EUR",
		"currency": "EUR",
		"stockExchange": "CCY",
		"exchangeShortName": "FOREX"
	}
]
"""

FULL_QUOTE_LIST_ENDPOINT = "v3/quotes/forex"
# Provides a list of all quotes for all currency pairs that are traded on the forex market.

# Response:
"""
[
	{
		"symbol": "AEDAUD",
		"name": "AED/AUD",
		"price": 0.40401,
		"changesPercentage": 0.3901,
		"change": 0.0016,
		"dayLow": 0.40211,
		"dayHigh": 0.40535,
		"yearHigh": 0.440948,
		"yearLow": 0.356628,
		"marketCap": null,
		"priceAvg50": 0.39494148,
		"priceAvg200": 0.40097216,
		"volume": 0,
		"avgVolume": 0,
		"exchange": "FOREX",
		"open": 0.40223,
		"previousClose": 0.40244,
		"eps": null,
		"pe": null,
		"earningsAnnouncement": null,
		"sharesOutstanding": null,
		"timestamp": 1677792573
	}
]
"""

FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
# Provides a full quote for a specific currency pair.A complete quote comprises the current exchange rate for the currency pair, along with daily high, low, and open rates, the spread, and trading volume for the day.

# Path Params:
# symbol (required) - the currency pair symbol

# Response:
"""
[
	{
		"symbol": "EURUSD",
		"name": "EUR/USD",
		"price": 1.05972,
		"changesPercentage": -0.673,
		"change": -0.00718,
		"dayLow": 1.0579771,
		"dayHigh": 1.0676916,
		"yearHigh": 1.1183056,
		"yearLow": 0.9540164,
		"marketCap": null,
		"priceAvg50": 1.0728177,
		"priceAvg200": 1.0319284,
		"volume": 124655,
		"avgVolume": 124655,
		"exchange": "FOREX",
		"open": 1.0669,
		"previousClose": 1.067122,
		"eps": null,
		"pe": null,
		"earningsAnnouncement": null,
		"sharesOutstanding": null,
		"timestamp": 1677793653
	}
]
"""

INTRADAY_FOREX_ENDPOINT = "v3/historical-chart/{timeframe}/{symbol}"
# Provides a full quote for a specific currency pair.A complete quote comprises the current exchange rate for the currency pair, along with daily high, low, and open rates, the spread, and trading volume for the day.

# Path Params:
# symbol (required) - the currency pair symbol
# timeframe (required) - the timeframe of the data (1min, 5min, 15min, 30min, 1hour, 4hour)

# Query Params:
# from (optional) - the start date of the data
# to (optional) - the end date of the data

# Response:
"""
[
	{
		"date": "2023-03-02 16:46:00",
		"open": 1.0597,
		"low": 1.0596,
		"high": 1.0598,
		"close": 1.05972,
		"volume": 29
	}
]
"""

FOREX_DAILY_ENDPOINT = "v3/historical-price-full/{symbol}"
# Provides daily price data for all currency pairs that are traded on the forex market.

# Path Params:
# symbol (required) - the currency pair symbol

# Response:
"""
{
	"symbol": "EURUSD",
	"historical": [
		{
			"date": "2023-03-02",
			"open": 1.0669,
			"high": 1.0696331,
			"low": 1.056859,
			"close": 1.0599958,
			"adjClose": 1.0599958,
			"volume": 124526,
			"unadjustedVolume": 124526,
			"change": -0.0069042,
			"changePercent": -0.64712719,
			"vwap": 1.06,
			"label": "March 02, 23",
			"changeOverTime": -0.0064712719
		}
	]
}
"""
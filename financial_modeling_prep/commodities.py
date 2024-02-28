COMMODITIES_LIST_ENDPOINT = "v3/symbol/available-commodities"
# Provides a list of available commodities.

# Response:
"""
[
	{
		"symbol": "OUSX",
		"name": "Oat Futures",
		"currency": "USX",
		"stockExchange": "CBOT",
		"exchangeShortName": "COMMODITY"
	}
]
"""

FULL_QUOTE_LIST_ENDPOINT = "v3/quotes/commodity"
# Provides a list of all quotes for all commodities that are traded on exchanges around the world.

# Response:
"""
[
	{
		"symbol": "KEUSX",
		"name": "KC HRW Wheat Futures",
		"price": 825.75,
		"changesPercentage": 1.1639,
		"change": 9.5,
		"dayLow": 813.75,
		"dayHigh": 832.75,
		"yearHigh": 1379.25,
		"yearLow": 803.25,
		"marketCap": null,
		"priceAvg50": 861.665,
		"priceAvg200": 938.525,
		"volume": 18637,
		"avgVolume": 15566,
		"exchange": "COMMODITY",
		"open": 820.75,
		"previousClose": 816.25,
		"eps": null,
		"pe": null,
		"earningsAnnouncement": null,
		"sharesOutstanding": null,
		"timestamp": 1677784798
	}
]
"""

FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
# Provides real-time quotes for all commodities that are traded on exchanges around the world.

# Query Parameters:
# symbol: string (required) - The commodity symbol.

# Response:
"""
[
	{
		"symbol": "OUSX",
		"name": "Oat Futures",
		"price": 332.25,
		"changesPercentage": -0.9687,
		"change": -3.25,
		"dayLow": 331.75,
		"dayHigh": 338,
		"yearHigh": 811,
		"yearLow": 329.75,
		"marketCap": null,
		"priceAvg50": 367.17,
		"priceAvg200": 446.43875,
		"volume": 347,
		"avgVolume": 268,
		"exchange": "COMMODITY",
		"open": 337.25,
		"previousClose": 335.5,
		"eps": null,
		"pe": null,
		"earningsAnnouncement": null,
		"sharesOutstanding": null,
		"timestamp": 1677784672
	}
]
"""


INTRADAY_COMMODITIES_ENDPOINT = "v3/historical-chart/{timeframe}/{symbol}"
# Provides intraday price data for all commodities that are traded on exchanges around the world.

# Path Parameters:
# timeframe: string (required) - The timeframe for the chart data. Available values: 1min, 5min, 15min, 30min, 1hour, 4hour.
# symbol: string (required) - The commodity symbol.

# Query Parameters:
# from: string (optional) - From date (YYYY-MM-DD)
# to: string (optional) - To date (YYYY-MM-DD)

# Response:
"""
[
	{
		"date": "2023-03-02 16:46:00",
		"open": 332.25,
		"low": 332.25,
		"high": 332.25,
		"close": 332.25,
		"volume": 347
	}
]
"""

COMMODITIES_DAILY_ENDPOINT = "v3/historical-price-full/{symbol}"
# Provides daily price data for all commodities that are traded on exchanges around the world.

# Path Parameters:
# symbol: string (required) - The commodity symbol.

# Response:
"""
{
	"symbol": "OUSX",
	"historical": [
		{
			"date": "2023-03-02",
			"open": 337.25,
			"high": 338,
			"low": 331.75,
			"close": 332.25,
			"adjClose": 332.25,
			"volume": 347,
			"unadjustedVolume": 347,
			"change": -5,
			"changePercent": -1.48258,
			"vwap": 334,
			"label": "March 02, 23",
			"changeOverTime": -0.0148258
		}
	]
}
"""

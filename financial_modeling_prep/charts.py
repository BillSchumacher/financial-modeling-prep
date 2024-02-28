INTRADAY_CHART_ENDPOINT = "v3/historical-chart/{timeframe}/{symbol}"
# The FMP Chart Intraday endpoint provides an intraday chart for a given company. The chart displays the stock price of the company at different time intervals throughout the day. The user can specify the time interval that they want to view, such as 1 minute, 5 minutes, 15 minutes, or 60 minutes.

# Path Params:
# timeframe: The time interval for the chart. The user can specify 1min, 5min, 15min, 30min, 1hour, 4hour.
# symbol: The stock symbol of the company.

# Query Params:
# from: The start date of the chart in the format YYYY-MM-DD.
# to: The end date of the chart in the format YYYY-MM-DD.

# Response:
"""
[
	{
		"date": "2023-03-02 16:00:00",
		"open": 145.92,
		"low": 145.72,
		"high": 146,
		"close": 145.79,
		"volume": 1492644
	}
]
"""

DAILY_CHART_EOD_ENDPOINT = "v3/historical-price-full/{symbol}"
# The FMP Daily Chart endpoint provides a daily chart for a given company. The chart displays the opening price, high price, low price, and closing price of the company's stock for each day in a specified date range. By default the limit is 5 years of historical data, to get data prior to this date, please use the to & from parameters with a limit of 5 years.

# Path Params:
# symbol: The stock symbol of the company.

# Query Params:
# from: The start date of the chart in the format YYYY-MM-DD.
# to: The end date of the chart in the format YYYY-MM-DD.
# serietype: The type of series. The user can specify 'line' or 'candle'.

# Response:
"""
{
	"symbol": "AAPL",
	"historical": [
		{
			"date": "2023-10-06",
			"open": 173.8,
			"high": 176.61,
			"low": 173.18,
			"close": 176.53,
			"adjClose": 176.53,
			"volume": 21712747,
			"unadjustedVolume": 21712747,
			"change": 2.73,
			"changePercent": 1.57077,
			"vwap": 175.44,
			"label": "October 06, 23",
			"changeOverTime": 0.0157077
		},
		{
			"date": "2023-10-05",
			"open": 173.79,
			"high": 175.45,
			"low": 172.68,
			"close": 174.91,
			"adjClose": 174.91,
			"volume": 48251046,
			"unadjustedVolume": 47369743,
			"change": 1.12,
			"changePercent": 0.64446,
			"vwap": 174.23,
			"label": "October 05, 23",
			"changeOverTime": 0.0064446
		}
	]
}
"""


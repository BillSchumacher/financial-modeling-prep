SPLITS_CALENDAR_ENDPOINT = 'v3/stock_split_calendar'
# Query params
# from: str
# to: str

# Response
"""
[
	{
		"date": "2023-04-05",
		"label": "April 05, 23",
		"symbol": "SHECY",
		"numerator": 5,
		"denominator": 2
	}
]
"""

SPLITS_HISTORICAL_ENDPOINT = "v3/historical-price-full/stock_split/{symbol}"
# Path Params
# symbol: str

# Response
"""
{
	"symbol": "AAPL",
	"historical": [
		{
			"date": "2020-08-31",
			"label": "August 31, 20",
			"numerator": 4,
			"denominator": 1
		}
	]
}
"""
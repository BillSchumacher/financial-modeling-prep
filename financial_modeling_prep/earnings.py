EARNINGS_CALENDAR_ENDPOINT = "v3/earnings_calendar"
# A list of upcoming & past earnings announcements for publicly traded companies, including the date, estimated earnings per share (EPS), and actual EPS (if available).

# Query Params:
# from: date (string) - The date to start the earnings calendar from.
# to: date (string) - The date to end the earnings calendar at.

# Response:
"""
[
	{
		"date": "2023-05-13",
		"symbol": "VIKASECO.NS",
		"eps": 0.01967,
		"epsEstimated": null,
		"time": "bmo",
		"revenue": 683268000,
		"revenueEstimated": null,
		"fiscalDateEnding": "2023-03-31",
		"updatedFromDate": "2023-12-04"
	}
]
"""

EARNINGS_HISTORICAL_AND_UPCOMING_ENDPOINT = "v3/historical/earnings_calendar/{symbol}"
# A list of historical & upcoming earnings announcements for a specific company, including the date, estimated EPS, and actual EPS.

# Path Parameters:
# symbol: string - The company’s stock symbol.

# Query Params:
# limit: int - The number of earnings to return. Default is 100

# Response:
"""
[
	{
		"date": "1998-10-14",
		"symbol": "AAPL",
		"eps": 0.0055,
		"epsEstimated": 0.00393,
		"time": "amc",
		"revenue": 1556000000,
		"revenueEstimated": 2450700000,
		"updatedFromDate": "2023-12-04",
		"fiscalDateEnding": "1998-09-25"
	}
]
"""

EARNINGS_CONFIRMED_ENDPOINT = "v4/earning_calendar_confirmed"
# A list of earnings announcements for publicly traded companies that have already been confirmed.

# Query Params:
# from: date (string) - The date to start the earnings calendar from.
# to: date (string) - The date to end the earnings calendar at.
# limit: int - The number of earnings to return. Default is 100

# Response:
"""
[
	{
		"symbol": "MS",
		"exchange": "NYSE",
		"time": "08:30",
		"when": "pre market",
		"date": "2023-04-19",
		"publicationDate": "2023-01-31",
		"title": "Morgan Stanley Schedules Quarterly Investor Conference Call | Business Wire",
		"url": "https://www.businesswire.com/news/home/20230131006096/en"
	}
]
"""

EARNINGS_SURPRISES_ENDPOINT = "v3/earnings_surprises/{symbol}"
# A list of earnings announcements for publicly traded companies that were either positive or negative surprises. This endpoint includes the date of the earnings announcement, the estimated EPS, the actual EPS, and the earnings surprise.

# Path Parameters:
# symbol: string - The company’s stock symbol.

# Response:
"""
[
	{
		"date": "2023-02-02",
		"symbol": "AAPL",
		"actualEarningResult": 1.88,
		"estimatedEarning": 1.94
	}
]
"""

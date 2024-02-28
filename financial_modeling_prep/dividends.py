DIVIDENDS_CALENDAR_ENDPOINT = "v3/stock_dividend_calendar"
# Query Params
# from: date
# to: date
# apikey: str

# Response
"""
[
  {
    "date": "2023-08-10",
    "label": "August 10, 23",
    "adjDividend": 0.93204,
    "symbol": "CSYZ.DE",
    "dividend": 0.93204,
    "recordDate": "2023-08-11",
    "paymentDate": "2023-08-18",
    "declarationDate": null
  },
  ...
]
"""

DIVIDENDS_HISTORICAL_ENDPOINT = "v3/historical_price_full/stock_dividend/{symbol}"
# Path Params
# symbol - in URI

# Response
"""
{
	"symbol": "AAPL",
	"historical": [
		{
			"date": "2023-02-10",
			"label": "February 10, 23",
			"adjDividend": 0.23,
			"dividend": 0.23,
			"recordDate": "2023-02-13",
			"paymentDate": "2023-02-16",
			"declarationDate": "2023-02-02"
		}
	]
}
"""
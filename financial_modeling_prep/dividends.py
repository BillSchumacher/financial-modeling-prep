"""Dividends module."""
DIVIDENDS_CALENDAR_ENDPOINT = "v3/stock_dividend_calendar"
DIVIDENDS_HISTORICAL_ENDPOINT = "v3/historical_price_full/stock_dividend/{symbol}"


class Dividends:
    """
    A class to access dividend information for stocks.

    Explanation:
    This class provides methods to retrieve dividends calendar
     for a date range and historical dividends for a specific stock.

    Methods:
    - get_dividends_calendar: Get dividends calendar for a date range.
    - get_dividends_historical: Get historical dividends for a stock.
    """

    def __init__(self, api):
        """
        Initializes the Dividends class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_dividends_calendar(self, from_date, to_date):
        """Get dividends calendar for a date range.

        Args:
            from_date (str): The start date
            to_date (str): The end date

        Returns: [
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
        ]
        """
        return self.api.get(
            DIVIDENDS_CALENDAR_ENDPOINT, params={"from": from_date, "to": to_date}
        )

    def get_dividends_historical(self, symbol):
        """Get historical dividends for a stock.

        Args:
            symbol (str): The stock symbol

        Returns: {
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
        return self.api.get(DIVIDENDS_HISTORICAL_ENDPOINT.format(symbol=symbol))

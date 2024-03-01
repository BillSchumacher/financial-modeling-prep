"""Split class."""
SPLITS_CALENDAR_ENDPOINT = "v3/stock_split_calendar"
SPLITS_HISTORICAL_ENDPOINT = "v3/historical-price-full/stock_split/{symbol}"


class Splits:
    """Splits class.

    Methods:
    - `calendar(from_, to)`: Get stock splits calendar.
    - `historical(symbol)`: Get historical stock splits for a symbol.
    """

    def __init__(self, api):
        """
        Initializes the Splits class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def calendar(self, from_: str, to: str):
        """Get stock splits calendar.

        Args:
            from_ (str): From date
            to (str): To date

        Returns: [
            {
                "date": "2023-04-05",
                "label": "April 05, 23",
                "symbol": "SHECY",
                "numerator": 5,
                "denominator": 2
            }
        ]
        """
        return self.api.get(SPLITS_CALENDAR_ENDPOINT, {"from": from_, "to": to})

    def historical(self, symbol: str):
        """Get historical stock splits for a symbol.

        Args:
            symbol (str): The stock symbol

        Returns: {
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
        return self.api.get(SPLITS_HISTORICAL_ENDPOINT.format(symbol=symbol))

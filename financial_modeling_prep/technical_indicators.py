"""Provides the technical indicator values for a given stock symbol."""
TECHNICAL_INDICATOR_ENDPOINT = "v3/technical_indicator/{timeframe}/{symbol}"


class TechnicalIndicators:
    """Provides the technical indicator values for a given stock symbol.

    Methods:
    - `get_technical_indicator(timeframe, symbol, indicator_type, period)`:
    Provides the technical indicator values for a given stock symbol.

    """

    def __init__(self, api):
        """
        Initializes the TechnicalIndicators class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_technical_indicator(self, timeframe, symbol, indicator_type, period):
        # pylint: disable=line-too-long
        """Provides the technical indicator values for a given stock symbol.

        Args:
            timeframe (str): 1min, 5min, 15min, 30min, 1hour, 4hour, 1day
            symbol (str): Ticker symbol
            indicator_type (str): sma, ema, wma, dema, tema, williams, rsi, adx, standarddeviation
            period (int): Number of data points used to calculate each moving average value

        Returns: [
            {
                "date": "2023-10-09 16:00:00",
                "open": 178.99,
                "high": 178.99,
                "low": 178.83,
                "close": 178.98,
                "volume": 1157282,
                "sma": 178.87493000000003
            }
        ]
        """  # noqa: E501
        return self.api.get(
            TECHNICAL_INDICATOR_ENDPOINT.format(timeframe=timeframe, symbol=symbol),
            params={"type": indicator_type, "period": period},
        )

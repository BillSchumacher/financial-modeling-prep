"""Forex module."""
FOREX_LIST_ENDPOINT = "v3/symbol/available-forex-currency-pairs"
FULL_QUOTE_LIST_ENDPOINT = "v3/quotes/forex"
FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
INTRADAY_FOREX_ENDPOINT = "v3/historical-chart/{timeframe}/{symbol}"
FOREX_DAILY_ENDPOINT = "v3/historical-price-full/{symbol}"


class Forex:
    """Forex class to get forex data from the Yahoo Finance API.

    Methods:
    - get_forex_list()
    - get_full_quote_list()
    - get_full_quote(symbol)
    - get_intraday_forex(timeframe, symbol, from_=None, to=None)
    - get_forex_daily(symbol)
    """

    def __init__(self, api):
        """
        Initializes the Forex class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_forex_list(self):
        """Provides a list of all currency pairs that are traded on the forex market.

        Returns: [
            {
                "symbol": "MYREUR",
                "name": "MYR/EUR",
                "currency": "EUR",
                "stockExchange": "CCY",
                "exchangeShortName": "FOREX"
            }
        ]
        """
        return self.api.get(FOREX_LIST_ENDPOINT)

    def get_full_quote_list(self):
        """Provides a list of all quotes for all currency pairs.

        Returns: [
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
        return self.api.get(FULL_QUOTE_LIST_ENDPOINT)

    def get_full_quote(self, symbol):
        """Provides a full quote for a specific currency pair.

        A complete quote comprises the current exchange rate for the currency pair,
         along with daily high, low, and open rates, the spread,
         and trading volume for the day.

        Args:
            symbol (str): the currency pair symbol

        Returns: [
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
        return self.api.get(FULL_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_intraday_forex(self, timeframe, symbol, from_=None, to=None):
        """Provides intraday price data for a specific currency pair.

        Args:
            timeframe (str): the timeframe of the data
             (1min, 5min, 15min, 30min, 1hour, 4hour)
            symbol (str): the currency pair symbol
            from_ (str): the start date of the data
            to (str): the end date of the data

        Returns: [
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
        return self.api.get(
            INTRADAY_FOREX_ENDPOINT.format(timeframe=timeframe, symbol=symbol),
            params={"from": from_, "to": to},
        )

    def get_forex_daily(self, symbol):
        """Provides daily price data for all currency pairs.

        Args:
            symbol (str): the currency pair symbol

        Returns: {
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
        return self.api.get(FOREX_DAILY_ENDPOINT.format(symbol=symbol))

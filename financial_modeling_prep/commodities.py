"""Commodities module to retrieve commodities data."""
COMMODITIES_LIST_ENDPOINT = "v3/symbol/available-commodities"
FULL_QUOTE_LIST_ENDPOINT = "v3/quotes/commodity"
FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
INTRADAY_COMMODITIES_ENDPOINT = "v3/historical-chart/{timeframe}/{symbol}"
COMMODITIES_DAILY_ENDPOINT = "v3/historical-price-full/{symbol}"


class Commodities:
    """
    A class to retrieve commodities data.

    Methods:
        get_commodities_list():
            Provides a list of available commodities.

        get_full_quote_list():
            Provides a list of all quotes for all commodities traded.

        get_full_quote(symbol):
            Provides real-time quotes for all commodities traded.

        get_intraday_commodities(timeframe, symbol, from_date=None, to_date=None):
            Provides intraday price data for all commodities traded.

        get_commodities_daily(symbol):
            Provides daily price data for all commodities traded.
    """

    def __init__(self, api):
        """
        Initializes the Commodities class with the provided API object.

        Args:
            api: The API object for interacting with the Financial Modeling Prep API.

        Returns:
            None
        """
        self.api = api

    def get_commodities_list(self):
        """Provides a list of available commodities.

        Returns:
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
        return self.api.get(COMMODITIES_LIST_ENDPOINT)

    def get_full_quote_list(self):
        """Provides a list of all quotes for all commodities.

        Returns: [
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
        return self.api.get(FULL_QUOTE_LIST_ENDPOINT)

    def get_full_quote(self, symbol):
        """Provides real-time quotes for all commodities.

        Args:
            symbol (str): The commodity symbol.

        Returns: [
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
        return self.api.get(FULL_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_intraday_commodities(self, timeframe, symbol, from_date=None, to_date=None):
        """Provides intraday price data for all commodities that are traded.

        Args:
            timeframe (str): The timeframe for the chart data.
               Available values: 1min, 5min, 15min, 30min, 1hour, 4hour.
            symbol (str): The commodity symbol.
            from_date (str, optional): From date (YYYY-MM-DD). Defaults to None.
            to_date (str, optional): To date (YYYY-MM-DD). Defaults to None.

        Returns: [
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
        return self.api.get(
            INTRADAY_COMMODITIES_ENDPOINT.format(timeframe=timeframe, symbol=symbol),
            params={"from": from_date, "to": to_date},
        )

    def get_commodities_daily(self, symbol):
        """Provides daily price data for all commodities that are traded.

        Args:
            symbol (str): The commodity symbol.

        Returns: {
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
        return self.api.get(COMMODITIES_DAILY_ENDPOINT.format(symbol=symbol))

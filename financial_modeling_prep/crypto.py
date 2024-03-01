"""CryptoCurrency class for interacting with cryptocurrency data."""
CRYPTOCURRENCIES_LIST_ENDPOINT = "v3/symbol/available-crpytocurrencies"
FULL_QUOTE_LIST_ENDPOINT = "v3/quotes/crypto"
FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
INTRADAY_CRYPTOCURRENCY_ENDPOINT = "v3/historical-chart/{timeframe}/{symbol}"
CRYPTOCURRENCY_DAILY_ENDPOINT = "v3/historical-price-full/{symbol}"


class CryptoCurrency:
    """
    A class to interact with cryptocurrency data.

    Explanation:
    This class provides methods to retrieve information about cryptocurrencies,
     including lists of available cryptocurrencies, full quote lists,
     full quotes for specific cryptocurrencies, intraday price data,
     and daily price data.

    Methods:
    - get_cryptocurrencies_list: Get a list of available cryptocurrencies.
    - get_full_quote_list: Get a full quote list for all cryptocurrencies.
    - get_full_quote: Get a full quote for a specific cryptocurrency.
    - get_intraday_cryptocurrency: Get intraday price data for a cryptocurrency.
    - get_cryptocurrency_daily: Get daily price data for a cryptocurrency.
    """

    def __init__(self, api):
        """
        Initializes the CryptoCurrency class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_cryptocurrencies_list(self):
        """Get a list of available cryptocurrencies.

        Returns: [
            {
                "symbol": "NFTXUSD",
                "name": "NFTX",
                "currency": "USD",
                "stockExchange": "CCC",
                "exchangeShortName": "CRYPTO"
            }
        ]
        """
        return self.api.get(CRYPTOCURRENCIES_LIST_ENDPOINT)

    def get_full_quote_list(self):
        """Get a full quote list for all cryptocurrencies.

        Returns:[
            {
                "symbol": "SKMUSD",
                "name": "Skrumble Network USD",
                "price": 0.00041769692,
                "changesPercentage": -2.4658,
                "change": 0,
                "dayLow": 0.00041426468,
                "dayHigh": 0.0004249561,
                "yearHigh": 0.002322,
                "yearLow": 0.000236,
                "marketCap": 426753,
                "priceAvg50": 0.00041162,
                "priceAvg200": 0.0004344,
                "volume": 16571,
                "avgVolume": 15559,
                "exchange": "CRYPTO",
                "open": 0.00042011592,
                "previousClose": 0.00042011592,
                "eps": null,
                "pe": null,
                "earningsAnnouncement": null,
                "sharesOutstanding": 1021681024,
                "timestamp": 1677793500
            }
        ]
        """
        return self.api.get(FULL_QUOTE_LIST_ENDPOINT)

    def get_full_quote(self, symbol):
        """Get a full quote for a cryptocurrency.

        Args:
            symbol (str): The symbol of the cryptocurrency.

        Returns:[
            {
                "symbol": "BTCUSD",
                "name": "Bitcoin USD",
                "price": 23437.678,
                "changesPercentage": -0.4946,
                "change": -116.4961,
                "dayLow": 23249.398,
                "dayHigh": 23739.139,
                "yearHigh": 48086.836,
                "yearLow": 15599.047,
                "marketCap": 452495264650,
                "priceAvg50": 22692.229,
                "priceAvg200": 19745.85,
                "volume": 20698836992,
                "avgVolume": 21781427552,
                "exchange": "CRYPTO",
                "open": 23641.416,
                "previousClose": 23641.416,
                "eps": null,
                "pe": null,
                "earningsAnnouncement": null,
                "sharesOutstanding": 19306318,
                "timestamp": 1677793620
            }
        ]
        """
        return self.api.get(FULL_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_intraday_cryptocurrency(self, timeframe, symbol):
        """Get intraday price data for a cryptocurrency.

        Args:
            timeframe (str): The timeframe for the chart data.
             Supported values are "1min", "5min", "15min", "30min", "1hour", "4hour"
            symbol (str): The symbol of the cryptocurrency.

        Returns:[
            {
                "date": "2023-03-02 16:48:00",
                "open": 23435.18,
                "low": 23429.7,
                "high": 23445,
                "close": 23439,
                "volume": 10
            }
        ]
        """
        return self.api.get(
            INTRADAY_CRYPTOCURRENCY_ENDPOINT.format(timeframe=timeframe, symbol=symbol)
        )

    def get_cryptocurrency_daily(self, symbol):
        """Get daily price data for a cryptocurrency.

        Args:
            symbol (str): The symbol of the cryptocurrency.


        Returns:{
            "symbol": "BTCUSD",
            "historical": [
                {
                    "date": "2023-03-02",
                    "open": 23641.416,
                    "high": 23739.139,
                    "low": 23249.398,
                    "close": 23434.432,
                    "adjClose": 23434.432,
                    "volume": 20797822976,
                    "unadjustedVolume": 20797822976,
                    "change": -206.98,
                    "changePercent": -0.87551439,
                    "vwap": 23474.32,
                    "label": "March 02, 23",
                    "changeOverTime": -0.0087551439
                }
            ]
        }
        """
        return self.api.get(CRYPTOCURRENCY_DAILY_ENDPOINT.format(symbol=symbol))

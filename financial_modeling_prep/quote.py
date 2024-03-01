"""This module contains the Quote class."""
FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
QUOTE_ORDER_ENDPOINT = "v3/quote-order/{symbol}"
SIMPLE_QUOTE = "v3/quote-short/{symbol}"
OTC_QUOTE_ENDPOINT = "v3/otc/real-time-price/{symbol}"
EXCHANGE_PRICES_ENDPOINT = "v3/quotes/{exchange}"
STOCK_PRICE_CHANGE_ENDPOINT = "v3/stock-price-change/{symbol}"
AFTERMARKET_TRADE_ENDPOINT = "v4/pre-post-market-trade/{symbol}"
AFTERMARKET_QUOTE_ENDPOINT = "v4/pre-post-market/{symbol}"
BATCH_QUOTE_ENDPOINT = "v4/batch-pre-post-market/{symbol}"
BATCH_TRADE_ENDPOINT = "v4/batch-pre-post-market-trade/{symbol}"
LAST_FOREX_ENDPOINT = "v4/forex/last/{pair}"
LAST_CRYPTO_ENDPOINT = "v4/crypto/last/{pair}"
REALTIME_PRICE_ENDPOINT = "v3/stock/real-time-price/{symbol}"
ALL_LIVE_PRICES_SHORT_ENDPOINT = "v3/stock/real-time-price"
LIVE_FULL_PRICE_WITH_ORDERS_ENDPOINT = "v3/stock/full/real-time-price/{symbol}"
ALL_LIVE_FULL_PRICE_WITH_ORDERS_ENDPOINT = "v3/stock/full/real-time-price"
FOREX_PRICES_ENDPOINT = "v3/fx/{pair}"
ALL_FOREX_PRICES_ENDPOINT = "v3/fx"


class Quote:
    """Quote class.

    Methods:
    - get_full_quote(symbol)
    - get_quote_order(symbol)
    - get_simple_quote(symbol)
    - get_otc_quote(symbol)
    - get_exchange_prices(exchange)
    - get_stock_price_change(symbol)
    - get_aftermarket_trade(symbol)
    - get_aftermarket_quote(symbol)
    - get_batch_quote(symbol)
    - get_batch_trade(symbol)
    - get_last_forex(pair)
    - get_last_crypto(pair)
    - get_realtime_price(symbol)
    - get_all_live_prices_short()
    - get_live_full_price_with_orders(symbol)
    - get_all_live_full_price_with_orders()
    - get_forex_prices(pair)
    - get_all_forex_prices()
    """

    def __init__(self, api):
        """
        Initializes the Quote class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_full_quote(self, symbol):
        """This endpoint gives you the latest bid and ask prices for a stock.

         As well as the volume and last trade price in real time.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "price": 145.775,
                "changesPercentage": 0.32,
                "change": 0.465,
                "dayLow": 143.9,
                "dayHigh": 146.71,
                "yearHigh": 179.61,
                "yearLow": 124.17,
                "marketCap": 2306437439846,
                "priceAvg50": 140.8724,
                "priceAvg200": 147.18594,
                "exchange": "NASDAQ",
                "volume": 42478176,
                "avgVolume": 73638864,
                "open": 144.38,
                "previousClose": 145.31,
                "eps": 5.89,
                "pe": 24.75,
                "earningsAnnouncement": "2023-04-26T10:59:00.000+0000",
                "sharesOutstanding": 15821899776,
                "timestamp": 1677790773
            }
        ]
        """
        return self.api.get(FULL_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_quote_order(self, symbol):
        """This endpoint gives you the latest bid and ask prices for a stock.

         As well as the volume and last trade price in real time.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "price": 145.855,
                "changesPercentage": 0.3751,
                "change": 0.545,
                "dayLow": 143.9,
                "dayHigh": 146.71,
                "yearHigh": 179.61,
                "yearLow": 124.17,
                "marketCap": 2307703191828,
                "priceAvg50": 140.8724,
                "priceAvg200": 147.18594,
                "exchange": "NASDAQ",
                "volume": 42609394,
                "avgVolume": 73638864,
                "open": 144.38,
                "previousClose": 145.31,
                "eps": 5.89,
                "pe": 24.76,
                "earningsAnnouncement": "2023-04-26T10:59:00.000+0000",
                "sharesOutstanding": 15821899776,
                "timestamp": 1677790784
            }
        ]
        """
        return self.api.get(QUOTE_ORDER_ENDPOINT.format(symbol=symbol))

    def get_simple_quote(self, symbol):
        """This endpoint gives you a simplified view of a stock's quote.

         Including the current price, volume, and last trade price.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "price": 145.85,
                "volume": 42822124
            }
        ]
        """
        return self.api.get(SIMPLE_QUOTE.format(symbol=symbol))

    def get_otc_quote(self, symbol):
        """This endpoint gives you the latest bid and ask prices for an OTC stock.

        As well as the volume and last trade price in real time.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "prevClose": 44,
                "high": 44,
                "low": 44,
                "open": 44,
                "volume": 165,
                "lastSalePrice": 44,
                "fmpLast": 44,
                "lastUpdated": "2023-03-02T21:00:09.663+0000",
                "symbol": "BATRB"
            }
        ]
        """
        return self.api.get(OTC_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_exchange_prices(self, exchange):
        """This endpoint gives you a list of all exchange prices for a given stock.

        Args:
            exchange: the stock exchange

        Returns: [
            {
                "symbol": "A",
                "name": "Agilent Technologies, Inc.",
                "price": 141.69,
                "changesPercentage": 3.0398,
                "change": 4.18,
                "dayLow": 136.2,
                "dayHigh": 141.69,
                "yearHigh": 160.26,
                "yearLow": 112.52,
                "marketCap": 41920403400,
                "priceAvg50": 151.0052,
                "priceAvg200": 136.4237,
                "exchange": "NYSE",
                "volume": 1618424,
                "avgVolume": 1275277,
                "open": 136.3,
                "previousClose": 137.51,
                "eps": 4.18,
                "pe": 33.9,
                "earningsAnnouncement": "2023-02-28T21:00:00.000+0000",
                "sharesOutstanding": 295860000,
                "timestamp": 1677790798
            }
        ]
        """
        return self.api.get(EXCHANGE_PRICES_ENDPOINT.format(exchange=exchange))

    def get_stock_price_change(self, symbol):
        """Change in a stock's price over a given period of time.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "1D": 0.4129,
                "5D": -1.2186,
                "1M": -3.25554,
                "3M": -1.28543,
                "6M": -6.35389,
                "ytd": 16.66267,
                "1Y": -12.39793,
                "3Y": 95.32144,
                "5Y": 231.21843,
                "10Y": 872.61662,
                "max": 146038.67166
            }
        ]
        """
        return self.api.get(STOCK_PRICE_CHANGE_ENDPOINT.format(symbol=symbol))

    def get_aftermarket_trade(self, symbol):
        """Information on trades that have occurred in the aftermarket.

        Args:
            symbol: the stock symbol

        Returns: {
            "symbol": "AAPL",
            "price": 145.89,
            "size": 100,
            "timestamp": 1677790907243
        }
        """
        return self.api.get(AFTERMARKET_TRADE_ENDPOINT.format(symbol=symbol))

    def get_aftermarket_quote(self, symbol):
        """Latest bid and ask prices for a stock in the aftermarket.

        Args:
            symbol: the stock symbol

        Returns: {
            "symbol": "AAPL",
            "ask": 145.9,
            "bid": 145.86,
            "asize": 1,
            "bsize": 1,
            "timestamp": 1677790916294
        }
        """
        return self.api.get(AFTERMARKET_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_batch_quote(self, symbol):
        """This endpoint gives you quotes for multiple stocks at once.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "ask": 145.87,
                "bid": 145.81,
                "asize": 1,
                "bsize": 2,
                "timestamp": 1677790923061
            }
        ]
        """
        return self.api.get(BATCH_QUOTE_ENDPOINT.format(symbol=symbol))

    def get_batch_trade(self, symbol):
        """Gets trades for multiple stocks at once.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "price": 145.861,
                "size": 100,
                "timestamp": 1677790926832
            }
        ]
        """
        return self.api.get(BATCH_TRADE_ENDPOINT.format(symbol=symbol))

    def get_last_forex(self, pair):
        """This endpoint gives you the latest price for a currency pair.

        Args:
            pair: the currency pair

        Returns: {
            "symbol": "EURUSD",
            "ask": 1.07833,
            "bid": 1.07832,
            "timestamp": 1701956301
        }
        """
        return self.api.get(LAST_FOREX_ENDPOINT.format(pair=pair))

    def get_last_crypto(self, pair):
        """This endpoint gives you the latest price for a cryptocurrency.

        Args:
            pair: the cryptocurrency pair

        Returns: {
            "symbol": "BTCUSD",
            "price": 23487,
            "size": 0.00028901,
            "timestamp": 1677788306
        }
        """
        return self.api.get(LAST_CRYPTO_ENDPOINT.format(pair=pair))

    def get_realtime_price(self, symbol):
        """This endpoint gives you the latest price.

         For a stock, ETF, mutual fund, or cryptocurrency.

        Args:
            symbol: the stock symbol

        Returns: {
            "symbol": "AAPL",
            "price": 145.78
        }
        """
        return self.api.get(REALTIME_PRICE_ENDPOINT.format(symbol=symbol))

    def get_all_live_prices_short(self):
        """This endpoint gives you a list of all real-time stock prices.

        Returns: {
            "stockList": [
                {
                    "symbol": "RENUSD",
                    "price": 0.1269
                }
            ]
        }
        """
        return self.api.get(ALL_LIVE_PRICES_SHORT_ENDPOINT)

    def get_live_full_price_with_orders(self, symbol):
        """This endpoint gives you the latest bid and ask prices for a stock.

         As well as the volume and last trade price in real time.

        Args:
            symbol: the stock symbol

        Returns: [
            {
                "bidSize": 16,
                "askPrice": 145.74,
                "volume": 41710959,
                "askSize": 4,
                "bidPrice": 145.73,
                "lastSalePrice": 145.74,
                "lastSaleSize": 300,
                "lastSaleTime": 1677790688967,
                "fmpLast": 145.74,
                "lastUpdated": 1677790688804,
                "symbol": "AAPL"
            }
        ]
        """
        return self.api.get(LIVE_FULL_PRICE_WITH_ORDERS_ENDPOINT.format(symbol=symbol))

    def get_all_live_full_price_with_orders(self):
        """This endpoint gives you a list of all real-time full stock prices.

        Returns: [
            {
                "bidSize": 0,
                "askPrice": 0,
                "volume": 25297.60463177,
                "askSize": 0,
                "bidPrice": 0,
                "lastSalePrice": 1.13155,
                "lastSaleSize": 401.95,
                "lastSaleTime": 1677783619,
                "fmpLast": 1.13155,
                "lastUpdated": 1677783619,
                "symbol": "LSKUSD"
            }
        ]
        """
        return self.api.get(ALL_LIVE_FULL_PRICE_WITH_ORDERS_ENDPOINT)

    def get_forex_prices(self, pair):
        """This endpoint gives you the latest bid and ask prices for a currency pair.

        Args:
            pair: the currency pair

        Returns: [
            {
                "ticker": "EUR/USD",
                "bid": "1.18382",
                "ask": "1.18386",
                "open": "1.18458",
                "low": "1.18193",
                "high": "1.18837",
                "changes": -0.062469398436573544,
                "date": "2020-09-06 20:41:57"
            }
        ]
        """
        return self.api.get(FOREX_PRICES_ENDPOINT.format(pair=pair))

    def get_all_forex_prices(self):
        """This endpoint gives you a list of all foreign exchange (FX) prices.

        Returns: [
            {
                "ticker": "USD/JPY",
                "bid": "136.664",
                "ask": "136.664",
                "open": "136.178",
                "low": "136.024",
                "high": "137.106",
                "changes": 0.48599999999999,
                "date": "2023-03-02 15:59:17"
            }
        ]
        """
        return self.api.get(ALL_FOREX_PRICES_ENDPOINT)

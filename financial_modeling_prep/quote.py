FULL_QUOTE_ENDPOINT = "v3/quote/{symbol}"
# This endpoint gives you the latest bid and ask prices for a stock, as well as the volume and last trade price in real time.
# Path params
# symbol: the stock symbol

# Response
"""
[
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

QUOTE_ORDER_ENDPOINT = "v3/quote-order/{symbol}"
# This endpoint gives you a simplified view of a stock's quote, including the current price, volume, and last trade price.
# Path params
# symbol: the stock symbol

# Response:
"""
[
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

SIMPLE_QUOTE = "v3/quote-short/{symbol}"
# Get a simple quote for a stock, including the price, change, and volume. This endpoint can be used to get a quick snapshot of a stock's performance or to calculate its valuation.

# Path params
# symbol: the stock symbol

# Response:
"""
[
	{
		"symbol": "AAPL",
		"price": 145.85,
		"volume": 42822124
	}
]
"""

OTC_QUOTE_ENDPOINT = "v3/otc/real-time-price/{symbol}"
# This endpoint gives you the latest bid and ask prices for an over-the-counter (OTC) stock, as well as the volume and last trade price in real time.
# Path params
# symbol: the stock symbol

# Response:
"""
[
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

EXCHANGE_PRICES_ENDPOINT = "v3/quotes/{exchange}"
# This endpoint gives you a list of all exchange prices for a given stock.

# Path params
# exchange: the stock exchange

# Response:
"""
[
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

STOCK_PRICE_CHANGE_ENDPOINT = "v3/stock-price-change/{symbol}"
# This endpoint gives you the change in a stock's price over a given period of time.

# Path params
# symbol: the stock symbol

# Response:
"""
[
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

AFTERMARKET_TRADE_ENDPOINT = "v4/pre-post-market-trade/{symbol}"
# This endpoint gives you information on trades that have occurred in the aftermarket.

# Path params
# symbol: the stock symbol

# Response:
"""
{
	"symbol": "AAPL",
	"price": 145.89,
	"size": 100,
	"timestamp": 1677790907243
}
"""

AFTERMARKET_QUOTE_ENDPOINT = "v4/pre-post-market/{symbol}"
# This endpoint gives you the latest bid and ask prices for a stock in the aftermarket.

# Path params
# symbol: the stock symbol

# Response:
"""
{
	"symbol": "AAPL",
	"ask": 145.9,
	"bid": 145.86,
	"asize": 1,
	"bsize": 1,
	"timestamp": 1677790916294
}
"""

BATCH_QUOTE_ENDPOINT = "v4/batch-pre-post-market/{symbol}"
# This endpoint gives you quotes for multiple stocks at once.

# Path params
# symbol: the stock symbol

# Response:
"""
[
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

BATCH_TRADE_ENDPOINT = "v4/batch-pre-post-market-trade/{symbol}"
# This endpoint gives you the ability to place trades for multiple stocks at once.

# Path params
# symbol: the stock symbol

# Response:
"""
[
	{
		"symbol": "AAPL",
		"price": 145.861,
		"size": 100,
		"timestamp": 1677790926832
	}
]
"""

LAST_FOREX_ENDPOINT = "v4/forex/last/{pair}"
# This endpoint gives you the latest bid and ask prices for a currency pair.

# Path params
# pair: the currency pair

# Response:
"""
{
	"symbol": "EURUSD",
	"ask": 1.07833,
	"bid": 1.07832,
	"timestamp": 1701956301
}
"""

LAST_CRYPTO_ENDPOINT = "v4/crypto/last/{pair}"
# This endpoint gives you the latest price for a cryptocurrency.

# Path params
# pair: the cryptocurrency pair

# Response:
"""
{
	"symbol": "BTCUSD",
	"price": 23487,
	"size": 0.00028901,
	"timestamp": 1677788306
}
"""

REALTIME_PRICE_ENDPOINT = "v3/stock/real-time-price/{symbol}"
# This endpoint gives you the latest price for a stock, ETF, mutual fund, or cryptocurrency.

# Path params
# symbol: the stock symbol

# Response:
"""
{
	"symbol": "AAPL",
	"price": 145.78
}
"""

ALL_LIVE_PRICES_SHORT_ENDPOINT = "v3/stock/real-time-price"
# This endpoint gives you a list of all real-time stock prices.

# Response:
"""
{
	"stockList": [
		{
			"symbol": "RENUSD",
			"price": 0.1269
		}
	]
}
"""

LIVE_FULL_PRICE_WITH_ORDERS_ENDPOINT = "v3/stock/full/real-time-price/{symbol}"
# This endpoint gives you the latest bid and ask prices for a stock, as well as the volume and last trade price, in real time.

# Path params
# symbol: the stock symbol

# Response:
"""
[
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

ALL_LIVE_FULL_PRICE_WITH_ORDERS_ENDPOINT = "v3/stock/full/real-time-price"
# This endpoint gives you a list of all real-time full stock prices.

# Response:
"""
[
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

FOREX_PRICES_ENDPOINT = "v3/fx/{pair}"
# This endpoint gives you the latest bid and ask prices for a currency pair.

# Path params
# pair: the currency pair

# Response:
"""
[
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

ALL_FOREX_PRICES_ENDPOINT = "v3/fx"
# This endpoint gives you a list of all foreign exchange (FX) prices.

# Response:
"""
[
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


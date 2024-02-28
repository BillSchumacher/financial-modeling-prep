"""

Login: { "event": "login", "data": { "apiKey": "your_api_key" } }
Subscribe: { "event": "subscribe", "data": { "ticker": "aapl" } }

Response:
s: Ticker related to the asset.
t: Timestamp
type: Trade type (Communicates what type of price update this is. Will always be 'T' for last trade message, 'Q' for top-of-book update message, and 'B' for trade break messages.)
ap: The current lowest ask price. Only available for Quote updates, null otherwise.
as: The number of shares at the ask price. Only available for Quote updates, null otherwise.
bs: The number shares at the bid price. Only available for Quote updates, null otherwise.
bp: The current highest bid price. Only available for Quote updates, null otherwise.
lp: The last price the last trade was executed at. Only available for Trade and Break updates, null otherwise.
ls: The amount of shares (volume) traded at the last price. Only available for Trade and Break updates, null otherwise.
"""


COMPANY_WEBSOCKET_ENDPOINT = "wss://websockets.financemodelingprep.com"
# Provides a Real-time feed of stock price and quote data.

# Response:
"""
{
	"s": "spot",
	"t": 1645216790788174600,
	"type": "Q",
	"ap": 152.46,
	"as": 200,
	"bp": 152.31,
	"bs": 100,
	"lp": 152.17,
	"ls": 100
}
"""

CRYPTO_WEBSOCKET_ENDPOINT = "wss://crypto.financemodelingprep.com"
# Provides a Real-time feed of cryptocurrency price and quote data.

# Login: { "event": "login", "data": { "apiKey": "your_api_key" } }
# Subscribe: { "event": "subscribe", "data": { "ticker": "btcusd" } }

# Response:
"""
{
	"s": "btcusd",
	"t": 16487238632060000000,
	"e": "binance",
	"type": "Q",
	"bs": 0.00689248,
	"bp": 47244.8,
	"as": 1.72784126,
	"ap": 47244.9
}
"""

FOREX_WEBSOCKET_ENDPOINT = "wss://forex.financemodelingprep.com"
# Provides a Real-time feed of forex price and quote data.

# Login: { "event": "login", "data": { "apiKey": "your_api" } }
# Subscribe: { "event": "subscribe", "data": { "ticker": "EURUSD" } }

# Response:
"""
{
	"s": "eurusd",
	"t": 1701958248213,
	"type": "Q",
	"ap": 1.07865,
	"as": 1000000,
	"bp": 1.07856,
	"bs": 1000000
}
"""

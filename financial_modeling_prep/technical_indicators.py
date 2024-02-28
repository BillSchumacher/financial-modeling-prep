TECHNICAL_INDICATOR_ENDPOINT = "v3/technical_indicator/{timeframe}/{symbol}"
# Provides the technical indicator values for a given stock symbol.

# Path Params
# timeframe: str - 1min, 5min, 15min, 30min, 1hour, 4hour, 1day
# symbol: str
# type: str - sma, ema, wma, dema, tema, williams, rsi, adx, standarddeviation
# Query Params
# period: int

# Response
"""
[
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
"""

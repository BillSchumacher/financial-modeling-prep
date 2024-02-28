MARKET_INDEX_ENDPOINT = "v3/quotes/index"
# The FMP Market Index endpoint provides a list of all the major stock market indices, such as the S&P 500, the Dow Jones Industrial Average, and the Nasdaq Composite Index. This information can be used by investors to track the performance of the overall stock market and to identify sectors and industries that are outperforming or underperforming the market.

# Response:
"""
[
	{
		"symbol": "^PSE",
		"price": 4317.4824,
		"extendedPrice": null,
		"change": 2.1523,
		"dayHigh": 4318.9136,
		"dayLow": 4244.7,
		"previousClose": 4315.33,
		"volume": null,
		"open": 4315.33,
		"close": null,
		"lastTradeTime": "2022-10-05T17:04:00.000Z",
		"lastExtendedTradeTime": null,
		"updatedAt": "2022-10-05T17:19:02.530Z",
		"createdAt": "2022-09-23T20:08:00.942Z",
		"type": "stock",
		"name": "NYSE Arca Tech 100 Index",
		"range": "3753.82 - 5380.34",
		"yearHigh": 5380.34,
		"yearLow": 3753.82,
		"priceAvg50": null,
		"priceAvg200": null,
		"changesPercentage": 0.0499
	}
]
"""


SECTOR_PE_RATIO_ENDPOINT = "v4/sector_price_earning_ratio"
# The FMP Sector PE Ratio endpoint provides the price-to-earnings (PE) ratio for each sector of the stock market. The PE ratio is a measure of how expensive a stock is relative to its earnings. Investors can use the sector PE ratio to identify sectors that are overvalued or undervalued.

# Query Params:
# date: date in the format 'YYYY-MM-DD'
# exchange: exchange name (optional)

# Response:
"""
[
	{
		"date": "2023-03-03",
		"sector": "Basic Materials",
		"exchange": "NYSE",
		"pe": "18.33197269872979"
	}
]
"""

INDUSTRY_PE_RATIO_ENDPOINT = "v4/industry_price_earning_ratio"
# The FMP Industry PE Ratio endpoint provides the price-to-earnings (PE) ratio for each industry of the stock market. The PE ratio is a measure of how expensive a stock is relative to its earnings. Investors can use the industry PE ratio to identify industries that are overvalued or undervalued.

# Query Params:
# date: date in the format 'YYYY-MM-DD'
# exchange: exchange name (optional)

# Response:
"""
[
	{
		"date": "2023-03-03",
		"industry": "Advertising Agencies",
		"exchange": "NYSE",
		"pe": "3.4058333333333337"
	}
]
"""

SECTOR_PERFORMANCE_ENDPOINT = "v3/sectors-performance"
# The FMP Sector Performance endpoint provides the performance of each sector of the stock market over a specified period of time. This information can be used by investors to identify sectors that are outperforming or underperforming the market.

# Response:
"""
[
	{
		"sector": "Real Estate",
		"changesPercentage": 47.3976468395652
	},
	{
		"sector": "Technology",
		"changesPercentage": 211.59579270694476
	}
]
"""

SECTOR_HISTORICAL_PERFORMANCE_ENDPOINT = "v3/historical-sectors-performance"
# The FMP Sector Historical endpoint provides historical data on the performance of each sector of the stock market. This information can be used by investors to identify trends in sector performance and to make informed investment decisions.

# Query Params:
# limit: int (optional) - 50

# Response:
"""
[
	{
		"date": "2023-10-18",
		"utilitiesChangesPercentage": -1.25732,
		"basicMaterialsChangesPercentage": -1.66297,
		"communicationServicesChangesPercentage": -1.04542,
		"conglomeratesChangesPercentage": null,
		"consumerCyclicalChangesPercentage": -1.38072,
		"consumerDefensiveChangesPercentage": -0.23968,
		"energyChangesPercentage": 0.18781,
		"financialChangesPercentage": null,
		"financialServicesChangesPercentage": -0.59453,
		"healthcareChangesPercentage": -1.15814,
		"industrialsChangesPercentage": -1.50882,
		"realEstateChangesPercentage": -1.15307,
		"servicesChangesPercentage": null,
		"technologyChangesPercentage": -0.46983
	}
]
"""

MARKET_BIGGEST_GAINERS_ENDPOINT = "v3/stock_market/gainers"
# The FMP Market Biggest Gainers endpoint provides a list of the stocks that have gained the most value on a given day. This information can be used by investors to identify stocks that are momentum and to potential investment opportunities.

# Response:
"""
[
	{
		"symbol": "PIK",
		"name": "Kidpik Corp.",
		"change": 0.27,
		"price": 1.8,
		"changesPercentage": 17.6471
	}
]
"""

MARKET_BIGGEST_LOSERS_ENDPOINT = "v3/stock_market/losers"
# The FMP Market Biggest Losers endpoint provides a list of the stocks that have lost the most value on a given day. This information can be used by investors to identify stocks that are underperforming and to potential trading opportunities.

# Response:
"""
[
	{
		"symbol": "DSLVF",
		"name": "VelocityShares 3x Inverse Silver ETN Linked to the S&P GSCI Silver Index ER",
		"change": -0.13,
		"price": 1.13,
		"changesPercentage": -10.3175
	}
]
"""

MARKET_MOST_ACTIVE_ENDPOINT = "v3/stock_market/actives"
# The FMP Market Most Active endpoint provides a list of the stocks that have the highest trading volume on a given day. This information can be used by investors to identify stocks that are liquid and to potential trading opportunities.

# Response:
"""
[
	{
		"symbol": "MU",
		"name": "Micron Technology, Inc.",
		"change": 2.24,
		"price": 53.96,
		"changesPercentage": 4.331
	}
]
"""

ANALYSIS_BY_SYMBOL_ENDPOINT = "v4/commitment_of_traders_report_analysis/{symbol}"
# Provides an analysis of the Commitment of Traders (COT) report for a given symbol.

# Path Params:
# symbol: str - stock symbol

# Response:
"""
[
	{
		"symbol": "M6",
		"date": "2022-08-23 00:00:00",
		"sector": "CURRENCIES",
		"currentLongMarketSituation": 0.43,
		"currentShortMarketSituation": 0.57,
		"marketSituation": "Bearish",
		"previousLongMarketSituation": 0.46,
		"previousShortMarketSituation": 0.55,
		"previousMarketSituation": "Bearish",
		"netPostion": -31316,
		"previousNetPosition": -21371,
		"changeInNetPosition": 0,
		"marketSentiment": "Bearish",
		"reversalTrend": false,
		"name": "Mexican Peso (M6)",
		"exchange": "MEXICAN PESO - CHICAGO MERCANTILE EXCHANGE"
	}
]
"""

ANALYSIS_BY_DATES_ENDPOINT = "v4/commitment_of_traders_report_analysis"
# Provides an analysis of the Commitment of Traders (COT) report for a given date range.

# Query Params:
# from: date in the format 'YYYY-MM-DD'
# to: date in the format 'YYYY-MM-DD'

# Response:
"""
[
	{
		"symbol": "T6",
		"date": "2022-08-23 00:00:00",
		"sector": "CURRENCIES",
		"currentLongMarketSituation": 0.77,
		"currentShortMarketSituation": 0.23,
		"marketSituation": "Bullish",
		"previousLongMarketSituation": 0.69,
		"previousShortMarketSituation": 0.22,
		"previousMarketSituation": "Bullish",
		"netPostion": 6885,
		"previousNetPosition": 5925,
		"changeInNetPosition": 16.2,
		"marketSentiment": "Increasing Bullish",
		"reversalTrend": false,
		"name": "South African Rand (T6)",
		"exchange": "SO AFRICAN RAND - CHICAGO MERCANTILE EXCHANGE"
	}
]
"""

REPORT_BY_SYMBOL = "v4/commitment_of_traders_report/{symbol}"
# Provides the Commitment of Traders (COT) report for a given symbol.

# Path Params:
# symbol: str - stock symbol

# Response:
"""
[
	{
		"symbol": "M6",
		"date": "2022-08-23 00:00:00",
		"sector": "CURRENCIES",
		"as_of_date_in_form_yyyy_mm_dd": "2022-08-23T04:00:00.000Z",
		"cftc_market_code_in_initials": "CME",
		"cftc_contract_market_code": "095741",
		"cftc_market_code": null,
		"cftc_region_code": "00",
		"cftc_commodity_code": "095",
		"open_interest_all": 205575,
		"noncomm_positions_long_all": 103056,
		"noncomm_positions_short_all": 134372,
		"noncomm_postions_spread_all": 1366,
		"comm_positions_long_all": 93894,
		"comm_positions_short_all": 66404,
		"tot_rept_positions_long_all": 0,
		"tot_rept_positions_short_all": 202142,
		"nonrept_positions_long_all": 7259,
		"nonrept_positions_short_all": 3433,
		"open_interest_old": 205575,
		"noncomm_positions_long_old": 103056,
		"noncomm_positions_short_old": 134372,
		"noncomm_positions_spread_old": 1366,
		"comm_positions_long_old": 93894,
		"comm_positions_short_old": 66404,
		"tot_rept_positions_long_old": 198316,
		"tot_rept_positions_short_old": 202142,
		"nonrept_positions_long_old": 7259,
		"nonrept_positions_short_old": 3433,
		"open_interest_other": 0,
		"noncomm_positions_long_other": 0,
		"noncomm_positions_short_other": 0,
		"noncomm_positions_spread_other": 0,
		"comm_positions_long_other": 0,
		"comm_positions_short_other": 0,
		"tot_rept_positions_long_other": 0,
		"tot_rept_positions_short_other": 0,
		"nonrept_positions_long_other": 0,
		"nonrept_positions_short_other": 0,
		"change_in_open_interest_all": 3957,
		"change_in_noncomm_long_all": -5586,
		"change_in_noncomm_short_all": 4359,
		"change_in_noncomm_spread_all": 1169,
		"change_in_comm_long_all": 7897,
		"change_in_comm_short_all": -1790,
		"change_in_tot_rept_long_all": 3480,
		"change_in_tot_rept_short_all": 3738,
		"change_in_nonrept_long_all": 477,
		"change_in_nonrept_short_all": 219,
		"pct_of_open_interest_all": 100,
		"pct_of_oi_noncomm_long_all": 50.1,
		"pct_of_oi_noncomm_short_all": 65.4,
		"pct_of_oi_noncomm_spread_all": 0.7,
		"pct_of_oi_comm_long_all": 45.7,
		"pct_of_oi_comm_short_all": 32.3,
		"pct_of_oi_tot_rept_long_all": 96.5,
		"pct_of_oi_tot_rept_short_all": 98.3,
		"pct_of_oi_nonrept_long_all": 3.5,
		"pct_of_oi_nonrept_short_all": 1.7,
		"pct_of_open_interest_ol": 100,
		"pct_of_oi_noncomm_long_ol": 50.1,
		"pct_of_oi_noncomm_short_ol": 65.4,
		"pct_of_oi_noncomm_spread_ol": 0.7,
		"pct_of_oi_comm_long_ol": 45.7,
		"pct_of_oi_comm_short_ol": 32.3,
		"pct_of_oi_tot_rept_long_ol": 96.5,
		"pct_of_oi_tot_rept_short_ol": 98.3,
		"pct_of_oi_nonrept_long_ol": 3.5,
		"pct_of_oi_nonrept_short_ol": 1.7,
		"pct_of_open_interest_other": 0,
		"pct_of_oi_noncomm_long_other": 0,
		"pct_of_oi_noncomm_short_other": 0,
		"pct_of_oi_noncomm_spread_other": 0,
		"pct_of_oi_comm_long_other": 0,
		"pct_of_oi_comm_short_other": 0,
		"pct_of_oi_tot_rept_long_other": 0,
		"pct_of_oi_tot_rept_short_other": 0,
		"pct_of_oi_nonrept_long_other": 0,
		"pct_of_oi_nonrept_short_other": 0,
		"traders_tot_all": 146,
		"traders_noncomm_long_all": 59,
		"traders_noncomm_short_all": 30,
		"traders_noncomm_spread_all": 6,
		"traders_comm_long_all": 35,
		"traders_comm_short_all": 31,
		"traders_tot_rept_long_all": 95,
		"traders_tot_rept_short_all": 66,
		"traders_tot_ol": 146,
		"traders_noncomm_long_ol": 59,
		"traders_noncomm_short_ol": 30,
		"traders_noncomm_spead_ol": 6,
		"traders_comm_long_ol": 35,
		"traders_comm_short_ol": 31,
		"traders_tot_rept_long_ol": 95,
		"traders_tot_rept_short_ol": 66,
		"traders_tot_other": 0,
		"traders_noncomm_long_other": 0,
		"traders_noncomm_short_other": 0,
		"traders_noncomm_spread_other": 0,
		"traders_comm_long_other": 0,
		"traders_comm_short_other": 0,
		"traders_tot_rept_long_other": 0,
		"traders_tot_rept_short_other": 0,
		"conc_gross_le_4_tdr_long_all": 43.4,
		"conc_gross_le_4_tdr_short_all": 72.1,
		"conc_gross_le_8_tdr_long_all": 57.3,
		"conc_gross_le_8_tdr_short_all": 83.2,
		"conc_net_le_4_tdr_long_all": 43.4,
		"conc_net_le_4_tdr_short_all": 72.1,
		"conc_net_le_8_tdr_long_all": 57.3,
		"conc_net_le_8_tdr_short_all": 83.1,
		"conc_gross_le_4_tdr_long_ol": 43.4,
		"conc_gross_le_4_tdr_short_ol": 72.1,
		"conc_gross_le_8_tdr_long_ol": 57.3,
		"conc_gross_le_8_tdr_short_ol": 83.2,
		"conc_net_le_4_tdr_long_ol": 43.4,
		"conc_net_le_4_tdr_short_ol": 72.1,
		"conc_net_le_8_tdr_long_ol": 57.3,
		"conc_net_le_8_tdr_short_ol": 83.1,
		"conc_gross_le_4_tdr_long_other": 0,
		"conc_gross_le_4_tdr_short_other": 0,
		"conc_gross_le_8_tdr_long_other": 0,
		"conc_gross_le_8_tdr_short_other": 0,
		"conc_net_le_4_tdr_long_other": 0,
		"conc_net_le_4_tdr_short_other": 0,
		"conc_net_le_8_tdr_long_other": 0,
		"conc_net_le_8_tdr_short_other": 0,
		"contract_units": "MXN 500,000",
		"name": "Mexican Peso (M6)",
		"exchange": "MEXICAN PESO - CHICAGO MERCANTILE EXCHANGE"
	}
]
"""

REPORT_BY_DATES_ENDPOINT = "v4/commitment_of_traders_report"
# Provides the Commitment of Traders (COT) report for a given date range.

# Query Params:
# from: date in the format 'YYYY-MM-DD'
# to: date in the format 'YYYY-MM-DD'

# Response:
"""
[
	{
		"symbol": "ZO",
		"date": "2022-08-30 00:00:00",
		"short_name": "Oats (ZO)",
		"sector": "GRAINS",
		"market_and_exchange_names": "OATS - CHICAGO BOARD OF TRADE",
		"cftc_contract_market_code": "004603",
		"cftc_market_code": "CBT",
		"cftc_region_code": "0",
		"cftc_commodity_code": "4",
		"open_interest_all": 3238,
		"noncomm_positions_long_all": 685,
		"noncomm_positions_short_all": 541,
		"noncomm_postions_spread_all": 213,
		"comm_positions_long_all": 963,
		"comm_positions_short_all": 1348,
		"tot_rept_positions_long_all": 1861,
		"tot_rept_positions_short_all": 2102,
		"nonrept_positions_long_all": 1377,
		"nonrept_positions_short_all": 1136,
		"open_interest_old": 3200,
		"noncomm_positions_long_old": 708,
		"noncomm_positions_short_old": 541,
		"noncomm_positions_spread_old": 190,
		"comm_positions_long_old": 963,
		"comm_positions_short_old": 1348,
		"tot_rept_positions_long_old": 1861,
		"tot_rept_positions_short_old": 2079,
		"nonrept_positions_long_old": 1339,
		"nonrept_positions_short_old": 1121,
		"open_interest_other": 38,
		"noncomm_positions_long_other": 0,
		"noncomm_positions_short_other": 23,
		"noncomm_positions_spread_other": 0,
		"comm_positions_long_other": 0,
		"comm_positions_short_other": 0,
		"tot_rept_positions_long_other": 0,
		"tot_rept_positions_short_other": 23,
		"nonrept_positions_long_other": 38,
		"nonrept_positions_short_other": 15,
		"change_in_open_interest_all": 0,
		"change_in_noncomm_long_all": 0,
		"change_in_noncomm_short_all": 0,
		"change_in_comm_long_all": 0,
		"change_in_comm_short_all": 0,
		"change_in_tot_rept_long_all": 0,
		"change_in_tot_rept_short_all": 0,
		"change_in_nonrept_long_all": 0,
		"change_in_nonrept_short_all": 0,
		"pct_of_open_interest_all": 100,
		"pct_of_oi_noncomm_long_all": 21.2,
		"pct_of_oi_noncomm_short_all": 16.7,
		"pct_of_oi_noncomm_spread_all": 6.6,
		"pct_of_oi_comm_long_all": 29.7,
		"pct_of_oi_comm_short_all": 41.6,
		"pct_of_oi_tot_rept_long_all": 57.5,
		"pct_of_oi_tot_rept_short_all": 64.9,
		"pct_of_oi_nonrept_long_all": 42.5,
		"pct_of_oi_nonrept_short_all": 35.1,
		"pct_of_open_interest_ol": 100,
		"pct_of_oi_noncomm_long_ol": 22.1,
		"pct_of_oi_noncomm_short_ol": 16.9,
		"pct_of_oi_noncomm_spread_ol": 5.9,
		"pct_of_oi_comm_long_ol": 30.1,
		"pct_of_oi_comm_short_ol": 42.1,
		"pct_of_oi_tot_rept_long_ol": 58.2,
		"pct_of_oi_tot_rept_short_ol": 65,
		"pct_of_oi_nonrept_long_ol": 41.8,
		"pct_of_oi_nonrept_short_ol": 35,
		"pct_of_open_interest_other": 100,
		"pct_of_oi_noncomm_long_other": 0,
		"pct_of_oi_noncomm_short_other": 60.5,
		"pct_of_oi_noncomm_spread_other": 0,
		"pct_of_oi_comm_long_other": 0,
		"pct_of_oi_comm_short_other": 0,
		"pct_of_oi_tot_rept_long_other": 0,
		"pct_of_oi_tot_rept_short_other": 60.5,
		"pct_of_oi_nonrept_long_other": 100,
		"pct_of_oi_nonrept_short_other": 39.5,
		"traders_tot_all": 21,
		"traders_noncomm_long_all": 7,
		"traders_noncomm_short_all": 2,
		"traders_noncomm_spread_all": 2,
		"traders_comm_long_all": 8,
		"traders_comm_short_all": 5,
		"traders_tot_rept_long_all": 16,
		"traders_tot_rept_short_all": 9,
		"traders_tot_ol": 21,
		"traders_noncomm_long_ol": 8,
		"traders_noncomm_short_ol": 2,
		"traders_noncomm_spead_ol": 2,
		"traders_comm_long_ol": 8,
		"traders_comm_short_ol": 5,
		"traders_tot_rept_long_ol": 16,
		"traders_tot_rept_short_ol": 9,
		"traders_tot_other": 2,
		"traders_noncomm_long_other": 0,
		"traders_noncomm_short_other": 2,
		"traders_noncomm_spread_other": 0,
		"traders_comm_long_other": 0,
		"traders_comm_short_other": 0,
		"traders_tot_rept_long_other": 0,
		"traders_tot_rept_short_other": 2,
		"conc_gross_le_4_tdr_long_all": 24,
		"conc_gross_le_4_tdr_short_all": 47.7,
		"conc_gross_le_8_tdr_long_all": 41.3,
		"conc_gross_le_8_tdr_short_all": 64.5,
		"conc_net_le_4_tdr_long_all": 22.7,
		"conc_net_le_4_tdr_short_all": 45.9,
		"conc_net_le_8_tdr_long_all": 38.6,
		"conc_net_le_8_tdr_short_all": 57,
		"conc_gross_le_4_tdr_long_ol": 24.3,
		"conc_gross_le_4_tdr_short_ol": 48,
		"conc_gross_le_8_tdr_long_ol": 41.8,
		"conc_gross_le_8_tdr_short_ol": 64.9,
		"conc_net_le_4_tdr_long_ol": 23,
		"conc_net_le_4_tdr_short_ol": 46.4,
		"conc_net_le_8_tdr_long_ol": 39,
		"conc_net_le_8_tdr_short_ol": 57.7,
		"conc_gross_le_4_tdr_long_other": 0,
		"conc_gross_le_4_tdr_short_other": 60.5,
		"conc_gross_le_8_tdr_long_other": 0,
		"conc_gross_le_8_tdr_short_other": 60.5,
		"conc_net_le_4_tdr_long_other": 0,
		"conc_net_le_4_tdr_short_other": 60.5,
		"conc_net_le_8_tdr_long_other": 0,
		"conc_net_le_8_tdr_short_other": 60.5,
		"contract_units": "(CONTRACTS OF 5,000 BUSHELS)",
		"updatedAt": "2022-09-02T19:30:25.920Z",
		"createdAt": "2022-09-02T19:30:25.920Z",
		"as_of_date_in_form_yymmdd": "220830",
		"change_in_noncomm_spead_all": 0
	}
]
"""


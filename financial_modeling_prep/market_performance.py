"""Market Performance API endpoints."""
MARKET_INDEX_ENDPOINT = "v3/quotes/index"
SECTOR_PE_RATIO_ENDPOINT = "v4/sector_price_earning_ratio"
INDUSTRY_PE_RATIO_ENDPOINT = "v4/industry_price_earning_ratio"
SECTOR_PERFORMANCE_ENDPOINT = "v3/sectors-performance"
SECTOR_HISTORICAL_PERFORMANCE_ENDPOINT = "v3/historical-sectors-performance"
MARKET_BIGGEST_GAINERS_ENDPOINT = "v3/stock_market/gainers"
MARKET_BIGGEST_LOSERS_ENDPOINT = "v3/stock_market/losers"
MARKET_MOST_ACTIVE_ENDPOINT = "v3/stock_market/actives"
ANALYSIS_BY_SYMBOL_ENDPOINT = "v4/commitment_of_traders_report_analysis/{symbol}"
ANALYSIS_BY_DATES_ENDPOINT = "v4/commitment_of_traders_report_analysis"
REPORT_BY_SYMBOL = "v4/commitment_of_traders_report/{symbol}"
REPORT_BY_DATES_ENDPOINT = "v4/commitment_of_traders_report"


class MarketPerformance:
    """
    A class to retrieve and analyze market performance data.

    Explanation:
    This class provides methods to fetch information about market indices,
     sector PE ratios, industry PE ratios, sector performance,
     historical sector performance, biggest gainers, biggest losers,
     most active stocks, Commitment of Traders (COT) report analysis by
     symbol or dates, and COT report by symbol or dates.

    Methods:
    - get_market_index: Get a list of all major stock market indices.
    - get_sector_pe_ratio:
      Get the price-to-earnings (PE) ratio for each sector of the stock market.
    - get_industry_pe_ratio:
      Get the price-to-earnings (PE) ratio for each industry of the stock market.
    - get_sector_performance:
      Get the performance of each sector of the stock market.
    - get_sector_historical_performance:
      Get historical data on the performance of each sector of the stock market.
    - get_market_biggest_gainers: Get the biggest gainers in the market.
    - get_market_biggest_losers: Get the biggest losers in the market.
    - get_market_most_active: Get the most active stocks in the market.
    - get_analysis_by_symbol:
      Get the Commitment of Traders (COT) report analysis for a given symbol.
    - get_analysis_by_dates:
      Get the Commitment of Traders (COT) report analysis for a given date range.
    - get_report_by_symbol:
      Get the Commitment of Traders (COT) report for a given symbol.
    - get_report_by_dates:
      Get the Commitment of Traders (COT) report for a given date range.
    """

    def __init__(self, api):
        """
        Initializes the MarketPerformance class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_market_index(self):
        """Get the list of all major stock market indices.

        Returns: [
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
        return self.api.get(MARKET_INDEX_ENDPOINT)

    def get_sector_pe_ratio(self, date, exchange=None):
        """Get the price-to-earnings (PE) ratio for each sector of the stock market.

        Args:
            date (str): date in the format 'YYYY-MM-DD'
            exchange (str): exchange name (optional)

        Returns: [
            {
                "date": "2023-03-03",
                "sector": "Basic Materials",
                "exchange": "NYSE",
                "pe": "18.33197269872979"
            }
        ]
        """
        return self.api.get(
            SECTOR_PE_RATIO_ENDPOINT, params={"date": date, "exchange": exchange}
        )

    def get_industry_pe_ratio(self, date, exchange=None):
        """Get the price-to-earnings (PE) ratio for each industry of the stock market.

        Args:
            date (str): date in the format 'YYYY-MM-DD'
            exchange (str): exchange name (optional)

        Returns: [
            {
                "date": "2023-03-03",
                "industry": "Advertising Agencies",
                "exchange": "NYSE",
                "pe": "3.4058333333333337"
            }
        ]
        """
        return self.api.get(
            INDUSTRY_PE_RATIO_ENDPOINT, params={"date": date, "exchange": exchange}
        )

    def get_sector_performance(self):
        """Get the performance of each sector of the stock market.

        Returns: [
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
        return self.api.get(SECTOR_PERFORMANCE_ENDPOINT)

    def get_sector_historical_performance(self, limit=None):
        """Get historical data on the performance of each sector of the stock market.

        Args:
            limit (int): number of results to return

        Returns: [
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
        return self.api.get(
            SECTOR_HISTORICAL_PERFORMANCE_ENDPOINT, params={"limit": limit}
        )

    def get_market_biggest_gainers(self):
        """Get the biggest gainers in the market.

        Returns: [
            {
                "symbol": "PIK",
                "name": "Kidpik Corp.",
                "change": 0.27,
                "price": 1.8,
                "changesPercentage": 17.6471
            }
        ]
        """
        return self.api.get(MARKET_BIGGEST_GAINERS_ENDPOINT)

    def get_market_biggest_losers(self):
        """Get the biggest losers in the market.

        Returns: [
            {
                "symbol": "DSLVF",
                "name": "VelocityShares 3x Inverse Silver ETN Linked...",
                "change": -0.13,
                "price": 1.13,
                "changesPercentage": -10.3175
            }
        ]
        """
        return self.api.get(MARKET_BIGGEST_LOSERS_ENDPOINT)

    def get_market_most_active(self):
        """Get the most active stocks in the market.

        Returns: [
            {
                "symbol": "MU",
                "name": "Micron Technology, Inc.",
                "change": 2.24,
                "price": 53.96,
                "changesPercentage": 4.331
            }
        ]
        """
        return self.api.get(MARKET_MOST_ACTIVE_ENDPOINT)

    def get_analysis_by_symbol(self, symbol):
        """Get the Commitment of Traders (COT) report analysis for a given symbol.

        Args:
            symbol (str): stock symbol

        Returns: [
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
        return self.api.get(ANALYSIS_BY_SYMBOL_ENDPOINT.format(symbol=symbol))

    def get_analysis_by_dates(self, from_date, to_date):
        """Get the Commitment of Traders (COT) report analysis for a given date range.

        Args:
            from_date (str): date in the format 'YYYY-MM-DD'
            to_date (str): date in the format 'YYYY-MM-DD'

        Returns: [
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
        return self.api.get(
            ANALYSIS_BY_DATES_ENDPOINT, params={"from": from_date, "to": to_date}
        )

    def get_report_by_symbol(self, symbol):
        """Get the Commitment of Traders (COT) report for a given symbol.

        Args:
            symbol (str): stock symbol

        Returns: [
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
        return self.api.get(REPORT_BY_SYMBOL.format(symbol=symbol))

    def get_report_by_dates(self, from_date, to_date):
        """Get the Commitment of Traders (COT) report for a given date range.

        Args:
            from_date (str): date in the format 'YYYY-MM-DD'
            to_date (str): date in the format 'YYYY-MM-DD'

        Returns:[
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
        return self.api.get(
            REPORT_BY_DATES_ENDPOINT, params={"from": from_date, "to": to_date}
        )

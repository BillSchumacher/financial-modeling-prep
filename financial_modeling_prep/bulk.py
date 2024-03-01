"""Bulk Data API endpoints and methods."""
BATCH_EOD_PRICES_ENDPOINT = "v4/batch-request-end-of-day-prices"
BULK_INCOME_STATEMENTS_ENDPOINT = "v4/income-statement-bulk"
BULK_BALANCE_SHEETS_ENDPOINT = "v4/balance-sheet-statement-bulk"
BULK_CASH_FLOW_STATEMENTS_ENDPOINT = "v4/cash-flow-statement-bulk"
BULK_RATIOS_ENDPOINT = "v4/ratios-bulk"
BULK_KEY_METRICS_ENDPOINT = "v4/key-metrics-bulk"
BULK_EARNING_SURPRISES_ENDPOINT = "v4/earnings-surprises-bulk"
BULK_PROFILES_ENDPOINT = "v4/profile/all"
BULK_STOCK_PEERS_ENDPOINT = "v4/stock_peers_bulk"
BULK_RATINGS_ENDPOINT = "v4/rating-bulk"
ALL_LATEST_DCF_ENDPOINT = "v4/dcf-bulk"
BULK_KEY_METRICS_TTM_ENDPOINT = "v4/key-metrics-ttm-bulk"
BULK_RATIO_TTM_ENDPOINT = "v4/ratios-ttm-bulk"
BULK_SCORES_ENDPOINT = "v4/scores-bulk"
BULK_FINANCIAL_GROWTH_ENDPOINT = "v4/financial-growth-bulk"
BULK_INCOME_STATEMENTS_GROWTH_ENDPOINT = "v4/income-statement-growth-bulk"
BULK_BALANCE_SHEETS_GROWTH_ENDPOINT = "v4/balance-sheet-statement-growth-bulk"
BULK_CASH_FLOW_STATEMENTS_GROWTH_ENDPOINT = "v4/cash-flow-statement-growth-bulk"
BULK_PRICE_TARGET_SUMMARY_ENDPOINT = "v4/price-target-summary-bulk"
BULK_UPGRADES_DOWNGRADES_CONSENSUS_ENDPOINT = "v4/upgrades-downgrades-consensus-bulk"
BULK_ETF_HOLDERS_ENDPOINT = "v4/etf-holder-bulk"


class BulkData:
    """Efficiently access comprehensive data for numerous companies at once.

    Including financial statements, ratios, key metrics, stock splits,
        stock dividends, and various other relevant information.
    """

    def __init__(self, api):
        """
        Initializes the BulkData class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def batch_eod_prices(self, date: str):
        """Batch request that contains all end of day prices for specific date.

        :param date: (required) The date for which to return end of day prices.
            The date must be a valid trading day and in the format YYYY-MM-DD.
        :return:
        """
        return self.api.get(BATCH_EOD_PRICES_ENDPOINT, {"date": date})

    def bulk_income_statements(self, year: int, period: str):
        """All quarter or annual Income Statements for specific year.

        :param year: (required) The year for which to return income statements.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return income statements.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_INCOME_STATEMENTS_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_balance_sheets(self, year: int, period: str):
        """All quarter or annual Balance Sheets for specific year.

        :param year: (required) The year for which to return balance sheets.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return balance sheets.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_BALANCE_SHEETS_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_cash_flow_statements(self, year: int, period: str):
        """All quarter or annual Cash Flow Statements for specific year.

        :param year: (required) The year for which to return cash flow statements.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return cash flow statements.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_CASH_FLOW_STATEMENTS_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_ratios(self, year: int, period: str):
        """All quarter or annual Ratios for specific year.

        :param year: (required) The year for which to return ratios.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return ratios.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(BULK_RATIOS_ENDPOINT, {"year": year, "period": period})

    def bulk_key_metrics(self, year: int, period: str):
        """All quarter or annual Key Metrics for specific year.

        :param year: (required) The year for which to return key metrics.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return key metrics.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(BULK_KEY_METRICS_ENDPOINT, {"year": year, "period": period})

    def bulk_earnings_surprises(self, year: int):
        """All Earnings Surprises for specific year.

        :param year: (required) The year for which to return earnings surprises.
            The year must be a valid year in the format YYYY.
        :return:
        """
        return self.api.get(BULK_EARNING_SURPRISES_ENDPOINT, {"year": year})

    def bulk_profiles(self):
        """All profiles from our API in one CSV file.

        :return:
        """
        return self.api.get(BULK_PROFILES_ENDPOINT)

    def bulk_stock_peers(self):
        """Stock peers for all symbols with profile.

        :return:
        """
        return self.api.get(BULK_STOCK_PEERS_ENDPOINT)

    def bulk_ratings(self):
        """All latest company ratings.

        :return:
        """
        return self.api.get(BULK_RATINGS_ENDPOINT)

    def bulk_latest_dcf(self):
        """All latest DCF values.

        :return:
        """
        return self.api.get(ALL_LATEST_DCF_ENDPOINT)

    def bulk_key_metrics_ttm(self):
        """Key Metrics TTM for every stock.

        :return:
        """
        return self.api.get(BULK_KEY_METRICS_TTM_ENDPOINT)

    def bulk_ratios_ttm(self):
        """Ratios TTM for every stock.

        :return:
        """
        return self.api.get(BULK_RATIO_TTM_ENDPOINT)

    def bulk_scores(self):
        """All stock financial scores.

        :return:
        """
        return self.api.get(BULK_SCORES_ENDPOINT)

    def bulk_financial_growth(self, year: int, period: str):
        """All quarter or annual growth entries for specific year.

        :param year: (required) The year for which to return growth entries.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return growth entries.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_FINANCIAL_GROWTH_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_income_statements_growth(self, year: int, period: str):
        """All quarter or annual Income Statement Growth for specific year.

        Args:
            year: (required) The year for which to return income statement growth.
              The year must be a valid year in the format YYYY.
            period: (required) The period for which to return income statement growth.
              The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_INCOME_STATEMENTS_GROWTH_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_balance_sheets_growth(self, year: int, period: str):
        """All quarter or annual Balance Sheet Growth for specific year.

        :param year: (required) The year for which to return balance sheet growth.
            The year must be a valid year in the format YYYY.
        :param period: (required) The period for which to return balance sheet growth.
            The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_BALANCE_SHEETS_GROWTH_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_cash_flow_statements_growth(self, year: int, period: str):
        """All quarter or annual Cash Flow Statement Growth for specific year.

        Args:
            year: (required) The year for which to return cash flow statement growth.
              The year must be a valid year in the format YYYY.
            period: (required) The period to return cash flow statement growth.
              The period must be either 'annual' or 'quarterly'.
        :return:
        """
        return self.api.get(
            BULK_CASH_FLOW_STATEMENTS_GROWTH_ENDPOINT, {"year": year, "period": period}
        )

    def bulk_price_target_summary(self):
        """All price target summaries.

        :return:
        """
        return self.api.get(BULK_PRICE_TARGET_SUMMARY_ENDPOINT)

    def bulk_upgrades_downgrades_consensus(self):
        """All upgrades downgrades consensus.

        :return:
        """
        return self.api.get(BULK_UPGRADES_DOWNGRADES_CONSENSUS_ENDPOINT)

    def bulk_etf_holdings(self):
        """Latest ETF Holders in bulk.

        :return:
        """
        return self.api.get(BULK_ETF_HOLDERS_ENDPOINT)

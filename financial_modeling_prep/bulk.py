# Efficiently access comprehensive data for numerous companies at once, including financial statements, ratios, key metrics, stock splits, stock dividends, and various other relevant information.


BATCH_EOD_PRICES_ENDPOINT = "v4/batch-request-end-of-day-prices"
# Batch request that contains all end of day prices for specific date

# Query Parameters
# date: date (required) - The date for which to return end of day prices. The date must be a valid trading day and in the format YYYY-MM-DD.

BULK_INCOME_STATEMENTS_ENDPOINT = "v4/income-statement-bulk"
# All quarter or annual Income Statements for specific year

# Query Parameters
# year: int (required) - The year for which to return income statements. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return income statements. The period must be either 'annual' or 'quarterly'.

BULK_BALANCE_SHEETS_ENDPOINT = "v4/balance-sheet-statement-bulk"
# All quarter or annual Balance Sheets for specific year

# Query Parameters
# year: int (required) - The year for which to return balance sheets. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return balance sheets. The period must be either 'annual' or 'quarterly'.

BULK_CASH_FLOW_STATEMENTS_ENDPOINT = "v4/cash-flow-statement-bulk"
# All quarter or annual Cash Flow Statements for specific year

# Query Parameters
# year: int (required) - The year for which to return cash flow statements. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return cash flow statements. The period must be either 'annual' or 'quarterly'.

BULK_RATIOS_ENDPOINT = "v4/ratios-bulk"
# All quarter or annual Ratios for specific year

# Query Parameters
# year: int (required) - The year for which to return ratios. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return ratios. The period must be either 'annual' or 'quarterly'.

BULK_KEY_METRICS_ENDPOINT = "v4/key-metrics-bulk"
# All quarter or annual Key Metrics for specific year

# Query Parameters
# year: int (required) - The year for which to return key metrics. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return key metrics. The period must be either 'annual' or 'quarterly'.

BULK_EARNING_SURPRISES_ENDPOINT = "v4/earnings-surprises-bulk"
# All Earnings Surprises for specific year

# Query Parameters
# year: int (required) - The year for which to return earnings surprises. The year must be a valid year in the format YYYY.

BULK_PROFILES_ENDPOINT = "v4/profile/all"
# It contains all profiles from our API in one CSV file

BULK_STOCK_PEERS_ENDPOINT = "v4/stock_peers_bulk"
# Stock peers for all symbols with profile

BULK_RATINGS_ENDPOINT = "v4/rating-bulk"
# All latest company ratings.

ALL_LATEST_DCF_ENDPOINT = "v4/dcf-bulk"

BULK_KEY_METRICS_TTM_ENDPOINT = "v4/key-metrics-ttm-bulk"
# Key Metrics TTM for every stock

BULK_RATIO_TTM_ENDPOINT = "v4/ratios-ttm-bulk"
# Ratios TTM for every stock

BULK_SCORES_ENDPOINT = "v4/scores-bulk"
# All stock financial scores

BULK_FINANCIAL_GROWTH_ENDPOINT = "v4/financial-growth-bulk"
# All quarter or annual growth entries for specific year

# Query Parameters
# year: int (required) - The year for which to return growth entries. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return growth entries. The period must be either 'annual' or 'quarterly'.

BULK_INCOME_STATEMENTS_GROWTH_ENDPOINT = "v4/income-statement-growth-bulk"
# All quarter or annual Income Statement Growth for specific year

# Query Parameters
# year: int (required) - The year for which to return income statement growth. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return income statement growth. The period must be either 'annual' or 'quarterly'.

BULK_BALANCE_SHEETS_GROWTH_ENDPOINT = "v4/balance-sheet-statement-growth-bulk"
# All quarter or annual Balance Sheet Growth for specific year

# Query Parameters
# year: int (required) - The year for which to return balance sheet growth. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return balance sheet growth. The period must be either 'annual' or 'quarterly'.

BULK_CASH_FLOW_STATEMENTS_GROWTH_ENDPOINT = "v4/cash-flow-statement-growth-bulk"
# All quarter or annual Cash Flow Statement Growth for specific year

# Query Parameters
# year: int (required) - The year for which to return cash flow statement growth. The year must be a valid year in the format YYYY.
# period: str (required) - The period for which to return cash flow statement growth. The period must be either 'annual' or 'quarterly'.

BULK_PRICE_TARGET_SUMMARY_ENDPOINT = "v4/price-target-summary-bulk"
# All price target summaries

BULK_UPGRADES_DOWNGRADES_CONSENSUS_ENDPOINT = "v4/upgrades-downgrades-consensus-bulk"
# All upgrades downgrades consensus

BULK_ETF_HOLDERS_ENDPOINT = "v4/etf-holder-bulk"
# Latest ETF Holders in bulk

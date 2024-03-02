"""Financial Modeling Prep API client."""
from __future__ import annotations

from requests_cache import CachedSession

from financial_modeling_prep.bulk import BulkData
from financial_modeling_prep.charts import Charts
from financial_modeling_prep.commodities import Commodities
from financial_modeling_prep.company_info import CompanyInfo
from financial_modeling_prep.company_search import CompanySearch
from financial_modeling_prep.constituents import Constituents
from financial_modeling_prep.crypto import CryptoCurrency
from financial_modeling_prep.dividends import Dividends
from financial_modeling_prep.earnings import Earnings
from financial_modeling_prep.earnings_transcripts import EarningsTranscripts
from financial_modeling_prep.economic_data import EconomicData
from financial_modeling_prep.esg import ESG
from financial_modeling_prep.etf_holdings import ETFHoldings
from financial_modeling_prep.financial_statements import FinancialStatements
from financial_modeling_prep.forex import Forex
from financial_modeling_prep.fundraising import Fundraising
from financial_modeling_prep.insider_trading import InsiderTrading
from financial_modeling_prep.institutional_stock_ownership import (
    InstitutionalStockOwnership,
)
from financial_modeling_prep.ipo_calendar import IPOCalendar
from financial_modeling_prep.market_performance import MarketPerformance
from financial_modeling_prep.mergers_and_acquisitions import MergersAndAcquisitions
from financial_modeling_prep.mutual_fund_holdings import MutualFundHoldings
from financial_modeling_prep.news import News
from financial_modeling_prep.price_targets import PriceTargets
from financial_modeling_prep.quote import Quote
from financial_modeling_prep.sales_revenue_by_segments import SalesRevenueBySegments
from financial_modeling_prep.sec_filings import SECFilings
from financial_modeling_prep.senate import Senate
from financial_modeling_prep.splits import Splits
from financial_modeling_prep.statement_analysis import StatementAnalysis
from financial_modeling_prep.stock_list import StockList
from financial_modeling_prep.technical_indicators import TechnicalIndicators
from financial_modeling_prep.upgrades_downgrades import UpgradesAndDowngrades
from financial_modeling_prep.valuation import Valuation
from financial_modeling_prep.websockets import (
    CompanyWSClient,
    CryptoWSClient,
    ForexWSClient,
)

session = CachedSession(
    "fmp_cache",
    ignored_parameters=["api_key"],
    use_cache_dir=True,
    cache_control=True,
    expire_after=300,
    allowable_methods=("GET", "POST"),
)


class FinancialModelingPrep:
    """A class for interacting with the Financial Modeling Prep API.

    Methods:
    - get(endpoint, params=None):
    """

    def __init__(self, api_key):
        """Initializes the FinancialModelingPrep API client.

        Args:
            api_key (str): The API key for FinancialModelingPrep.com.

        Returns:
            None
        """
        self.api_key = api_key
        self.bulk_data = BulkData(self)
        self.charts = Charts(self)
        self.commodities = Commodities(self)
        self.company_info = CompanyInfo(self)
        self.company_search = CompanySearch(self)
        self.constituents = Constituents(self)
        self.crypto = CryptoCurrency(self)
        self.dividends = Dividends(self)
        self.earnings = Earnings(self)
        self.earnings_transcripts = EarningsTranscripts(self)
        self.economic_data = EconomicData(self)
        self.esg = ESG(self)
        self.etf_holdings = ETFHoldings(self)
        self.financial_statements = FinancialStatements(self)
        self.forex = Forex(self)
        self.fundraising = Fundraising(self)
        self.insider_trading = InsiderTrading(self)
        self.institutional_stock_ownership = InstitutionalStockOwnership(self)
        self.ipo_calendar = IPOCalendar(self)
        self.market_performance = MarketPerformance(self)
        self.mergers_and_acquisitions = MergersAndAcquisitions(self)
        self.mutual_fund_holdings = MutualFundHoldings(self)
        self.news = News(self)
        self.price_targets = PriceTargets(self)
        self.quote = Quote(self)
        self.sales_revenue_by_segments = SalesRevenueBySegments(self)
        self.sec_filings = SECFilings(self)
        self.senate = Senate(self)
        self.splits = Splits(self)
        self.statement_analysis = StatementAnalysis(self)
        self.stock_list = StockList(self)
        self.technical_indicators = TechnicalIndicators(self)
        self.upgrades_and_downgrades = UpgradesAndDowngrades(self)
        self.valuation = Valuation(self)

    def get(self, endpoint, params: dict | None = None):
        """
        Makes an API request to the specified endpoint with optional parameters.

        Args:
            endpoint (str): The API endpoint to request data from.
            params (dict, optional): Additional parameters for the API request.

        Returns:
            dict: The json response.
            Invalid API Key: {
                'Error Message':
                'Invalid API KEY. Please retry or visit our documentation to
                create one FREE https://financialmodelingprep.com/developer/docs'
            }
        """
        if params is None:
            params = {}
        params["apikey"] = self.api_key

        response = session.get(
            f"https://financialmodelingprep.com/api/{endpoint}",
            params=params,
            timeout=5,
        )
        return response.json()


__all__ = [
    "CompanyWSClient",
    "CryptoWSClient",
    "FinancialModelingPrep",
    "ForexWSClient",
]

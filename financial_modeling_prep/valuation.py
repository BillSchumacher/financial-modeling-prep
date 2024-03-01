"""Valuation module for the Stocks API."""
DISCOUNTED_CASHFLOW_ENDPOINT = "v3/discounted-cash-flow/{symbol}"
ADVANCED_DCF_ENDPOINT = "v4/advanced_discounted_cash_flow"
LEVERED_DCF_ENDPOINT = "v4/advanced_levered_discounted_cash_flow"
COMPANY_RATING_ENDPOINT = "v3/ratings/{symbol}"
HISTORICAL_RATING_ENDPOINT = "v3/historical-rating/{symbol}"


class Valuation:
    """
    A class to access valuation information for companies.

    Explanation:
    This class provides methods to retrieve discounted cash flow (DCF) valuations,
     advanced DCF valuations with multiple scenarios, levered DCF valuations
      considering debt levels, company ratings, and historical ratings for companies.

    Methods:
    - discounted_cashflow:
    Get the discounted cash flow (DCF) valuation for a company.
    - advanced_dcf:
    Get the DCF valuation for a company with advanced features.
    - levered_dcf:
    Get the DCF valuation for a company, taking into account its debt levels.
    - company_rating: Get the rating of a company.
    - historical_rating: Get the historical rating of a company.
    """

    def __init__(self, api):
        """
        Initializes the Valuation class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def discounted_cashflow(self, symbol: str):
        """Get the discounted cash flow (DCF) valuation for a company.

        A method to estimate the value of an investment
         based on its expected future cash flows.

        Args:
            symbol (str): Symbol of the company

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-03-03",
                "dcf": 151.0983806294802,
                "Stock Price": 149.65
            }
        ]
        """
        return self.api.get(DISCOUNTED_CASHFLOW_ENDPOINT.format(symbol=symbol))

    def advanced_dcf(self, symbol: str):
        """Get the DCF valuation for a company with advanced features.

        Like modeling multiple scenarios and using different valuation methods.

        Args:
            symbol (str): Symbol of the company

        Returns: [
            {
                "symbol": "AAPL",
                "price": 140.56,
                "beta": 1.25,
                "finalTaxRate": 13.3,
                "totalDebt": 124719000000,
                "totalEquity": 2370533014640,
                "totalCapital": 2495252014640,
                "dilutedSharesOutstanding": 16864919000,
                "debtWeighting": 5,
                "equityWeighting": 95,
                "year": "2017",
                "period": "FY",
                "revenue": 229234000000,
                "ebitda": 76569000000,
                "operatingCashFlow": 63598000000,
                "ebit": 66412000000,
                "weightedAverageShsOutDil": 21006768000,
                "netDebt": 95391000000,
                "inventories": 4855000000,
                "receivables": 35673000000,
                "payable": 49049000000,
                "inventoriesChange": 2723000000,
                "receivablesChange": 6374000000,
                "payableChange": 11755000000,
                "capitalExpenditure": -12795000000,
                "previousRevenue": 215639000000,
                "revenuePercentage": 0,
                "taxRate": 13.3,
                "ebitdaPercentage": 33.4,
                "receivablesPercentage": 15.56,
                "inventoriesPercentage": 2.12,
                "payablePercentage": 21.4,
                "ebitPercentage": 28.97,
                "capitalExpenditurePercentage": -5.58,
                "operatingCashFlowPercentage": 27.74,
                "afterTaxCostOfDebt": 1.84,
                "marketRiskPremium": 4.72,
                "longTermGrowthRate": 2,
                "costOfEquity": 10.56,
                "wacc": 10.11,
                "taxRateCash": 24556477,
                "ebiat": -15644326940,
                "ufcf": 44807553059,
                "riskFreeRate": 4.66,
                "sumPvUfcf": 0,
                "terminalValue": 563455390558,
                "presentTerminalValue": 348096433212,
                "enterpriseValue": 348096433212,
                "equityValue": 252705433212,
                "equityValuePerShare": 12.03,
                "freeCashFlowT1": 45703704120,
                "costofDebt": 2.12,
                "depreciation": 10157000000,
                "totalCash": 74181000000,
                "depreciationPercentage": 4.43,
                "totalCashPercentage": 32.36
            }
        ]
        """
        return self.api.get(ADVANCED_DCF_ENDPOINT, params={"symbol": symbol})

    def levered_dcf(self, symbol: str):
        """Get the DCF valuation for a company, taking into account its debt levels.

        Args:
            symbol (str): Symbol of the company

        Returns: [
            {
                "year": "2026",
                "symbol": "AAPL",
                "revenue": 601449529857,
                "revenuePercentage": 11.13,
                "capitalExpenditure": -20996099483,
                "capitalExpenditurePercentage": -3.49,
                "price": 145.91,
                "beta": 1.277894,
                "dilutedSharesOutstanding": 16325819000,
                "costofDebt": 2.44,
                "taxRate": 16.2,
                "afterTaxCostOfDebt": 2.05,
                "riskFreeRate": 4.27,
                "marketRiskPremium": 4.72,
                "costOfEquity": 10.3,
                "totalDebt": 120069000000,
                "totalEquity": 2382100250290,
                "totalCapital": 2502169250290,
                "debtWeighting": 4.8,
                "equityWeighting": 95.2,
                "wacc": 9.91,
                "operatingCashFlow": 173976072642,
                "pvLfcf": 104844776023,
                "sumPvLfcf": 0,
                "longTermGrowthRate": 2,
                "freeCashFlow": 152979973159,
                "terminalValue": 2193339068057,
                "presentTerminalValue": 1367716367760,
                "enterpriseValue": 1886225847690,
                "netDebt": 96423000000,
                "equityValue": 1789802847690,
                "equityValuePerShare": 109.63,
                "freeCashFlowT1": 173408405771,
                "operatingCashFlowPercentage": 28.93
            }
        ]
        """
        return self.api.get(LEVERED_DCF_ENDPOINT, params={"symbol": symbol})

    def company_rating(self, symbol: str):
        """Get the rating of a company.

        Investors can use this information to get a quick overview of a
         company's financial health and to compare different companies.

        Args:
            symbol (str): Symbol of the company

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-03-01",
                "rating": "S",
                "ratingScore": 5,
                "ratingRecommendation": "Strong Buy",
                "ratingDetailsDCFScore": 5,
                "ratingDetailsDCFRecommendation": "Strong Buy",
                "ratingDetailsROEScore": 5,
                "ratingDetailsROERecommendation": "Strong Buy",
                "ratingDetailsROAScore": 3,
                "ratingDetailsROARecommendation": "Neutral",
                "ratingDetailsDEScore": 5,
                "ratingDetailsDERecommendation": "Strong Buy",
                "ratingDetailsPEScore": 5,
                "ratingDetailsPERecommendation": "Strong Buy",
                "ratingDetailsPBScore": 5,
                "ratingDetailsPBRecommendation": "Strong Buy"
            }
        ]
        """
        return self.api.get(COMPANY_RATING_ENDPOINT.format(symbol=symbol))

    def historical_rating(self, symbol: str, limit: int = 140):
        """Get the historical rating of a company.

        Investors can use this information to track the changes in a
         company's rating over time and to identify trends in its performance.

        Args:
            symbol (str): Symbol of the company
            limit (int, optional): Limit the number of ratings to be returned.
              Defaults to 140.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-03-01",
                "rating": "S",
                "ratingScore": 5,
                "ratingRecommendation": "Strong Buy",
                "ratingDetailsDCFScore": 5,
                "ratingDetailsDCFRecommendation": "Strong Buy",
                "ratingDetailsROEScore": 5,
                "ratingDetailsROERecommendation": "Strong Buy",
                "ratingDetailsROAScore": 3,
                "ratingDetailsROARecommendation": "Neutral",
                "ratingDetailsDEScore": 5,
                "ratingDetailsDERecommendation": "Strong Buy",
                "ratingDetailsPEScore": 5,
                "ratingDetailsPERecommendation": "Strong Buy",
                "ratingDetailsPBScore": 5,
                "ratingDetailsPBRecommendation": "Strong Buy"
            }
        ]
        """
        return self.api.get(
            HISTORICAL_RATING_ENDPOINT.format(symbol=symbol), params={"limit": limit}
        )

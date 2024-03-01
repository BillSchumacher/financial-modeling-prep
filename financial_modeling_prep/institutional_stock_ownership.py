"""Provides access to the Institutional Stock Ownership API."""
FORM_13F_ENDPOINT = "v3/form-thirteen/{cik}"
FORM_13F_DATES_ENDPOINT = "v3/form-thirteen-date/{cik}"
FORM_13F_ASSET_ALLOCATION_ENDPOINT = "v4/13f-asset-allocation"
INSTITUTIONAL_HOLDERS_LIST_ENDPOINT = "v4/institutional-ownership/list"
INSTITUTIONAL_HOLDERS_SEARCH_ENDPOINT = "v4/institutional-ownership/name"
PORTFOLIO_HOLDINGS_DATES_ENDPOINT = "v4/institutional-ownership/portfolio-date"
INSTITUTIONAL_HOLDER_RSS_ENDPOINT = "v4/institutional-ownership/rss_feed"
INSTITUTIONAL_STOCK_OWNERSHIP_ENDPOINT = "v4/institutional-ownership/symbol-ownership"
STOCK_OWNERSHIP_BY_HOLDERS_ENDPOINT = (
    "v4/institutional-ownership/institutional-holders/symbol-ownership-percent"
)
PORTFOLIO_HOLDINGS_SUMMARY_ENDPOINT = (
    "v4/institutional-ownership/portfolio-holdings-summary"
)
INDUSTRY_OWNERSHIP_SUMMARY_ENDPOINT = (
    "v4/institutional-ownership/industry/portfolio-holdings-summary"
)
OWNERSHIP_BY_SHARES_HELD_ENDPOINT = (
    "v4/institutional-ownership/institutional-holders/symbol-ownership"
)
PORTFOLIO_COMPOSITION_ENDPOINT = "v4/institutional-ownership/portfolio-holdings"
INSTITUTIONAL_HOLDER_ENDPOINT = "v3/institutional-holder/{symbol}"


class InstitutionalStockOwnership:
    """Provides access to the Institutional Stock Ownership API.

    Methods:
    - get_form_13f(cik, date=None)
    - get_form_13f_dates(cik)
    - get_form_13f_asset_allocation(date)
    - get_institutional_holders_list()
    - search_institutional_holders(name)
    - get_portfolio_holdings_dates(cik)
    - get_institutional_holder_rss(page=None)
    - get_institutional_stock_ownership(symbol, include_current_quarter=None)
    - get_stock_ownership_by_holders(symbol, date, page=None)
    - get_portfolio_holdings_summary(cik, page=None)
    - get_industry_ownership_summary(date, cik, page=None)
    - get_ownership_by_shares_held(symbol, date, page=None)
    - get_portfolio_composition(cik, date, page=None)
    - get_institutional_holder(symbol)
    """

    def __init__(self, api):
        """
        Initializes the InstitutionalStockOwnership with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_form_13f(self, cik, date=None):
        """Provides quarterly reports on the equity holdings.

         Of institutional investment managers with over
          $100 million in assets under management.

        Args:
            cik (str): CIK of the company
            date (str): The date of the filing. Format: YYYY-MM-DD

        Returns: [
            {
                "date": "2021-09-30",
                "fillingDate": "2021-11-15",
                "acceptedDate": "2021-11-15",
                "cik": "0001388838",
                "cusip": "256135203",
                "tickercusip": "RDY",
                "nameOfIssuer": "DR REDDYS LABS LTD",
                "shares": 53700,
                "titleOfClass": "ADR",
                "value": 3498000,
                "link": "https://www.sec.gov/Archives/edgar/data/1388838/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
            }
        ]
        """
        return self.api.get(FORM_13F_ENDPOINT.format(cik=cik), params={"date": date})

    def get_form_13f_dates(self, cik):
        """Provides the dates on which Form 13F reports are filed.

        Args:
            cik (str): CIK of the company

        Returns: [
            "2022-12-31",
            "2022-09-30",
            "2022-06-30",
            "2022-03-31",
            "2021-12-31",
            "2021-09-30",
            "2021-06-30",
            "2021-03-31"
        ]
        """
        return self.api.get(FORM_13F_DATES_ENDPOINT.format(cik=cik))

    def get_form_13f_asset_allocation(self, date):
        """Provides the asset allocation of institutional investment managers.

        Including their holdings of stocks, bonds, and other assets.

        Args:
            date (str): The date of the filing. Format: YYYY-MM-DD

        Returns: [
            {
                "date": "2021-09-30",
                "industryTitle": "ACCIDENT & HEALTH INSURANCE",
                "averageWeight": "0.11918551364000854"
            },
            {
                "date": "2021-09-30",
                "industryTitle": "ADHESIVES & SEALANTS",
                "averageWeight": "0.013160932833083866"
            }
        ]
        """
        return self.api.get(FORM_13F_ASSET_ALLOCATION_ENDPOINT, params={"date": date})

    def get_institutional_holders_list(self):
        """Provides a list of all institutional investment managers.

        That are required to file Form 13F reports.

        Returns: [
            {
                "cik": "0001511144",
                "name": "10-15 ASSOCIATES, INC."
            },
            {
                "cik": "0001602119",
                "name": "1060 CAPITAL, LLC"
            }
        ]
        """
        return self.api.get(INSTITUTIONAL_HOLDERS_LIST_ENDPOINT)

    def search_institutional_holders(self, name):
        """Allows users to search for institutional investment managers.

         By name, ticker symbol, or CUSIP number.

        Args:
            name (str): The name of the institutional investment manager,
             e.g. "BERKSHIRE"

        Returns: [
            {
                "cik": "0001067983",
                "name": "BERKSHIRE HATHAWAY INC"
            }
        ]
        """
        return self.api.get(
            INSTITUTIONAL_HOLDERS_SEARCH_ENDPOINT, params={"name": name}
        )

    def get_portfolio_holdings_dates(self, cik):
        """Provides dates that investment managers file their portfolio holdings.

        Args:
            cik (str): CIK of the company

        Returns: [
            {
                "date": "2022-12-31"
            },
            {
                "date": "2022-09-30"
            }
        ]
        """
        return self.api.get(PORTFOLIO_HOLDINGS_DATES_ENDPOINT, params={"cik": cik})

    def get_institutional_holder_rss(self, page=None):
        """Provides an RSS feed of the latest institutional investment manager filings.

        Args:
            page (int): The page number of the feed

        Returns: [
            {
                "date": "2022-09-30",
                "acceptedDate": "2022-11-01 16:00:01",
                "name": "CHAPMAN INVESTMENT MANAGEMENT, LLC",
                "cik": "0001751006"
            }
        ]
        """
        return self.api.get(INSTITUTIONAL_HOLDER_RSS_ENDPOINT, params={"page": page})

    def get_institutional_stock_ownership(self, symbol, include_current_quarter=None):
        """Provides a list of institutional investment managers holding a given stock.

        Args:
            symbol (str): The stock symbol, e.g. "AAPL"
            include_current_quarter (bool): Include the current quarter

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "date": "2022-12-31",
                "investorsHolding": 4322,
                "lastInvestorsHolding": 4189,
                "investorsHoldingChange": 133,
                "numberOf13Fshares": 9328570063,
                "lastNumberOf13Fshares": 9185100866,
                "numberOf13FsharesChange": 143469197,
                "totalInvested": 1259491958234,
                "lastTotalInvested": 1663982277483,
                "totalInvestedChange": -404490319249,
                "ownershipPercent": 57.14,
                "lastOwnershipPercent": 56.2612,
                "ownershipPercentChange": 0.8788,
                "newPositions": 321,
                "lastNewPositions": 111,
                "newPositionsChange": 210,
                "increasedPositions": 1527,
                "lastIncreasedPositions": 1651,
                "increasedPositionsChange": -124,
                "closedPositions": 95,
                "lastClosedPositions": 72,
                "closedPositionsChange": 23,
                "reducedPositions": 2240,
                "lastReducedPositions": 2132,
                "reducedPositionsChange": 108,
                "totalCalls": 37201304688,
                "lastTotalCalls": 3002662883440,
                "totalCallsChange": -2965461578752,
                "totalPuts": 33685223389,
                "lastTotalPuts": 50897951618820,
                "totalPutsChange": -50864266395431,
                "putCallRatio": 0.9055,
                "lastPutCallRatio": 16.9509,
                "putCallRatioChange": -16.0455
            }
        ]
        """
        return self.api.get(
            INSTITUTIONAL_STOCK_OWNERSHIP_ENDPOINT,
            params={"symbol": symbol, "includeCurrentQuarter": include_current_quarter},
        )

    def get_stock_ownership_by_holders(self, symbol, date, page=None):
        """Provides the stock ownership of individual holders.

         Including institutional and individual investors.

        Args:
            symbol (str): The stock symbol, e.g. "AAPL"
            date (str): The date of the filing. Format: YYYY-MM-DD
            page (int): The page number of the feed

        Returns: [
            {
                "date": "2021-09-30",
                "cik": "0000102909",
                "filingDate": "2021-11-12",
                "investorName": "VANGUARD GROUP INC",
                "symbol": "AAPL",
                "securityName": "APPLE INC",
                "typeOfSecurity": "COM",
                "securityCusip": "037833100",
                "sharesType": "SH",
                "putCallShare": "Share",
                "investmentDiscretion": "SOLE",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "weight": 4.4505,
                "lastWeight": 4.3113,
                "changeInWeight": 0.1392,
                "changeInWeightPercentage": 3.2279,
                "marketValue": 179186073000,
                "lastMarketValue": 173245709000,
                "changeInMarketValue": 5940364000,
                "changeInMarketValuePercentage": 3.4289,
                "sharesNumber": 1266332667,
                "lastSharesNumber": 1264936543,
                "changeInSharesNumber": 1396124,
                "changeInSharesNumberPercentage": 0.1104,
                "quarterEndPrice": 141.2945214521,
                "avgPricePaid": 136.5555426888,
                "isNew": false,
                "isSoldOut": false,
                "ownership": 7.5823,
                "lastOwnership": 7.6066,
                "changeInOwnership": -0.0244,
                "changeInOwnershipPercentage": -0.3206,
                "holdingPeriod": 32,
                "firstAdded": "2013-12-31",
                "performance": 5994507414.1991,
                "performancePercentage": 3.4704,
                "lastPerformance": 18555654047.2223,
                "changeInPerformance": -12561146633.0232,
                "isCountedForPerformance": true
            }
        ]
        """
        return self.api.get(
            STOCK_OWNERSHIP_BY_HOLDERS_ENDPOINT,
            params={"symbol": symbol, "date": date, "page": page},
        )

    def get_portfolio_holdings_summary(self, cik, page=None):
        """Provides a summary of portfolio holdings.

         Including the top holdings, sector allocation, and industry allocation.

        Args:
            cik (str): CIK of the company
            page (int): The page number

        Returns: [
            {
                "date": "2021-09-30",
                "cik": "0001067983",
                "investorName": "BERKSHIRE HATHAWAY INC",
                "portfolioSize": 43,
                "performance3yearRelativeToSP500Percentage": 14.2185,
                "performance5yearRelativeToSP500Percentage": 45.5084,
                "performanceSinceInceptionRelativeToSP500Percentage": 67.7794
            }
        ]
        """
        return self.api.get(
            PORTFOLIO_HOLDINGS_SUMMARY_ENDPOINT, params={"cik": cik, "page": page}
        )

    def get_industry_ownership_summary(self, date, cik, page=None):
        """Provides a summary of industry ownership.

         Including the top industries and the average weight of each industry.

        Args:
            date (str): The date of the filing. Format: YYYY-MM-DD
            cik (str): CIK of the company
            page (int): The page number

        Returns: [
            {
                "date": "2021-09-30",
                "cik": "0001067983",
                "investorName": "BERKSHIRE HATHAWAY INC",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "weight": 42.7776,
                "lastWeight": 41.465,
                "changeInWeight": 1.3126,
                "changeInWeightPercentage": 3.1656,
                "performance": 4204116550.5744,
                "performancePercentage": 3.4601,
                "lastPerformance": 13281918464.8517,
                "changeInPerformance": -9077801914.2773
            }
        ]
        """
        return self.api.get(
            INDUSTRY_OWNERSHIP_SUMMARY_ENDPOINT,
            params={"date": date, "cik": cik, "page": page},
        )

    def get_ownership_by_shares_held(self, symbol, date, page=None):
        """Provides the ownership of stocks by number of shares held.

        Args:
            symbol (str): The stock symbol, e.g. "AAPL"
            date (str): The date of the filing. Format: YYYY-MM-DD
            page (int): The page number of the feed

        Returns: [
            {
                "date": "2021-09-30",
                "cik": "0001308668",
                "filingDate": "2021-10-26",
                "investorName": "GUIDESTONE CAPITAL MANAGEMENT, LLC",
                "symbol": "AAPL",
                "securityName": "APPLE INC",
                "typeOfSecurity": "COM",
                "securityCusip": "037833100",
                "sharesType": "SH",
                "putCallShare": "Share",
                "investmentDiscretion": "SOLE",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "weight": 100,
                "lastWeight": 100,
                "changeInWeight": 0,
                "changeInWeightPercentage": 0,
                "marketValue": 83304000,
                "lastMarketValue": 80631000,
                "changeInMarketValue": 2673000,
                "changeInMarketValuePercentage": 3.3151,
                "sharesNumber": 588722,
                "lastSharesNumber": 588722,
                "changeInSharesNumber": 0,
                "changeInSharesNumberPercentage": 0,
                "quarterEndPrice": 141.2945214521,
                "avgPricePaid": 136.5555426888,
                "isNew": false,
                "isSoldOut": false,
                "ownership": 0.0035,
                "lastOwnership": 0.0035,
                "changeInOwnership": 0,
                "changeInOwnershipPercentage": -0.4305,
                "holdingPeriod": 8,
                "firstAdded": "2019-12-31",
                "performance": 2789941.0555,
                "performancePercentage": 3.4704,
                "lastPerformance": 8814163.2552,
                "changeInPerformance": -6024222.1997,
                "isCountedForPerformance": true
            }
        ]
        """
        return self.api.get(
            OWNERSHIP_BY_SHARES_HELD_ENDPOINT,
            params={"symbol": symbol, "date": date, "page": page},
        )

    def get_portfolio_composition(self, cik, date, page=None):
        """Provides the composition of portfolios.

         Including the asset allocation, sector allocation,
         and industry allocation.

        Args:
            cik (str): CIK of the company
            date (str): The date of the filing. Format: YYYY-MM-DD
            page (int): The page number of the feed

        Returns: [
            {
                "date": "2021-09-30",
                "cik": "0001067983",
                "filingDate": "2021-11-15",
                "investorName": "BERKSHIRE HATHAWAY INC",
                "symbol": "AAPL",
                "securityName": "APPLE INC",
                "typeOfSecurity": "COM",
                "securityCusip": "037833100",
                "sharesType": "SH",
                "putCallShare": "Share",
                "investmentDiscretion": "DFND",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "weight": 42.7776,
                "lastWeight": 41.465,
                "changeInWeight": 1.3126,
                "changeInWeightPercentage": 3.1656,
                "marketValue": 125529681000,
                "lastMarketValue": 121502087000,
                "changeInMarketValue": 4027594000,
                "changeInMarketValuePercentage": 3.3148,
                "sharesNumber": 887135554,
                "lastSharesNumber": 887135554,
                "changeInSharesNumber": 0,
                "changeInSharesNumberPercentage": 0,
                "quarterEndPrice": 141.2945214521,
                "avgPricePaid": 136.5555426888,
                "isNew": false,
                "isSoldOut": false,
                "ownership": 5.3118,
                "lastOwnership": 5.3348,
                "changeInOwnership": -0.023,
                "changeInOwnershipPercentage": -0.4305,
                "holdingPeriod": 23,
                "firstAdded": "2016-03-31",
                "performance": 4204116550.5744,
                "performancePercentage": 3.4704,
                "lastPerformance": 13281918464.8517,
                "changeInPerformance": -9077801914.2773,
                "isCountedForPerformance": true
            }
        ]
        """
        return self.api.get(
            PORTFOLIO_COMPOSITION_ENDPOINT,
            params={"cik": cik, "date": date, "page": page},
        )

    def get_institutional_holder(self, symbol):
        """Provides detailed information on individual investment managers.

         Including their holdings, contact information, and investment style.

        Args:
            symbol (str): The stock symbol, e.g. "AAPL"

        Returns: [
            {
                "holder": "EWG ELEVATE INC.",
                "shares": 13944,
                "dateReported": "2022-12-31",
                "change": 2286
            }
        ]

        """
        return self.api.get(INSTITUTIONAL_HOLDER_ENDPOINT.format(symbol=symbol))

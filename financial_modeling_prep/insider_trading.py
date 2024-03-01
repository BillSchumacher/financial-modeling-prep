"""Insider Trading API endpoints."""
INSIDER_TRADES_RSS_ENDPOINT = "v4/insider-trading-rss-feed"
INSIDER_TRADES_SEARCH_ENDPOINT = "v4/insider-trading"
TRANSACTION_TYPES_ENDPOINT = "v4/insider-trading-transaction-type"
INSIDERS_BY_SYMBOL_ENDPOINT = "v4/insider-roaster"
INSIDER_TRADE_STATISTICS_ENDPOINT = "v4/insider-roaster-statistics"
CIK_MAPPER_ENDPOINT = "v4/mapper-cik-name"
CIK_MAPPER_BY_SYMBOL_ENDPOINT = "v4/mapper-cik-company/{symbol}"
FAIL_TO_DELIVER_ENDPOINT = "v4/fail-to-deliver"


class InsiderTrading:
    """
    A class to access insider trading data.

    Explanation:
      This class provides methods to retrieve information about insider trades,
       insider transaction types, insiders by company symbol,
       insider trade statistics, CIK number mapping, fail to deliver data, and more.

    Methods:
    - insider_trades_rss: Get an RSS feed of insider trades.
    - insider_trades_search:
     Search for insider trades by company name, ticker symbol, or insider name.
    - transaction_types: Get a list of insider transaction types.
    - insiders_by_symbol: Get a list of insiders for a given company.
    - insider_trade_statistics:
      Get statistics on insider trading activity for a company.
    - cik_mapper: Convert a CIK number to a company name.
    - cik_mapper_by_symbol: Get a list of CIK numbers and company names by symbol.
    - fail_to_deliver: Get a list of fail to deliver data for a company.
    """

    def __init__(self, api):
        """
        Initializes the InsiderTrading class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def insider_trades_rss(self, page=None):
        """Provides an RSS feed of insider trades, updated in real-time.

        Args:
            page (int, optional): The page number to retrieve

        Returns: [
            {
                "title": "4 - Atlantic Union Bankshares Corp (0000883948) (Issuer)",
                "fillingDate": "2022-10-05 13:43:47",
                "symbol": "AUB",
                "link": "https://www.sec.gov/Archives/edgar/data/883948/...",
                "reportingCik": "0001745407",
                "issuerCik": "0000883948"
            }
        ]
        """
        return self.api.get(INSIDER_TRADES_RSS_ENDPOINT, params={"page": page})

    def insider_trades_search(
        self, symbol=None, reporting_cik=None, company_cik=None, page=None
    ):
        """Allows users to search for insider trades.

         By company name, ticker symbol, or insider name.

        Args:
            symbol (str, optional): The ticker symbol of the company
            reporting_cik (str, optional): The CIK of the reporting owner
            company_cik (str, optional): The CIK of the company
            page (int, optional): The page number to retrieve

        Returns: [
            {
                "symbol": "AAPL",
                "filingDate": "2022-10-04 22:05:07",
                "transactionDate": "2022-10-03",
                "reportingCik": "0001767094",
                "transactionType": "S-Sale",
                "securitiesOwned": 270196,
                "securitiesTransacted": 42393,
                "companyCik": "0000320193",
                "reportingName": "O'BRIEN DEIRDRE",
                "typeOfOwner": "officer: Senior Vice President",
                "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "securityName": "Common Stock",
                "price": 141.09,
                "formType": "4",
                "acquistionOrDisposition": "D"
            }
        ]
        """
        return self.api.get(
            INSIDER_TRADES_SEARCH_ENDPOINT,
            params={
                "symbol": symbol,
                "reportingCik": reporting_cik,
                "companyCik": company_cik,
                "page": page,
            },
        )

    def transaction_types(self):
        """Provides a list of all insider transaction types.

        Such as purchases, sales, and gifts.

        Returns: [
            "J-Other",
            "P-Purchase",
            "W-Will",
            "I-Discretionary",
            "Z-Trust",
            "F-InKind"
        ]
        """
        return self.api.get(TRANSACTION_TYPES_ENDPOINT)

    def insiders_by_symbol(self, symbol):
        """Provides a list of all insiders for a given company.

        Args:
            symbol (str): The ticker symbol of the company

        Returns: [
            {
                "typeOfOwner": "officer: SVP, GC and Secretary",
                "transactionDate": "2022-10-03",
                "owner": "Adams Katherine L."
            }
        ]
        """
        return self.api.get(INSIDERS_BY_SYMBOL_ENDPOINT, params={"symbol": symbol})

    def insider_trade_statistics(self, symbol):
        """Provides statistics on insider trading activity.

        Such as the total number of insider trades,
         the average value of insider trades, and the most popular insider stocks.

        Args:
            symbol (str): The ticker symbol of the company

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "year": 2022,
                "quarter": 4,
                "purchases": 6,
                "sales": 30,
                "buySellRatio": 0.2,
                "totalBought": 1492148,
                "totalSold": 2810029,
                "averageBought": 248691.3333,
                "averageSold": 93667.6333,
                "pPurchases": 0,
                "sSales": 15
            }
        ]
        """
        return self.api.get(
            INSIDER_TRADE_STATISTICS_ENDPOINT, params={"symbol": symbol}
        )

    def cik_mapper(self, page=None, name=None):
        """Converts a CIK number to a company name.

        Args:
            page (int, optional): The page number to retrieve
            name (str, optional): The name of the company or person

        Returns: [
            {
                "reportingCik": "0001453356",
                "reportingName": "10X Fund, L.P."
            }
        ]
        """
        return self.api.get(CIK_MAPPER_ENDPOINT, params={"page": page, "name": name})

    def cik_mapper_by_symbol(self, symbol):
        """Provides a list of all CIK numbers and corresponding company names.

        Args:
            symbol (str): The ticker symbol of the company

        Returns: [
            {
                "symbol": "MSFT",
                "companyCik": "0000789019"
            }
        ]
        """
        return self.api.get(CIK_MAPPER_BY_SYMBOL_ENDPOINT.format(symbol=symbol))

    def fail_to_deliver(self, symbol, page=None):
        """Provides a list of all fail to deliver data.

        Args:
            symbol (str): The ticker symbol of the company
            page (int, optional): The page number to retrieve

        Returns: [
            {
                "symbol": "GE",
                "date": "2023-09-27",
                "price": 109.93,
                "quantity": 3320,
                "cusip": "369604301",
                "name": "GEN ELEC CO COM NEW (NY)"
            }
        ]
        """
        return self.api.get(
            FAIL_TO_DELIVER_ENDPOINT, params={"symbol": symbol, "page": page}
        )

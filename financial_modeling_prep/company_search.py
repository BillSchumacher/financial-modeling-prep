"""Company Search API."""
GENERAL_SEARCH_ENDPOINT = "v3/search"
TICKER_SEARCH_ENDPOINT = "v3/search-ticker"
NAME_SEARCH_ENDPOINT = "v3/search-name"
CIK_NAME_SEARCH_ENDPOINT = "v3/cik-search/{company_name}"
CIK_SEARCH_ENDPOINT = "v3/cik/{cik_number}"
CUSIP_SEARCH_ENDPOINT = "v3/cusip/{cusip_number}"


class CompanySearch:
    """
    The Company Search API.

    Used to find company names, stock symbols,
     and other financial instruments by using a search query.

    Methods:
    - `general_search(query, limit=10, exchange=None)`:
    Search over 70,000 symbols by symbol name or company name,
     including cryptocurrencies, forex, stocks, etf and other financial instruments.
    - `ticker_search(query, limit=10, exchange=None)`:
    Find ticker symbols and exchanges for both equity securities and
    exchange-traded funds (ETFs) by searching with the company name or ticker symbol.
    - `name_search(query, limit=10, exchange=None)`:
    Find ticker symbols and exchange information for equity securities
     and exchange-traded funds (ETFs) by searching with the company name.
    - `cik_name_search(company_name)`:
    Discover CIK numbers for SEC-registered entities with our CIK Name Search.
    - `cik_search(cik_number)`:
    Quickly find registered company names linked to SEC-registered
     entities using their CIK Number with our CIK Search.
    - `cusip_search(cusip_number)`:
    Access information about financial instruments and securities by
     simply entering their unique CUSIP (Committee on Uniform
      Securities Identification Procedures) numbers with our CUSIP Search.


    """

    def __init__(self, api):
        """
        Initializes the CompanySearch class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def general_search(self, query: str, limit: int = 10, exchange: str = None) -> dict:
        """
        Search over 70,000 symbols by symbol name or company name.

        Including cryptocurrencies, forex, stocks, etf and other financial instruments.

        Args:
            query: string - The search query (Symbol)
            limit: int - The number of results to return
            exchange: string - The exchange to search

        Returns: [
            {
                "symbol": "PRAA",
                "name": "PRA Group, Inc.",
                "currency": "USD",
                "stockExchange": "NasdaqGS",
                "exchangeShortName": "NASDAQ"
            },
            {
                "symbol": "PAAS",
                "name": "Pan American Silver Corp.",
                "currency": "USD",
                "stockExchange": "NasdaqGS",
                "exchangeShortName": "NASDAQ"
            }
        ]
        """
        params = {"query": query, "limit": limit, "exchange": exchange}
        return self.api.get(GENERAL_SEARCH_ENDPOINT, params=params)

    def ticker_search(self, query: str, limit: int = 10, exchange: str = None) -> dict:
        """
        Find ticker symbols and exchanges.

        For both equity securities and exchange-traded funds (ETFs)
          by searching with the company name or ticker symbol.

        Args:
            query: string - The search query (Company Name or Ticker Symbol)
            limit: int - The number of results to return
            exchange: string - The exchange to search

        Returns: [
            {
                "symbol": "PRAA",
                "name": "PRA Group, Inc.",
                "currency": "USD",
                "stockExchange": "NasdaqGS",
                "exchangeShortName": "NASDAQ"
            },
            {
                "symbol": "PAAS",
                "name": "Pan American Silver Corp.",
                "currency": "USD",
                "stockExchange": "NasdaqGS",
                "exchangeShortName": "NASDAQ"
            }
        ]
        """
        params = {"query": query, "limit": limit, "exchange": exchange}
        return self.api.get(TICKER_SEARCH_ENDPOINT, params=params)

    def name_search(self, query: str, limit: int = 10, exchange: str = None) -> dict:
        """
        Find ticker symbols and exchange information.

        For equity securities and exchange-traded funds (ETFs)
         by searching with the company name.

        Args:
            query: string - The search query (Company Name)
            limit: int - The number of results to return
            exchange: string - The exchange to search

        Returns: [
            {
                "symbol": "PRAA",
                "name": "PRA Group, Inc.",
                "currency": "USD",
                "stockExchange": "NasdaqGS",
                "exchangeShortName": "NASDAQ"
            },
            {
                "symbol": "PAAS",
                "name": "Pan American Silver Corp.",
                "currency": "USD",
                "stockExchange": "NasdaqGS",
                "exchangeShortName": "NASDAQ"
            }
        ]
        """
        params = {"query": query, "limit": limit, "exchange": exchange}
        return self.api.get(NAME_SEARCH_ENDPOINT, params=params)

    def cik_name_search(self, company_name: str) -> dict:
        """
        Discover CIK numbers for SEC-registered entities with our CIK Name Search.

        Args:
            company_name: string - The company name to search

        Returns: [
            {
                "name": "BERKSHIRE BANCORP INC.",
                "cik": "0000000000"
            },
            {
                "name": "BERKSHIRE FOCUS FUND",
                "cik": "0000000000"
            },
            {
                "name": "BERKSHIRE GREY, INC.",
                "cik": "0001824734"
            }
        ]
        """
        return self.api.get(CIK_NAME_SEARCH_ENDPOINT.format(company_name=company_name))

    def cik_search(self, cik_number: str) -> dict:
        """
        Quickly find registered company names.

        Linked to SEC-registered entities using their CIK Number with our CIK Search.

        Args:
            cik_number: string - The CIK number to search

        Returns: [
            {
                "name": "BERKSHIRE HATHAWAY INC.",
                "cik": "0001067983"
            }
        ]
        """
        return self.api.get(CIK_SEARCH_ENDPOINT.format(cik_number=cik_number))

    def cusip_search(self, cusip_number: str) -> dict:
        """
        Access information about financial instruments and securities.

        By simply entering their unique CUSIP
        (Committee on Uniform Securities Identification Procedures)
        numbers with our CUSIP Search.

        Args:
            cusip_number: string - The CUSIP number to search

        Returns: [
            {
                "company": "AAON, INC.",
                "ticker": "AAON",
                "cusip": "000360206"
            }
        ]
        """
        return self.api.get(CUSIP_SEARCH_ENDPOINT.format(cusip_number=cusip_number))

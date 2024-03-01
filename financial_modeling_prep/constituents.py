"""Constituents module for the API."""
SP500_CONSTITUENTS_ENDPOINT = "v3/sp500_constituent"
HISTORICAL_SP500_CONSTITUENTS_ENDPOINT = "v3/historical/sp500_constituent"
NASDAQ_CONSTITUENTS_ENDPOINT = "v3/nasdaq_constituent"
HISTORICAL_NASDAQ_CONSTITUENTS_ENDPOINT = "v3/historical/nasdaq_constituent"
DOW_JONES_CONSTITUENTS_ENDPOINT = "v3/dowjones_constituent"
HISTORICAL_DOW_JONES_CONSTITUENTS_ENDPOINT = "v3/historical/dowjones_constituent"


class Constituents:
    """
    A class to access information about index constituents.

    Explanation:
    This class provides methods to retrieve lists of companies included in the
     S&P 500, NASDAQ, and Dow Jones indices, as well as historical data for
      these index constituents.

    Methods:
    - sp500_constituents:
     Provides a list of all companies that are included in the S&P 500 index.
    - historical_sp500_constituents:
     Provides historical data for all companies in the S&P 500 index.
    - nasdaq_constituents:
     Provides a list of all companies that are included in the NASDAQ index.
    - historical_nasdaq_constituents:
     Provides historical data for all companies in the NASDAQ index.
    - dow_jones_constituents:
     Provides a list of all companies that are included in the Dow Jones index.
    - historical_dow_jones_constituents:
     Provides historical data for all companies in the Dow Jones index.
    """

    def __init__(self, api):
        """
        Initializes the Constituents class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def sp500_constituents(self, datatype: str = "json"):
        """Provides a list of all companies that are included in the S&P 500 index.

        Args:
            datatype (str, optional): json, csv. Defaults to "json".

        Returns:
            dict: [
            {
                "symbol": "VLTO",
                "name": "Veralto",
                "sector": "Industrials",
                "subSector": "",
                "headQuarter": "Waltham, Massachusetts",
                "dateFirstAdded": "2023-10-02",
                "cik": "0001967680",
                "founded": "2023"
            }
        ]
        """
        params = {"datatype": datatype}
        return self.api.get(SP500_CONSTITUENTS_ENDPOINT, params=params)

    def historical_sp500_constituents(self):
        """Provides historical data for all companies in the S&P 500 index.

        Returns:
            dict: [
            {
                "dateAdded": "October 3, 2023",
                "addedSecurity": "",
                "removedTicker": "DXC",
                "removedSecurity": "DXC Technology",
                "date": "2023-10-03",
                "symbol": "DXC",
                "reason": "Market capitalization change."
            }
        ]
        """
        return self.api.get(HISTORICAL_SP500_CONSTITUENTS_ENDPOINT)

    def nasdaq_constituents(self, datatype: str = "json"):
        """Provides a list of all companies that are included in the NASDAQ index.

        Args:
            datatype (str, optional): json, csv. Defaults to "json".

        Returns:
            dict: [
            {
                "symbol": "AAPL",
                "name": "Apple Inc.",
                "sector": "Technology",
                "subSector": "Technology",
                "headQuarter": "Cupertino, CA",
                "dateFirstAdded": null,
                "cik": "0000320193",
                "founded": "1976-04-01"
            }
        ]
        """
        params = {"datatype": datatype}
        return self.api.get(NASDAQ_CONSTITUENTS_ENDPOINT, params=params)

    def historical_nasdaq_constituents(self):
        """Provides historical data for all companies in the NASDAQ index.

        Returns:
            dict: [
            {
                "dateAdded": "December 21, 2020",
                "addedSecurity": "Okta Inc",
                "removedTicker": "",
                "removedSecurity": null,
                "date": "2020-12-21",
                "symbol": "OKTA",
                "reason": "Market capitalization change"
            }
        ]
        """
        return self.api.get(HISTORICAL_NASDAQ_CONSTITUENTS_ENDPOINT)

    def dow_jones_constituents(self, datatype: str = "json"):
        """Provides a list of all companies that are included in the Dow Jones index.

        Args:
            datatype (str, optional): json, csv. Defaults to "json".

        Returns:
            dict: [
            {
                "symbol": "AMGN",
                "name": "Amgen Inc.",
                "sector": "Healthcare",
                "subSector": "Healthcare",
                "headQuarter": "Thousand Oaks, CA",
                "dateFirstAdded": "2020-08-31",
                "cik": "0000318154",
                "founded": "1980-04-08"
            }
        ]
        """
        params = {"datatype": datatype}
        return self.api.get(DOW_JONES_CONSTITUENTS_ENDPOINT, params=params)

    def historical_dow_jones_constituents(self):
        """Provides historical data for all companies in the Dow Jones index.

        Returns:
            dict: [
            {
                "dateAdded": "August 31, 2020",
                "addedSecurity": "Salesforce.Com Inc",
                "removedTicker": "",
                "removedSecurity": "",
                "date": "2020-08-31",
                "symbol": "CRM",
                "reason": "Market capitalization change."
            }
        ]
        """
        return self.api.get(HISTORICAL_DOW_JONES_CONSTITUENTS_ENDPOINT)

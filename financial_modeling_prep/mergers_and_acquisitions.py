"""Mergers and Acquisitions (M&A) API endpoints."""
MA_RSS_FEED_ENDPOINT = "v4/mergers-acquisitions-rss-feed"
SEARCH_MA_ENDPOINT = "v4/mergers-acquisitions/search"


class MergersAndAcquisitions:
    """
    A class to retrieve information about mergers and acquisitions (M&A) activities.

    Explanation:
    This class provides methods to fetch M&A news and announcements from the
     FMP M&A RSS Feed, as well as search for M&A deals based on company names.

    Methods:
    - get_mergers_and_acquisitions:
     Get a real-time stream of M&A news and announcements.
    - search_mergers_and_acquisitions: Search for M&A deals based on company names.
    """

    def __init__(self, api):
        """
        Initializes the MergersAndAcquisitions class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_mergers_and_acquisitions(self, page: int = 0):
        """Provides real-time stream of M&A news and announcements.

        Args:
            page (int, optional): The page number. Default is 0.

        Returns: [
            {
                "companyName": "GRIZZLY NEW PUBCO, INC.",
                "cik": "0001946991",
                "symbol": "CDCN",
                "targetedCompanyName": "DTRT HEALTH ACQUISITION CORP.",
                "targetedCik": "0001865537",
                "targetedSymbol": "DTRTU",
                "transactionDate": "2022-10-19",
                "acceptanceTime": "2022-10-19 21:17:55",
                "url": "https://www.sec.gov/Archives/edgar/data/1946991/..."
            }
        ]
        """
        return self.api.get(MA_RSS_FEED_ENDPOINT, {"page": page})

    def search_mergers_and_acquisitions(self, name: str):
        """Search for M&A deals based on a variety of criteria.

        Users can also specify a date range to search for M&A deals
          that were announced during that period.

        Args:
            name (str): The name of the company.

        Returns: [
            {
                "companyName": "Syros Pharmaceuticals, Inc.",
                "cik": "0001556263",
                "symbol": "SYRS",
                "targetedCompanyName": "TYME",
                "targetedCik": null,
                "targetedSymbol": "TYME",
                "transactionDate": "2022-07-18",
                "acceptanceTime": "2022-07-18 07:58:48",
                "url": "https://www.sec.gov/Archives/edgar/data/1556263/..."
            }
        ]
        """
        return self.api.get(SEARCH_MA_ENDPOINT, {"name": name})

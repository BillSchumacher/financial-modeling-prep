"""SECFilings class for interacting with the SEC Filings API endpoints."""
from datetime import date

RSS_FEED_ENDPOINT = "v4/rss_feed"
RSS_FEED_V3_ENDPOINT = "v3/rss_feed"
RSS_FEED_8K_ENDPOINT = "v4/rss_feed_8k"
SEC_FILINGS_ENDPOINT = "v3/sec_filings/{symbol}"
INDIVIDUAL_INDUSTRY_CLASSIFICATION_ENDPOINT = "v4/standard_industrial_classification"
ALL_INDUSTRY_CLASSIFICATION_ENDPOINT = "v4/standard_industrial_classification/all"
ALL_INDUSTRY_CLASSIFICATION_CODES_ENDPOINT = (
    "v4/standard_industrial_classification_list"
)


class SECFilings:
    """Real-time SEC filings from publicly traded companies."""

    def __init__(self, api):
        """
        Initializes the SECFilings class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def rss_feed(
        self,
        limit: int = 100,
        filing_type: str = None,
        from_: date = None,
        to: date = None,
        is_done: bool = None,
    ) -> dict:
        """A real-time feed of SEC filings from publicly traded companies.

         Including the filing type, link to SEC page, and direct link to the filing.
        This endpoint can be used to stay up-to-date on the latest SEC filings
         for all companies or for a specific set of companies.

        Args:
            limit (int, optional): The number of filings to return. Default is 100.
            filing_type (str, optional): The type of filing to return. Default is all.
             See the SEC documentation for a list of filing types.
            from_ (date, optional): The start date for the filings to return.
            to (date, optional): The end date for the filings to return.
            is_done (bool, optional): If true, only return filings that are complete.
             If false, return filings that are not complete. Default is all filings.

        Returns: [
            {
                "title": "6-K - Sangoma Technologies Corp (0001753368) (Filer)",
                "date": "2023-09-27 17:07:28",
                "link": "https://www.sec.gov/Archives/edgar/data/1753368/...",
                "cik": "0001753368",
                "form_type": "6-K",
                "ticker": "SANG",
                "done": true
            }
        ]
        """
        params = {
            "limit": limit,
            "type": filing_type,
            "from": from_,
            "to": to,
            "isDone": is_done,
        }
        return self.api.get(RSS_FEED_ENDPOINT, params=params)

    def rss_feed_v3(self, page: int = 0, datatype: str = "json") -> dict:
        """A real-time feed of SEC filings from publicly traded companies.

         Including the filing type, link to SEC page, and direct link to the filing.
          This endpoint can be used to stay up-to-date on the latest SEC filings
           for all companies or for a specific set of companies.

        Args:
            page (int, optional): The page number to return. Default is 0
            datatype (str, optional): csv,json

        Returns: [
            {
                "title": "6-K - BRP Inc. (0001748797) (Filer)",
                "date": "2023-10-04 17:29:28",
                "link": "https://www.sec.gov/Archives/edgar/data/1748797/...",
                "cik": "0001748797",
                "form_type": "6-K",
                "ticker": "DOOO",
                "done": true
            }
        ]
        """
        params = {"page": page, "datatype": datatype}
        return self.api.get(RSS_FEED_V3_ENDPOINT, params=params)

    def rss_feed_8k(
        self,
        page: int = 0,
        from_: date = None,
        to: date = None,
        has_financial: bool = None,
        limit: int = 10,
    ) -> dict:
        """A real-time feed of 8-K filings from publicly traded companies.

         Including the filing type, link to SEC page, and direct link to the filing.
         This endpoint can be used to stay up-to-date on the latest 8-K filings
          for all companies or for a specific set of companies.

        Args:
            page (int, optional): The page number to return. Default is 0
            from_ (date, optional): The start date for the filings to return.
            to (date, optional): The end date for the filings to return.
            has_financial (bool, optional):
             If true, only return filings that contain financial data.
             If false, only return filings that do not contain financial data.
             Default is all filings.
            limit (int, optional): The number of filings to return. Default is 10.

        Returns: [
            {
                "title": "8-K - BUTLER NATIONAL CORP (0000015847) (Filer)",
                "symbol": "BUKS",
                "cik": "0000015847",
                "link": "https://www.sec.gov/Archives/edgar/data/15847/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/...",
                "date": "2022-08-25 10:05:41"
            }
        ]
        """
        params = {
            "page": page,
            "from": from_,
            "to": to,
            "hasFinancial": has_financial,
            "limit": limit,
        }
        return self.api.get(RSS_FEED_8K_ENDPOINT, params=params)

    def sec_filings(
        self, symbol: str, page: int = 0, filing_type: str = "10-K"
    ) -> dict:
        """Direct link to SEC filings for a specific company.

         Including the filing type, link to SEC page, and direct link to the filing.
          This endpoint can be used to get all SEC filings for a specific company.

        Args:
            symbol (str): The stock symbol of the company
            page (int, optional): The page number to return. Default is 0
            filing_type (str, optional): 10-K

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "type": "10-K",
                "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/...",
                "acceptedDate": "2022-10-27 18:01:14",
                "fillingDate": "2022-10-28 00:00:00"
            }
        ]
        """
        params = {"page": page, "type": filing_type}
        return self.api.get(SEC_FILINGS_ENDPOINT.format(symbol=symbol), params=params)

    def individual_industry_classification(
        self, symbol: str, cik: str = None, sic_code: str = None
    ) -> dict:
        """Identify the industry classification for a company.

         This endpoint can be used to get the industry classification
          for a specific company.

        Args:
            symbol (str): The stock symbol of the company
            cik (str, optional): The CIK number of the company
            sic_code (str, optional): The SIC code of the company

        Returns: [
            {
                "symbol": "AAPL",
                "name": "Apple Inc. ",
                "cik": "0000320193",
                "sicCode": "3571",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "businessAdress": "['ONE APPLE PARK WAY', 'CUPERTINO CA 95014']",
                "phoneNumber": "(408) 996-1010"
            }
        ]
        """
        params = {"symbol": symbol, "cik": cik, "sicCode": sic_code}
        return self.api.get(INDIVIDUAL_INDUSTRY_CLASSIFICATION_ENDPOINT, params=params)

    def all_industry_classification(self) -> dict:
        """Get a comprehensive overview of all industries.

         Classified according to the SIC system.

        Returns: [
            {
                "symbol": "A",
                "name": "AGILENT TECHNOLOGIES, INC. ",
                "cik": "0001090872",
                "sicCode": "3826",
                "industryTitle": "LABORATORY ANALYTICAL INSTRUMENTS",
                "businessAdress": "['5301 STEVENS CREEK BLVD, MS 1A-LC',...",
                "phoneNumber": "(408) 345-8886"
            }
        ]
        """
        return self.api.get(ALL_INDUSTRY_CLASSIFICATION_ENDPOINT)

    def all_industry_classification_codes(
        self, industry_title: str = None, sic_code: str = None
    ) -> dict:
        """Get SIC system and identify the SIC code for a particular industry.

        Args:
            industry_title (str, optional): The title of the industry
            sic_code (str, optional): The SIC code of the industry

        Returns: [
            {
                "office": "Office of Life Sciences",
                "sicCode": "200",
                "industryTitle": "AGRICULTURAL PROD-LIVESTOCK & ANIMAL SPECIALTIES"
            }
        ]
        """
        params = {"industryTitle": industry_title, "sicCode": sic_code}
        return self.api.get(ALL_INDUSTRY_CLASSIFICATION_CODES_ENDPOINT, params=params)

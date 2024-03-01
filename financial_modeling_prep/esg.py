"""Environmental, Social, and Governance (ESG) data for stocks and funds."""
ESG_SEARCH_ENDPOINT = "v4/esg-environmental-social-governance-data"
ESG_RATINGS_ENDPOINT = "v4/esg-enviromental-social-governance-data-ratings"
ESG_BENCHMARK_ENDPOINT = "v4/esg-environmental-social-governance-sector-benchmark"


class ESG:
    """
    A class to access ESG data for stocks and funds.

    Explanation:
    This class provides methods to search for ESG data,
    retrieve ESG ratings, and get ESG benchmark data for
    specific symbols or years.

    Methods:
    - esg_search: Search for ESG data for a specific symbol.
    - esg_ratings: Get ESG ratings for a specific symbol.
    - esg_benchmark: Get ESG benchmark data for a specific year.
    """

    def __init__(self, api):
        """
        Initializes the ESG class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def esg_search(self, symbol: str) -> dict:
        """Search for ESG data for a specific symbol.

        Args:
            symbol (str): Stock or fund ticker symbol

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "date": "2022-03-26",
                "environmentalScore": 68.625,
                "socialScore": 75.57444444444445,
                "governanceScore": 72.17694444444444,
                "ESGScore": 72.12546296296297,
                "companyName": "Apple Inc.",
                "industry": "Electronic Computers",
                "formType": "10-Q",
                "acceptedDate": "2022-04-28 18:03:58",
                "url": "https://www.sec.gov/Archives/edgar/data/320193/..."
            }
        ]
        """
        return self.api.get(url=ESG_SEARCH_ENDPOINT, params={"symbol": symbol})

    def esg_ratings(self, symbol: str) -> dict:
        """Get ESG ratings for a specific symbol.

        Args:
            symbol (str): Stock or fund ticker symbol

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "companyName": "Apple Inc.",
                "industry": "ELECTRONIC COMPUTERS",
                "year": 2022,
                "ESGRiskRating": "B",
                "industryRank": "7 out of 7"
            }
        ]
        """
        return self.api.get(url=ESG_RATINGS_ENDPOINT, params={"symbol": symbol})

    def esg_benchmark(self, year: int) -> dict:
        """Get ESG benchmark data for a specific year.

        Args:
            year (int): Year of the data

        Returns: [
            {
                "year": 2022,
                "sector": "WATER SUPPLY",
                "environmentalScore": 63.05443771241376,
                "socialScore": 64.0875999431528,
                "governanceScore": 66.21121341610079,
                "ESGScore": 64.45108369055579
            }
        ]
        """
        return self.api.get(url=ESG_BENCHMARK_ENDPOINT, params={"year": year})

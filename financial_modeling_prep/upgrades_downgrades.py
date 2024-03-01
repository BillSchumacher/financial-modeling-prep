"""Upgrades and Downgrades API endpoints."""
UPGRADES_AND_DOWNGRADES_RSS_FEED_ENDPOINT = "v4/upgrades-downgrades-rss-feed"
UPGRADES_AND_DOWNGRADES_CONSENSUS_ENDPOINT = "v4/upgrades-downgrades-consensus"
UPGRADES_AND_DOWNGRADES_BY_COMPANY_ENDPOINT = "v4/upgrades-downgrades-grading-company"


class UpgradesAndDowngrades:
    """
    A class to access stock upgrades and downgrades information.

    Explanation:
    This class provides methods to retrieve RSS feeds of stock upgrades and
     downgrades from different analysts, consensus ratings for companies, and
     a comprehensive list of upgrades and downgrades for a specific company.

    Methods:
    - get_rss_feed:
    Get an RSS feed of all stock upgrades and downgrades from different analysts.
    - get_consensus:
    Get the consensus rating for a company, which is the average rating of analysts.
    - get_by_company:
    Get a list of all stock upgrades and downgrades for a specific company.
    """

    def __init__(self, api):
        """
        Initializes the UpgradesAndDowngrades class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_rss_feed(self, page: int = 0) -> dict:
        """Get an RSS feed of all stock upgrades and downgrades from different analysts.

        This RSS feed is updated on a daily basis, so you can always stay
         up-to-date on the latest analyst ratings without having to
         manually check for updates.

        Args:
            page (int, optional): The page number to retrieve.
             Each page contains 100 items. Defaults to 0.

        Returns: [
            {
                "symbol": "DAL",
                "publishedDate": "2023-10-04T15:24:00.000Z",
                "newsURL": "https://www.benzinga.com/analyst-ratings/analyst-color/...",
                "newsTitle": "Delta Air Lines 3Q23 Earnings In Focus: BofA ...",
                "newsBaseURL": "benzinga.com",
                "newsPublisher": "Benzinga",
                "newGrade": "Buy",
                "previousGrade": "Buy",
                "gradingCompany": "Bank of America Securities",
                "action": "hold",
                "priceWhenPosted": 36.055
            }
        ]
        """
        return self.api.get(UPGRADES_AND_DOWNGRADES_RSS_FEED_ENDPOINT, {"page": page})

    def get_consensus(self, symbol: str) -> dict:
        """Get the consensus rating for a company, the average rating from analysts.

        This information can be used to get a general idea of what analysts
         think about a company's stock and to make more informed investment decisions.

        Args:
            symbol (str): The ticker symbol of the company.

        Returns: [
            {
                "symbol": "AAPL",
                "strongBuy": 0,
                "buy": 22,
                "hold": 10,
                "sell": 1,
                "strongSell": 0,
                "consensus": "Buy"
            }
        ]
        """
        return self.api.get(
            UPGRADES_AND_DOWNGRADES_CONSENSUS_ENDPOINT, {"symbol": symbol}
        )

    def get_by_company(self, company: str) -> dict:
        """Get a list of all stock upgrades and downgrades for a specific company.

        Including the rating change, the analyst firm, and the date
         of the rating change.

        This information can be used to track analyst sentiment for
         a company and to identify potential investment opportunities or risks.

        Args:
            company (str): The name of the company.

        Returns: [
            {
                "symbol": "ATUS",
                "publishedDate": "2022-02-18T08:14:00.000Z",
                "newsURL": "https://www.benzinga.com/news/22/02/25712046/...",
                "newsTitle": "Barclays Maintains Equal-Weight on Altice...",
                "newsBaseURL": "benzinga.com",
                "newsPublisher": "Benzinga",
                "newGrade": "Equal-Weight",
                "previousGrade": "Equal-Weight",
                "gradingCompany": "Barclays",
                "action": "hold",
                "priceWhenPosted": 11.52
            }
        ]
        """
        return self.api.get(
            UPGRADES_AND_DOWNGRADES_BY_COMPANY_ENDPOINT, {"company": company}
        )

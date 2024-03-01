"""Price Targets API endpoints."""
PRICE_TARGETS_ENDPOINT = "v4/price-target"
PRICE_TARGET_SUMMARY_ENDPOINT = "v4/price-target-summary"
PRICE_TARGET_BY_NAME_ENDPOINT = "v4/price-target-analyst-name"
PRICE_TARGET_BY_COMPANY_ENDPOINT = "v4/price-target-analyst-company"
PRICE_TARGET_CONSENSUS_ENDPOINT = "v4/price-target-consensus"
PRICE_TARGET_RSS_FEED_ENDPOINT = "v4/price-target-rss-feed"


class PriceTargets:
    """
    A class to access price target information for companies.

    Explanation:
    This class provides methods to retrieve price targets for companies,
     price target summaries from different analysts, price targets by analyst name,
     price targets for companies in specific industries or sectors, consensus price
     targets, and an RSS feed of price target updates.

    Methods:
    - price_target: Get the price target for a company.
    - price_target_summary: Get a summary of the price targets for a company.
    - price_target_by_name:
     Get the price targets for a company from a specific analyst.
    - price_target_by_company:
     Get the price targets for all companies in a specific industry or sector.
    - price_target_consensus: Get the consensus price target for a company.
    - price_target_rss_feed: Get an RSS feed of price target updates for a company.
    """

    def __init__(self, api):
        """
        Initializes the PriceTargets class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def price_target(self, symbol: str):
        """Get the price target for a company.

        Which is the price at which an analyst believes the company's
         stock is fairly valued.
        Price targets can be used to make investment decisions,
         such as whether to buy, sell, or hold a stock.

        Args:
            symbol: (str) (required) The company's ticker symbol.

        Returns: [
            {
                "symbol": "AAPL",
                "publishedDate": "2023-09-18T02:36:00.000Z",
                "newsURL": "https://www.benzinga.com/analyst-ratings/...",
                "newsTitle": "Apple Analyst Says iPhone 15 Pro,...",
                "analystName": "Daniel Ives",
                "priceTarget": 240,
                "adjPriceTarget": 240,
                "priceWhenPosted": 175.01,
                "newsPublisher": "Benzinga",
                "newsBaseURL": "benzinga.com",
                "analystCompany": "Wedbush"
            }
        ]
        """
        return self.api.get(PRICE_TARGETS_ENDPOINT, params={"symbol": symbol})

    def price_target_summary(self, symbol: str):
        r"""Get a summary of the price targets for a company from different analysts.

        This summary includes the average price target,
         the high price target, and the low price target.

        Args:
            symbol: (str) (required) The company's ticker symbol.

        Returns: [
            {
                "symbol": "AAPL",
                "lastMonth": 5,
                "lastMonthAvgPriceTarget": 220.2,
                "lastQuarter": 11,
                "lastQuarterAvgPriceTarget": 217.18,
                "lastYear": 46,
                "lastYearAvgPriceTarget": 186.8,
                "allTime": 113,
                "allTimeAvgPriceTarget": 186.31,
                "publishers": "[\"Benzinga\",\"TheFly\",\"Pulse 2.0\",..."
            }
        ]
        """
        return self.api.get(PRICE_TARGET_SUMMARY_ENDPOINT, params={"symbol": symbol})

    def price_target_by_name(self, name: str):
        """Get the price targets for a company from a specific analyst.

        This can be useful if you want to track the price targets
         of a particular analyst that you trust.

        Args:
            name: (str) (required) The name of the analyst.

        Returns: [
            {
                "symbol": "CAH",
                "publishedDate": "2023-04-12T09:24:00.000Z",
                "newsURL": "https://www.benzinga.com/trading-ideas/long-ideas/23/...",
                "newsTitle": "These 3 Health Care Stocks Delivering High-Dividend...",
                "analystName": "Tim Anderson",
                "priceTarget": 127,
                "adjPriceTarget": 127,
                "priceWhenPosted": 79.185,
                "newsPublisher": "Benzinga",
                "newsBaseURL": "benzinga.com",
                "analystCompany": "Wolfe Research"
            }
        ]
        """
        return self.api.get(PRICE_TARGET_BY_NAME_ENDPOINT, params={"name": name})

    def price_target_by_company(self, company: str):
        """Get the price targets for all companies in a specific industry or sector.

        This can be useful if you want to compare the price targets
         of different companies in the same industry.

        Args:
            company: (str) (required) The name of the company.

        Returns: [
            {
                "symbol": "LYB",
                "publishedDate": "2023-10-04T08:12:00.000Z",
                "newsURL": "https://www.benzinga.com/news/23/10/35086481/...",
                "newsTitle": "Alphabet To Rally Over 10%? Here Are 10...",
                "analystName": "Lauren Lieberman",
                "priceTarget": 146,
                "adjPriceTarget": 146,
                "priceWhenPosted": 93.79,
                "newsPublisher": "Benzinga",
                "newsBaseURL": "benzinga.com",
                "analystCompany": "Barclays"
            }
        ]
        """
        return self.api.get(
            PRICE_TARGET_BY_COMPANY_ENDPOINT, params={"company": company}
        )

    def price_target_consensus(self, symbol: str):
        """Get the consensus price target for a company.

        Which is the average of all price targets from different analysts.
        This can be useful if you want to get a general idea of what
         analysts think about a company's stock.

        Args:
            symbol: (str) (required) The company's ticker symbol.

        Returns: [
            {
                "symbol": "AAPL",
                "targetHigh": 240,
                "targetLow": 110,
                "targetConsensus": 189.18,
                "targetMedian": 195
            }
        ]
        """
        return self.api.get(PRICE_TARGET_CONSENSUS_ENDPOINT, params={"symbol": symbol})

    def price_target_rss_feed(self, page: int = 0):
        """Get an RSS feed of price target updates for a company.

        This way, you can stay up-to-date on the latest price targets from analysts.

        Args:
            page: (int) (optional) The page number of the RSS feed. Default is 0.

        Returns: [
            {
                "symbol": "FVRR",
                "publishedDate": "2023-10-04T16:24:00.000Z",
                "newsURL": "https://www.benzinga.com/analyst-ratings/analyst-color/...",
                "newsTitle": "Fiverr's Promise In 2024: Analyst Sees Upswing...",
                "analystName": "Kunal Madhukar",
                "priceTarget": 33,
                "adjPriceTarget": 33,
                "priceWhenPosted": 24.75,
                "newsPublisher": "Benzinga",
                "newsBaseURL": "benzinga.com",
                "analystCompany": "UBS"
            }
        ]
        """
        return self.api.get(PRICE_TARGET_RSS_FEED_ENDPOINT, params={"page": page})

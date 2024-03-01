"""News module for the Financial Modeling Prep API."""
FMP_ARTICLES_ENDPOINT = "v3/fmp/articles"
GENERAL_NEWS_ENDPOINT = "v4/general_news"
STOCK_NEWS = "v3/stock_news"
STOCK_NEWS_SENTIMENTS_RSS_FEED = "v4/stock-news-sentiments-rss-feed"
FOREX_NEWS_ENDPOINT = "v4/forex_news"
CRYPTO_NEWS_ENDPOINT = "v4/crypto_news"
PRESS_RELEASES_ENDPOINT = "v3/press-releases/{symbol}"
HISTORICAL_SOCIAL_SENTIMENT_ENDPOINT = "v4/historical/social-sentiment"
TRENDING_SOCIAL_SENTIMENT_ENDPOINT = "v4/social-sentiments/trending"
SOCIAL_SENTIMENT_CHANGE_ENDPOINT = "v4/social-sentiments/change"


class News:
    """
    A class to access news and social sentiment data.

    Explanation:
    This class provides methods to retrieve various types of news articles,
     press releases, social sentiment data, and trending sentiment data
     for stocks, cryptocurrencies, and companies.

    Methods:
    - get_fmp_articles: Get the latest articles from various sources.
    - get_general_news: Get the latest general news articles.
    - get_stock_news: Get the latest stock news articles.
    - get_stock_news_sentiments_rss_feed:
     Get an RSS feed of stock news articles with sentiment analysis.
    - get_forex_news: Get the latest forex news articles.
    - get_crypto_news: Get the latest cryptocurrency news articles.
    - get_press_releases: Get the latest press releases.
    - get_historical_social_sentiment: Provide historical social sentiment data.
    - get_trending_social_sentiment: Provide trending social sentiment data.
    - get_social_sentiment_change: Provide social sentiment change data.
    """

    def __init__(self, api):
        """
        Initializes the News class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_fmp_articles(self, page=0, size=5):
        """Get a list of the latest articles from a variety of sources.

        Including the headline, snippet, and publication URL.

        Args:
            page (int): 0
            size (int): 5

        Returns: [
            {
                "title": "SolarEdge Stock Plummets 25% After Q3 Revenue Warning",
                "date": "2023-10-20 11:28:00",
                "content": "<p><a href='https://financialmodelingprep.com/...",
                "tickers": "NASDAQ:SEDG",
                "image": "https://cdn.financialmodelingprep.com/images/...",
                "link": "https://financialmodelingprep.com/market-news/...",
                "author": "Davit Kirakosyan",
                "site": "Financial Modeling Prep"
            }
        ]
        """
        return self.api.get(FMP_ARTICLES_ENDPOINT, {"page": page, "size": size})

    def get_general_news(self, page=0):
        """Get a list of the latest general news articles from a variety of sources.

         Including the headline, snippet, and publication URL.

        Args:
            page (int): 0

        Returns: [
            {
                "publishedDate": "2023-10-19T22:00:09.000Z",
                "title": "Xi Jinping calls for ceasefire in...",
                "image": "https://cdn.i-scmp.com/sites/default/files/...",
                "site": "scmp",
                "text": "Chinese president also says Beijing is willing...",
                "url": "https://www.scmp.com/news/china/diplomacy/article/..."
            }
        ]
        """
        return self.api.get(GENERAL_NEWS_ENDPOINT, {"page": page})

    def get_stock_news(self, page=0, tickers=None, limit=50):
        """Get a list of the latest stock news articles from a variety of sources.

        Including the headline, snippet, and publication URL.

        Args:
            page (int): 0
            tickers (str): AAPL,FB
            limit (int): 50

        Returns: [
            {
                "symbol": "TSM",
                "publishedDate": "2023-10-19 10:38:47",
                "title": "Chip Stock Soars After Beat-and-Raise",
                "image": "https://cdn.snapi.dev/images/v1/k/j/138124333-m...",
                "site": "Schaeffers Research",
                "text": "Taiwan Semiconductor Mfg.",
                "url": "https://www.schaeffersresearch.com/content/news/2023/..."
            }
        ]
        """
        return self.api.get(
            STOCK_NEWS, {"page": page, "tickers": tickers, "limit": limit}
        )

    def get_stock_news_sentiments_rss_feed(self, page=0):
        """Get an RSS feed of the latest stock news articles.

         With their sentiment analysis, including the headline, snippet,
          publication URL, ticker symbol, and sentiment score.

        Args:
            page (int): 0

        Returns: [
            {
                "symbol": "MSFT",
                "publishedDate": "2023-10-10T21:10:53.000Z",
                "title": "No Call Of Duty On Game Pass This Year, ...",
                "image": "https://cdn.benzinga.com/files/images/story/...",
                "site": "benzinga",
                "text": "Activision Blizzard Inc (NASDAQ: ATVI) outlined...",
                "url": "https://www.benzinga.com/general/gaming/23/10/...",
                "sentiment": "Positive",
                "sentimentScore": 0.9812
            }
        ]
        """
        return self.api.get(STOCK_NEWS_SENTIMENTS_RSS_FEED, {"page": page})

    def get_forex_news(self, page=0, symbol=None):
        """Get a list of the latest forex news articles from a variety of sources.

        Including the headline, snippet, and publication URL.

        Args:
            page (int): 0
            symbol (str): EURUSD

        Returns: [
            {
                "publishedDate": "2022-10-05T16:14:56.000Z",
                "title": "Atlanta Fed GDPNow rises to 2.7% from 2.3%",
                "image": "https://images.forexlive.com/images/Atlanta%20Fed_id_...",
                "site": "Forexlive",
                "text": "Atlanta Fed GDPNow estimate for 3Q growthThe Atlanta Fed...",
                "tickers": [],
                "updatedAt": "2022-10-05T16:24:53.109Z",
                "createdAt": "2022-10-05T16:24:53.109Z",
                "type": "forex"
            }
        ]
        """
        return self.api.get(FOREX_NEWS_ENDPOINT, {"page": page, "symbol": symbol})

    def get_crypto_news(self, page=0, symbol=None):
        """Get a list of the latest cryptocurrency news articles.

        From a variety of sources, including the headline, snippet, and publication URL.

        Args:
            page (int): 0
            symbol (str): BTCUSD

        Returns: [
            {
                "publishedDate": "2022-10-05T15:57:27.000Z",
                "title": "Abu Dhabi to Host Inaugural Middle East Blockchain Awards",
                "image": "",
                "site": "Coinjournal",
                "text": "Dubai, United Arab Emirates, 5th October, 2022,...",
                "url": "https://coinjournal.net/news/abu-dhabi-to-host-inaugural...",
                "tickers": [],
                "updatedAt": "2022-10-05T16:32:00.592Z",
                "createdAt": "2022-10-05T16:32:00.592Z",
                "type": "crypto"
            }
        ]
        """
        return self.api.get(CRYPTO_NEWS_ENDPOINT, {"page": page, "symbol": symbol})

    def get_press_releases(self, symbol, page=0):
        """Get a list of the latest press releases from a variety of sources.

        Including the headline, snippet, and publication URL.

        Args:
            symbol (str): AAPL
            page (int): 0

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-02-02 16:30:00",
                "title": "APPLE REPORTS FIRST QUARTER RESULTS",
                "text": "CUPERTINO, CALIF.--( BUSINESS WIRE )--APPLE® TODAY..."
            }
        ]
        """
        return self.api.get(
            PRESS_RELEASES_ENDPOINT.format(symbol=symbol), {"page": page}
        )

    def get_historical_social_sentiment(self, symbol, page=0):
        """Provide historical social sentiment data for a given ticker or company name.

        Args:
            symbol (str): AAPL
            page (int): 0

        Returns: [
            {
                "date": "2022-06-30 23:00:00",
                "symbol": "AAPL",
                "stocktwitsPosts": 13,
                "twitterPosts": 163,
                "stocktwitsComments": 9,
                "twitterComments": 7769,
                "stocktwitsLikes": 16,
                "twitterLikes": 40957,
                "stocktwitsImpressions": 15141,
                "twitterImpressions": 1576854,
                "stocktwitsSentiment": 0.5411,
                "twitterSentiment": 0.5888
            }
        ]
        """
        return self.api.get(
            HISTORICAL_SOCIAL_SENTIMENT_ENDPOINT, {"symbol": symbol, "page": page}
        )

    def get_trending_social_sentiment(self, sentiment_type, source):
        """Provides trending social sentiment data for a given ticker or company name.

        Args:
            sentiment_type (str): bullish, bearish
            source (str): stocktwits

        Returns: [
            {
                "symbol": "PNI",
                "name": "PIMCO New York Municipal Income Fund II",
                "rank": 1,
                "sentiment": 100,
                "lastSentiment": 13.3333
            }
        ]
        """
        return self.api.get(
            TRENDING_SOCIAL_SENTIMENT_ENDPOINT,
            {"type": sentiment_type, "source": source},
        )

    def get_social_sentiment_change(self, sentiment_type, source):
        """Provides social sentiment change data.

        For a given ticker or company name over a given time period.

        Args:
            sentiment_type (str): bullish, bearish
            source (str): stocktwits

        Returns: [
            {
                "symbol": "NBTX",
                "name": "Nanobiotix S.A.",
                "rank": 1,
                "sentiment": 21.4778,
                "sentimentChange": 10209.3333
            }
        ]
        """
        return self.api.get(
            SOCIAL_SENTIMENT_CHANGE_ENDPOINT, {"type": sentiment_type, "source": source}
        )

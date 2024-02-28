FMP_ARTICLES_ENDPOINT = "v3/fmp/articles"
# Query Parameters:
# page: int - Default: 0
# size: int - Default: 5

# Response:
"""
[
	{
		"title": "SolarEdge Stock Plummets 25% After Q3 Revenue Warning",
		"date": "2023-10-20 11:28:00",
		"content": "<p><a href='https://financialmodelingprep.com/financial-summary/SEDG'>SolarEdge Technologies (NASDAQ:SEDG)</a> shares plunged more than 25% intra-day today following the company's preliminary Q3 financial results. Revenue for the quarter is now expected to be between $720 million and $730 million, a significant drop from the earlier projection of $880 million to $920 million,....",
		"tickers": "NASDAQ:SEDG",
		"image": "https://cdn.financialmodelingprep.com/images/fmp-1697815718768.jpg",
		"link": "https://financialmodelingprep.com/market-news/fmp-solaredge-stock-plummets-25-after-q3-revenue-warning",
		"author": "Davit Kirakosyan",
		"site": "Financial Modeling Prep"
	}
]
"""

GENERAL_NEWS_ENDPOINT = "v4/general_news"
# Get a list of the latest general news articles from a variety of sources, including the headline, snippet, and publication URL.

# Query Parameters:
# page: int - Default: 0

# Response:
"""
[
	{
		"publishedDate": "2023-10-19T22:00:09.000Z",
		"title": "Xi Jinping calls for ceasefire in Israel-Gaza war, says two-state solution is ‘fundamental way out’",
		"image": "https://cdn.i-scmp.com/sites/default/files/styles/1280x720/public/d8/images/canvas/2023/10/19/ace90641-0118-4671-b211-3ce4669f9aa3_ccf76346.jpg?itok=mlnC2VFw",
		"site": "scmp",
		"text": "Chinese president also says Beijing is willing to work with Arab countries for ‘comprehensive, just, and lasting solution’ to the crisis...",
		"url": "https://www.scmp.com/news/china/diplomacy/article/3238538/xi-jinping-calls-ceasefire-israel-gaza-war-says-two-state-solution-fundamental-way-out?utm_source=rss_feed"
	}
]
"""

STOCK_NEWS = "v3/stock_news"
# Get a list of the latest stock news articles from a variety of sources, including the headline, snippet, and publication URL.

# Query Parameters:
# page: int - Default: 0
# tickers: string - AAPL,FB
# limit: int - Default: 50

# Response:
"""
[
	{
		"symbol": "TSM",
		"publishedDate": "2023-10-19 10:38:47",
		"title": "Chip Stock Soars After Beat-and-Raise",
		"image": "https://cdn.snapi.dev/images/v1/k/j/138124333-m-normal-none-1981779-2111438.jpg",
		"site": "Schaeffers Research",
		"text": "Taiwan Semiconductor Mfg.",
		"url": "https://www.schaeffersresearch.com/content/news/2023/10/19/chip-stock-soars-after-beat-and-raise"
	}
]
"""

STOCK_NEWS_SENTIMENTS_RSS_FEED = "v4/stock-news-sentiments-rss-feed"
# Get an RSS feed of the latest stock news articles with their sentiment analysis, including the headline, snippet, publication URL, ticker symbol, and sentiment score.

# Query Parameters:
# page: int - Default: 0

# Response:
"""
[
	{
		"symbol": "MSFT",
		"publishedDate": "2023-10-10T21:10:53.000Z",
		"title": "No Call Of Duty On Game Pass This Year, But Diablo IV May Arrive In 2024",
		"image": "https://cdn.benzinga.com/files/images/story/2023/10/10/shutterstock_2093878507_1.jpg?optimize=medium&dpr=1&auto=webp&height=800&width=1456&fit=crop",
		"site": "benzinga",
		"text": "Activision Blizzard Inc (NASDAQ: ATVI) outlined its plans for Xbox Game Pass in the wake of the impending Microsoft Corp (NASDAQ: MSFT) acquisition, indicating it intends to start offering its games on the service in 2024. The acquisition is set to conclude shortly, but the company has made it clear that highly anticipated titles such as Call of Duty: Modern Warfare III and Diablo IV will not be available on Game Pass this year. See Also: Microsoft Announces Games Leaving Xbox Game Pass In Octob...",
		"url": "https://www.benzinga.com/general/gaming/23/10/35171171/no-call-of-duty-on-game-pass-this-year-but-diablo-iv-may-arrive-in-2024",
		"sentiment": "Positive",
		"sentimentScore": 0.9812
	}
]
"""

FOREX_NEWS_ENDPOINT = "v4/forex_news"
# Get a list of the latest forex news articles from a variety of sources, including the headline, snippet, and publication URL.

# Query Parameters:
# page: int - Default: 0
# symbol: string - EURUSD,GBPJPY

# Response:
"""
[
	{
		"publishedDate": "2022-10-05T16:14:56.000Z",
		"title": "Atlanta Fed GDPNow rises to 2.7% from 2.3%",
		"image": "https://images.forexlive.com/images/Atlanta%20Fed_id_4a7edf49-2203-4f0f-be54-907510ec2589_size900.jpg",
		"site": "Forexlive",
		"text": "Atlanta Fed GDPNow estimate for 3Q growthThe Atlanta Fed GDPNow estimate for 3Q growth rises to 2.7% from 2.3% after the US morning economic data Economic Data Economic data typically comes in the form of news releases that are disseminated daily. This information is extremely valuable to retail and institutional forex traders, given the influence such data has on currency rates.Most of the major economic events that are released are reported by sovereign governments throughout the globe. Moreover, there are several economic data points that are released by private organizations that can also move the market.By and large, when new information becomes available the value of a currency pair will change to reflect a potentially new equilibrium created by traders. This information that changes the value of a currency pair can ultimately come in many forms, with economic indicators or data being primary drivers.Why Economic Data Matters in ForexEconomic data is an important barometer that investors can use to measure the performance of an economy. This in turn can influence currency rates.For example, the stronger the economic data, the more likely growth will rise in the country, causing a currency to strengthen. If Gross Domestic Product (GDP) growth in the United States is high, this will help cause the US dollar to rise in value.The reverse is also true. Typically, weaker economic data can forecast a slowing of growth. What traders’ attempt, when trading economic data is to measure how economic indicators are perceived relative to expectations.Before nearly every economic release, the market generally prices in is the median expectation reflected by analysts and economists. These known variables are simply expectations, and the unknown is the actual release. Since currency pairs can move significantly based on new data, traders are always trying to anticipate where the actual figures will come in upon release.Changes to economic data will also filter down to potential changes to interest rates by a central bank. Overall, economic announcements from the United States and Eurozone are heavily watched as they will influence the perceptions of market participants which help drive interest rates and other monetary policy by the Federal Reserve or European Central Bank (ECB) respectively. Economic data typically comes in the form of news releases that are disseminated daily. This information is extremely valuable to retail and institutional forex traders, given the influence such data has on currency rates.Most of the major economic events that are released are reported by sovereign governments throughout the globe. Moreover, there are several economic data points that are released by private organizations that can also move the market.By and large, when new information becomes available the value of a currency pair will change to reflect a potentially new equilibrium created by traders. This information that changes the value of a currency pair can ultimately come in many forms, with economic indicators or data being primary drivers.  Why Economic Data Matters in ForexEconomic data is an important barometer that investors can use to measure the performance of an economy.  This in turn can influence currency rates. For example, the stronger the economic data, the more likely growth will rise in the country, causing a currency to strengthen...",
		"tickers": [],
		"updatedAt": "2022-10-05T16:24:53.109Z",
		"createdAt": "2022-10-05T16:24:53.109Z",
		"type": "forex"
	}
]
"""

CRYPTO_NEWS_ENDPOINT = "v4/crypto_news"
# Get a list of the latest cryptocurrency news articles from a variety of sources, including the headline, snippet, and publication URL.

# Query Parameters:
# page: int - Default: 0
# symbol: string - BTCUSD

# Response:
"""
[
	{
		"publishedDate": "2022-10-05T15:57:27.000Z",
		"title": "Abu Dhabi to Host Inaugural Middle East Blockchain Awards",
		"image": "",
		"site": "Coinjournal",
		"text": "Dubai, United Arab Emirates, 5th October, 2022, Chainwire The first edition of the Middle East Blockchain Awards will be held in Abu Dhabi in November 2022, to recognise and reward outstanding efforts within the fields of blockchain and Web 3.0 innovations. Hoko Agency Middle East will host the Awards, in association with Abu Dhabi Global Market&rsquo;s flagship platform, Abu Dhabi Finance Week; and the Middle East, Africa and Asia Crypto and Blockchain Association (MEAACBA). Frontrunners in the industry will be recognised through the Middle East Blockchain Awards (MEBA), with all nominations assessed by a panel of prestigious experts. Judges include: &#9679; Dr. Marwan Al Zarouni, CEO of Dubai Blockchain Centre (DBCC) &#9679; Jehanzeb Awan, Board Member of MEAACBA, Founding Partner and CEO of J. Awan and Partners &#9679; Miriam Kiwan, Former Head of Digital Assets at ADGM, Board Member at BlackOack Global &#9679; Misha Hanin, Co-founder and CEO of BEDU &#9679; Saqr Ereiqat, Co-Founder and CCO of Crypto Oasis &#9679; Matthew Amlot, Managing Editor of Arabian Business MEBA will be held in the stunning Palm Garden at the five-star W Abu Dhabi &ndash; Yas Island on 18 November 2022 in the midst of the high-energy F1 Race Weekend. The black-tie event promises a spectacular evening of recognition, insight and entertainment, attended by high-profile individuals from across the GCC. Abu Dhabi was chosen as the host city for the inaugural awards because of the UAE leadership&rsquo;s commitment to progression and innovation in blockchain and digital transformation. The UAE as a whole has made significant moves towards the regulation, safety and transparency of blockchain and digital assets, driving the importance of global standards for industry compliance that will benefit all aspects of Web 3.0. This forward-thinking approach has attracted numerous global players to establish their presence in the emirates, creating a strong ecosystem that contributes towards its reputation as a hub for crypto and beyond. Jehanzeb Awan, Board Member of MEAACBA, Founding Partner and CEO of J. Awan and Partners said: &ldquo;Blockchain is creating a digital ecosystem which will support a new world of services and products ranging from financial services through to real economy. The Middle East Blockchain Awards will help drive innovation, reward excellence and provide a benchmark for companies to aspire to and in doing so contribute significantly to the regional ecosystem.&rdquo; Max Palethorpe, Founder and CEO of Hoko Group said: &ldquo;The Middle East Blockchain Awards come at a time when people and businesses are pushing the boundaries of what was previously thought impossible, making significant headway into a digital-first world. This is a very exciting period for anyone involved in the Web 3.0 ecosystem. It&rsquo;s our privilege to honour those who are forging new paths with the recognition they deserve.&rdquo; Award categories include Most Innovative DeFi Platform 2022, Most Promising DEX to Watch 2022, Most Powerful CEX 2022, Best Mobile Crypto Wallet 2022, Best NFT Marketplace 2022, Best Crypto Investment Fund 2022, Most Promising Web 3.0 Ecosystem 2022, Best Nft &amp; Gamefi Project 2022, Top Global Crypto Youtuber / Influencer 2022, Most Influential Woman in Blockchain &amp; Crypto 2022, Most Influential CMO in Blockchain &amp; Crypto 2022, Most Influential Global Crypto News Service 2022, Most Influential CEO In Blockchain &amp; Crypto 2022, and Most Promising ESG Crypto Project. Entries can be submitted at www.mebawards.io For more updates follow Meba on: Instagram: meba_awards Linkedin: MEBA Awards Twitter: @meba_awards Contact Head of PR, Yousef Batter, White Label Strategy, yousef.batter@whitelabelstrategy.io, +971 55 935 6531",
		"url": "https://coinjournal.net/news/abu-dhabi-to-host-inaugural-middle-east-blockchain-awards/",
		"tickers": [],
		"updatedAt": "2022-10-05T16:32:00.592Z",
		"createdAt": "2022-10-05T16:32:00.592Z",
		"type": "crypto"
	}
]
"""

PRESS_RELEASES_ENDPOINT = "v3/press-releases/{symbol}"
# Get a list of the latest press releases from a variety of sources, including the headline, snippet, and publication URL.

# Path Parameters:
# symbol: string - AAPL

# Query Parameters:
# page: int - Default: 0

# Response:
"""
[
	{
		"symbol": "AAPL",
		"date": "2023-02-02 16:30:00",
		"title": "APPLE REPORTS FIRST QUARTER RESULTS",
		"text": "CUPERTINO, CALIF.--( BUSINESS WIRE )--APPLE® TODAY ANNOUNCED FINANCIAL RESULTS FOR ITS FISCAL 2023 FIRST QUARTER ENDED DECEMBER 31, 2022. THE COMPANY POSTED QUARTERLY REVENUE OF $117.2 BILLION, DOWN 5 PERCENT YEAR OVER YEAR, AND QUARTERLY EARNINGS PER DILUTED SHARE OF $1.88."
	}
]
"""

HISTORICAL_SOCIAL_SENTIMENT_ENDPOINT = "v4/historical/social-sentiment"
# Provide historical social sentiment data for a given ticker or company name.

# Query Parameters:
# symbol: string - AAPL
# page: int - Default: 0

# Response:
"""
[
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

TRENDING_SOCIAL_SENTIMENT_ENDPOINT = "v4/social-sentiments/trending"
# Provides trending social sentiment data for a given ticker or company name.

# Query Parameters:
# type: string - bullish, bearish
# source: string - stocktwits

# Response:
"""
[
	{
		"symbol": "PNI",
		"name": "PIMCO New York Municipal Income Fund II",
		"rank": 1,
		"sentiment": 100,
		"lastSentiment": 13.3333
	}
]
"""

SOCIAL_SENTIMENT_CHANGE_ENDPOINT = "v4/social-sentiments/change"
# Provides social sentiment change data for a given ticker or company name over a given time period.

# Query Parameters:
# type: string - bullish, bearish
# source: string - stocktwits

# Response:
"""
[
	{
		"symbol": "NBTX",
		"name": "Nanobiotix S.A.",
		"rank": 1,
		"sentiment": 21.4778,
		"sentimentChange": 10209.3333
	}
]
"""
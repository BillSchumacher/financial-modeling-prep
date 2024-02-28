PRICE_TARGETS_ENDPOINT = "v4/price-target"
# Get the price target for a company, which is the price at which an analyst believes the company's stock is fairly valued. Price targets can be used to make investment decisions, such as whether to buy, sell, or hold a stock.

# Query Parameters
# symbol: (str) (required) The company's ticker symbol.

# Response:
"""
[
	{
		"symbol": "AAPL",
		"publishedDate": "2023-09-18T02:36:00.000Z",
		"newsURL": "https://www.benzinga.com/analyst-ratings/analyst-color/23/09/34673717/apple-analyst-says-iphone-15-pro-pro-max-preorders-strong-out-of-the-gates-increasi",
		"newsTitle": "Apple Analyst Says iPhone 15 Pro, Pro Max Preorders Strong Out Of The Gates, Increasing Confidence In Estimates For Holiday Quarter",
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

PRICE_TARGET_SUMMARY_ENDPOINT = "v4/price-target-summary"
# Get a summary of the price targets for a company from different analysts. This summary includes the average price target, the high price target, and the low price target.

# Query Parameters
# symbol: (str) (required) The company's ticker symbol.

# Response:
"""
[
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
		"publishers": "[\"Benzinga\",\"TheFly\",\"Pulse 2.0\",\"MarketWatch\",\"TipRanks Contributor\",\"Investing\",\"StreetInsider\",\"Barrons\",\"Investor's Business Daily\"]"
	}
]

"""

PRICE_TARGET_BY_NAME_ENDPOINT = "v4/price-target-analyst-name"
# Get the price targets for a company from a specific analyst. This can be useful if you want to track the price targets of a particular analyst that you trust.

# Query Parameters
# name: (str) (required) The name of the analyst.

# Response:
"""
[
	{
		"symbol": "CAH",
		"publishedDate": "2023-04-12T09:24:00.000Z",
		"newsURL": "https://www.benzinga.com/trading-ideas/long-ideas/23/04/31768582/these-3-health-care-stocks-delivering-high-dividend-yields-are-recommended-by-wall-stree",
		"newsTitle": "These 3 Health Care Stocks Delivering High-Dividend Yields Are Recommended By Wall Street's Most Accurate Analysts",
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

PRICE_TARGET_BY_COMPANY_ENDPOINT = "v4/price-target-analyst-company"
# Get the price targets for all companies in a specific industry or sector. This can be useful if you want to compare the price targets of different companies in the same industry.

# Query Parameters
# company: (str) (required) The name of the company.

# Response:
"""
[
	{
		"symbol": "LYB",
		"publishedDate": "2023-10-04T08:12:00.000Z",
		"newsURL": "https://www.benzinga.com/news/23/10/35086481/alphabet-to-rally-over-10-here-are-10-other-analyst-forecasts-for-wednesday",
		"newsTitle": "Alphabet To Rally Over 10%? Here Are 10 Other Analyst Forecasts For Wednesday",
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

PRICE_TARGET_CONSENSUS_ENDPOINT = "v4/price-target-consensus"
# Get the consensus price target for a company, which is the average of all price targets from different analysts. This can be useful if you want to get a general idea of what analysts think about a company's stock.

# Query Parameters
# symbol: (str) (required) The company's ticker symbol.

# Response:
"""
[
	{
		"symbol": "AAPL",
		"targetHigh": 240,
		"targetLow": 110,
		"targetConsensus": 189.18,
		"targetMedian": 195
	}
]
"""

PRICE_TARGET_RSS_FEED_ENDPOINT = "v4/price-target-rss-feed"
# Get an RSS feed of price target updates for a company. This way, you can stay up-to-date on the latest price targets from analysts.

# Query Parameters
# page: (int) (optional) The page number of the RSS feed. Default is 0.

# Response:
"""
[
	{
		"symbol": "FVRR",
		"publishedDate": "2023-10-04T16:24:00.000Z",
		"newsURL": "https://www.benzinga.com/analyst-ratings/analyst-color/23/10/35094606/fiverrs-promise-in-2024-analyst-sees-upswing-despite-current-market-uncertainty",
		"newsTitle": "Fiverr's Promise In 2024: Analyst Sees Upswing Despite Current Market Uncertainty",
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

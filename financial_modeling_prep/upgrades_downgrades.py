UPGRADES_AND_DOWNGRADES_RSS_FEED_ENDPOINT = "v4/upgrades-downgrades-rss-feed"
# Subscribe to an RSS feed of all stock upgrades and downgrades from different analysts. This RSS feed is updated on a daily basis, so you can always stay up-to-date on the latest analyst ratings without having to manually check for updates.

# Query Params
# page: int - The page number to retrieve. Each page contains 100? items. (default: 0)

# Response:
"""
[
	{
		"symbol": "DAL",
		"publishedDate": "2023-10-04T15:24:00.000Z",
		"newsURL": "https://www.benzinga.com/analyst-ratings/analyst-color/23/10/35094507/delta-air-lines-3q23-earnings-in-focus-bofa-securities-expects-no-surprises-and-hig",
		"newsTitle": "Delta Air Lines 3Q23 Earnings In Focus: BofA Securities Expects No Surprises And Highlights Cost Pressure",
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

UPGRADES_AND_DOWNGRADES_CONSENSUS_ENDPOINT = "v4/upgrades-downgrades-consensus"
# Get the consensus rating for a company, which is the average rating from different analysts. This information can be used to get a general idea of what analysts think about a company's stock and to make more informed investment decisions.

# Query Params
# symbol: str - The ticker symbol of the company.

# Response:
"""
[
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

UPGRADES_AND_DOWNGRADES_BY_COMPANY_ENDPOINT = "v4/upgrades-downgrades-grading-company"
# Get a comprehensive list of all stock upgrades and downgrades for a specific company, including the rating change, the analyst firm, and the date of the rating change. This information can be used to track analyst sentiment for a company and to identify potential investment opportunities or risks.

# Query Params
# company: str - The name of the company.

# Response:
"""
[
	{
		"symbol": "ATUS",
		"publishedDate": "2022-02-18T08:14:00.000Z",
		"newsURL": "https://www.benzinga.com/news/22/02/25712046/barclays-maintains-equal-weight-on-altice-usa-lowers-price-target-to-17",
		"newsTitle": "Barclays Maintains Equal-Weight on Altice USA, Lowers Price Target to $17",
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
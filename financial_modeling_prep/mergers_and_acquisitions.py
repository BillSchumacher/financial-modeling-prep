MA_RSS_FEED_ENDPOINT = "v4/mergers-acquisitions-rss-feed"
# The FMP M&A RSS Feed provides investors, analysts, and other market participants with a real-time stream of M&A news and announcements.

# Query Parameters
# page: int - The page number. Default is 0.

# Response:
"""
[
	{
		"companyName": "GRIZZLY NEW PUBCO, INC.",
		"cik": "0001946991",
		"symbol": "CDCN",
		"targetedCompanyName": "DTRT HEALTH ACQUISITION CORP.",
		"targetedCik": "0001865537",
		"targetedSymbol": "DTRTU",
		"transactionDate": "2022-10-19",
		"acceptanceTime": "2022-10-19 21:17:55",
		"url": "https://www.sec.gov/Archives/edgar/data/1946991/000119312522265503/d400348ds4.htm"
	}
]
"""

SEARCH_MA_ENDPOINT = "v4/mergers-acquisitions/search"
# The FMP Search M&A endpoint allows users to search for M&A deals based on a variety of criteria, Users can also specify a date range to search for M&A deals that were announced during that period.

# Query Parameters
# name: str - The name of the company.

# Response:
"""
[
	{
		"companyName": "Syros Pharmaceuticals, Inc.",
		"cik": "0001556263",
		"symbol": "SYRS",
		"targetedCompanyName": "TYME",
		"targetedCik": null,
		"targetedSymbol": "TYME",
		"transactionDate": "2022-07-18",
		"acceptanceTime": "2022-07-18 07:58:48",
		"url": "https://www.sec.gov/Archives/edgar/data/1556263/000119312522195811/d365321ds4.htm"
	}
]
"""
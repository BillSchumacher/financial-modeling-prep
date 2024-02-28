ESG_SEARCH_ENDPOINT = "v4/esg-environmental-social-governance-data"
# Find companies and funds that align with your ESG values with FMP's ESG Search tool. Search by ESG rating, performance, controversies, and business involvement screens.

# Query Params:
# symbol - string - Stock or fund ticker symbol

# Response:
"""
[
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
		"url": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000059/0000320193-22-000059-index.htm"
	}
]
"""

ESG_RATINGS_ENDPOINT = "v4/esg-enviromental-social-governance-data-ratings"
# Get ESG ratings for companies and funds to make informed investment decisions. FMP's ESG Ratings are based on a variety of data sources, including corporate sustainability reports, ESG research firms, and government agencies.

# Query Params:
# symbol - string - Stock or fund ticker symbol

# Response:
"""
[
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


ESG_BENCHMARK_ENDPOINT = "v4/esg-environmental-social-governance-sector-benchmark"
# Compare the ESG performance of companies and funds to their peers with FMP's ESG Benchmark tool. Identify ESG leaders and laggards to make informed investment decisions.

# Query Params:
# year - integer - Year of the data

# Response:
"""
[
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

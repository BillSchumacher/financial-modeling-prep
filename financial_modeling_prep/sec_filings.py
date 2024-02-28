RSS_FEED_ENDPOINT = "v4/rss_feed"
# A real-time feed of SEC filings from publicly traded companies, including the filing type, link to SEC page, and direct link to the filing. This endpoint can be used to stay up-to-date on the latest SEC filings for all companies or for a specific set of companies.

# Query Params:
# limit: int - The number of filings to return. Default is 100.
# type: string - The type of filing to return. Default is all types. See the SEC documentation for a list of filing types.
# from : date - The start date for the filings to return.
# to : date - The end date for the filings to return.
# isDone: bool - If true, only return filings that are complete. If false, only return filings that are not complete. Default is all filings.

# Response:
"""
[
	{
		"title": "6-K - Sangoma Technologies Corp (0001753368) (Filer)",
		"date": "2023-09-27 17:07:28",
		"link": "https://www.sec.gov/Archives/edgar/data/1753368/000175336823000021/0001753368-23-000021-index.htm",
		"cik": "0001753368",
		"form_type": "6-K",
		"ticker": "SANG",
		"done": true
	}
]
"""

RSS_FEED_V3_ENDPOINT = "v3/rss_feed"
# A real-time feed of SEC filings from publicly traded companies, including the filing type, link to SEC page, and direct link to the filing. This endpoint can be used to stay up-to-date on the latest SEC filings for all companies or for a specific set of companies.

# Query Params:
# page: int - The page number to return. Default is 0
# datatype: string - csv,json

# Response:
"""
[
	{
		"title": "6-K - BRP Inc. (0001748797) (Filer)",
		"date": "2023-10-04 17:29:28",
		"link": "https://www.sec.gov/Archives/edgar/data/1748797/000119312523250827/0001193125-23-250827-index.htm",
		"cik": "0001748797",
		"form_type": "6-K",
		"ticker": "DOOO",
		"done": true
	}
]
"""

RSS_FEED_8K_ENDPOINT = "v4/rss_feed_8k"
# A real-time feed of 8-K filings from publicly traded companies, including the filing type, link to SEC page, and direct link to the filing. This endpoint can be used to stay up-to-date on the latest 8-K filings for all companies or for a specific set of companies.

# Query Params:
# page: int - The page number to return. Default is 0
# from : date - The start date for the filings to return.
# to : date - The end date for the filings to return.
# hasFinancial: bool - If true, only return filings that contain financial data. If false, only return filings that do not contain financial data. Default is all filings.
# limit: int - The number of filings to return. Default is 10.

# Response:
"""
[
	{
		"title": "8-K - BUTLER NATIONAL CORP (0000015847) (Filer)",
		"symbol": "BUKS",
		"cik": "0000015847",
		"link": "https://www.sec.gov/Archives/edgar/data/15847/000143774922021312/0001437749-22-021312-index.htm",
		"finalLink": "https://www.sec.gov/Archives/edgar/data/15847/000143774922021312/buks20220822_8k.htm",
		"date": "2022-08-25 10:05:41"
	}
]
"""

SEC_FILINGS_ENDPOINT = "v3/sec_filings/{symbol}"
# Direct link to SEC filings for a specific company, including the filing type, link to SEC page, and direct link to the filing. This endpoint can be used to get all SEC filings for a specific company.

# Path Params:
# symbol: string - The stock symbol of the company

# Query Params:
# page: int - The page number to return. Default is 0
# type: string - 10-K

# Response:
"""
[
	{
		"symbol": "AAPL",
		"cik": "0000320193",
		"type": "10-K",
		"link": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/0000320193-22-000108-index.htm",
		"finalLink": "https://www.sec.gov/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm",
		"acceptedDate": "2022-10-27 18:01:14",
		"fillingDate": "2022-10-28 00:00:00"
	}
]
"""

INDIVIDUAL_INDUSTRY_CLASSIFICATION_ENDPOINT = "v4/standard_industrial_classification"
# Identify the industry classification for a company. This endpoint can be used to get the industry classification for a specific company.

# Query Params:
# symbol: string - The stock symbol of the company
# cik: (optional) string - The CIK number of the company
# sicCode: (optional) string - The SIC code of the company

# Response:
"""
[
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

ALL_INDUSTRY_CLASSIFICATION_ENDPOINT = "v4/standard_industrial_classification/all"
# Get a comprehensive overview of all industries, classified according to the SIC system.

# Response:
"""
[
	{
		"symbol": "A",
		"name": "AGILENT TECHNOLOGIES, INC. ",
		"cik": "0001090872",
		"sicCode": "3826",
		"industryTitle": "LABORATORY ANALYTICAL INSTRUMENTS",
		"businessAdress": "['5301 STEVENS CREEK BLVD, MS 1A-LC', 'P.O. BOX 58059', 'SANTA CLARA CA 95052-8059', '5301 STEVENS CREEK BLVD', 'SANTA CLARA CA 95051']",
		"phoneNumber": "(408) 345-8886"
	}
]
"""

ALL_INDUSTRY_CLASSIFICATION_CODES_ENDPOINT = "v4/standard_industrial_classification_list"
# Learn more about the SIC system and identify the SIC code for a particular industry.

# Query Params:
# industryTitle: optional, string - The title of the industry
# sicCode: optional, string - The SIC code of the industry

# Response:
"""
[
	{
		"office": "Office of Life Sciences",
		"sicCode": "200",
		"industryTitle": "AGRICULTURAL PROD-LIVESTOCK & ANIMAL SPECIALTIES"
	}
]
"""


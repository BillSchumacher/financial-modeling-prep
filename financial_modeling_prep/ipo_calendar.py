IPO_CONFIRMED_ENDPOINT = "v4/ipo-calendar-confirmed"
# The FMP IPO Confirmed endpoint provides a list of IPOs that have been confirmed and are scheduled to take place in the near future.

# Query Params
# from: date (string) - The starting date of the IPOs. The date format is YYYY-MM-DD.
# to: date (string) - The ending date of the IPOs. The date format is YYYY-MM-DD.

# Response:
"""
[
	{
		"symbol": "CETUU",
		"cik": "0001936702",
		"form": "CERT",
		"filingDate": "2023-01-31",
		"acceptedDate": "2023-01-31 15:04:42",
		"effectivenessDate": "2023-01-31",
		"url": "https://www.sec.gov/Archives/edgar/data/1936702/000135445723000056/8A_Cert_CETU.pdf"
	}
]
"""


IPO_PROSPECTUS_ENDPOINT = "v4/ipo-calendar-prospectus"
# The FMP IPO Prospectus endpoint provides a link to the IPO prospectus for a given company. The IPO prospectus is a legal document that provides detailed information about the company, its IPO, and its securities.

# Query Params
# from: date (string) - The starting date of the IPOs. The date format is YYYY-MM-DD.
# to: date (string) - The ending date of the IPOs. The date format is YYYY-MM-DD.

# Response:
"""
[
	{
		"symbol": "NYX",
		"cik": "0001679379",
		"form": "S-1/A",
		"filingDate": "2023-02-01",
		"acceptedDate": "2023-02-01 17:30:40",
		"ipoDate": "2023",
		"pricePublicPerShare": 5,
		"pricePublicTotal": 8200000,
		"discountsAndCommissionsPerShare": 0.4,
		"discountsAndCommissionsTotal": 656000,
		"proceedsBeforeExpensesPerShare": 4.6,
		"proceedsBeforeExpensesTotal": 7544000,
		"url": "https://www.sec.gov/Archives/edgar/data/1679379/000121390023006765/fs12023a4_nyiaxinc.htm"
	}
]
"""


IPO_CALENDAR_BY_SYMBOL = " v3/ipo_calendar"
# The FMP IPO Calendar By Symbol endpoint provides a list of IPOs that have been confirmed and are scheduled to take place in the near future for a given company. This endpoint includes the same information as the FMP IPO Confirmed endpoint, but it is filtered to only include IPOs for the specified company.

# Query Params
# from (string) - The starting date of the IPOs. The date format is YYYY-MM-DD.
# to (string) - The ending date of the IPOs. The date format is YYYY-MM-DD.

# Response:
"""
[
	{
		"date": "2023-03-09",
		"company": "Atlas Energy Solutions Inc.",
		"symbol": "AESI",
		"exchange": "NYSE",
		"actions": "Expected",
		"shares": null,
		"priceRange": "20.00 - 23.00",
		"marketCap": null
	}
]
"""
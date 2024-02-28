MUTUAL_FUND_DATES_ENDPOINT = "v4/mutual-fund-holdins/portfolio-date"
# The FMP Mutual Fund Dates endpoint provides a list of the dates on which mutual fund holdings are updated. This information can be used by investors to stay up-to-date on the latest changes to mutual fund portfolios. For example, an investor may want to know when a mutual fund's holdings are updated in order to make sure that they are still aligned with their investment goals.

# Query Parameters:
# symbol: str
# cik: str (optional)

# Response:
"""
[
	{
		"date": "2023-03-31"
	},
	{
		"date": "2022-12-31"
	}
]
"""


MUTUAL_FUNDS_ENDPOINT = "v4/mutual-fund-holdings"
# The FMP Mutual Funds endpoint provides a list of all the mutual funds that are registered with the Securities and Exchange Commission (SEC). This information can be used by investors to identify potential investment opportunities. For example, an investor who is interested in investing in the technology sector may want to browse the list of mutual funds that track the S&P 500 index.

# Query Parameters:
# symbol: str
# date: date
# cik: str (optional)

# Response:
"""
[
	{
		"cik": "0000036405",
		"acceptanceTime": "2023-05-26 15:28:00",
		"date": "2023-03-31",
		"symbol": "NXPI",
		"name": "NXP Semiconductors NV",
		"lei": "724500M9BY5293JDF951",
		"title": "NXP SEMICONDUCTO",
		"cusip": "N6596X109",
		"isin": "NL0009538784",
		"balance": 6046657,
		"units": "NS",
		"cur_cd": "USD",
		"valUsd": 1127550364.08,
		"pctVal": 0.03930805710834702,
		"payoffProfile": "Long",
		"assetCat": "EC",
		"issuerCat": "CORP",
		"invCountry": "US",
		"isRestrictedSec": "N",
		"fairValLevel": "1",
		"isCashCollateral": "N",
		"isNonCashCollateral": "N",
		"isLoanByFund": "N"
	}
]
"""

MUTUAL_FUND_BY_NAME_ENDPOINT = "v4/mutual-fund-holdings/name"
# The FMP Mutual Fund By Name endpoint provides detailed information about a specific mutual fund. This information includes the fund's ticker symbol, name, investment objective, expense ratio, and asset under management. Investors can use this information to learn more about a particular mutual fund before deciding whether to invest in it.

# Query Parameters:
# name: str

# Response:
"""
[
	{
		"cik": "0000036405",
		"symbol": "VXF",
		"classId": "C000007782",
		"seriesId": "S000002841",
		"entityName": "VANGUARD INDEX FUNDS",
		"entityOrgType": "30",
		"seriesName": "Vanguard Extended Market Index Fund",
		"className": "ETF Shares",
		"reportingFileNumber": "811-02652",
		"address1": "PO BOX 2600",
		"city": "VALLEY FORGE",
		"zipCode": "19482",
		"state": "PA",
		"address2": "V26"
	}
]
"""

MUTUAL_FUND_HOLDER_ENDPOINT = "v3/mutual-fund-holder/{symbol}"
# The FMP Mutual Fund Holder endpoint provides a list of all the institutional investors that own shares of a particular mutual fund. This information can be used by investors to track the ownership of a mutual fund and to identify potential trends. For example, an investor may want to know which institutions are buying or selling shares of a particular mutual fund.

# Path Params:
# symbol: str

# Response:
"""
[
	{
		"holder": "CYPRESS FUNDS LLC",
		"shares": 371332,
		"dateReported": "2022-09-30",
		"change": -360468,
		"weightPercent": null
	}
]
"""
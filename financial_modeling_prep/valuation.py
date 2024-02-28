DISCOUNTED_CASHFLOW_ENDPOINT = "v3/discounted-cash-flow/{symbol}"
# Get the discounted cash flow (DCF) valuation for a company, a method to estimate the value of an investment based on its expected future cash flows.

# Path Params
# symbol: (string) (required) symbol of the company

# Response:
"""
[
	{
		"symbol": "AAPL",
		"date": "2023-03-03",
		"dcf": 151.0983806294802,
		"Stock Price": 149.65
	}
]
"""

ADVANCED_DCF_ENDPOINT = "v4/advanced_discounted_cash_flow"
# Calculate the DCF valuation for a company with advanced features like modeling multiple scenarios and using different valuation methods.

# Path params
# symbol: (string) (required) symbol of the company

# Response:
"""
[
	{
		"symbol": "AAPL",
		"price": 140.56,
		"beta": 1.25,
		"finalTaxRate": 13.3,
		"totalDebt": 124719000000,
		"totalEquity": 2370533014640,
		"totalCapital": 2495252014640,
		"dilutedSharesOutstanding": 16864919000,
		"debtWeighting": 5,
		"equityWeighting": 95,
		"year": "2017",
		"period": "FY",
		"revenue": 229234000000,
		"ebitda": 76569000000,
		"operatingCashFlow": 63598000000,
		"ebit": 66412000000,
		"weightedAverageShsOutDil": 21006768000,
		"netDebt": 95391000000,
		"inventories": 4855000000,
		"receivables": 35673000000,
		"payable": 49049000000,
		"inventoriesChange": 2723000000,
		"receivablesChange": 6374000000,
		"payableChange": 11755000000,
		"capitalExpenditure": -12795000000,
		"previousRevenue": 215639000000,
		"revenuePercentage": 0,
		"taxRate": 13.3,
		"ebitdaPercentage": 33.4,
		"receivablesPercentage": 15.56,
		"inventoriesPercentage": 2.12,
		"payablePercentage": 21.4,
		"ebitPercentage": 28.97,
		"capitalExpenditurePercentage": -5.58,
		"operatingCashFlowPercentage": 27.74,
		"afterTaxCostOfDebt": 1.84,
		"marketRiskPremium": 4.72,
		"longTermGrowthRate": 2,
		"costOfEquity": 10.56,
		"wacc": 10.11,
		"taxRateCash": 24556477,
		"ebiat": -15644326940,
		"ufcf": 44807553059,
		"riskFreeRate": 4.66,
		"sumPvUfcf": 0,
		"terminalValue": 563455390558,
		"presentTerminalValue": 348096433212,
		"enterpriseValue": 348096433212,
		"equityValue": 252705433212,
		"equityValuePerShare": 12.03,
		"freeCashFlowT1": 45703704120,
		"costofDebt": 2.12,
		"depreciation": 10157000000,
		"totalCash": 74181000000,
		"depreciationPercentage": 4.43,
		"totalCashPercentage": 32.36
	}
]
"""


LEVERED_DCF_ENDPOINT = "v4/advanced_levered_discounted_cash_flow"
# Get the DCF valuation for a company, taking into account its debt levels.

# Query params
# symbol: (string) (required) symbol of the company

# Response:
"""
[
	{
		"year": "2026",
		"symbol": "AAPL",
		"revenue": 601449529857,
		"revenuePercentage": 11.13,
		"capitalExpenditure": -20996099483,
		"capitalExpenditurePercentage": -3.49,
		"price": 145.91,
		"beta": 1.277894,
		"dilutedSharesOutstanding": 16325819000,
		"costofDebt": 2.44,
		"taxRate": 16.2,
		"afterTaxCostOfDebt": 2.05,
		"riskFreeRate": 4.27,
		"marketRiskPremium": 4.72,
		"costOfEquity": 10.3,
		"totalDebt": 120069000000,
		"totalEquity": 2382100250290,
		"totalCapital": 2502169250290,
		"debtWeighting": 4.8,
		"equityWeighting": 95.2,
		"wacc": 9.91,
		"operatingCashFlow": 173976072642,
		"pvLfcf": 104844776023,
		"sumPvLfcf": 0,
		"longTermGrowthRate": 2,
		"freeCashFlow": 152979973159,
		"terminalValue": 2193339068057,
		"presentTerminalValue": 1367716367760,
		"enterpriseValue": 1886225847690,
		"netDebt": 96423000000,
		"equityValue": 1789802847690,
		"equityValuePerShare": 109.63,
		"freeCashFlowT1": 173408405771,
		"operatingCashFlowPercentage": 28.93
	}
]
"""

COMPANY_RATING_ENDPOINT = "v3/ratings/{symbol}"
# The FMP Company Rating endpoint provides a rating of a company based on its financial statements, discounted cash flow analysis, financial ratios, and intrinsic value. Investors can use this rating to get a quick overview of a company's financial health and to compare different companies.

# Path Params
# symbol: (string) (required) symbol of the company

# Response:
"""
[
	{
		"symbol": "AAPL",
		"date": "2023-03-01",
		"rating": "S",
		"ratingScore": 5,
		"ratingRecommendation": "Strong Buy",
		"ratingDetailsDCFScore": 5,
		"ratingDetailsDCFRecommendation": "Strong Buy",
		"ratingDetailsROEScore": 5,
		"ratingDetailsROERecommendation": "Strong Buy",
		"ratingDetailsROAScore": 3,
		"ratingDetailsROARecommendation": "Neutral",
		"ratingDetailsDEScore": 5,
		"ratingDetailsDERecommendation": "Strong Buy",
		"ratingDetailsPEScore": 5,
		"ratingDetailsPERecommendation": "Strong Buy",
		"ratingDetailsPBScore": 5,
		"ratingDetailsPBRecommendation": "Strong Buy"
	}
]
"""

HISTORICAL_RATING_ENDPOINT = "v3/historical-rating/{symbol}"
# The FMP Historical Rating endpoint provides the historical rating of a company. Investors can use this information to track the changes in a company's rating over time and to identify trends in its performance.

# Path Params
# symbol: (string) (required) symbol of the company

# Query Params
# limit: (number) (optional) limit the number of ratings to be returned (default: 140)

# Response:
"""
[
	{
		"symbol": "AAPL",
		"date": "2023-03-01",
		"rating": "S",
		"ratingScore": 5,
		"ratingRecommendation": "Strong Buy",
		"ratingDetailsDCFScore": 5,
		"ratingDetailsDCFRecommendation": "Strong Buy",
		"ratingDetailsROEScore": 5,
		"ratingDetailsROERecommendation": "Strong Buy",
		"ratingDetailsROAScore": 3,
		"ratingDetailsROARecommendation": "Neutral",
		"ratingDetailsDEScore": 5,
		"ratingDetailsDERecommendation": "Strong Buy",
		"ratingDetailsPEScore": 5,
		"ratingDetailsPERecommendation": "Strong Buy",
		"ratingDetailsPBScore": 5,
		"ratingDetailsPBRecommendation": "Strong Buy"
	}
]
"""
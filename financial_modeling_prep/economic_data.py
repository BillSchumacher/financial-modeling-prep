TREASURY_RATES_ENDPOINT = "v4/treasury"
# Provides real-time and historical Treasury rates for all maturities

# Query Parameters
# from: date - The start date for the data
# to: date - The end date for the data

# Response
"""
[
	{
		"date": "2022-08-24",
		"month1": "2.29",
		"month2": "2.62",
		"month3": "2.82",
		"month6": "3.28",
		"year1": "3.35",
		"year2": "3.36",
		"year3": "3.40",
		"year5": "3.20",
		"year7": "3.20",
		"year10": "3.11",
		"year20": "3.55",
		"year30": "3.32"
	}
]
"""

ECONOMIC_INDICATORS_ENDPOINT = "v4/economic"
# Provides real-time and historical economic data for a variety of economic indicators, such as GDP, unemployment, and inflation.

# Query Parameters
# name: string - The name of the economic indicator (GDP, realGDP, nominalPotentialGDP, realGDPPerCapita, federalFunds, CPI, inflationRate, inflation, retailSales, consumerSentiment, durableGoods, unemploymentRate, totalNonfarmPayroll, initialClaims, industrialProductionTotalIndex, newPrivatelyOwnedHousingUnitsStartedTotalUnits, totalVehicleSales, retailMoneyFunds, smoothedUSRecessionProbabilities, 3MonthOr90DayRatesAndYieldsCertificatesOfDeposit, commercialBankInterestRateOnCreditCardPlansAllAccounts, 30YearFixedRateMortgageAverage, 15YearFixedRateMortgageAverage)
# from: date - The start date for the data
# to: date - The end date for the data

# Response
"""
[
	{
		"date": "2022-04-01",
		"value": "24882.878"
	},
	{
		"date": "2022-01-01",
		"value": "24386.734"
	}
]
"""

ECONOMIC_CALENDAR_ENDPOINT = "v4/economic_calendar"
# Provides a calendar of upcoming economic data releases.

# Query Parameters
# from: date - The start date for the data
# to: date - The end date for the data

# Response
"""
[
	{
		"date": "2022-10-06 00:00:00",
		"event": "Total Vehicle Sales (Sep)",
		"country": "US",
		"actual": null,
		"previous": 13.2,
		"change": null,
		"changePercentage": null,
		"estimate": null,
		"impact": "Low"
	}
]
"""

MARKET_RISK_PREMIUM_ENDPOINT = "v4/market_risk_premium"
# Provides real-time and historical market risk premium data.

# Query Parameters
# date?

# Response
"""
[
	{
		"country": "Abu Dhabi",
		"continent": null,
		"totalEquityRiskPremium": 5.75,
		"countryRiskPremium": 0.75
	}
]
"""
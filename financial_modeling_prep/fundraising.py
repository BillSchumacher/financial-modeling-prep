CROWDFUNDING_RSS_ENDPOINT = "v4/crowdfunding-offerings-rss-feed"
# Provides an RSS feed of crowdfunding campaigns, updated in real time.

# Query Parameters
# page - integer - The page number to retrieve. Default is 0.

# Response:
"""
[
	{
		"cik": "0001706842",
		"companyName": "StartUpWind, Inc",
		"url": "https://www.sec.gov/Archives/edgar/data/1706842/000166516022002605/xslC_X01/primary_doc.xml",
		"formType": "C/A",
		"formSignification": "Offering Statement Amendement",
		"industry": null,
		"fillingDate": "2022-10-05 00:00:00",
		"date": "01-20-2016",
		"nameOfIssuer": "StartUpWind, Inc",
		"legalStatusForm": "Corporation",
		"jurisdictionOrganization": "DE",
		"issuerStreet": "11610 Orchard Spring Ct",
		"issuerCity": "Cupertino",
		"issuerStateOrCountry": "CA",
		"issuerZipCode": "95014-5122",
		"issuerWebsite": "https://www.startupwind.com",
		"intermediaryCompanyName": "StartEngine Capital, LLC",
		"intermediaryCommissionCik": "0001665160",
		"intermediaryCommissionFileNumber": "007-00007",
		"compensationAmount": "Up to 9% percent",
		"financialInterest": "Three percent (3%) of securities of the total amount of investments raised in the offering, along the same terms as investors.",
		"securityOfferedType": "Common Stock",
		"securityOfferedOtherDescription": null,
		"numberOfSecurityOffered": 4444,
		"offeringPrice": 2.25,
		"offeringAmount": 9999,
		"overSubscriptionAccepted": "Y",
		"overSubscriptionAllocationType": "Other",
		"maximumOfferingAmount": 1234998,
		"offeringDeadlineDate": "01-03-2023",
		"currentNumberOfEmployees": 14,
		"totalAssetMostRecentFiscalYear": 75983,
		"totalAssetPriorFiscalYear": 73308,
		"cashAndCashEquiValentMostRecentFiscalYear": 73503,
		"cashAndCashEquiValentPriorFiscalYear": 68328,
		"accountsReceivableMostRecentFiscalYear": 2480,
		"accountsReceivablePriorFiscalYear": 4980,
		"shortTermDebtMostRecentFiscalYear": 172224,
		"shortTermDebtPriorFiscalYear": 170806,
		"longTermDebtMostRecentFiscalYear": 41000,
		"longTermDebtPriorFiscalYear": 41000,
		"revenueMostRecentFiscalYear": 252313,
		"revenuePriorFiscalYear": 204150,
		"costGoodsSoldMostRecentFiscalYear": 0,
		"costGoodsSoldPriorFiscalYear": 0,
		"taxesPaidMostRecentFiscalYear": 0,
		"taxesPaidPriorFiscalYear": 0,
		"netIncomeMostRecentFiscalYear": -74835,
		"netIncomePriorFiscalYear": -133946,
		"updatedAt": "2022-10-05T17:13:01.157Z",
		"createdAt": "2022-10-05T17:13:01.157Z",
		"acceptanceTime": "2022-10-05 13:08:07"
	}
]
"""


CROWDFUNDING_SEARCH_ENDPOINT = "v4/crowdfunding-offerings/search"
# Allows users to search for crowdfunding campaigns by company name, campaign name, or platform.

# Query Parameters
# name - string (required) - The name of the company, campaign, or platform to search for.

# Response:
"""
[
	{
		"cik": "0001912939",
		"name": "Enotap LLC",
		"date": "2022-07-20 17:06:10"
	}
]
"""

CROWDFUNDING_BY_CIK_ENDPOINT = "v4/crowdfunding-offerings"
# Provides a list of all crowdfunding campaigns that have been launched by a particular company.

# Query Parameters
# cik - string (required) - The CIK of the company to search for.

# Response:
"""
[
	{
		"formType": "C-U",
		"formSignification": "Progress Update",
		"acceptanceTime": "2022-07-21 17:28:54",
		"cik": "0001916078",
		"nameOfIssuer": "OYO Fitness, Inc",
		"legalStatusForm": "Corporation",
		"jurisdictionOrganization": "DE",
		"issuerStreet": "374 N. 750TH RD",
		"issuerCity": "OVERBROOK",
		"issuerStateOrCountry": "KS",
		"issuerZipCode": "66524",
		"issuerWebsite": "https://www.oyofitness.com/",
		"intermediaryCompanyName": "StartEngine Capital, LLC",
		"intermediaryCommissionCik": "0001665160",
		"intermediaryCommissionFileNumber": "007-00007",
		"compensationAmount": "7 - 13 percent",
		"financialInterest": "Two percent (2%) of securities of the total amount of investments raised in the offering, along the same terms as investors.",
		"securityOfferedType": "Other",
		"securityOfferedOtherDescription": "Non-Voting Common Stock",
		"numberOfSecurityOffered": 5000,
		"offeringPrice": 2,
		"offeringAmount": 10000,
		"overSubscriptionAccepted": "Y",
		"overSubscriptionAllocationType": "Other",
		"maximumOfferingAmount": 1070000,
		"offeringDeadlineDate": "07-19-2022",
		"currentNumberOfEmployees": 5,
		"totalAssetMostRecentFiscalYear": 497717,
		"totalAssetPriorFiscalYear": 248472,
		"cashAndCashEquiValentMostRecentFiscalYear": 150142,
		"cashAndCashEquiValentPriorFiscalYear": 54571,
		"accountsReceivableMostRecentFiscalYear": 0,
		"accountsReceivablePriorFiscalYear": 0,
		"shortTermDebtMostRecentFiscalYear": 3286745,
		"shortTermDebtPriorFiscalYear": 2214117,
		"longTermDebtMostRecentFiscalYear": 82243,
		"longTermDebtPriorFiscalYear": 105850,
		"revenueMostRecentFiscalYear": 4344154,
		"revenuePriorFiscalYear": 11078510,
		"costGoodsSoldMostRecentFiscalYear": 2445024,
		"costGoodsSoldPriorFiscalYear": 5737776,
		"taxesPaidMostRecentFiscalYear": 0,
		"taxesPaidPriorFiscalYear": 0,
		"netIncomeMostRecentFiscalYear": -964551,
		"netIncomePriorFiscalYear": -10860
	}
]
"""

EQUITY_OFFERING_RSS_ENDPOINT = "v4/fundraising-rss-feed"
# Provides an RSS feed of equity offering announcements, updated in real time.

# Query Parameters
# page - integer - The page number to retrieve. Default is 0.

# Response:
"""
[
	{
		"cik": "0001949154",
		"url": "https://www.sec.gov/Archives/edgar/data/1949154/000194915422000002/xslFormDX01/primary_doc.xml",
		"companyName": "Avlok Capital, LP - C2",
		"entityName": "Avlok Capital, LP - C2",
		"fillingDate": "2022-10-05 00:00:00",
		"date": "2022-10-05T04:00:00.000Z",
		"formType": "D",
		"formSignification": "Notice of Exempt Offering of Securities",
		"issuerStreet": "119 South Main Street",
		"issuerCity": "Seattle",
		"issuerStateOrCountry": "WA",
		"issuerStateOrCountryDescription": "WASHINGTON",
		"issuerZipCode": "98104",
		"issuerPhoneNumber": "3603409337",
		"jurisdictionOfIncorporation": "DELAWARE",
		"entityType": "Limited Partnership",
		"incorporatedWithinFiveYears": "",
		"yearOfIncorporation": "2022",
		"relatedPersonFirstName": "Ltd.",
		"relatedPersonLastName": "Belltower Fund Group",
		"relatedPersonStreet": "119 South Main Street",
		"relatedPersonCity": "Seattle",
		"relatedPersonStateOrCountry": "WA",
		"relatedPersonStateOrCountryDescription": "WASHINGTON",
		"relatedPersonZipCode": "98104",
		"relatedPersonRelationship": "Director",
		"industryGroupType": "Pooled Investment Fund",
		"revenueRange": "Decline to Disclose",
		"federalExemptionsExclusions": "06c,3C.1",
		"isAmendment": false,
		"dateOfFirstSale": "2022-10-05",
		"durationOfOfferingIsMoreThanYear": false,
		"securitiesOfferedAreOfEquityType": true,
		"isBusinessCombinationTransaction": false,
		"minimumInvestmentAccepted": 4000,
		"totalOfferingAmount": 700800,
		"totalAmountSold": 200800,
		"totalAmountRemaining": 500000,
		"hasNonAccreditedInvestors": false,
		"totalNumberAlreadyInvested": 8,
		"salesCommissions": 0,
		"findersFees": 0,
		"grossProceedsUsed": 20000,
		"createdDate": "2022-10-05T22:03:01.774Z",
		"updatedDate": "2022-10-05T22:03:01.774Z",
		"acceptanceTime": "2022-10-05 13:58:59"
	}
]
"""

EQUITY_OFFERING_SEARCH_ENDPOINT = "v4/fundraising/search"
# Allows users to search for equity offerings by company name, offering name, or exchange.

# Query Parameters
# name - string (required) - The name of the company, offering, or exchange to search for.

# Response:
"""
[
	{
		"cik": "0001428287",
		"name": "KANJOYA, INC",
		"date": "2013-11-04 18:16:21"
	},
	{
		"cik": "0001428287",
		"name": "KANJOYA, INC",
		"date": "2012-07-27 12:56:40"
	}
]
"""

EQUITY_OFFERING_BY_CIK_ENDPOINT = "v4/fundraising"
# Provides a list of all equity offerings that have been launched by a particular company.

# Query Parameters
# cik - string (required) - The CIK of the company to search for.

# Response:
"""
[
	{
		"formType": "D",
		"formSignification": "Notice of Exempt Offering of Securities",
		"acceptanceTime": "2014-02-28 16:00:25",
		"cik": "0001547416",
		"entityName": "NJOY INC",
		"issuerStreet": "15211 N. KIERLAND BLVD., SUITE 200",
		"issuerCity": "SCOTTSDALE",
		"issuerStateOrCountry": "AZ",
		"issuerStateOrCountryDescription": "ARIZONA",
		"issuerZipCode": "85254",
		"issuerPhoneNumber": "480-397-2300",
		"jurisdictionOfIncorporation": "DELAWARE",
		"entityType": "Corporation",
		"incorporatedWithinFiveYears": null,
		"yearOfIncorporation": "",
		"relatedPersonFirstName": "CRAIG",
		"relatedPersonLastName": "WEISS",
		"relatedPersonStreet": "c/o NJOY, INC.",
		"relatedPersonCity": "SCOTTSDALE",
		"relatedPersonStateOrCountry": "AZ",
		"relatedPersonStateOrCountryDescription": "ARIZONA",
		"relatedPersonZipCode": "85254",
		"relatedPersonRelationship": "Executive Officer, Director",
		"industryGroupType": "Other",
		"revenueRange": "Decline to Disclose",
		"federalExemptionsExclusions": "06b",
		"isAmendment": false,
		"dateOfFirstSale": "2014-02-14",
		"durationOfOfferingIsMoreThanYear": false,
		"securitiesOfferedAreOfEquityType": true,
		"isBusinessCombinationTransaction": false,
		"minimumInvestmentAccepted": 0,
		"totalOfferingAmount": 71999990,
		"totalAmountSold": 71999990,
		"totalAmountRemaining": 0,
		"hasNonAccreditedInvestors": false,
		"totalNumberAlreadyInvested": 24,
		"salesCommissions": 0,
		"findersFees": 0,
		"grossProceedsUsed": 0
	}
]
"""


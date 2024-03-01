"""Economic Data API module."""
TREASURY_RATES_ENDPOINT = "v4/treasury"
ECONOMIC_INDICATORS_ENDPOINT = "v4/economic"
ECONOMIC_CALENDAR_ENDPOINT = "v4/economic_calendar"
MARKET_RISK_PREMIUM_ENDPOINT = "v4/market_risk_premium"


class EconomicData:
    """
    A class to access sales revenue segmentation information for companies.

    Explanation:
    This class provides methods to retrieve revenue breakdowns by
      product category and geographic region for a company.

    Methods:
    - `get_treasury_rates(from_date, to_date)`:
    Provides real-time and historical Treasury rates for all maturities.
    - `get_economic_indicators(name, from_date, to_date)`:
    Provides real-time and historical economic data for economic indicators.
    - `get_economic_calendar(from_date, to_date)`:
    Provides a calendar of upcoming economic data releases.
    - `get_market_risk_premium()`:
    Provides real-time and historical market risk premium data.

    """

    def __init__(self, api):
        """
        Initializes the EconomicData class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_treasury_rates(self, from_date, to_date):
        """
        Provides real-time and historical Treasury rates for all maturities.

        Args:
            from_date (str): The start date for the data
            to_date (str): The end date for the data

        Returns: [
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
        return self.api.get(
            TREASURY_RATES_ENDPOINT, params={"from": from_date, "to": to_date}
        )

    def get_economic_indicators(self, name, from_date, to_date):
        """Provides real-time and historical economic data.

        For a variety of economic indicators, such as GDP, unemployment, and inflation.

        Args:
            name (str): The name of the economic indicator
              GDP, realGDP, nominalPotentialGDP, realGDPPerCapita,
              federalFunds, CPI, inflationRate, inflation, retailSales,
              consumerSentiment, durableGoods, unemploymentRate,
              totalNonfarmPayroll, initialClaims, industrialProductionTotalIndex,
              newPrivatelyOwnedHousingUnitsStartedTotalUnits, totalVehicleSales,
              retailMoneyFunds, smoothedUSRecessionProbabilities,
              3MonthOr90DayRatesAndYieldsCertificatesOfDeposit,
              commercialBankInterestRateOnCreditCardPlansAllAccounts,
              30YearFixedRateMortgageAverage, 15YearFixedRateMortgageAverage
            from_date (str): The start date for the data
            to_date (str): The end date for the data

        Returns: [
            {
                "date": "2022-04-01",
                "value": "24882.878"
            },
            {
                "date": "2022-01-01",
                "value": "24386.734"
            }
        """
        return self.api.get(
            ECONOMIC_INDICATORS_ENDPOINT,
            name=name,
            params={"name": name, "from": from_date, "to": to_date},
        )

    def get_economic_calendar(self, from_date, to_date):
        """Provides a calendar of upcoming economic data releases.

        Args:
            from_date (str): The start date for the data
            to_date (str): The end date for the data

        Returns: [
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
        return self.api.get(
            ECONOMIC_CALENDAR_ENDPOINT, params={"from": from_date, "to": to_date}
        )

    def get_market_risk_premium(self):
        """Provides real-time and historical market risk premium data.

        # Query Parameters
        # date?

        Returns: [
            {
                "country": "Abu Dhabi",
                "continent": null,
                "totalEquityRiskPremium": 5.75,
                "countryRiskPremium": 0.75
            }
        ]
        """
        return self.api.get(MARKET_RISK_PREMIUM_ENDPOINT)

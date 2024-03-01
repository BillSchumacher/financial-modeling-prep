"""Earnings API endpoints."""
EARNINGS_CALENDAR_ENDPOINT = "v3/earnings_calendar"
EARNINGS_HISTORICAL_AND_UPCOMING_ENDPOINT = "v3/historical/earnings_calendar/{symbol}"
EARNINGS_CONFIRMED_ENDPOINT = "v4/earning_calendar_confirmed"
EARNINGS_SURPRISES_ENDPOINT = "v3/earnings_surprises/{symbol}"


class Earnings:
    """Earnings API endpoints.

    Methods:
    - earnings_calendar(from_: str, to: str)
    - historical_and_upcoming_earnings_calendar(symbol: str, limit: int = 100)
    - earnings_confirmed(from_: str, to: str, limit: int = 100)
    - earnings_surprises(symbol: str)
    """

    def __init__(self, api):
        """
        Initializes the Earnings class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def earnings_calendar(self, from_: str, to: str) -> dict:
        """A list of upcoming & past earnings announcements.

        For publicly traded companies, including the date,
        estimated earnings per share (EPS), and actual EPS (if available).

        Args:
            from_: date (string) - The date to start the earnings calendar from.
            to: date (string) - The date to end the earnings calendar at.

        Returns: [
            {
                "date": "2023-05-13",
                "symbol": "VIKASECO.NS",
                "eps": 0.01967,
                "epsEstimated": null,
                "time": "bmo",
                "revenue": 683268000,
                "revenueEstimated": null,
                "fiscalDateEnding": "2023-03-31",
                "updatedFromDate": "2023-12-04"
            }
        ]
        """
        return self.api.get(
            EARNINGS_CALENDAR_ENDPOINT, params={"from": from_, "to": to}
        )

    def historical_and_upcoming_earnings_calendar(
        self, symbol: str, limit: int = 100
    ) -> dict:
        """A list of historical & upcoming earnings announcements.

         For a specific company, including the date, estimated EPS, and actual EPS.

        Args:
            symbol: string - The company’s stock symbol.
            limit: int - The number of earnings to return. Default is 100

        Returns: [
            {
                "date": "1998-10-14",
                "symbol": "AAPL",
                "eps": 0.0055,
                "epsEstimated": 0.00393,
                "time": "amc",
                "revenue": 1556000000,
                "revenueEstimated": 2450700000,
                "updatedFromDate": "2023-12-04",
                "fiscalDateEnding": "1998-09-25"
            }
        ]
        """
        return self.api.get(
            EARNINGS_HISTORICAL_AND_UPCOMING_ENDPOINT.format(symbol=symbol), limit=limit
        )

    def earnings_confirmed(self, from_: str, to: str, limit: int = 100) -> dict:
        """A list of earnings announcements that have already been confirmed.

        Args:
            from_: date (string) - The date to start the earnings calendar from.
            to: date (string) - The date to end the earnings calendar at.
            limit: int - The number of earnings to return. Default is 100

        Returns: [
            {
                "symbol": "MS",
                "exchange": "NYSE",
                "time": "08:30",
                "when": "pre market",
                "date": "2023-04-19",
                "publicationDate": "2023-01-31",
                "title": "Morgan Stanley Schedules Quarterly Investor...",
                "url": "https://www.businesswire.com/news/home/20230131006096/en"
            }
        ]
        """
        return self.api.get(
            EARNINGS_CONFIRMED_ENDPOINT,
            params={"from": from_, "to": to, "limit": limit},
        )

    def earnings_surprises(self, symbol: str) -> dict:
        """A list of earnings announcements that were positive or negative surprises.

        This endpoint includes the date of the earnings announcement,
          the estimated EPS, the actual EPS, and the earnings surprise.

        Args:
            symbol: string - The company’s stock symbol.

        Returns: [
            {
                "date": "2023-02-02",
                "symbol": "AAPL",
                "actualEarningResult": 1.88,
                "estimatedEarning": 1.94
            }
        ]
        """
        return self.api.get(EARNINGS_SURPRISES_ENDPOINT.format(symbol=symbol))

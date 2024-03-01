"""IPO calendar module."""
IPO_CONFIRMED_ENDPOINT = "v4/ipo-calendar-confirmed"
IPO_PROSPECTUS_ENDPOINT = "v4/ipo-calendar-prospectus"
IPO_CALENDAR_BY_SYMBOL = " v3/ipo_calendar"


class IPOCalendar:
    """IPO calendar class.

    Methods:
    - get_ipo_calendar(from_date, to_date)
    - get_ipo_prospectus(from_date, to_date)
    - get_ipo_calendar_by_symbol(symbol, from_date, to_date)
    """

    def __init__(self, api):
        """
        Initializes the IPOCalendar class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_ipo_calendar(self, from_date, to_date):
        """Get IPO calendar.

        Args:
            from_date (str): The starting date of the IPOs.
             The date format is YYYY-MM-DD.
            to_date (str): The ending date of the IPOs.
             The date format is YYYY-MM-DD.

        Returns: [
            {
                "symbol": "CETUU",
                "cik": "0001936702",
                "form": "CERT",
                "filingDate": "2023-01-31",
                "acceptedDate": "2023-01-31 15:04:42",
                "effectivenessDate": "2023-01-31",
                "url": "https://www.sec.gov/Archives/edgar/data/1936702/..."
            }
        ]
        """
        return self.api.get(IPO_CONFIRMED_ENDPOINT, {"from": from_date, "to": to_date})

    def get_ipo_prospectus(self, from_date, to_date):
        """Get IPO prospectus.

        Args:
            from_date (str): The starting date of the IPOs.
             The date format is YYYY-MM-DD.
            to_date (str): The ending date of the IPOs.
             The date format is YYYY-MM-DD.

        Returns: [
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
                "url": "https://www.sec.gov/Archives/edgar/data/1679379..."
            }
        ]
        """
        return self.api.get(IPO_PROSPECTUS_ENDPOINT, {"from": from_date, "to": to_date})

    def get_ipo_calendar_by_symbol(self, symbol, from_date, to_date):
        """Get IPO calendar by symbol.

        Args:
            symbol (str): The symbol of the company.
            from_date (str): The starting date of the IPOs.
             The date format is YYYY-MM-DD.
            to_date (str): The ending date of the IPOs.
             The date format is YYYY-MM-DD.

        Returns: [
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
        return self.api.get(
            IPO_CALENDAR_BY_SYMBOL, {"symbol": symbol, "from": from_date, "to": to_date}
        )

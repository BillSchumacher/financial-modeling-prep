"""Earnings Transcripts API endpoints."""
EARNINGS_TRANSCRIPT_ENDPOINT = "v3/earning_call_transcript/{symbol}"
TRANSCRIPT_DATES_ENDPOINT = "v4/earning_call_transcripts"
BATCH_EARNING_CALL_TRANSCRIPT_ENDPOINT = "v4/batch_earning_call_transcript/{symbol}"


class EarningsTranscripts:
    """
    A class to access earnings transcripts for companies.

    Explanation:
    This class provides methods to retrieve earnings call transcripts,
     upcoming earnings call dates, and batch transcripts for specific companies.

    Methods:
    - get_earnings_transcript:
     Get the full transcript of an earnings call for a specific company.
    - get_transcript_dates:
     Get a list of all upcoming earnings call dates for a specific company.
    - get_batch_earnings_transcripts: Get batch transcripts for a specific company.
    """

    def __init__(self, api):
        """
        Initializes the EarningsTranscripts class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_earnings_transcript(self, symbol, year=None, quarter=None):
        """Get the full transcript of an earnings call for a specific company.

        This endpoint can be used to learn more about a company's
         financial performance, future plans, and overall strategy.

        Args:
            symbol (str): The company's ticker symbol
            year (int): The year of the transcript
            quarter (int): The quarter of the transcript

        Returns: [
            {
                "symbol": "AAPL",
                "quarter": 3,
                "year": 2020,
                "date": "2020-07-30 23:35:04",
                "content": "Operator: Good day, everyone. Welcome to the..."
            }
        ]
        """
        return self.api.get(
            EARNINGS_TRANSCRIPT_ENDPOINT.format(symbol=symbol),
            params={"year": year, "quarter": quarter},
        )

    def get_transcript_dates(self, symbol):
        """Get a list of all upcoming earnings call dates for a specific company.

        Args:
            symbol (str): The company's ticker symbol

        Returns: [
                1,
                2023,
                "2023-02-02 21:33:03"
            ]
        ]
        """
        return self.api.get(TRANSCRIPT_DATES_ENDPOINT, params={"symbol": symbol})

    def get_batch_earnings_transcripts(self, symbol, year=None):
        """Get batch transcripts for a specific company.

        Args:
            symbol (str): The company's ticker symbol
            year (int): The year of the transcript

        Returns:[
            {
                "symbol": "AAPL",
                "quarter": 4,
                "year": 2020,
                "date": "2020-10-29 23:40:53",
                "content": "Operator: Good day everyone and welcome to the..."
            }
        ]
        """
        return self.api.get(
            BATCH_EARNING_CALL_TRANSCRIPT_ENDPOINT.format(symbol=symbol),
            params={"year": year},
        )

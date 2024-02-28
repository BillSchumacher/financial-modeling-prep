EARNINGS_TRANSCRIPT_ENDPOINT = "v3/earning_call_transcript/{symbol}"
# Get the full transcript of an earnings call for a specific company in text format. This endpoint can be used to learn more about a company's financial performance, future plans, and overall strategy.

# Path Params:
# symbol (required) - the company's ticker symbol

# Query Params:
# year (optional) - the year of the transcript
# quarter (optional) - the quarter of the transcript

# Response:
"""
[
	{
		"symbol": "AAPL",
		"quarter": 3,
		"year": 2020,
		"date": "2020-07-30 23:35:04",
		"content": "Operator: Good day, everyone. Welcome to the Apple Incorporated Third Quarter Fiscal Year 2020 Earnings Conference Call. Today's call is being recorded. At this time, for opening remarks and introductions, I would like to turn things over to Mr. Tejas Gala, Senior Manager, Corporate Finance and Investor Relations. Please go ahead, sir.\nTejas Gala: Thank you. Good afternoon and thank you for joining us. Speaking first today is Apple's CEO, Tim Cook; and he'll be followed by CFO, Luca Maestri. After that, we'll open the call to questions from analysts. Please note that some of the information you'll hear during our discussion today will consist of forward-looking statements including without limitation..."
	}
]
"""

TRANSCRIPT_DATES_ENDPOINT = "v4/earning_call_transcripts"
# Get a list of all upcoming earnings call dates for a specific company. This endpoint can be used to plan your trading activity around earnings call dates.

# Query Params:
# symbol (required) - the company's ticker symbol

# Response:
"""
[
	[
		1,
		2023,
		"2023-02-02 21:33:03"
	]
]
"""

BATCH_EARNING_CALL_TRANSCRIPT_ENDPOINT = "v4/batch_earning_call_transcript/{symbol}"

# Path Params:
# symbol (required) - the company's ticker symbol

# Query Params:
# year (optional) - the year of the transcript

# Response:
"""
[
	{
		"symbol": "AAPL",
		"quarter": 4,
		"year": 2020,
		"date": "2020-10-29 23:40:53",
		"content": "Operator: Good day everyone and welcome to the Apple Inc. Fourth Quarter Fiscal Year 2020 Earnings Conference Call. Today’s call is being recorded. At this time for opening remarks and introductions, I would like to turn things over to Tejas Gala, Senior Analyst, Corporate Finance and Investor Relations. Please go ahead, sir.\nTejas Gala: Thank you. Good afternoon and thank you for joining us. Speaking first today is Apple’s CEO, Tim Cook, and he will be followed by CFO"
	}
]
"""
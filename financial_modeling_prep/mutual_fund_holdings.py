"""Mutual Fund Holdings API endpoints."""
MUTUAL_FUND_DATES_ENDPOINT = "v4/mutual-fund-holdins/portfolio-date"
MUTUAL_FUNDS_ENDPOINT = "v4/mutual-fund-holdings"
MUTUAL_FUND_BY_NAME_ENDPOINT = "v4/mutual-fund-holdings/name"
MUTUAL_FUND_HOLDER_ENDPOINT = "v3/mutual-fund-holder/{symbol}"


class MutualFundHoldings:
    """
    A class to access mutual fund holdings information.

    Explanation:
    This class provides methods to retrieve mutual fund portfolio dates,
     holdings, mutual funds by name, and mutual fund holders.

    Methods:
    - portfolio_date: Get mutual fund portfolio date.
    - holdings: Get mutual fund holdings.
    - by_name: Get mutual fund by name.
    - holder: Get mutual fund holder.
    """

    def __init__(self, api):
        """
        Initializes the MutualFundHoldings class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def portfolio_date(self, symbol, cik=None):
        """Get mutual fund portfolio date.

        Args:
            symbol (str): Symbol of the mutual fund.
            cik (str): CIK of the mutual fund.

        Returns: [
            {
                "date": "2023-03-31"
            },
            {
                "date": "2022-12-31"
            }
        ]
        """
        return self.api.get(
            MUTUAL_FUND_DATES_ENDPOINT, params={"symbol": symbol, "cik": cik}
        )

    def holdings(self, symbol, date, cik=None):
        """Get mutual fund holdings.

        Args:
            symbol (str): Symbol of the mutual fund.
            date (str): Date of the mutual fund holdings.
            cik (str): CIK of the mutual fund.

        Returns: [
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
        return self.api.get(
            MUTUAL_FUNDS_ENDPOINT, params={"symbol": symbol, "date": date, "cik": cik}
        )

    def by_name(self, name):
        """Get mutual fund by name.

        Args:
            name (str): Name of the mutual fund.

        Returns: [
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
        return self.api.get(MUTUAL_FUND_BY_NAME_ENDPOINT, params={"name": name})

    def holder(self, symbol):
        """Get mutual fund holder.

        Args:
            symbol (str): Symbol of the mutual fund.

        Returns: [
            {
                "holder": "CYPRESS FUNDS LLC",
                "shares": 371332,
                "dateReported": "2022-09-30",
                "change": -360468,
                "weightPercent": null
            }
        ]
        """
        return self.api.get(MUTUAL_FUND_HOLDER_ENDPOINT.format(symbol=symbol))

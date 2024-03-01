"""ETF Holdings API endpoints."""
ETF_HOLDING_DATES_ENDPOINT = "v4/etf-holdings/portfolio-date"
ETF_HOLDINGS_ENDPOINT = "v4/etf-holdings"
ETF_HOLDER_ENDPOINT = "v3/etf-holder/{symbol}"
ETF_INFORMATION_ENDPOINT = "v4/etf-info"
ETF_SECTOR_WEIGHTING_ENDPOINT = "v3/etf-sector-weightings/{symbol}"
ETF_COUNTRY_WEIGHTING_ENDPOINT = "v3/etf-country-weightings/{symbol}"
ETF_SECTOR_EXPOSURE_ENDPOINT = "v3/etf-stock-exposure/{symbol}"


class ETFHoldings:
    """
    A class to interact with ETF holdings data.

    Explanation:
    This class provides methods to retrieve information about ETF holdings,
     ETF holders, ETF information, sector weighting, country weighting,
      and sector exposure for a given ETF symbol.

    Methods:
    - get_etf_holdings: Get a list of all the securities held by an ETF.
    - get_etf_holding_dates: Get a list of dates when ETF holdings are updated.
    - get_etf_holder: Get a list of institutional investors that own shares of an ETF.
    - get_etf_information: Get basic information about an ETF.
    - get_etf_sector_weighting:
     Get the percentage breakdown of an ETF's assets by sector.
    - get_etf_country_weighting:
     Get the percentage breakdown of an ETF's assets by country.
    - get_etf_sector_exposure:
     Get the measure of an ETF's performance attributable to each sector.
    """

    def __init__(self, api):
        """
        Initializes the ETFHoldings class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_etf_holdings(self, symbol: str, cik: str = None, date: str = None):
        """Provides a list of all the securities that are held by an ETF.

        For example, an investor may want to know which ETF has the
          highest exposure to a particular industry or sector.

        Args:
            symbol (str): symbol
            cik (str, optional): cik. Defaults to None.
            date (str, optional): date. Defaults to None.

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
            ETF_HOLDINGS_ENDPOINT, {"symbol": symbol, "cik": cik, "date": date}
        )

    def get_etf_holding_dates(self, symbol: str, cik: str = None):
        """Provides a list of the dates on which ETF holdings are updated.

        For example, an investor may want to know when an ETF's holdings are updated
          in order to make sure that they are still aligned with their investment goals.

        Args:
            symbol (str): symbol
            cik (str, optional): cik. Defaults to None.

        Returns: [
            {
                "date": "2023-03-31"
            },
            {
                "date": "2022-12-31"
            }
        ]
        """
        return self.api.get(ETF_HOLDING_DATES_ENDPOINT, {"symbol": symbol, "cik": cik})

    def get_etf_holder(self, symbol: str):
        """Provides a list of all the institutional investors that own shares of an ETF.

        For example, an investor may want to know which institutions are
          buying or selling shares of a particular ETF.

        Args:
            symbol (str): symbol

        Returns: [
            {
                "asset": "AAPL",
                "name": "Apple Inc.",
                "isin": "US0378331005",
                "cusip": "037833100",
                "sharesNumber": 163400200,
                "weightPercentage": 6.71,
                "marketValue": 24766568314,
                "updated": "2023-02-16"
            }
        ]
        """
        return self.api.get(ETF_HOLDER_ENDPOINT.format(symbol=symbol))

    def get_etf_information(self, symbol: str):
        """Provides basic information about an ETF.

        Such as its ticker symbol, name, expense ratio, and asset under management.
        For example, an investor may want to compare the expense ratios of different
          ETFs to find the one that is most cost-effective.

        Args:
            symbol (str): symbol

        Returns: [
            {
                "symbol": "SPY",
                "assetClass": "Equity",
                "aum": 375825060000,
                "avgVolume": 81144062,
                "cusip": "",
                "description": "The Trust seeks to achieve its investment objective...",
                "domicile": "US",
                "etfCompany": "SPDR",
                "expenseRatio": 0.0945,
                "inceptionDate": "1993-01-22",
                "isin": "",
                "name": "SPDR S&P 500 ETF Trust",
                "nav": 375825.06,
                "navCurrency": "USD",
                "sectorsList": [
                    {
                        "exposure": "2.53%",
                        "industry": "Real Estate"
                    }
                ],
                "website": "https://www.ssga.com/us/en/institutional/etfs/...",
                "holdingsCount": 503
            }
        ]
        """
        return self.api.get(ETF_INFORMATION_ENDPOINT, {"symbol": symbol})

    def get_etf_sector_weighting(self, symbol: str):
        """Provides a breakdown of the percentage of an ETF's assets in each sector.

         For example, an investor may want to invest in an ETF that
          has a high exposure to the technology sector if they believe
          that the technology sector is poised for growth.

        Args:
            symbol (str): symbol

        Returns: [
            {
                "sector": "Technology",
                "weightPercentage": "90.11%"
            }
        ]
        """
        return self.api.get(ETF_SECTOR_WEIGHTING_ENDPOINT.format(symbol=symbol))

    def get_etf_country_weighting(self, symbol: str):
        """Provides a breakdown of the percentage of an ETF's assets in each country.

         For example, an investor may want to invest in an ETF that
           has a high exposure to China if they believe that the
           Chinese economy is poised for growth.

        Args:
            symbol (str): symbol

        Returns: [
            {
                "country": "United States",
                "weightPercentage": "96.54%"
            }
        ]
        """
        return self.api.get(ETF_COUNTRY_WEIGHTING_ENDPOINT.format(symbol=symbol))

    def get_etf_sector_exposure(self, symbol: str):
        """Provides a measure of an ETF's performance is attributable to each sector.

         For example, an investor may want to invest in an ETF that
          has a high exposure to the technology sector if they believe
           that the technology sector is likely to outperform the overall market.

        Args:
            symbol (str): symbol

        Returns: [
            {
                "etfSymbol": "QDVE.DE",
                "assetExposure": "AAPL",
                "sharesNumber": 5128516,
                "weightPercentage": 27,
                "marketValue": 798715081.84
            }
        ]
        """
        return self.api.get(ETF_SECTOR_EXPOSURE_ENDPOINT.format(symbol=symbol))

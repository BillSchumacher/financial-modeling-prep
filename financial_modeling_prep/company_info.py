"""Company Info API endpoints."""
COMPANY_PROFILE_ENDPOINT = "v3/profile/{symbol}"
EXECUTIVE_COMPENSATION_ENDPOINT = "v4/governance/executive_compensation"
COMPENSATION_BENCHMARK_ENDPOINT = "v4/executive-compensation-benchmark"
COMPANY_NOTES_ENDPOINT = "v4/company-notes"
HISTORICAL_EMPLOYEE_ENDPOINT = "v4/historical/employee_count"
EMPLOYEE_COUNT_ENDPOINT = "v4/employee_count"
STOCK_SCREEN_ENDPOINT = "v3/stock-screener"
STOCK_GRADE_ENDPOINT = "v3/grade/{symbol}"
EXECUTIVES_ENDPOINT = "v3/key-executives/{symbol}"
COMPANY_CORE_INFORMATION_ENDPOINT = "v4/company-core-information"
MARKET_CAPITALIZATION_ENDPOINT = "v3/market-capitalization/{symbol}"
HISTORICAL_MARKET_CAPITALIZATION_ENDPOINT = (
    "v3/historical-market-capitalization/{symbol}"
)
ALL_COUNTRIES_ENDPOINT = "v3/get-all-countries"
ANALYST_ESTIMATES_ENDPOINT = "v3/analyst-estimates/{symbol}"
ANALYST_RECOMMENDATION_ENDPOINT = "v3/analyst-stock-recommendations/{symbol}"
COMPANY_OUTLOOK_ENDPOINT = "v4/company-outlook"
STOCK_PEERS_ENDPOINT = "v4/stock_peers"
MARKET_OPEN_ENDPOINT = "v3/is-the-market-open"
DELISTED_COMPANIES_ENDPOINT = "v3/delisted-companies"
COMPANY_SHARE_FLOAT_ENDPOINT = "v4/shares_float"
HISTORICAL_SHARE_FLOAT_ENDPOINT = "v4/historical/shares_float"
ALL_SHARES_FLOAT_ENDPOINT = "v4/shares_float"


class CompanyInfo:
    """
    A class to access insider trading data.

    Explanation:
    This class provides methods to retrieve information about insider trades,
     insider transaction types, insiders by company symbol,
      insider trade statistics, CIK number mapping, fail to deliver data, and more.

    Methods:
    - insider_trades_rss: Get an RSS feed of insider trades.
    - insider_trades_search:
      Search for insider trades by company name, ticker symbol, or insider name.
    - transaction_types: Get a list of insider transaction types.
    - insiders_by_symbol: Get a list of insiders for a given company.
    - insider_trade_statistics:
      Get statistics on insider trading activity for a company.
    - cik_mapper: Convert a CIK number to a company name.
    - cik_mapper_by_symbol:
      Get a list of CIK numbers and company names by symbol.
    - fail_to_deliver: Get a list of fail to deliver data for a company.
    """

    def __init__(self, api):
        """
        Initializes the CompanyInfo class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_company_profile(self, symbol: str) -> dict:
        """Get a comprehensive overview of a company with our Company Profile endpoint.

         This endpoint provides key information such as price, beta,
            market capitalization, description, headquarters, and more.

        Args:
            symbol: str - The stock symbol of the company.

        Returns:[
            {
                "symbol": "AAPL",
                "price": 178.72,
                "beta": 1.286802,
                "volAvg": 58405568,
                "mktCap": 2794144143933,
                "lastDiv": 0.96,
                "range": "124.17-198.23",
                "changes": -0.13,
                "companyName": "Apple Inc.",
                "currency": "USD",
                "cik": "0000320193",
                "isin": "US0378331005",
                "cusip": "037833100",
                "exchange": "NASDAQ Global Select",
                "exchangeShortName": "NASDAQ",
                "industry": "Consumer Electronics",
                "website": "https://www.apple.com",
                "description": "Apple Inc. designs, manufactures, and markets...",
                "ceo": "Mr. Timothy D. Cook",
                "sector": "Technology",
                "country": "US",
                "fullTimeEmployees": "164000",
                "phone": "408 996 1010",
                "address": "One Apple Park Way",
                "city": "Cupertino",
                "state": "CA",
                "zip": "95014",
                "dcfDiff": 4.15176,
                "dcf": 150.082,
                "image": "https://financialmodelingprep.com/image-stock/AAPL.png",
                "ipoDate": "1980-12-12",
                "defaultImage": false,
                "isEtf": false,
                "isActivelyTrading": true,
                "isAdr": false,
                "isFund": false
            }
        ]
        """
        return self.api.get(COMPANY_PROFILE_ENDPOINT.format(symbol=symbol))

    def get_executive_compensation(self, symbol: str) -> dict:
        """Get the compensation of the company's executives.

        This endpoint provides information on the compensation of a
         company's executives, including the CEO, CFO, and COO.

        Args:
            symbol: str - The stock symbol of the company.

        Returns: [
            {
                "cik": "0000320193",
                "symbol": "AAPL",
                "companyName": "Apple Inc.",
                "industryTitle": "ELECTRONIC COMPUTERS",
                "acceptedDate": "2022-01-06 16:30:34",
                "filingDate": "2022-01-06",
                "nameAndPosition": "Kate Adams Senior Vice President, ...",
                "year": 2020,
                "salary": 1000000,
                "bonus": 0,
                "stock_award": 21657687,
                "incentive_plan_compensation": 3577000,
                "all_other_compensation": 14310,
                "total": 26248995,
                "url": "https://www.sec.gov/Archives/edgar/data/320193/..."
            }
        ]
        """
        return self.api.get(EXECUTIVE_COMPENSATION_ENDPOINT.format(symbol=symbol))

    def get_compensation_benchmark(self, year: int):
        """Compare a company's executive compensation to other companies.

        In the same industry with our Compensation Benchmark endpoint.
        This can help you understand how competitive a company's
         executive compensation is.

        Args:
            year: int - The year you want to get the compensation benchmark for.

        Returns: [
            {
                "industryTitle": "AGRICULTURAL PROD-LIVESTOCK & ANIMAL SPECIALTIES",
                "year": 2022,
                "averageCompensation": 312314.6
            }
        ]
        """
        return self.api.get(COMPENSATION_BENCHMARK_ENDPOINT, {"year": year})

    def get_company_notes(self, symbol: str) -> dict:
        """Stay up-to-date on a company's financial condition.

        Including operations, and risks with our Company Notes endpoint.

        This endpoint provides information about notes reported by a
         company in their financial statements.

        Args:
            symbol: str - The stock symbol of the company you want to get the notes for.

        Returns: [
            {
                "cik": "0000320193",
                "symbol": "AAPL",
                "title": "1.375% Notes due 2024",
                "exchange": "NASDAQ"
            }
        ]
        """
        return self.api.get(COMPANY_NOTES_ENDPOINT, {"symbol": symbol})

    def get_historical_employee_count(self, symbol: str) -> dict:
        """Track how a company's workforce has grown or shrunk over time.

        This endpoint provides information about the number of
         employees at a company over time.

        Args:
            symbol: str - The stock symbol of the company.

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "acceptanceTime": "2022-10-27 18:01:14",
                "periodOfReport": "2022-09-24",
                "companyName": "Apple Inc.",
                "formType": "10-K",
                "filingDate": "2022-10-28",
                "employeeCount": 164000,
                "source": "https://www.sec.gov/Archives/edgar/data/320193/..."
            }
        ]
        """
        return self.api.get(HISTORICAL_EMPLOYEE_ENDPOINT, {"symbol": symbol})

    def get_employee_count(self, symbol: str) -> dict:
        """Get the number of employees at a company.

        This endpoint provides information about the number of employees at a company.

        Args:
            symbol: str - The stock symbol of the company.

        Returns: [
            {
                "symbol": "AAPL",
                "cik": "0000320193",
                "acceptanceTime": "2022-10-27 18:01:14",
                "periodOfReport": "2022-09-24",
                "companyName": "Apple Inc.",
                "formType": "10-K",
                "filingDate": "2022-10-28",
                "employeeCount": 164000,
                "source": "https://www.sec.gov/Archives/edgar/data/320193/..."
            }
        ]
        """
        return self.api.get(EMPLOYEE_COUNT_ENDPOINT, {"symbol": symbol})

    def get_stock_screener(
        self,
        market_cap_more_than=None,
        market_cap_lower_than=None,
        price_more_than=None,
        price_lower_than=None,
        beta_more_than=None,
        beta_lower_than=None,
        volume_more_than=None,
        volume_lower_than=None,
        dividend_more_than=None,
        dividend_lower_than=None,
        is_etf=None,
        is_fund=None,
        sector=None,
        industry=None,
        country=None,
        exchange=None,
        limit=None,
    ):
        """Find stocks that meet your investment criteria.

        This endpoint allows you to search for stocks based on various criteria,
         such as market cap, price, volume, beta, sector, and country.

        Args:
            market_cap_more_than: int - The minimum market capitalization.
            market_cap_lower_than: int - The maximum market capitalization.
            price_more_than: int - The minimum price.
            price_lower_than: int - The maximum price.
            beta_more_than: int - The minimum beta.
            beta_lower_than: int - The maximum beta.
            volume_more_than: int - The minimum volume.
            volume_lower_than: int - The maximum volume.
            dividend_more_than: int - The minimum dividend.
            dividend_lower_than: int - The maximum dividend.
            is_etf: bool - Whether the stocks you want to find are ETFs.
            is_fund: bool - Whether the stocks you want to find are funds.
            sector: str - The sector of the stocks you want to find.
            industry: str - The industry of the stocks you want to find.
            country: str - The country of the stocks you want to find.
            exchange: str - The exchange of the stocks you want to find.
            limit: int - The maximum number of stocks you want to find.


        Returns: [
            {
                "symbol": "BAC-PL",
                "companyName": "Bank of America Corporation",
                "marketCap": 9519430436381,
                "sector": "Financial Services",
                "industry": "Banks—Diversified",
                "beta": 1.399232,
                "price": 1181.25,
                "lastAnnualDividend": 72.5,
                "volume": 2817,
                "exchange": "New York Stock Exchange",
                "exchangeShortName": "NYSE",
                "country": "US",
                "isEtf": false,
                "isActivelyTrading": true
            }
        ]
        """
        params = {
            "marketCapMoreThan": market_cap_more_than,
            "marketCapLowerThan": market_cap_lower_than,
            "priceMoreThan": price_more_than,
            "priceLowerThan": price_lower_than,
            "betaMoreThan": beta_more_than,
            "betaLowerThan": beta_lower_than,
            "volumeMoreThan": volume_more_than,
            "volumeLowerThan": volume_lower_than,
            "dividendMoreThan": dividend_more_than,
            "dividendLowerThan": dividend_lower_than,
            "isEtf": is_etf,
            "isFund": is_fund,
            "sector": sector,
            "industry": industry,
            "country": country,
            "exchange": exchange,
            "limit": limit,
        }
        return self.api.get(STOCK_SCREEN_ENDPOINT, params=params)

    def get_stock_grade(self, symbol: str, limit: int = 500) -> dict:
        """Get the grade of a stock with our Stock Grade endpoint.

        This endpoint provides a grade for a stock based on various criteria,
          such as value, growth, profitability, and momentum.

        Args:
            symbol: str - The stock symbol of the company you want to get the grade for.
            limit: int - The maximum number of grades you want to get.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-02-03",
                "gradingCompany": "Cowen & Co.",
                "previousGrade": "Outperform",
                "newGrade": "Outperform"
            }
        ]
        """
        return self.api.get(STOCK_GRADE_ENDPOINT.format(symbol), {"limit": limit})

    def get_executives(self, symbol: str) -> dict:
        """Get the executives of a company with our Company Executives endpoint.

        This endpoint provides information about the executives of a company,
         including their names, titles, and salaries.

        Args:
            symbol: str - The stock symbol of the company.

        Returns: [
            {
                "title": "Senior Vice President of People & Retail",
                "name": "Ms. Deirdre  O'Brien",
                "pay": 5019783,
                "currencyPay": "USD",
                "gender": "female",
                "yearBorn": 1967,
                "titleSince": 1676248586
            }
        ]
        """
        return self.api.get(EXECUTIVES_ENDPOINT.format(symbol))

    def get_company_core_information(self, symbol: str) -> dict:
        """Verify a company's identity or find additional information about a company.

        This endpoint provides core information such as CIK, exchange, and address.

        Args:
            symbol: str - The stock symbol of the company.

        Returns:[
            {
                "cik": "0000320193",
                "symbol": "AAPL",
                "exchange": "NASDAQ",
                "sicCode": "3571",
                "sicGroup": "Consumer Electronics",
                "sicDescription": "ELECTRONIC COMPUTERS",
                "stateLocation": "CA",
                "stateOfIncorporation": "CA",
                "fiscalYearEnd": "09-25",
                "businessAddress": "ONE APPLE PARK WAY,CUPERTINO CA 95014,...",
                "mailingAddress": "ONE APPLE PARK WAY,CUPERTINO CA 95014",
                "taxIdentificationNumber": "94-2404110",
                "registrantName": "Apple Inc."
            }
        ]
        """
        return self.api.get(COMPANY_CORE_INFORMATION_ENDPOINT, {"symbol": symbol})

    def get_market_capitalization(self, symbol: str) -> dict:
        """Get the market capitalization of a company.

        This endpoint provides information about the market capitalization of a company.

        Args:
            symbol: str - The stock symbol you want to get.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-03-02",
                "marketCap": 2309048053309
            }
        ]
        """
        return self.api.get(MARKET_CAPITALIZATION_ENDPOINT.format(symbol=symbol))

    def get_historical_market_capitalization(
        self, symbol: str, from_date: str, to_date: str, limit: int = 500
    ) -> dict:
        """Provides comprehensive historical market capitalization data for companies.

         Enabling users to analyze the company's growth trajectory and
         identify performance trends over time.
         Please note that each query is limited to a maximum of five years of data.

        Args:
            symbol: str - The stock symbol of the company.
            from_date: str - The start date you want to get.
            to_date: str - The end date you want to get.
            limit: int - The maximum number of results you want to get.


        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-03-02",
                "marketCap": 2313794623242
            }
        ]
        """
        return self.api.get(
            HISTORICAL_MARKET_CAPITALIZATION_ENDPOINT.format(symbol=symbol),
            {"from": from_date, "to": to_date, "limit": limit},
        )

    def get_all_countries(self):
        """Provides a list of all countries where stocks are traded.

        Investors can use this information to identify new investment
          opportunities and to diversify their portfolios.

        Returns: [
            "FK",
            "RU",
            "DK",
            "SN",
            "SI",
            "CZ",
            "KR"
        ]
        """
        return self.api.get(ALL_COUNTRIES_ENDPOINT)

    def get_analyst_estimates(self, symbol: str, period: str, limit: int = 30) -> dict:
        """Provides analyst estimates for a company's future earnings and revenue.

        Investors can use this information to get a sense of what analysts expect
         from a company and to identify potential investment opportunities.

        Args:
            symbol: str - The stock symbol of the company.
            period: str - The period you want to get. (annual, quarter)
            limit: int - The maximum number of analyst estimates you want to get.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-12-31",
                "estimatedRevenueLow": 338710374830,
                "estimatedRevenueHigh": 508065562246,
                "estimatedRevenueAvg": 423387968538,
                "estimatedEbitdaLow": 110816277291,
                "estimatedEbitdaHigh": 166224415938,
                "estimatedEbitdaAvg": 138520346615,
                "estimatedEbitLow": 99597027281,
                "estimatedEbitHigh": 149395540924,
                "estimatedEbitAvg": 124496284103,
                "estimatedNetIncomeLow": 83849180538,
                "estimatedNetIncomeHigh": 125773770810,
                "estimatedNetIncomeAvg": 104811475674,
                "estimatedSgaExpenseLow": 20384820993,
                "estimatedSgaExpenseHigh": 30577231491,
                "estimatedSgaExpenseAvg": 25481026242,
                "estimatedEpsAvg": 6.01,
                "estimatedEpsHigh": 7.209999999999999,
                "estimatedEpsLow": 4.81,
                "numberAnalystEstimatedRevenue": 12,
                "numberAnalystsEstimatedEps": 12
            }
        ]
        """
        return self.api.get(
            ANALYST_ESTIMATES_ENDPOINT.format(symbol=symbol),
            {"period": period, "limit": limit},
        )

    def get_analyst_recommendations(self, symbol: str, limit: int = 10) -> dict:
        """Provides recommendations for buying, selling, or holding a company's stock.

        Investors can use this information to get a sense of what analysts
         think of a company's stock and to make informed investment decisions.

        Args:
            symbol: str - The stock symbol of the company.
            limit: int - The maximum number of analyst recommendations you want to get.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-08-01",
                "analystRatingsbuy": 21,
                "analystRatingsHold": 6,
                "analystRatingsSell": 0,
                "analystRatingsStrongSell": 0,
                "analystRatingsStrongBuy": 11
            }
        ]
        """
        return self.api.get(
            ANALYST_RECOMMENDATION_ENDPOINT.format(symbol=symbol), {"limit": limit}
        )

    def get_company_outlook(self, symbol: str) -> dict:
        """Get the outlook of a company with our Company Outlook endpoint.

         This endpoint provides an outlook for a company based on various
          criteria, such as value, growth, profitability, and momentum.

        Args:
            symbol: str - The stock symbol of the company.

        Returns: {
            "profile": {
                "symbol": "AAPL",
                "price": 173.66,
                "beta": 1.286802,
                "volAvg": 58221571,
                "mktCap": 2715035094200,
                "lastDiv": 0.96,
                "range": "124.17-198.23",
                "changes": 1.26,
                "companyName": "Apple Inc.",
                "currency": "USD",
                "cik": "0000320193",
                "isin": "US0378331005",
                "cusip": "037833100",
                "exchange": "NASDAQ Global Select",
                "exchangeShortName": "NASDAQ",
                "industry": "Consumer Electronics",
                "website": "https://www.apple.com",
                "description": "Apple Inc. designs, manufactures, and markets ...",
                "ceo": "Mr. Timothy D. Cook",
                "sector": "Technology",
                "country": "US",
                "fullTimeEmployees": "164000",
                "phone": "408 996 1010",
                "address": "One Apple Park Way",
                "city": "Cupertino",
                "state": "CA",
                "zip": "95014",
                "dcfDiff": 4.15176,
                "dcf": 150.082,
                "image": "https://financialmodelingprep.com/image-stock/AAPL.png",
                "ipoDate": "1980-12-12",
                "defaultImage": false,
                "isEtf": false,
                "isActivelyTrading": true,
                "isAdr": false,
                "isFund": false
            },
            "metrics": {
                "dividendYielTTM": 0,
                "volume": 51278844,
                "yearHigh": 198.23,
                "yearLow": 124.17
            },
            "ratios": [
                {
                    "dividendYielTTM": 0.005412875734193251,
                    "dividendYielPercentageTTM": 0.5412875734193251,
                    "peRatioTTM": 28.76791523047699,
                    "pegRatioTTM": 3.398209986600091,
                    "payoutRatioTTM": 0.15797804981004643,
                    "currentRatioTTM": 0.9815625425125837,
                    "quickRatioTTM": 0.8135848211070477,
                    "cashRatioTTM": 0.22733129006185832,
                    "daysOfSalesOutstandingTTM": 37.25360935371536,
                    "daysOfInventoryOutstandingTTM": 12.357922226265103,
                    "operatingCycleTTM": 21.543743710742863,
                    "daysOfPayablesOutstandingTTM": 78.5066807297448,
                    "cashConversionCycleTTM": -38.205912470922975,
                    "grossProfitMarginTTM": 0.4344924765518984,
                    "operatingProfitMarginTTM": 0.2923062096772093,
                    "pretaxProfitMarginTTM": 0.2901417695274957,
                    "netProfitMarginTTM": 0.2468138972164414,
                    "effectiveTaxRateTTM": 0.1493334530275147,
                    "returnOnAssetsTTM": 0.2828335890257225,
                    "returnOnEquityTTM": 1.649211812157629,
                    "returnOnCapitalEmployedTTM": 0.5342187314054504,
                    "netIncomePerEBTTTM": 0.8506665469724853,
                    "ebtPerEbitTTM": 0.9925952987721205,
                    "ebitPerRevenueTTM": 0.2923062096772093,
                    "debtRatioTTM": 0.32617195661387666,
                    "debtEquityRatioTTM": 1.8130537213392175,
                    "longTermDebtToCapitalizationTTM": 0.6193501531466102,
                    "totalDebtToCapitalizationTTM": 0.6445144319803721,
                    "interestCoverageTTM": 29.863225119744545,
                    "cashFlowToDebtRatioTTM": 1.0346998535871157,
                    "companyEquityMultiplierTTM": 5.558582473371603,
                    "receivablesTurnoverTTM": 9.79770836523248,
                    "payablesTurnoverTTM": 4.649285851945438,
                    "inventoryTurnoverTTM": 29.535709427288804,
                    "fixedAssetTurnoverTTM": 8.815912743972445,
                    "assetTurnoverTTM": 1.1459386696434435,
                    "operatingCashFlowPerShareTTM": 7.203132909243405,
                    "freeCashFlowPerShareTTM": 6.433270686869992,
                    "cashPerShareTTM": 3.980350134740222,
                    "operatingCashFlowSalesRatioTTM": 0.2945097191437048,
                    "freeCashFlowOperatingCashFlowRatioTTM": 0.8931211971133437,
                    "cashFlowCoverageRatiosTTM": 1.0346998535871157,
                    "shortTermCoverageRatiosTTM": 10.08760817200464,
                    "capitalExpenditureCoverageRatioTTM": 9.356392221762516,
                    "dividendPaidAndCapexCoverageRatioTTM": 4.179338384771762,
                    "priceBookValueRatioTTM": 45.22758813485085,
                    "priceToBookRatioTTM": 45.22758813485085,
                    "priceToSalesRatioTTM": 7.07163774460648,
                    "priceEarningsRatioTTM": 28.76791523047699,
                    "priceToFreeCashFlowsRatioTTM": 26.884996031172328,
                    "priceToOperatingCashFlowsRatioTTM": 24.10895400488184,
                    "priceCashFlowRatioTTM": 24.10895400488184,
                    "priceEarningsToGrowthRatioTTM": 3.398209986600091,
                    "priceSalesRatioTTM": 7.07163774460648,
                    "enterpriseValueMultipleTTM": 23.12482605516728,
                    "priceFairValueTTM": 45.22758813485085,
                    "dividendPerShareTTM": 0.94
                }
            ],
            "insideTrades": [
                {
                    "symbol": "AAPL",
                    "filingDate": "2023-10-03 21:09:17",
                    "transactionDate": "2023-10-01",
                    "reportingCik": "0001496686",
                    "transactionType": "M-Exempt",
                    "securitiesOwned": 626085,
                    "companyCik": "0000320193",
                    "reportingName": "WILLIAMS JEFFREY E",
                    "typeOfOwner": "officer: COO",
                    "acquistionOrDisposition": "A",
                    "formType": "4",
                    "securitiesTransacted": 136268,
                    "price": 0,
                    "securityName": "Common Stock",
                    "link": "https://www.sec.gov/Archives/edgar/data/320193/..."
                }
            ],
            "keyExecutives": [
                {
                    "title": "Senior Vice President of People & Retail",
                    "name": "Ms. Deirdre  O'Brien",
                    "pay": 5019783,
                    "currencyPay": "USD",
                    "gender": "female",
                    "yearBorn": 1967,
                    "titleSince": 1676248586
                }
            ],
            "splitsHistory": [
                {
                    "date": "2020-08-31",
                    "label": "August 31, 20",
                    "numerator": 4,
                    "denominator": 1
                }
            ],
            "stockDividend": [
                {
                    "date": "2023-08-11",
                    "label": "August 11, 23",
                    "adjDividend": 0.24,
                    "dividend": 0.24,
                    "recordDate": "2023-08-14",
                    "paymentDate": "2023-08-17",
                    "declarationDate": "2023-08-03"
                }
            ],
            "stockNews": [
                {
                    "symbol": "AAPL",
                    "publishedDate": "2023-10-04 15:15:36",
                    "title": "Apple CEO Tim Cook Sells Shares Valued at About $88M",
                    "image": "https://cdn.snapi.dev/images/v1/p/w/gettyimages-...",
                    "site": "Investopedia",
                    "text": "Apple (AAPL) CEO Tim Cook made his biggest sale of ...",
                    "url": "https://www.investopedia.com/apple-ceo-tim-cook-sells-..."
                }
            ],
            "rating": [
                {
                    "symbol": "AAPL",
                    "date": "2023-10-03",
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
            ],
            "financialsAnnual": {
                "income": [
                    {
                        "date": "2022-09-24",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2022-10-28",
                        "acceptedDate": "2022-10-27 18:01:14",
                        "calendarYear": "2022",
                        "period": "FY",
                        "revenue": 394328000000,
                        "costOfRevenue": 223546000000,
                        "grossProfit": 170782000000,
                        "grossProfitRatio": 0.4330963056,
                        "researchAndDevelopmentExpenses": 26251000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 25094000000,
                        "otherExpenses": -334000000,
                        "operatingExpenses": 51345000000,
                        "costAndExpenses": 274891000000,
                        "interestIncome": 2825000000,
                        "interestExpense": 2931000000,
                        "depreciationAndAmortization": 11104000000,
                        "ebitda": 130541000000,
                        "ebitdaratio": 0.3310467428,
                        "operatingIncome": 119437000000,
                        "operatingIncomeRatio": 0.302887444,
                        "totalOtherIncomeExpensesNet": -334000000,
                        "incomeBeforeTax": 119103000000,
                        "incomeBeforeTaxRatio": 0.3020404333,
                        "incomeTaxExpense": 19300000000,
                        "netIncome": 99803000000,
                        "netIncomeRatio": 0.2530964071,
                        "eps": 6.15,
                        "epsdiluted": 6.11,
                        "weightedAverageShsOut": 16215963000,
                        "weightedAverageShsOutDil": 16325819000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2021-09-25",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2021-10-29",
                        "acceptedDate": "2021-10-28 18:04:28",
                        "calendarYear": "2021",
                        "period": "FY",
                        "revenue": 365817000000,
                        "costOfRevenue": 212981000000,
                        "grossProfit": 152836000000,
                        "grossProfitRatio": 0.4177935963,
                        "researchAndDevelopmentExpenses": 21914000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 21973000000,
                        "otherExpenses": 258000000,
                        "operatingExpenses": 43887000000,
                        "costAndExpenses": 256868000000,
                        "interestIncome": 2843000000,
                        "interestExpense": 2645000000,
                        "depreciationAndAmortization": 11284000000,
                        "ebitda": 120233000000,
                        "ebitdaratio": 0.3286697994,
                        "operatingIncome": 108949000000,
                        "operatingIncomeRatio": 0.2978237753,
                        "totalOtherIncomeExpensesNet": 258000000,
                        "incomeBeforeTax": 109207000000,
                        "incomeBeforeTaxRatio": 0.2985290459,
                        "incomeTaxExpense": 14527000000,
                        "netIncome": 94680000000,
                        "netIncomeRatio": 0.2588179336,
                        "eps": 5.67,
                        "epsdiluted": 5.61,
                        "weightedAverageShsOut": 16701272000,
                        "weightedAverageShsOutDil": 16864919000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2020-09-26",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2020-10-30",
                        "acceptedDate": "2020-10-29 18:06:25",
                        "calendarYear": "2020",
                        "period": "FY",
                        "revenue": 274515000000,
                        "costOfRevenue": 169559000000,
                        "grossProfit": 104956000000,
                        "grossProfitRatio": 0.3823324773,
                        "researchAndDevelopmentExpenses": 18752000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 19916000000,
                        "otherExpenses": 803000000,
                        "operatingExpenses": 38668000000,
                        "costAndExpenses": 208227000000,
                        "interestIncome": 3763000000,
                        "interestExpense": 2873000000,
                        "depreciationAndAmortization": 11056000000,
                        "ebitda": 77344000000,
                        "ebitdaratio": 0.2817478098,
                        "operatingIncome": 66288000000,
                        "operatingIncomeRatio": 0.2414731435,
                        "totalOtherIncomeExpensesNet": 803000000,
                        "incomeBeforeTax": 67091000000,
                        "incomeBeforeTaxRatio": 0.2443983025,
                        "incomeTaxExpense": 9680000000,
                        "netIncome": 57411000000,
                        "netIncomeRatio": 0.2091361128,
                        "eps": 3.31,
                        "epsdiluted": 3.28,
                        "weightedAverageShsOut": 17352119000,
                        "weightedAverageShsOutDil": 17528214000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...m",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/320193..."
                    },
                    {
                        "date": "2019-09-28",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2019-10-31",
                        "acceptedDate": "2019-10-30 18:12:36",
                        "calendarYear": "2019",
                        "period": "FY",
                        "revenue": 260174000000,
                        "costOfRevenue": 161782000000,
                        "grossProfit": 98392000000,
                        "grossProfitRatio": 0.3781776811,
                        "researchAndDevelopmentExpenses": 16217000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 18245000000,
                        "otherExpenses": 1807000000,
                        "operatingExpenses": 34462000000,
                        "costAndExpenses": 196244000000,
                        "interestIncome": 4961000000,
                        "interestExpense": 3576000000,
                        "depreciationAndAmortization": 12547000000,
                        "ebitda": 76477000000,
                        "ebitdaratio": 0.2939455903,
                        "operatingIncome": 63930000000,
                        "operatingIncomeRatio": 0.2457201719,
                        "totalOtherIncomeExpensesNet": 1807000000,
                        "incomeBeforeTax": 65737000000,
                        "incomeBeforeTaxRatio": 0.2526655238,
                        "incomeTaxExpense": 10481000000,
                        "netIncome": 55256000000,
                        "netIncomeRatio": 0.2123809451,
                        "eps": 2.99,
                        "epsdiluted": 2.97,
                        "weightedAverageShsOut": 18471336000,
                        "weightedAverageShsOutDil": 18595652000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2018-09-29",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2018-11-05",
                        "acceptedDate": "2018-11-05 08:01:40",
                        "calendarYear": "2018",
                        "period": "FY",
                        "revenue": 265595000000,
                        "costOfRevenue": 163756000000,
                        "grossProfit": 101839000000,
                        "grossProfitRatio": 0.3834371882,
                        "researchAndDevelopmentExpenses": 14236000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 16705000000,
                        "otherExpenses": 2005000000,
                        "operatingExpenses": 30941000000,
                        "costAndExpenses": 194697000000,
                        "interestIncome": 5686000000,
                        "interestExpense": 3240000000,
                        "depreciationAndAmortization": 10903000000,
                        "ebitda": 81801000000,
                        "ebitdaratio": 0.3079914908,
                        "operatingIncome": 70898000000,
                        "operatingIncomeRatio": 0.2669402662,
                        "totalOtherIncomeExpensesNet": 2005000000,
                        "incomeBeforeTax": 72903000000,
                        "incomeBeforeTaxRatio": 0.2744893541,
                        "incomeTaxExpense": 13372000000,
                        "netIncome": 59531000000,
                        "netIncomeRatio": 0.2241420207,
                        "eps": 3,
                        "epsdiluted": 2.98,
                        "weightedAverageShsOut": 19821508000,
                        "weightedAverageShsOutDil": 20000436000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    }
                ]
            },
            "financialsQuarter": {
                "income": [
                    {
                        "date": "2023-07-01",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2023-08-04",
                        "acceptedDate": "2023-08-03 18:04:43",
                        "calendarYear": "2023",
                        "period": "Q3",
                        "revenue": 81797000000,
                        "costOfRevenue": 45384000000,
                        "grossProfit": 36413000000,
                        "grossProfitRatio": 0.4451630255,
                        "researchAndDevelopmentExpenses": 7442000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 5973000000,
                        "otherExpenses": -265000000,
                        "operatingExpenses": 13415000000,
                        "costAndExpenses": 58799000000,
                        "interestIncome": 980000000,
                        "interestExpense": 998000000,
                        "depreciationAndAmortization": 3052000000,
                        "ebitda": 22998000000,
                        "ebitdaratio": 0.2811594557,
                        "operatingIncome": 22998000000,
                        "operatingIncomeRatio": 0.2811594557,
                        "totalOtherIncomeExpensesNet": -265000000,
                        "incomeBeforeTax": 22733000000,
                        "incomeBeforeTaxRatio": 0.2779197281,
                        "incomeTaxExpense": 2852000000,
                        "netIncome": 19881000000,
                        "netIncomeRatio": 0.2430529237,
                        "eps": 1.27,
                        "epsdiluted": 1.26,
                        "weightedAverageShsOut": 15697614000,
                        "weightedAverageShsOutDil": 15775021000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2023-04-01",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2023-05-05",
                        "acceptedDate": "2023-05-04 18:03:52",
                        "calendarYear": "2023",
                        "period": "Q2",
                        "revenue": 94836000000,
                        "costOfRevenue": 52860000000,
                        "grossProfit": 41976000000,
                        "grossProfitRatio": 0.4426167278,
                        "researchAndDevelopmentExpenses": 7457000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 6201000000,
                        "otherExpenses": 64000000,
                        "operatingExpenses": 13658000000,
                        "costAndExpenses": 66518000000,
                        "interestIncome": 918000000,
                        "interestExpense": 930000000,
                        "depreciationAndAmortization": 2898000000,
                        "ebitda": 31216000000,
                        "ebitdaratio": 0.3291577038,
                        "operatingIncome": 28318000000,
                        "operatingIncomeRatio": 0.2985996879,
                        "totalOtherIncomeExpensesNet": 64000000,
                        "incomeBeforeTax": 28382000000,
                        "incomeBeforeTaxRatio": 0.2992745371,
                        "incomeTaxExpense": 4222000000,
                        "netIncome": 24160000000,
                        "netIncomeRatio": 0.2547555781,
                        "eps": 1.53,
                        "epsdiluted": 1.52,
                        "weightedAverageShsOut": 15787154000,
                        "weightedAverageShsOutDil": 15847050000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2022-12-31",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2023-02-03",
                        "acceptedDate": "2023-02-02 18:01:30",
                        "calendarYear": "2023",
                        "period": "Q1",
                        "revenue": 117154000000,
                        "costOfRevenue": 66822000000,
                        "grossProfit": 50332000000,
                        "grossProfitRatio": 0.4296225481,
                        "researchAndDevelopmentExpenses": 7709000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 6607000000,
                        "otherExpenses": -393000000,
                        "operatingExpenses": 14316000000,
                        "costAndExpenses": 81138000000,
                        "interestIncome": 868000000,
                        "interestExpense": 1003000000,
                        "depreciationAndAmortization": 2916000000,
                        "ebitda": 38932000000,
                        "ebitdaratio": 0.332314731,
                        "operatingIncome": 36016000000,
                        "operatingIncomeRatio": 0.3074244157,
                        "totalOtherIncomeExpensesNet": -393000000,
                        "incomeBeforeTax": 35623000000,
                        "incomeBeforeTaxRatio": 0.3040698568,
                        "incomeTaxExpense": 5625000000,
                        "netIncome": 29998000000,
                        "netIncomeRatio": 0.2560561312,
                        "eps": 1.89,
                        "epsdiluted": 1.88,
                        "weightedAverageShsOut": 15892723000,
                        "weightedAverageShsOutDil": 15955718000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2022-09-24",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2022-10-28",
                        "acceptedDate": "2022-10-27 18:01:14",
                        "calendarYear": "2022",
                        "period": "Q4",
                        "revenue": 90146000000,
                        "costOfRevenue": 52051000000,
                        "grossProfit": 38095000000,
                        "grossProfitRatio": 0.4225922393,
                        "researchAndDevelopmentExpenses": 6761000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 6440000000,
                        "otherExpenses": -237000000,
                        "operatingExpenses": 13201000000,
                        "costAndExpenses": 65252000000,
                        "interestIncome": 753000000,
                        "interestExpense": 827000000,
                        "depreciationAndAmortization": 2865000000,
                        "ebitda": 27759000000,
                        "ebitdaratio": 0.3079337963,
                        "operatingIncome": 24894000000,
                        "operatingIncomeRatio": 0.2761520201,
                        "totalOtherIncomeExpensesNet": -237000000,
                        "incomeBeforeTax": 24657000000,
                        "incomeBeforeTaxRatio": 0.2735229517,
                        "incomeTaxExpense": 3936000000,
                        "netIncome": 20721000000,
                        "netIncomeRatio": 0.2298604486,
                        "eps": 1.29,
                        "epsdiluted": 1.29,
                        "weightedAverageShsOut": 16030382000,
                        "weightedAverageShsOutDil": 16118465000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    },
                    {
                        "date": "2022-06-25",
                        "symbol": "AAPL",
                        "reportedCurrency": "USD",
                        "cik": "0000320193",
                        "fillingDate": "2022-07-29",
                        "acceptedDate": "2022-07-28 18:06:56",
                        "calendarYear": "2022",
                        "period": "Q3",
                        "revenue": 82959000000,
                        "costOfRevenue": 47074000000,
                        "grossProfit": 35885000000,
                        "grossProfitRatio": 0.4325630733,
                        "researchAndDevelopmentExpenses": 6797000000,
                        "generalAndAdministrativeExpenses": 0,
                        "sellingAndMarketingExpenses": 0,
                        "sellingGeneralAndAdministrativeExpenses": 6012000000,
                        "otherExpenses": -10000000,
                        "operatingExpenses": 12809000000,
                        "costAndExpenses": 59883000000,
                        "interestIncome": 722000000,
                        "interestExpense": 719000000,
                        "depreciationAndAmortization": 2805000000,
                        "ebitda": 25881000000,
                        "ebitdaratio": 0.3119733844,
                        "operatingIncome": 23076000000,
                        "operatingIncomeRatio": 0.2781615015,
                        "totalOtherIncomeExpensesNet": -10000000,
                        "incomeBeforeTax": 23066000000,
                        "incomeBeforeTaxRatio": 0.27804096,
                        "incomeTaxExpense": 3624000000,
                        "netIncome": 19442000000,
                        "netIncomeRatio": 0.2343567304,
                        "eps": 1.2,
                        "epsdiluted": 1.2,
                        "weightedAverageShsOut": 16162945000,
                        "weightedAverageShsOutDil": 16262203000,
                        "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                        "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
                    }
                ]
            }
        }

        """
        return self.api.get(COMPANY_OUTLOOK_ENDPOINT, {"symbol": symbol})

    def get_stock_peers(self, symbol):
        """Provides a group of companies that are similar.

        Traded on the same exchange, are in the same sector,
         and have a similar market capitalization.

        Investors can use this information to compare a company to its
         competitors and to identify companies that are performing well.


        Args:
            symbol (str): Stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "peersList": [
                    "LPL",
                    "SNEJF",
                    "PCRFY",
                    "SONO",
                    "VZIO",
                    "MICS",
                    "WLDSW",
                    "KOSS",
                    "GPRO",
                    "SONY",
                    "UEIC",
                    "HEAR",
                    "VUZI",
                    "WLDS"
                ]
            }
        ]

        """
        return self.api.get(STOCK_PEERS_ENDPOINT, {"symbol": symbol})

    def get_mark_open(self):
        """Provides information on whether the markets are open or closed.

        Investors can use this information to make informed investment
         decisions and to avoid trading during market closures.

        Returns: {
            "stockExchangeName": "New York Stock Exchange",
            "stockMarketHours": {},
            "stockMarketHolidays": [],
            "isTheStockMarketOpen": true,
            "isTheEuronextMarketOpen": false,
            "isTheForexMarketOpen": true,
            "isTheCryptoMarketOpen": true
        }
        """
        return self.api.get(MARKET_OPEN_ENDPOINT)

    def get_delisted_companies(self, page: int = 0):
        """Provides a list of companies that have been delisted from the stock exchange.

        Investors can use this information to identify companies that have
         been delisted and to understand the reasons for their delisting.

        Args:
            page (int, optional): The page number of the results. Defaults to 0.

        Returns: [
            {
                "symbol": "GLCN",
                "companyName": "VanEck China Growth Leaders ETF",
                "exchange": "AMEX",
                "ipoDate": "2010-10-14",
                "delistedDate": "2023-09-21"
            }
        ]
        """
        return self.api.get(DELISTED_COMPANIES_ENDPOINT, {"page": page})

    def get_company_share_float(self, symbol):
        """Provides the total number of shares traded for a given company.

        This is also known as the company's float.
        The float is calculated by subtracting the number of restricted
         shares from the total number of outstanding shares.

        Args:
            symbol (str): Stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "freeFloat": 99.89311242764762,
                "floatShares": 15891096314,
                "outstandingShares": 15908100096,
                "source": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "date": "2022-11-01"
            }
        ]
        """
        return self.api.get(COMPANY_SHARE_FLOAT_ENDPOINT, {"symbol": symbol})

    def get_historical_share_float(self, symbol):
        """Provides historical data on the number of shares traded for a given company.

        This is also known as the company's float. The float is calculated by
         subtracting the number of restricted shares from the total
         number of outstanding shares.

        Args:
            symbol (str): Stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2024-01-31",
                "freeFloat": 99.9125,
                "floatShares": "15448370837",
                "outstandingShares": "15461900000",
                "source": null
            }
        ]
        """
        return self.api.get(HISTORICAL_SHARE_FLOAT_ENDPOINT, {"symbol": symbol})

    def get_all_shares_float(self):
        """The number of shares available for trading.

        This includes Restricted Stock Units (RSUs)

        Returns: [
            {
                "symbol": "AAPL",
                "freeFloat": 99.89311242764762,
                "floatShares": 15891096314,
                "outstandingShares": 15908100096,
                "source": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "date": "2022-11-01"
            }
        ]
        """
        return self.api.get(ALL_SHARES_FLOAT_ENDPOINT)

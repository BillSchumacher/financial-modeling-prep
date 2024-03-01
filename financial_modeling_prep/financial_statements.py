"""The financial statements.

Including balance sheet, income statement,
and cash flow statement available in annual and
quarterly format sourced from SEC filings
"""

INCOME_STATEMENT_ENDPOINT_SYMBOL = "v3/income-statement/{symbol}"
INCOME_STATEMENT_ENDPOINT_CIK = "v3/income-statement/{cik}"
BALANCE_SHEET_STATEMENTS_SYMBOL = "v3/balance-sheet-statement/{symbol}"
BALANCE_SHEET_STATEMENTS_CIK = "v3/balance-sheet-statement/{cik}"
CASHFLOW_STATEMENT_ENDPOINT_SYMBOL = "v3/cash-flow-statement/{symbol}"
CASHFLOW_STATEMENT_ENDPOINT_CIK = "v3/cash-flow-statement/{cik}"
INCOME_STATEMENT_AS_REPORTED_ENDPOINT = "v3/income-statement-as-reported/{symbol}"
BALANCE_SHEET_STATEMENT_AS_REPORTED_ENDPOINT = (
    "v3/balance-sheet-statement-as-reported/{symbol}"
)
CASHFLOW_STATEMENT_AS_REPORTED_ENDPOINT = "v3/cash-flow-statement-as-reported/{symbol}"
FULL_FINANCIAL_STATEMENTS_AS_REPORTED_ENDPOINT = (
    "v3/financial-statement-full-as-reported/{symbol}"
)
LIST_OF_DATES_AND_LINKS_ENDPOINT = "v4/financial-reports-dates"
ANNUAL_REPORTS_ON_FORM_10_K_ENDPOINT_JSON = "v4/financial-reports-json"
ANNUAL_REPORTS_ON_FORM_10_K_ENDPOINT_XLSX = "v4/financial-reports-json"


class FinancialStatements:
    """The financial statements.

    Including balance sheet, income statement
    and cash flow statement available in annual and quarterly format
    sourced from SEC filings.

    Methods:
    - get_income_statement_by_symbol(
        symbol: str, period: str = "annual,quarter",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_income_statement_by_cik(
        cik: str, period: str = "annual,quarter",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_balance_sheet_statement_by_symbol(
        symbol: str, period: str = "annual,quarter",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_balance_sheet_statement_by_cik(
        cik: str, period: str = "annual,quarter",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_cashflow_statement_by_symbol(
        symbol: str, period: str = "annual,quarter",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_cashflow_statement_by_cik(
        cik: str, period: str = "annual,quarter",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_income_statement_as_reported(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_balance_sheet_statement_as_reported(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_cashflow_statement_as_reported(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_full_financial_statements_as_reported(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_list_of_dates_and_links(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_annual_reports_on_form_10_k(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    - get_annual_reports_on_form_10_k_xlsx(
        symbol: str, period: str = "annual",
        datatype: str = "json", limit: int = 100
    ) -> dict
    """

    def __init__(self, api):
        """
        Initializes the FinancialStatements class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_income_statement_by_symbol(
        self,
        symbol: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the income statement for a company by its symbol.

        This endpoint can be used to assess a company's
        profitability and to identify potential risks.

        Args:
            symbol (str): Stock symbol
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
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
                "link": "https://www.sec.gov/Archives/edgar/data/320193...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
            }
        ]
        """
        return self.api.get(
            INCOME_STATEMENT_ENDPOINT_SYMBOL.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_income_statement_by_cik(
        self,
        cik: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the income statement for a company by its CIK.

        This endpoint can be used to assess a company's
         profitability and to identify potential risks.

        Args:
            cik (str): CIK
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
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
            }
        ]
        """
        return self.api.get(
            INCOME_STATEMENT_ENDPOINT_CIK.format(cik=cik),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_balance_sheet_statement_by_symbol(
        self,
        symbol: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the balance sheet for a company by its symbol.

        This endpoint can be used to assess a company's financial
         health and to identify potential risks.

        Args:
            symbol (str): Stock symbol
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "reportedCurrency": "USD",
                "cik": "0000320193",
                "fillingDate": "2022-10-28",
                "acceptedDate": "2022-10-27 18:01:14",
                "calendarYear": "2022",
                "period": "FY",
                "cashAndCashEquivalents": 23646000000,
                "shortTermInvestments": 24658000000,
                "cashAndShortTermInvestments": 48304000000,
                "netReceivables": 60932000000,
                "inventory": 4946000000,
                "otherCurrentAssets": 21223000000,
                "totalCurrentAssets": 135405000000,
                "propertyPlantEquipmentNet": 42117000000,
                "goodwill": 0,
                "intangibleAssets": 0,
                "goodwillAndIntangibleAssets": 0,
                "longTermInvestments": 120805000000,
                "taxAssets": 0,
                "otherNonCurrentAssets": 54428000000,
                "totalNonCurrentAssets": 217350000000,
                "otherAssets": 0,
                "totalAssets": 352755000000,
                "accountPayables": 64115000000,
                "shortTermDebt": 21110000000,
                "taxPayables": 0,
                "deferredRevenue": 7912000000,
                "otherCurrentLiabilities": 60845000000,
                "totalCurrentLiabilities": 153982000000,
                "longTermDebt": 98959000000,
                "deferredRevenueNonCurrent": 0,
                "deferredTaxLiabilitiesNonCurrent": 0,
                "otherNonCurrentLiabilities": 49142000000,
                "totalNonCurrentLiabilities": 148101000000,
                "otherLiabilities": 0,
                "capitalLeaseObligations": 0,
                "totalLiabilities": 302083000000,
                "preferredStock": 0,
                "commonStock": 64849000000,
                "retainedEarnings": -3068000000,
                "accumulatedOtherComprehensiveIncomeLoss": -11109000000,
                "othertotalStockholdersEquity": 0,
                "totalStockholdersEquity": 50672000000,
                "totalEquity": 50672000000,
                "totalLiabilitiesAndStockholdersEquity": 352755000000,
                "minorityInterest": 0,
                "totalLiabilitiesAndTotalEquity": 352755000000,
                "totalInvestments": 145463000000,
                "totalDebt": 120069000000,
                "netDebt": 96423000000,
                "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
            }
        ]
        """
        return self.api.get(
            BALANCE_SHEET_STATEMENTS_SYMBOL.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_balance_sheet_statement_by_cik(
        self,
        cik: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the balance sheet for a company by its symbol.

         This endpoint can be used to assess a company's financial
          health and to identify potential risks.

        Args:
            cik (str): cik
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "reportedCurrency": "USD",
                "cik": "0000320193",
                "fillingDate": "2022-10-28",
                "acceptedDate": "2022-10-27 18:01:14",
                "calendarYear": "2022",
                "period": "FY",
                "cashAndCashEquivalents": 23646000000,
                "shortTermInvestments": 24658000000,
                "cashAndShortTermInvestments": 48304000000,
                "netReceivables": 60932000000,
                "inventory": 4946000000,
                "otherCurrentAssets": 21223000000,
                "totalCurrentAssets": 135405000000,
                "propertyPlantEquipmentNet": 42117000000,
                "goodwill": 0,
                "intangibleAssets": 0,
                "goodwillAndIntangibleAssets": 0,
                "longTermInvestments": 120805000000,
                "taxAssets": 0,
                "otherNonCurrentAssets": 54428000000,
                "totalNonCurrentAssets": 217350000000,
                "otherAssets": 0,
                "totalAssets": 352755000000,
                "accountPayables": 64115000000,
                "shortTermDebt": 21110000000,
                "taxPayables": 0,
                "deferredRevenue": 7912000000,
                "otherCurrentLiabilities": 60845000000,
                "totalCurrentLiabilities": 153982000000,
                "longTermDebt": 98959000000,
                "deferredRevenueNonCurrent": 0,
                "deferredTaxLiabilitiesNonCurrent": 0,
                "otherNonCurrentLiabilities": 49142000000,
                "totalNonCurrentLiabilities": 148101000000,
                "otherLiabilities": 0,
                "capitalLeaseObligations": 0,
                "totalLiabilities": 302083000000,
                "preferredStock": 0,
                "commonStock": 64849000000,
                "retainedEarnings": -3068000000,
                "accumulatedOtherComprehensiveIncomeLoss": -11109000000,
                "othertotalStockholdersEquity": 0,
                "totalStockholdersEquity": 50672000000,
                "totalEquity": 50672000000,
                "totalLiabilitiesAndStockholdersEquity": 352755000000,
                "minorityInterest": 0,
                "totalLiabilitiesAndTotalEquity": 352755000000,
                "totalInvestments": 145463000000,
                "totalDebt": 120069000000,
                "netDebt": 96423000000,
                "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
            }
        ]
        """
        return self.api.get(
            BALANCE_SHEET_STATEMENTS_CIK.format(cik=cik),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_cashflow_statement_by_symbol(
        self,
        symbol: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the cash flow statement for a company by its CIK.

         This endpoint can be used to assess a company's cash flow
          generating ability and to identify potential risks.

        Args:
            symbol (str): symbol
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "reportedCurrency": "USD",
                "cik": "0000320193",
                "fillingDate": "2022-10-28",
                "acceptedDate": "2022-10-27 18:01:14",
                "calendarYear": "2022",
                "period": "FY",
                "netIncome": 99803000000,
                "depreciationAndAmortization": 11104000000,
                "deferredIncomeTax": 895000000,
                "stockBasedCompensation": 9038000000,
                "changeInWorkingCapital": 1200000000,
                "accountsReceivables": -1823000000,
                "inventory": 1484000000,
                "accountsPayables": 9448000000,
                "otherWorkingCapital": -7909000000,
                "otherNonCashItems": 111000000,
                "netCashProvidedByOperatingActivities": 122151000000,
                "investmentsInPropertyPlantAndEquipment": -10708000000,
                "acquisitionsNet": -306000000,
                "purchasesOfInvestments": -76923000000,
                "salesMaturitiesOfInvestments": 67363000000,
                "otherInvestingActivites": -1780000000,
                "netCashUsedForInvestingActivites": -22354000000,
                "debtRepayment": -9543000000,
                "commonStockIssued": 0,
                "commonStockRepurchased": -89402000000,
                "dividendsPaid": -14841000000,
                "otherFinancingActivites": 3037000000,
                "netCashUsedProvidedByFinancingActivities": -110749000000,
                "effectOfForexChangesOnCash": 0,
                "netChangeInCash": -10952000000,
                "cashAtEndOfPeriod": 24977000000,
                "cashAtBeginningOfPeriod": 35929000000,
                "operatingCashFlow": 122151000000,
                "capitalExpenditure": -10708000000,
                "freeCashFlow": 111443000000,
                "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
            }
        ]
        """
        return self.api.get(
            CASHFLOW_STATEMENT_ENDPOINT_SYMBOL.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_cashflow_statement_by_cik(
        self,
        cik: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the cash flow statement for a company by its CIK.

         This endpoint can be used to assess a company's cash flow
          generating ability and to identify potential risks.

        Args:
            cik (str): CIK
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "reportedCurrency": "USD",
                "cik": "0000320193",
                "fillingDate": "2022-10-28",
                "acceptedDate": "2022-10-27 18:01:14",
                "calendarYear": "2022",
                "period": "FY",
                "netIncome": 99803000000,
                "depreciationAndAmortization": 11104000000,
                "deferredIncomeTax": 895000000,
                "stockBasedCompensation": 9038000000,
                "changeInWorkingCapital": 1200000000,
                "accountsReceivables": -1823000000,
                "inventory": 1484000000,
                "accountsPayables": 9448000000,
                "otherWorkingCapital": -7909000000,
                "otherNonCashItems": 111000000,
                "netCashProvidedByOperatingActivities": 122151000000,
                "investmentsInPropertyPlantAndEquipment": -10708000000,
                "acquisitionsNet": -306000000,
                "purchasesOfInvestments": -76923000000,
                "salesMaturitiesOfInvestments": 67363000000,
                "otherInvestingActivites": -1780000000,
                "netCashUsedForInvestingActivites": -22354000000,
                "debtRepayment": -9543000000,
                "commonStockIssued": 0,
                "commonStockRepurchased": -89402000000,
                "dividendsPaid": -14841000000,
                "otherFinancingActivites": 3037000000,
                "netCashUsedProvidedByFinancingActivities": -110749000000,
                "effectOfForexChangesOnCash": 0,
                "netChangeInCash": -10952000000,
                "cashAtEndOfPeriod": 24977000000,
                "cashAtBeginningOfPeriod": 35929000000,
                "operatingCashFlow": 122151000000,
                "capitalExpenditure": -10708000000,
                "freeCashFlow": 111443000000,
                "link": "https://www.sec.gov/Archives/edgar/data/320193/...",
                "finalLink": "https://www.sec.gov/Archives/edgar/data/..."
            }
        ]
        """
        return self.api.get(
            CASHFLOW_STATEMENT_ENDPOINT_CIK.format(cik=cik),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_income_statement_as_reported(
        self,
        symbol: str,
        period: str = "annual",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        # pylint: disable=line-too-long
        """Get the income statement for a company as reported by the company.

         Without any adjustments.
         This endpoint can be used to assess a company's profitability
          and to identify potential risks.

        Args:
            symbol (str): Stock symbol
            period (str, optional): Period. Defaults to 'annual'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "period": "FY",
                "revenuefromcontractwithcustomerexcludingassessedtax": 316199000000,
                "costofgoodsandservicessold": 201471000000,
                "grossprofit": 170782000000,
                "researchanddevelopmentexpense": 26251000000,
                "sellinggeneralandadministrativeexpense": 25094000000,
                "operatingexpenses": 51345000000,
                "operatingincomeloss": 119437000000,
                "nonoperatingincomeexpense": -334000000,
                "incomelossfromcontinuingoperationsbeforeincometaxesextraordinaryitemsnoncontrollinginterest": 119103000000,
                "incometaxexpensebenefit": 19300000000,
                "netincomeloss": 99803000000,
                "earningspersharebasic": 6.15,
                "earningspersharediluted": 6.11,
                "weightedaveragenumberofsharesoutstandingbasic": 16215963000,
                "weightedaveragenumberofdilutedsharesoutstanding": 16325819000,
                "othercomprehensiveincomelossforeigncurrencytransactionandtranslationadjustmentnetoftax": -1511000000,
                "othercomprehensiveincomelossderivativeinstrumentgainlossbeforereclassificationaftertax": 3212000000,
                "othercomprehensiveincomelossderivativeinstrumentgainlossreclassificationaftertax": 1074000000,
                "othercomprehensiveincomelossderivativeinstrumentgainlossafterreclassificationandtax": 2138000000,
                "othercomprehensiveincomeunrealizedholdinggainlossonsecuritiesarisingduringperiodnetoftax": -12104000000,
                "othercomprehensiveincomelossreclassificationadjustmentfromaociforsaleofsecuritiesnetoftax": -205000000,
                "othercomprehensiveincomelossavailableforsalesecuritiesadjustmentnetoftax": -11899000000,
                "othercomprehensiveincomelossnetoftaxportionattributabletoparent": -11272000000,
                "comprehensiveincomenetoftax": 88531000000
            }
        ]
        """  # noqa: E501
        return self.api.get(
            INCOME_STATEMENT_AS_REPORTED_ENDPOINT.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_balance_sheet_statement_as_reported(
        self,
        symbol: str,
        period: str = "annual",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        """Get the balance sheet for a company as reported by the company.

         Without any adjustments.
         This endpoint can be used to assess a company's financial
          health and to identify potential risks.

        Args:
            symbol (str): Stock symbol
            period (str, optional): Period. Defaults to 'annual'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "period": "FY",
                "cashandcashequivalentsatcarryingvalue": 23646000000,
                "marketablesecuritiescurrent": 24658000000,
                "accountsreceivablenetcurrent": 28184000000,
                "inventorynet": 4946000000,
                "nontradereceivablescurrent": 32748000000,
                "otherassetscurrent": 21223000000,
                "assetscurrent": 135405000000,
                "marketablesecuritiesnoncurrent": 120805000000,
                "propertyplantandequipmentnet": 42117000000,
                "otherassetsnoncurrent": 54428000000,
                "assetsnoncurrent": 217350000000,
                "assets": 352755000000,
                "accountspayablecurrent": 64115000000,
                "otherliabilitiescurrent": 60845000000,
                "contractwithcustomerliabilitycurrent": 7912000000,
                "commercialpaper": 9982000000,
                "longtermdebtcurrent": 11128000000,
                "liabilitiescurrent": 153982000000,
                "longtermdebtnoncurrent": 98959000000,
                "otherliabilitiesnoncurrent": 49142000000,
                "liabilitiesnoncurrent": 148101000000,
                "liabilities": 302083000000,
                "commonstocksincludingadditionalpaidincapital": 64849000000,
                "retainedearningsaccumulateddeficit": -3068000000,
                "accumulatedothercomprehensiveincomelossnetoftax": -11109000000,
                "stockholdersequity": 50672000000,
                "liabilitiesandstockholdersequity": 352755000000,
                "commonstockparorstatedvaluepershare": 0.00001,
                "commonstocksharesauthorized": 50400000000,
                "commonstocksharesissued": 15943425000,
                "commonstocksharesoutstanding": 15943425000
            }
        ]
        """
        return self.api.get(
            BALANCE_SHEET_STATEMENT_AS_REPORTED_ENDPOINT.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_cash_flow_statement_as_reported(
        self,
        symbol: str,
        period: str = "annual",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        # pylint: disable=line-too-long
        """Get the cash flow statement for a company as reported by the company, without any adjustments. This endpoint can be used to assess a company's cash flow generating ability and to identify potential risks.

        Args:
            symbol (str): Stock symbol
            period (str, optional): Period. Defaults to 'annual'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "period": "FY",
                "cashcashequivalentsrestrictedcashandrestrictedcashequivalents": 24977000000,
                "netincomeloss": 99803000000,
                "depreciationdepletionandamortization": 11104000000,
                "sharebasedcompensation": 9038000000,
                "deferredincometaxexpensebenefit": 895000000,
                "othernoncashincomeexpense": -111000000,
                "increasedecreaseinaccountsreceivable": 1823000000,
                "increasedecreaseininventories": -1484000000,
                "increasedecreaseinotherreceivables": 7520000000,
                "increasedecreaseinotheroperatingassets": 6499000000,
                "increasedecreaseinaccountspayable": 9448000000,
                "increasedecreaseincontractwithcustomerliability": 478000000,
                "increasedecreaseinotheroperatingliabilities": 5632000000,
                "netcashprovidedbyusedinoperatingactivities": 122151000000,
                "paymentstoacquireavailableforsalesecuritiesdebt": 76923000000,
                "proceedsfrommaturitiesprepaymentsandcallsofavailableforsalesecurities": 29917000000,
                "proceedsfromsaleofavailableforsalesecuritiesdebt": 37446000000,
                "paymentstoacquirepropertyplantandequipment": 10708000000,
                "paymentstoacquirebusinessesnetofcashacquired": 306000000,
                "paymentsforproceedsfromotherinvestingactivities": 1780000000,
                "netcashprovidedbyusedininvestingactivities": -22354000000,
                "paymentsrelatedtotaxwithholdingforsharebasedcompensation": 6223000000,
                "paymentsofdividends": 14841000000,
                "paymentsforrepurchaseofcommonstock": 89402000000,
                "proceedsfromissuanceoflongtermdebt": 5465000000,
                "repaymentsoflongtermdebt": 9543000000,
                "proceedsfromrepaymentsofcommercialpaper": 3955000000,
                "proceedsfrompaymentsforotherfinancingactivities": -160000000,
                "netcashprovidedbyusedinfinancingactivities": -110749000000,
                "cashcashequivalentsrestrictedcashandrestrictedcashequivalentsperiodincreasedecreaseincludingexchangerateeffect": -10952000000,
                "incometaxespaidnet": 19573000000,
                "interestpaidnet": 2865000000
            }
        ]
        """  # noqa: E501
        return self.api.get(
            CASHFLOW_STATEMENT_AS_REPORTED_ENDPOINT.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_full_financial_statements_as_reported(
        self,
        symbol: str,
        period: str = "annual,quarter",
        datatype: str = "json",
        limit: int = 100,
    ) -> dict:
        # pylint: disable=line-too-long
        """Full Financial Statement As Reported API provides access to all three of the financial statements (income statement, balance sheet, and cash flow statement) for a company as reported by the company. This data can be used to get a complete overview of a company's financial performance and health.

        Args:
            symbol (str): Stock symbol
            period (str, optional): Period. Defaults to 'annual,quarter'.
            datatype (str, optional): Datatype. Defaults to 'json'.
            limit (int, optional): Limit. Defaults to 100.

        Returns: [
            {
                "date": "2022-09-24",
                "symbol": "AAPL",
                "period": "FY",
                "documenttype": "10-K",
                "documentannualreport": "true",
                "currentfiscalyearenddate": "--09-24",
                "documentperiodenddate": "2022-09-24",
                "documenttransitionreport": "false",
                "entityfilenumber": "001-36743",
                "entityregistrantname": "Apple Inc.",
                "entityincorporationstatecountrycode": "CA",
                "entitytaxidentificationnumber": "94-2404110",
                "entityaddressaddressline1": "One Apple Park Way",
                "entityaddresscityortown": "Cupertino",
                "entityaddressstateorprovince": "CA",
                "entityaddresspostalzipcode": 95014,
                "cityareacode": 408,
                "localphonenumber": "996-1010",
                "security12btitle": "Common Stock, $0.00001 par value per share",
                "tradingsymbol": "AAPL",
                "notradingsymbolflag": "true",
                "securityexchangename": "NASDAQ",
                "entitywellknownseasonedissuer": "Yes",
                "entityvoluntaryfilers": "No",
                "entitycurrentreportingstatus": "Yes",
                "entityinteractivedatacurrent": "Yes",
                "entityfilercategory": "Large Accelerated Filer",
                "entitysmallbusiness": "false",
                "entityemerginggrowthcompany": "false",
                "icfrauditorattestationflag": "true",
                "entityshellcompany": "false",
                "amendmentflag": "false",
                "documentfiscalyearfocus": 2022,
                "documentfiscalperiodfocus": "FY",
                "entitycentralindexkey": 320193,
                "auditorname": "Ernst & Young LLP",
                "auditorlocation": "San Jose, California",
                "auditorfirmid": 42,
                "revenuefromcontractwithcustomerexcludingassessedtax": 316199000000,
                "costofgoodsandservicessold": 201471000000,
                "grossprofit": 170782000000,
                "researchanddevelopmentexpense": 26251000000,
                "sellinggeneralandadministrativeexpense": 25094000000,
                "operatingexpenses": 51345000000,
                "operatingincomeloss": 119437000000,
                "nonoperatingincomeexpense": -334000000,
                "incomelossfromcontinuingoperationsbeforeincometaxesextraordinaryitemsnoncontrollinginterest": 119103000000,
                "incometaxexpensebenefit": 19300000000,
                "netincomeloss": 99803000000,
                "earningspersharebasic": 6.15,
                "earningspersharediluted": 6.11,
                "weightedaveragenumberofsharesoutstandingbasic": 16215963000,
                "weightedaveragenumberofdilutedsharesoutstanding": 16325819000,
                "othercomprehensiveincomelossforeigncurrencytransactionandtranslationadjustmentnetoftax": -1511000000,
                "othercomprehensiveincomelossderivativeinstrumentgainlossbeforereclassificationaftertax": 3212000000,
                "othercomprehensiveincomelossderivativeinstrumentgainlossreclassificationaftertax": 1074000000,
                "othercomprehensiveincomelossderivativeinstrumentgainlossafterreclassificationandtax": 2138000000,
                "othercomprehensiveincomeunrealizedholdinggainlossonsecuritiesarisingduringperiodnetoftax": -12104000000,
                "othercomprehensiveincomelossreclassificationadjustmentfromaociforsaleofsecuritiesnetoftax": -205000000,
                "othercomprehensiveincomelossavailableforsalesecuritiesadjustmentnetoftax": -11899000000,
                "othercomprehensiveincomelossnetoftaxportionattributabletoparent": -11272000000,
                "comprehensiveincomenetoftax": 88531000000,
                "cashandcashequivalentsatcarryingvalue": 23646000000,
                "marketablesecuritiescurrent": 24658000000,
                "accountsreceivablenetcurrent": 28184000000,
                "inventorynet": 4946000000,
                "nontradereceivablescurrent": 32748000000,
                "otherassetscurrent": 21223000000,
                "assetscurrent": 135405000000,
                "marketablesecuritiesnoncurrent": 120805000000,
                "propertyplantandequipmentnet": 42117000000,
                "otherassetsnoncurrent": 54428000000,
                "assetsnoncurrent": 217350000000,
                "assets": 352755000000,
                "accountspayablecurrent": 64115000000,
                "otherliabilitiescurrent": 60845000000,
                "contractwithcustomerliabilitycurrent": 7912000000,
                "commercialpaper": 9982000000,
                "longtermdebtcurrent": 11128000000,
                "liabilitiescurrent": 153982000000,
                "longtermdebtnoncurrent": 98959000000,
                "otherliabilitiesnoncurrent": 49142000000,
                "liabilitiesnoncurrent": 148101000000,
                "liabilities": 302083000000,
                "commonstocksincludingadditionalpaidincapital": 64849000000,
                "retainedearningsaccumulateddeficit": -3068000000,
                "accumulatedothercomprehensiveincomelossnetoftax": -11109000000,
                "stockholdersequity": 50672000000,
                "liabilitiesandstockholdersequity": 352755000000,
                "commonstockparorstatedvaluepershare": 0.00001,
                "commonstocksharesauthorized": 50400000000,
                "commonstocksharesissued": 15943425000,
                "commonstocksharesoutstanding": 15943425000,
                "stockissuedduringperiodvaluenewissues": 1175000000,
                "adjustmentsrelatedtotaxwithholdingforsharebasedcompensation": 2971000000,
                "adjustmentstoadditionalpaidincapitalsharebasedcompensationrequisiteserviceperiodrecognitionvalue": 9280000000,
                "dividends": 14793000000,
                "stockrepurchasedandretiredduringperiodvalue": 90186000000,
                "commonstockdividendspersharedeclared": 0.9,
                "cashcashequivalentsrestrictedcashandrestrictedcashequivalents": 24977000000,
                "depreciationdepletionandamortization": 11104000000,
                "sharebasedcompensation": 9038000000,
                "deferredincometaxexpensebenefit": 895000000,
                "othernoncashincomeexpense": -111000000,
                "increasedecreaseinaccountsreceivable": 1823000000,
                "increasedecreaseininventories": -1484000000,
                "increasedecreaseinotherreceivables": 7520000000,
                "increasedecreaseinotheroperatingassets": 6499000000,
                "increasedecreaseinaccountspayable": 9448000000,
                "increasedecreaseincontractwithcustomerliability": 478000000,
                "increasedecreaseinotheroperatingliabilities": 5632000000,
                "netcashprovidedbyusedinoperatingactivities": 122151000000,
                "paymentstoacquireavailableforsalesecuritiesdebt": 76923000000,
                "proceedsfrommaturitiesprepaymentsandcallsofavailableforsalesecurities": 29917000000,
                "proceedsfromsaleofavailableforsalesecuritiesdebt": 37446000000,
                "paymentstoacquirepropertyplantandequipment": 10708000000,
                "paymentstoacquirebusinessesnetofcashacquired": 306000000,
                "paymentsforproceedsfromotherinvestingactivities": 1780000000,
                "netcashprovidedbyusedininvestingactivities": -22354000000,
                "paymentsrelatedtotaxwithholdingforsharebasedcompensation": 6223000000,
                "paymentsofdividends": 14841000000,
                "paymentsforrepurchaseofcommonstock": 89402000000,
                "proceedsfromissuanceoflongtermdebt": 5465000000,
                "repaymentsoflongtermdebt": 9543000000,
                "proceedsfromrepaymentsofcommercialpaper": 3955000000,
                "proceedsfrompaymentsforotherfinancingactivities": -160000000,
                "netcashprovidedbyusedinfinancingactivities": -110749000000,
                "cashcashequivalentsrestrictedcashandrestrictedcashequivalentsperiodincreasedecreaseincludingexchangerateeffect": -10952000000,
                "incometaxespaidnet": 19573000000,
                "interestpaidnet": 2865000000,
                "performanceobligationsinarrangements": 3,
                "propertyplantandequipmentusefullife": "P1Y",
                "depreciation": 8700000000,
                "weightedaveragenumberdilutedsharesoutstandingadjustment": 109856000,
                "contractwithcustomerliabilityrevenuerecognized": 7500000000,
                "contractwithcustomerliability": 12400000000,
                "revenueremainingperformanceobligationpercentage": 0.64,
                "revenueremainingperformanceobligationexpectedtimingofsatisfactionperiod1": "P1Y",
                "cash": 18546000000,
                "equitysecuritiesfvnicost": 2929000000,
                "equitysecuritiesfvniaccumulatedgrossunrealizedlossbeforetax": 47000000,
                "equitysecuritiesfvnicurrentandnoncurrent": 2929000000,
                "availableforsaledebtsecuritiesamortizedcostbasis": 25134000000,
                "availableforsaledebtsecuritiesaccumulatedgrossunrealizedgainbeforetax": 2000000,
                "availableforsaledebtsecuritiesaccumulatedgrossunrealizedlossbeforetax": 1725000000,
                "availableforsalesecuritiesdebtsecurities": 23409000000,
                "cashcashequivalentsandmarketablesecuritiescost": 183061000000,
                "cashequivalentsandmarketablesecuritiesaccumulatedgrossunrealizedgainbeforetax": 11000000,
                "cashequivalentsandmarketablesecuritiesaccumulatedgrossunrealizedlossbeforetax": 13963000000,
                "cashcashequivalentsandmarketablesecurities": 169109000000,
                "restrictedinvestments": 12700000000,
                "availableforsalesecuritiesdebtmaturitiesrollingyeartwothroughfivefairvalue": 87031000000,
                "availableforsalesecuritiesdebtmaturitiesrollingyearsixthroughtenfairvalue": 16429000000,
                "availableforsalesecuritiesdebtmaturitiesrollingafteryeartenfairvalue": 17345000000,
                "availableforsalesecuritiesdebtmaturitiessinglematuritydate": 120805000000,
                "maximumlengthoftimeforeigncurrencycashflowhedge": "P12M",
                "fairvalueconcentrationofriskderivativefinancialinstrumentsassets": 7136000000,
                "derivativeassetsreductionformasternettingarrangementsincludingtheeffectsofcollateral": 7800000000,
                "derivativeliabilitiesreductionformasternettingarrangementsincludingtheeffectsofcollateral": 7800000000,
                "derivativefairvalueofderivativenet": 412000000,
                "numberofcustomerswithsignificantaccountsreceivablebalance": 1,
                "concentrationriskpercentage1": 0.1,
                "numberofsignificantvendors": 2,
                "derivativenotionalamount": 102670000000,
                "derivativeassetfairvaluegrossassetincludingnotsubjecttomasternettingarrangement": 4317000000,
                "derivativeliabilityfairvaluegrossliabilityincludingnotsubjecttomasternettingarrangement": 2205000000,
                "hedgedassetfairvaluehedge": 13378000000,
                "hedgedliabilityfairvaluehedge": 18739000000,
                "propertyplantandequipmentgross": 22126000000,
                "accumulateddepreciationdepletionandamortizationpropertyplantandequipment": 72340000000,
                "accruedincometaxesnoncurrent": 16657000000,
                "otheraccruedliabilitiesnoncurrent": 32485000000,
                "investmentincomeinterestanddividend": 2825000000,
                "interestexpense": 2931000000,
                "othernonoperatingincomeexpense": -228000000,
                "currentfederaltaxexpensebenefit": 7890000000,
                "deferredfederalincometaxexpensebenefit": -2265000000,
                "federalincometaxexpensebenefitcontinuingoperations": 5625000000,
                "currentstateandlocaltaxexpensebenefit": 1519000000,
                "deferredstateandlocalincometaxexpensebenefit": 84000000,
                "stateandlocalincometaxexpensebenefitcontinuingoperations": 1603000000,
                "currentforeigntaxexpensebenefit": 8996000000,
                "deferredforeignincometaxexpensebenefit": 3076000000,
                "foreignincometaxexpensebenefitcontinuingoperations": 12072000000,
                "incomelossfromcontinuingoperationsbeforeincometaxesforeign": 71300000000,
                "effectiveincometaxratereconciliationatfederalstatutoryincometaxrate": 0.21,
                "deferredtaxassetstaxcreditcarryforwardsforeign": 4400000000,
                "deferredtaxassetstaxcreditcarryforwardsresearch": 2500000000,
                "unrecognizedtaxbenefits": 16800000000,
                "unrecognizedtaxbenefitsthatwouldimpacteffectivetaxrate": 8000000000,
                "decreaseinunrecognizedtaxbenefitsisreasonablypossible": 4800000000,
                "losscontingencyestimateofpossibleloss": 12700000000,
                "incometaxreconciliationincometaxexpensebenefitatfederalstatutoryincometaxrate": 25012000000,
                "incometaxreconciliationstateandlocalincometaxes": 1518000000,
                "effectiveincometaxratereconciliationtaxcutsandjobsactof2017amount": 542000000,
                "incometaxreconciliationforeignincometaxratedifferential": -4366000000,
                "effectiveincometaxratereconciliationfdiiamount": 296000000,
                "incometaxreconciliationtaxcreditsresearch": 1153000000,
                "effectiveincometaxratereconciliationsharebasedcompensationexcesstaxbenefitamount": -1871000000,
                "incometaxreconciliationotheradjustments": -86000000,
                "effectiveincometaxratecontinuingoperations": 0.162,
                "deferredtaxassetsgoodwillandintangibleassets": 1496000000,
                "deferredtaxassetstaxdeferredexpensereservesandaccruals": 6515000000,
                "deferredtaxassetsleaseliabilities": 2400000000,
                "deferredtaxassetsdeferredincome": 5742000000,
                "deferredtaxassetsothercomprehensiveloss": 2913000000,
                "deferredtaxassetstaxcreditcarryforwards": 6962000000,
                "deferredtaxassetsother": 1596000000,
                "deferredtaxassetsgross": 27624000000,
                "deferredtaxassetsvaluationallowance": 7530000000,
                "deferredtaxassetsnet": 20094000000,
                "deferredtaxliabilitiesminimumtaxonforeignearnings": 1983000000,
                "deferredtaxliabilitiesleasingarrangements": 2163000000,
                "deferredtaxliabilitiesothercomprehensiveincome": 942000000,
                "deferredtaxliabilitiesother": 469000000,
                "deferredincometaxliabilities": 5557000000,
                "deferredtaxassetsliabilitiesnet": 14537000000,
                "unrecognizedtaxbenefitsincreasesresultingfrompriorperiodtaxpositions": 2284000000,
                "unrecognizedtaxbenefitsdecreasesresultingfrompriorperiodtaxpositions": 1982000000,
                "unrecognizedtaxbenefitsincreasesresultingfromcurrentperiodtaxpositions": 1936000000,
                "unrecognizedtaxbenefitsdecreasesresultingfromsettlementswithtaxingauthorities": 28000000,
                "unrecognizedtaxbenefitsreductionsresultingfromlapseofapplicablestatuteoflimitations": 929000000,
                "lesseeoperatingandfinanceleasetermofcontract": "P10Y",
                "operatingleasecost": 1900000000,
                "variableleasecost": 14900000000,
                "operatingleasepayments": 1800000000,
                "rightofuseassetsobtainedinexchangeforoperatingandfinanceleaseliabilities": 2800000000,
                "operatingandfinanceleaseweightedaverageremainingleaseterm": "P10Y1M6D",
                "operatingandfinanceleaseweightedaveragediscountratepercent": 0.023,
                "lesseeoperatingandfinanceleaseleasenotyetcommencedpaymentsdue": 1200000000,
                "lesseeoperatingandfinanceleaseleasenotyetcommencedtermofcontract": "P1Y",
                "operatingleaserightofuseasset": 10417000000,
                "operatingleaserightofuseassetstatementoffinancialpositionextensiblelist": "http://fasb.org/us-gaap/2022#OtherAssetsNoncurrent",
                "financeleaserightofuseasset": 952000000,
                "financeleaserightofuseassetstatementoffinancialpositionextensiblelist": "http://fasb.org/us-gaap/2022#PropertyPlantAndEquipmentNet",
                "operatingandfinanceleaserightofuseasset": 11369000000,
                "operatingleaseliabilitycurrent": 1534000000,
                "operatingleaseliabilitycurrentstatementoffinancialpositionextensiblelist": "http://fasb.org/us-gaap/2022#OtherLiabilitiesCurrent",
                "operatingleaseliabilitynoncurrent": 9936000000,
                "operatingleaseliabilitynoncurrentstatementoffinancialpositionextensiblelist": "http://fasb.org/us-gaap/2022#OtherLiabilitiesNoncurrent",
                "financeleaseliabilitycurrent": 129000000,
                "financeleaseliabilitycurrentstatementoffinancialpositionextensiblelist": "http://fasb.org/us-gaap/2022#OtherLiabilitiesCurrent",
                "financeleaseliabilitynoncurrent": 812000000,
                "financeleaseliabilitynoncurrentstatementoffinancialpositionextensiblelist": "http://fasb.org/us-gaap/2022#OtherLiabilitiesNoncurrent",
                "operatingandfinanceleaseliability": 12411000000,
                "lesseeoperatingleaseliabilitypaymentsduenexttwelvemonths": 1758000000,
                "lesseeoperatingleaseliabilitypaymentsdueyeartwo": 1742000000,
                "lesseeoperatingleaseliabilitypaymentsdueyearthree": 1677000000,
                "lesseeoperatingleaseliabilitypaymentsdueyearfour": 1382000000,
                "lesseeoperatingleaseliabilitypaymentsdueyearfive": 1143000000,
                "lesseeoperatingleaseliabilitypaymentsdueafteryearfive": 5080000000,
                "lesseeoperatingleaseliabilitypaymentsdue": 12782000000,
                "lesseeoperatingleaseliabilityundiscountedexcessamount": 1312000000,
                "operatingleaseliability": 11470000000,
                "financeleaseliabilitypaymentsduenexttwelvemonths": 155000000,
                "financeleaseliabilitypaymentsdueyeartwo": 130000000,
                "financeleaseliabilitypaymentsdueyearthree": 81000000,
                "financeleaseliabilitypaymentsdueyearfour": 48000000,
                "financeleaseliabilitypaymentsdueyearfive": 34000000,
                "financeleaseliabilitypaymentsdueafteryearfive": 906000000,
                "financeleaseliabilitypaymentsdue": 1354000000,
                "financeleaseliabilityundiscountedexcessamount": 413000000,
                "financeleaseliability": 941000000,
                "lesseeoperatingandfinanceleaseliabilitytobepaidyearone": 1913000000,
                "lesseeoperatingandfinanceleaseliabilitytobepaidyeartwo": 1872000000,
                "lesseeoperatingandfinanceleaseliabilitytobepaidyearthree": 1758000000,
                "lesseeoperatingandfinanceleaseliabilitytobepaidyearfour": 1430000000,
                "lesseeoperatingandfinanceleaseliabilitytobepaidyearfive": 1177000000,
                "lesseeoperatingandfinanceleaseliabilitytobepaidafteryearfive": 5986000000,
                "lesseeoperatingandfinanceleaseliabilitypaymentsdue": 14136000000,
                "lesseeoperatingandfinanceleaseliabilityundiscountedexcessamount": 1725000000,
                "debtinstrumentterm": "P9M",
                "shorttermdebtweightedaverageinterestrate": 0.0231,
                "interestcostsincurred": 2800000000,
                "longtermdebtfairvalue": 98800000000,
                "proceedsfromrepaymentsofshorttermdebtmaturinginthreemonthsorless": 5264000000,
                "proceedsfromshorttermdebtmaturinginmorethanthreemonths": 5948000000,
                "repaymentsofshorttermdebtmaturinginmorethanthreemonths": 7257000000,
                "proceedsfromrepaymentsofshorttermdebtmaturinginmorethanthreemonths": -1309000000,
                "debtinstrumentcarryingamount": 106324000000,
                "debtinstrumentunamortizeddiscountpremiumanddebtissuancecostsnet": 374000000,
                "hedgeaccountingadjustmentsrelatedtolongtermdebt": -1363000000,
                "debtinstrumentmaturityyearrangestart": 2022,
                "debtinstrumentmaturityyearrangeend": 2061,
                "debtinstrumentinterestratestatedpercentage": 0.0465,
                "debtinstrumentinterestrateeffectivepercentage": 0.0003,
                "longtermdebtmaturitiesrepaymentsofprincipalinnexttwelvemonths": 11139000000,
                "longtermdebtmaturitiesrepaymentsofprincipalinyeartwo": 9910000000,
                "longtermdebtmaturitiesrepaymentsofprincipalinyearthree": 10645000000,
                "longtermdebtmaturitiesrepaymentsofprincipalinyearfour": 11209000000,
                "longtermdebtmaturitiesrepaymentsofprincipalinyearfive": 9631000000,
                "longtermdebtmaturitiesrepaymentsofprincipalafteryearfive": 59290000000,
                "stockrepurchasedandretiredduringperiodshares": 569000000,
                "stockissuedduringperiodsharessharebasedpaymentarrangementnetofshareswithheldfortaxes": 85228000,
                "sharebasedcompensationarrangementbysharebasedpaymentawardawardvestingperiod1": "P4Y",
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsnumberofsharesofcommonstockissuedperunituponvesting": 1,
                "factorbywhicheachrsugrantedreducesandeachrsucanceledorsharewithheldfortaxesincreasessharesavailableforgrant": 2,
                "sharebasedcompensationarrangementbysharebasedpaymentawardpurchasepriceofcommonstockpercent": 0.85,
                "sharebasedcompensationarrangementbysharebasedpaymentawardofferingperiod": "P6M",
                "sharebasedcompensationarrangementbysharebasedpaymentawardmaximumemployeesubscriptionrate": 0.1,
                "employeestockpurchaseplanmaximumannualpurchasesperemployeeamount": 25000,
                "definedcontributionplanemployermatchingcontributionpercentofmatch": 0.5,
                "definedcontributionplanemployermatchingcontributionpercent": 0.06,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsvestedinperiodtotalfairvalue": 18200000000,
                "sharespaidfortaxwithholdingforsharebasedcompensation": 41000000,
                "employeeservicesharebasedcompensationnonvestedawardstotalcompensationcostnotyetrecognized": 16700000000,
                "employeeservicesharebasedcompensationnonvestedawardstotalcompensationcostnotyetrecognizedperiodforrecognition1": "P2Y7M6D",
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsnonvestednumber": 201501000,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsgrantsinperiod": 91674000,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsvestedinperiod": 115861000,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsforfeitedinperiod": 14739000,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsnonvestedweightedaveragegrantdatefairvalue": 109.48,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsgrantsinperiodweightedaveragegrantdatefairvalue": 150.7,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsvestedinperiodweightedaveragegrantdatefairvalue": 72.12,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsforfeituresweightedaveragegrantdatefairvalue": 99.77,
                "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsaggregateintrinsicvaluenonvested": 30312000000,
                "allocatedsharebasedcompensationexpense": 9038000000,
                "employeeservicesharebasedcompensationtaxbenefitfromcompensationexpense": 4002000000,
                "unrecordedunconditionalpurchaseobligationbalanceonfirstanniversary": 13488000000,
                "unrecordedunconditionalpurchaseobligationbalanceonsecondanniversary": 4876000000,
                "unrecordedunconditionalpurchaseobligationbalanceonthirdanniversary": 1418000000,
                "unrecordedunconditionalpurchaseobligationbalanceonfourthanniversary": 6780000000,
                "unrecordedunconditionalpurchaseobligationbalanceonfifthanniversary": 312000000,
                "unrecordedunconditionalpurchaseobligationdueafterfiveyears": 412000000,
                "unrecordedunconditionalpurchaseobligationbalancesheetamount": 27286000000,
                "othergeneralandadministrativeexpense": 7207000000,
                "noncurrentassets": 31119000000
            }
        ]
        """  # noqa: E501
        return self.api.get(
            FULL_FINANCIAL_STATEMENTS_AS_REPORTED_ENDPOINT.format(symbol=symbol),
            params={"period": period, "datatype": datatype, "limit": limit},
        )

    def get_list_of_dates_and_links(self, symbol: str) -> dict:
        # pylint: disable=line-too-long
        """Provides a list of all the dates for financial statements.

         This information can be used to identify the dates for which
          financial statements are available and to track a
           company's financial performance over time.

        Args:
            symbol (str): Stock symbol

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2022",
                "period": "FY",
                "linkXlsx": "https://fmpcloud.io/api/v4/financial-reports-xlsx?symbol=AAPL&year=2022&period=FY&apikey=YOUR_API_KEY",
                "linkJson": "https://fmpcloud.io/api/v4/financial-reports-json?symbol=AAPL&year=2022&period=FY&apikey=YOUR_API_KEY"
            }
        ]
        """  # noqa: E501
        return self.api.get(LIST_OF_DATES_AND_LINKS_ENDPOINT, params={"symbol": symbol})

    def get_annual_reports_on_form_10_k(
        self, symbol: str, year: int, period: str = "FY"
    ) -> dict:
        """Annual Reports on Form 10-K in JSON format.

        Args:
            symbol (str): Stock symbol
            year (int): Year
            period (str, optional): Period. Defaults to 'FY'.

        Returns: {
            "symbol": "AAPL",
            "period": "FY",
            "year": "2020",
            "Cover Page": [
                {
                    "Cover Page - USD ($) shares in Thousands, $ in Millions": [
                        "12 Months Ended"
                    ]
                },
                {
                    "items": [
                        "Sep. 26, 2020",
                        "Oct. 16, 2020",
                        "Mar. 27, 2020"
                    ]
                },
                {
                    "Document Type": [
                        "10-K"
                    ]
                },
                {
                    "Document Annual Report": [
                        "true"
                    ]
                },
                {
                    "Document Period End Date": [
                        "Sep. 26,2020"
                    ]
                },
                {
                    "Document Transition Report": [
                        "false"
                    ]
                },
                {
                    "Entity File Number": [
                        "001-36743"
                    ]
                },
                {
                    "Entity Registrant Name": [
                        "Apple Inc."
                    ]
                },
                {
                    "Entity Incorporation, State or Country Code": [
                        "CA"
                    ]
                },
                {
                    "Entity Tax Identification Number": [
                        "94-2404110"
                    ]
                },
                {
                    "Entity Address, Address Line One": [
                        "One Apple Park Way"
                    ]
                },
                {
                    "Entity Address, City or Town": [
                        "Cupertino"
                    ]
                },
                {
                    "Entity Address, State or Province": [
                        "CA"
                    ]
                },
                {
                    "Entity Address, Postal Zip Code": [
                        "95014"
                    ]
                },
                {
                    "City Area Code": [
                        "408"
                    ]
                },
                {
                    "Local Phone Number": [
                        "996-1010"
                    ]
                }
            ]
        }
        """
        return self.api.get(
            ANNUAL_REPORTS_ON_FORM_10_K_ENDPOINT_JSON,
            params={"symbol": symbol, "year": year, "period": period},
        )

    def get_annual_reports_on_form_10_k_xlsx(
        self, symbol: str, year: int, period: str = "FY"
    ) -> dict:
        """Annual Reports on Form 10-K in XLSX format.

        Args:
            symbol (str): Stock symbol
            year (int): Year
            period (str, optional): Period. Defaults to 'FY'.
        """
        return self.api.get(
            ANNUAL_REPORTS_ON_FORM_10_K_ENDPOINT_XLSX,
            params={"symbol": symbol, "year": year, "period": period},
        )

"""Statement Analysis module for the package."""
KEY_METRICS_ENDPOINT = "v3/key-metrics/{symbol}"
KEY_METRICS_TTM_ENDPOINT = "v3/key-metrics-ttm/{symbol}"
RATIOS_ENDPOINT = "v3/ratios/{symbol}"
RATIOS_TTM_ENDPOINT = "v3/ratios-ttm/{symbol}"
CASHFLOW_GROWTH_ENDPOINT = "v3/cash-flow-statement-growth/{symbol}"
INCOME_GROWTH_ENDPOINT = "v3/income-statement-growth/{symbol}"
BALANCE_SHEET_GROWTH_ENDPOINT = "v3/balance-sheet-statement-growth/{symbol}"
FINANCIAL_GROWTH_ENDPOINT = "v3/financial-growth/{symbol}"
FINANCIAL_SCORE_ENDPOINT = "v4/score"
OWNER_EARNINGS_ENDPOINT = "v4/owner-earnings"
ENTERPRISE_VALUES_ENDPOINT = "v4/enterprise-values/{symbol}"


class StatementAnalysis:
    """
    A class to perform analysis on financial statements.

    Explanation:
    This class provides methods to retrieve and analyze financial statement growth,
     balance sheet growth, income growth, cash flow growth, ratios, key metrics,
     financial scores, owner earnings, and enterprise values for a company.

    Methods:
    - get_financial_statement_growth: Get the financial growth rate for a company.
    - get_balance_sheet_growth: Get the balance sheet growth rate for a company.
    - get_income_growth: Get the income growth rate for a company.
    - get_cashflow_growth: Get the cash flow growth rate for a company.
    - get_ratios: Get financial ratios for a company.
    - get_ratios_ttm:
        Get financial ratios for a company for the trailing twelve months (TTM).
    - get_key_metrics: Get key financial metrics for a company.
    - get_key_metrics_ttm:
        Get key financial metrics for a company for the trailing twelve months (TTM).
    - get_financial_score: Get a financial score for a company.
    - get_owner_earnings: Get the owner earnings for a company.
    - get_enterprise_values: Get the enterprise value of a company.
    """

    def __init__(self, api):
        """
        Initializes the StatementAnalysis class with the provided API object.

        Args:
            api: The API object for interacting with the API.

        Returns:
            None
        """
        self.api = api

    def get_financial_statement_growth(self, symbol, period="annual", limit=40):
        """Get the financial growth rate for a company.

        Measure how quickly a company's overall financial performance is improving.

        Args:
            symbol (str): The company’s ticker symbol.
            period (str, optional): "annual" or "quarterly". Default is "annual".
            limit (int, optional): The number of results to return. Default is 40

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2022-09-24",
                "period": "FY",
                "revenueGrowth": 0.07793787604184606,
                "grossProfitGrowth": 0.11741997958596143,
                "ebitgrowth": 0.09626522501353844,
                "operatingIncomeGrowth": 0.09626522501353844,
                "netIncomeGrowth": 0.05410857625686523,
                "epsgrowth": 0.08465608465608473,
                "epsdilutedGrowth": 0.08912655971479501,
                "weightedAverageSharesGrowth": -0.029058205865996313,
                "weightedAverageSharesDilutedGrowth": -0.03196576277656596,
                "dividendsperShareGrowth": 0.05655348764792707,
                "operatingCashFlowGrowth": 0.17409984813241317,
                "freeCashFlowGrowth": 0.1989177326175594,
                "tenYRevenueGrowthPerShare": 3.0668993761434575,
                "fiveYRevenueGrowthPerShare": 1.213791990178702,
                "threeYRevenueGrowthPerShare": 0.7264312385752475,
                "tenYOperatingCFGrowthPerShare": 2.8770123198895177,
                "fiveYOperatingCFGrowthPerShare": 1.4717912851614252,
                "threeYOperatingCFGrowthPerShare": 1.0051619005026309,
                "tenYNetIncomeGrowthPerShare": 2.860169220093998,
                "fiveYNetIncomeGrowthPerShare": 1.6564176904593655,
                "threeYNetIncomeGrowthPerShare": 1.0574046479668893,
                "tenYShareholdersEquityGrowthPerShare": -0.30807952624500173,
                "fiveYShareholdersEquityGrowthPerShare": -0.5135153119200997,
                "threeYShareholdersEquityGrowthPerShare": -0.3621293491290547,
                "tenYDividendperShareGrowthPerShare": 8.62842256095334,
                "fiveYDividendperShareGrowthPerShare": 0.4957689252907237,
                "threeYDividendperShareGrowthPerShare": 0.19733255359833798,
                "receivablesGrowth": 0.18300780491593213,
                "inventoryGrowth": -0.24832826747720366,
                "assetGrowth": 0.004994273536902924,
                "bookValueperShareGrowth": -0.17279276744584973,
                "debtGrowth": -0.03728381401390325,
                "rdexpenseGrowth": 0.19791001186456147,
                "sgaexpensesGrowth": 0.14203795567287125
            }
        ]
        """
        return self.api.get(
            FINANCIAL_GROWTH_ENDPOINT,
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    def get_balance_sheet_growth(self, symbol, period="annual", limit=40):
        """Get the balance sheet growth rate for a company.

         Measure how quickly a company's assets and liabilities are growing.

        Args:
            symbol (str): The company’s ticker symbol.
            period (str, optional): "annual" or "quarterly". Default is "annual".
            limit (int, optional): The number of results to return. Default is 40

        Returns: [
            {
                "symbol": "AAPL",
                "date": "1986-09-30",
                "period": "FY",
                "calendarYear": 1986,
                "growthCashAndCashEquivalents": 0.7097922848664688,
                "growthShortTermInvestments": 0,
                "growthCashAndShortTermInvestments": 0.7097922848664688,
                "growthNetReceivables": 0.19482288828337874,
                "growthInventory": -0.34910179640718564,
                "growthPreferredStock": 0,
                "growthOtherCurrentAssets": -0.05107252298263534,
                "growthTotalCurrentAssets": 0.26614767059968375,
                "growthPropertyPlantEquipmentNet": 0.18694690265486727,
                "growthGoodwill": 0,
                "growthIntangibleAssets": 0,
                "growthGoodwillAndIntangibleAssets": 0,
                "growthLongTermInvestments": 0,
                "growthTaxAssets": 0,
                "growthOtherNonCurrentAssets": -0.4978902953586498,
                "growthTotalNonCurrentAssets": 0.044697633654688866,
                "growthOtherAssets": null,
                "growthTotalAssets": 0.239158299508652,
                "growthAccountPayables": 0,
                "growthShortTermDebt": 0,
                "growthTaxPayables": 0,
                "growthCapitalLeaseObligations": 0,
                "growthDeferredRevenue": 0,
                "growthOtherCurrentLiabilities": 0.11205145565335138,
                "growthTotalCurrentLiabilities": 0.11205145565335138,
                "growthLongTermDebt": 0,
                "growthDeferredRevenueNonCurrent": 0,
                "growthDeferredTaxLiabilitiesNonCurrent": 0.5227021040974529,
                "growthOtherNonCurrentLiabilities": 0,
                "growthTotalNonCurrentLiabilities": 0.5227021040974529,
                "growthOtherLiabilities": null,
                "growthTotalLiabilities": 0.20819289603318641,
                "growthCommonStock": 0,
                "growthRetainedEarnings": 0.48079925070246643,
                "growthAccumulatedOtherComprehensiveIncomeLoss": 0,
                "growthOthertotalStockholdersEquity": -0.045178105994787145,
                "growthTotalStockholdersEquity": 0.2608537693006358,
                "growthTotalLiabilitiesAndStockholdersEquity": 0.239158299508652,
                "growthTotalInvestments": 0,
                "growthTotalDebt": 0,
                "growthNetDebt": 0.7097922848664688,
                "updatedAt": "2022-09-12T18:16:18.330Z",
                "createdAt": "2022-09-12T18:16:19.091Z"
            }
        ]
        """
        return self.api.get(
            BALANCE_SHEET_GROWTH_ENDPOINT,
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    def get_income_growth(self, symbol, period="annual", limit=40):
        """Get the income growth rate for a company.

        Measure how quickly a company's income is growing.

        Args:
            symbol (str): The company’s ticker symbol.
            period (str, optional): "annual" or "quarterly". Default is "annual".
            limit (int, optional): The number of results to return. Default is 40

        Returns: [
            {
                "symbol": "AAPL",
                "date": "1986-09-30",
                "period": "FY",
                "calendarYear": 1986,
                "growthRevenue": -0.008549236302976593,
                "growthCostOfRevenue": -0.21933085501858737,
                "growthGrossProfit": 0.26071470972337646,
                "growthGrossProfitRatio": 0.2715857971830028,
                "growthResearchAndDevelopmentExpenses": 0,
                "growthGeneralAndAdministrativeExpenses": 0,
                "growthSellingGeneralAndAdministrativeExpenses": 0.12875076546233924,
                "growthSellingAndMarketingExpenses": 0,
                "growthOtherExpenses": 0.22248803827751196,
                "growthOperatingExpenses": 0.13438848920863308,
                "growthCostAndExpenses": -0.08051948051948052,
                "growthInterestExpense": 0,
                "growthInterestIncome": 0,
                "growthDepreciationAndAmortization": 0.22248803827751196,
                "growthEbitda": 1.23053152039555,
                "growthEbitdaRatio": 1.2497652955333003,
                "growthOperatingIncome": 0.856754921928038,
                "growthOperatingIncomeRatio": 0.8727656379065962,
                "growthTotalOtherIncomeExpensesNet": -2.32967032967033,
                "growthIncomeBeforeTax": 1.5816666666666668,
                "growthIncomeBeforeTaxRatio": 1.603928264717738,
                "growthIncomeTaxExpense": 1.6496598639455782,
                "growthNetIncome": 1.5163398692810457,
                "growthNetIncomeRatio": 1.538038157233204,
                "growthEps": 1.400089605734767,
                "growthEpsdiluted": 1.400089605734767,
                "growthWeightedAverageShsOut": 0.04847494550945378,
                "growthWeightedAverageShsOutDil": 0.04847494550945378,
                "updatedAt": "2022-09-12T18:16:18.330Z",
                "createdAt": "2022-09-12T18:16:19.087Z"
            }
        ]
        """
        return self.api.get(
            INCOME_GROWTH_ENDPOINT,
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    def get_cashflow_growth(self, symbol, period="annual", limit=40):
        """Get the cash flow growth rate for a company.

        Measure how quickly a company's cash flow is growing.

        Args:
            symbol (str): The company’s ticker symbol.
            period (str, optional): "annual" or "quarterly". Default is "annual".
            limit (int, optional): The number of results to return. Default is 40

        Returns: [
            {
                "symbol": "AAPL",
                "date": "1990-09-30",
                "period": "FY",
                "calendarYear": 1990,
                "growthNetIncome": 0.0460352422907489,
                "growthDepreciationAndAmortization": 0.624198717948718,
                "growthStockBasedCompensation": 0,
                "growthChangeInWorkingCapital": -2.33302752293578,
                "growthAccountsReceivables": 0,
                "growthInventory": -9.62589928057554,
                "growthAccountsPayables": 0,
                "growthOtherWorkingCapital": 0,
                "growthOtherNonCashItems": -1.0284552845528456,
                "growthNetCashProvidedByOperatingActivities": 0.9000591366055588,
                "growthInvestmentsInPropertyPlantAndEquipment": -0.06150627615062761,
                "growthAcquisitionsNet": 0,
                "growthPurchasesOfInvestments": 0.4465319386615213,
                "growthSalesMaturitiesOfInvestments": 0.48933197866395733,
                "growthNetCashUsedForInvestingActivities": 0.42272388985363435,
                "growthDebtRepayment": 0,
                "growthCommonStockIssued": 0.078125,
                "growthCommonStockRepurchased": 43.15503875968992,
                "growthDeferredIncomeTax": 0.24797843665768193,
                "growthDividendsPaid": 0.06958250497017893,
                "growthNetCashUsedProvidedByFinancingActivities": 10.85378590078329,
                "growthEffectOfForexChangesOnCash": 0,
                "growthNetChangeInCash": 0.17696025778732546,
                "growthCashAtEndOfPeriod": 0,
                "growthCashAtBeginningOfPeriod": 0.17696025778732546,
                "growthOperatingCashFlow": 0.9000591366055588,
                "growthCapitalExpenditure": -0.06150627615062761,
                "growthFreeCashFlow": 1.7566157286619455,
                "updatedAt": "2022-09-12T18:16:18.334Z",
                "createdAt": "2022-09-12T18:16:19.064Z",
                "growthOtherInvestingActivites": -3.9367469879518073,
                "growthOtherFinancingActivites": -1.9268635724331926
            }
        ]
        """
        return self.api.get(
            CASHFLOW_GROWTH_ENDPOINT,
            params={"symbol": symbol, "period": period, "limit": limit},
        )

    def get_ratios(self, symbol, period="annual", limit=140):
        """Get financial ratios for a company, such as the P/B ratio and the ROE.

        Assess a company's financial health and compare it to its competitors.

        Args:
            symbol (str): The company’s ticker symbol.
            period (str, optional): "annual" or "quarterly". Default is "annual".
            limit (int, optional): The number of results to return. Default is 140

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-07-01",
                "calendarYear": "2023",
                "period": "Q3",
                "currentRatio": 0.9815625425125837,
                "quickRatio": 0.8135848211070477,
                "cashRatio": 0.22733129006185832,
                "daysOfSalesOutstanding": 174.85836888883458,
                "daysOfInventoryOutstanding": 14.57760444209413,
                "operatingCycle": 57.69336663386155,
                "daysOfPayablesOutstanding": 92.60774722369116,
                "cashConversionCycle": -34.91438058982961,
                "grossProfitMargin": 0.44516302553883397,
                "operatingProfitMargin": 0.2811594557257601,
                "pretaxProfitMargin": 0.2779197281073878,
                "netProfitMargin": 0.24305292370135825,
                "effectiveTaxRate": 0.12545638499098227,
                "returnOnAssets": 0.059339537604689616,
                "returnOnEquity": 0.32984371370740284,
                "returnOnCapitalEmployed": 0.10947518743305962,
                "netIncomePerEBT": 0.8745436150090178,
                "ebtPerEbit": 0.9884772588920776,
                "ebitPerRevenue": 0.2811594557257601,
                "debtRatio": 0.32617195661387666,
                "debtEquityRatio": 1.8130537213392175,
                "longTermDebtToCapitalization": 0.6193501531466102,
                "totalDebtToCapitalization": 0.6445144319803721,
                "interestCoverage": 23.044088176352705,
                "cashFlowToDebtRatio": 0.24139824304538798,
                "companyEquityMultiplier": 5.558582473371603,
                "receivablesTurnover": 2.0874036645740826,
                "payablesTurnover": 0.9718409387781323,
                "inventoryTurnover": 6.173853897428922,
                "fixedAssetTurnover": 1.878231917336395,
                "assetTurnover": 0.24414245548266167,
                "operatingCashFlowPerShare": 1.6805101718006317,
                "freeCashFlowPerShare": 1.5471778067673214,
                "cashPerShare": 3.980350134740222,
                "payoutRatio": 0.19360193149237967,
                "operatingCashFlowSalesRatio": 0.3225057153685343,
                "freeCashFlowOperatingCashFlowRatio": 0.9206595905989385,
                "cashFlowCoverageRatios": 0.24139824304538798,
                "shortTermCoverageRatios": 2.3534659648496743,
                "capitalExpenditureCoverageRatio": -12.603917821309127,
                "dividendPaidAndCapexCoverageRatio": 15.022779043280183,
                "dividendPayoutRatio": 0.19360193149237964,
                "priceBookValueRatio": 50.517075149815845,
                "priceToBookRatio": 50.517075149815845,
                "priceToSalesRatio": 37.224668234531826,
                "priceEarningsRatio": 38.28864478119813,
                "priceToFreeCashFlowsRatio": 125.37020577181208,
                "priceToOperatingCashFlowsRatio": 115.4232823191812,
                "priceCashFlowRatio": 115.4232823191812,
                "priceEarningsToGrowthRatio": -2.2531394813551207,
                "priceSalesRatio": 37.224668234531826,
                "dividendYield": 0.0012640949594764,
                "enterpriseValueMultiple": 135.9134788929472,
                "priceFairValue": 50.517075149815845
            }
        ]
        """
        return self.api.get(
            RATIOS_ENDPOINT, params={"symbol": symbol, "period": period, "limit": limit}
        )

    def get_ratios_ttm(self, symbol):
        """Get financial ratios for a company.

         Such as the P/B ratio and the ROE, for the trailing twelve months (TTM).
         Get a more up-to-date view of a company's financial health.

        Args:
            symbol (str): The company’s ticker symbol.

        Returns: [
            {
                "dividendYielTTM": 0.005307735742518351,
                "dividendYielPercentageTTM": 0.530773574251835,
                "peRatioTTM": 29.337773737864076,
                "pegRatioTTM": 3.4655245227851905,
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
                "priceBookValueRatioTTM": 46.12349337027574,
                "priceToBookRatioTTM": 46.12349337027574,
                "priceToSalesRatioTTM": 7.211718556776834,
                "priceEarningsRatioTTM": 29.337773737864076,
                "priceToFreeCashFlowsRatioTTM": 27.41755612761048,
                "priceToOperatingCashFlowsRatioTTM": 24.586523979411346,
                "priceCashFlowRatioTTM": 24.586523979411346,
                "priceEarningsToGrowthRatioTTM": 3.4655245227851905,
                "priceSalesRatioTTM": 7.211718556776834,
                "enterpriseValueMultipleTTM": 23.569651715470826,
                "priceFairValueTTM": 46.12349337027574,
                "dividendPerShareTTM": 0.94
            }
        ]
        """
        return self.api.get(RATIOS_TTM_ENDPOINT, params={"symbol": symbol})

    def get_key_metrics(self, symbol):
        """Get key financial metrics for a company.

        Including revenue, net income, earnings per share (EPS),
           and price-to-earnings ratio (P/E ratio).
        Assess a company's financial performance and compare it to its competitors.

        Args:
            symbol (str): The company’s ticker symbol.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2022-09-24",
                "calendarYear": "2022",
                "period": "FY",
                "revenuePerShare": 24.31727304755197,
                "netIncomePerShare": 6.154614437637777,
                "operatingCashFlowPerShare": 7.532762624088375,
                "freeCashFlowPerShare": 6.872425646259799,
                "cashPerShare": 2.9787931805221803,
                "bookValuePerShare": 3.124822127430853,
                "tangibleBookValuePerShare": 3.124822127430853,
                "shareholdersEquityPerShare": 3.124822127430853,
                "interestDebtPerShare": 7.585118441624466,
                "marketCap": 2439367314090,
                "enterpriseValue": 2535790314090,
                "peRatio": 24.441823533260525,
                "priceToSalesRatio": 6.186137718067193,
                "pocfratio": 19.970096962693717,
                "pfcfRatio": 21.888923611981014,
                "pbRatio": 48.14034011071204,
                "ptbRatio": 48.14034011071204,
                "evToSales": 6.430662580618166,
                "enterpriseValueOverEBITDA": 19.42524045388039,
                "evToOperatingCashFlow": 20.75947240783948,
                "evToFreeCashFlow": 22.754146192134094,
                "earningsYield": 0.040913477615088595,
                "freeCashFlowYield": 0.04568520671581333,
                "debtToEquity": 2.3695334701610355,
                "debtToAssets": 0.3403750478377344,
                "netDebtToEBITDA": 0.738641499605488,
                "currentRatio": 0.8793560286267226,
                "interestCoverage": 40.74957352439441,
                "incomeQuality": 1.2239211246154926,
                "dividendYield": 0.006083954603424043,
                "payoutRatio": 0.14870294480125848,
                "salesGeneralAndAdministrativeToRevenue": 0,
                "researchAndDdevelopementToRevenue": 0.06657148363798665,
                "intangiblesToTotalAssets": 0,
                "capexToOperatingCashFlow": -0.08766199212450164,
                "capexToRevenue": -0.02715505873283155,
                "capexToDepreciation": -0.9643371757925072,
                "stockBasedCompensationToRevenue": 0.022920005680550203,
                "grahamNumber": 20.801963754945305,
                "roic": 0.5861678044404918,
                "returnOnTangibleAssets": 0.2829244092925685,
                "grahamNetNet": -12.67929632054538,
                "workingCapital": -18577000000,
                "tangibleAssetValue": 50672000000,
                "netCurrentAssetValue": -166678000000,
                "investedCapital": 2.3695334701610355,
                "averageReceivables": 56219000000,
                "averagePayables": 59439000000,
                "averageInventory": 5763000000,
                "daysSalesOutstanding": 56.400204905560855,
                "daysPayablesOutstanding": 104.6852773031054,
                "daysOfInventoryOnHand": 8.07569806661716,
                "receivablesTurnover": 6.471607693822622,
                "payablesTurnover": 3.486641191608828,
                "inventoryTurnover": 45.19733117670845,
                "roe": 1.9695887275023682,
                "capexPerShare": -0.6603369778285755
            }
        ]
        """
        return self.api.get(KEY_METRICS_ENDPOINT, params={"symbol": symbol})

    def get_key_metrics_ttm(self, symbol):
        """Get key financial metrics for a company.

         Including revenue, net income, EPS, and P/E ratio,
          for the trailing twelve months (TTM).

        Get a more up-to-date view of a company's financial performance.

        Args:
            symbol (str): The company’s ticker symbol.

        Returns: [
            {
                "revenuePerShareTTM": 24.458048210384074,
                "netIncomePerShareTTM": 6.036586197112504,
                "operatingCashFlowPerShareTTM": 7.203132909243405,
                "freeCashFlowPerShareTTM": 6.433270686869992,
                "cashPerShareTTM": 3.980350134740222,
                "bookValuePerShareTTM": 3.8396918155842026,
                "tangibleBookValuePerShareTTM": 3.8396918155842026,
                "shareholdersEquityPerShareTTM": 3.8396918155842026,
                "interestDebtPerShareTTM": 7.200966974981038,
                "marketCapTTM": 2767892759466,
                "enterpriseValueTTM": 2848764759466,
                "peRatioTTM": 29.32798343618193,
                "priceToSalesRatioTTM": 7.209311935848182,
                "pocfratioTTM": 24.578319216186145,
                "pfcfRatioTTM": 27.40840662130769,
                "pbRatioTTM": 46.10810150998109,
                "ptbRatioTTM": 46.10810150998109,
                "evToSalesTTM": 7.4199528549668825,
                "enterpriseValueOverEBITDATTM": 23.562009507183326,
                "evToOperatingCashFlowTTM": 25.194254629492715,
                "evToFreeCashFlowTTM": 28.20922256791468,
                "earningsYieldTTM": 0.03409712782251166,
                "freeCashFlowYieldTTM": 0.0364851563177914,
                "debtToEquityTTM": 1.8130537213392175,
                "debtToAssetsTTM": 0.32617195661387666,
                "netDebtToEBITDATTM": 0.6688887969893719,
                "currentRatioTTM": 0.9815625425125837,
                "interestCoverageTTM": 29.863225119744545,
                "incomeQualityTTM": 1.1932460953989026,
                "dividendYieldTTM": 0.005309507577062701,
                "dividendYieldPercentageTTM": 0.5309507577062702,
                "payoutRatioTTM": 0.15797804981004643,
                "salesGeneralAndAdministrativeToRevenueTTM": 0,
                "researchAndDevelopementToRevenueTTM": 0.07649511763771283,
                "intangiblesToTotalAssetsTTM": 0,
                "capexToOperatingCashFlowTTM": -0.10687880288665629,
                "capexToRevenueTTM": -0.03147684622056453,
                "capexToDepreciationTTM": -1.030176455545137,
                "stockBasedCompensationToRevenueTTM": 0.027312057051620986,
                "grahamNumberTTM": 22.83679462709757,
                "roicTTM": 0.5630471938175102,
                "returnOnTangibleAssetsTTM": 0.2828335890257225,
                "grahamNetNetTTM": -11.416830608779144,
                "workingCapitalTTM": -2304000000,
                "tangibleAssetValueTTM": 60274000000,
                "netCurrentAssetValueTTM": -152105000000,
                "investedCapitalTTM": 1.8130537213392175,
                "averageReceivablesTTM": 37542500000,
                "averagePayablesTTM": 44822000000,
                "averageInventoryTTM": 7416500000,
                "daysSalesOutstandingTTM": 37.25360935371536,
                "daysPayablesOutstandingTTM": 78.5066807297448,
                "daysOfInventoryOnHandTTM": 12.357922226265103,
                "receivablesTurnoverTTM": 9.79770836523248,
                "payablesTurnoverTTM": 4.649285851945438,
                "inventoryTurnoverTTM": 29.535709427288804,
                "roeTTM": 1.649211812157629,
                "capexPerShareTTM": -0.769862222373413,
                "dividendPerShareTTM": 0.94,
                "debtToMarketCapTTM": 0.03948129840878771
            }
        ]
        """
        return self.api.get(KEY_METRICS_TTM_ENDPOINT, params={"symbol": symbol})

    def get_financial_score(self, symbol):
        """Get a financial score for a company.

        Which is a measure of its overall financial health.

        Args:
            symbol (str): The company’s ticker symbol.

        Returns: [
            {
                "symbol": "AAPL",
                "altmanZScore": 8.218706082381152,
                "piotroskiScore": 8,
                "workingCapital": -2304000000,
                "totalAssets": 335038000000,
                "retainedEarnings": 1408000000,
                "ebit": 109174000000,
                "marketCap": 2747554229268,
                "totalLiabilities": 274764000000,
                "revenue": 383933000000
            }
        ]
        """
        return self.api.get(FINANCIAL_SCORE_ENDPOINT, params={"symbol": symbol})

    def get_owner_earnings(self, symbol):
        """Get the owner earnings for a company.

         Which is a measure of its profitability after accounting for all expenses,
          including taxes and debt payments.
        Assess a company's true profitability and compare it to its competitors.

        Args:
            symbol (str): The company’s ticker symbol.

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-07-01",
                "averagePPE": 0.12856,
                "maintenanceCapex": -2093000000,
                "ownersEarnings": 24287000000,
                "growthCapex": 0,
                "ownersEarningsPerShare": 1.54
            }
        ]
        """
        return self.api.get(OWNER_EARNINGS_ENDPOINT, params={"symbol": symbol})

    def get_enterprise_values(self, symbol, period="annual", limit=140):
        """Get the enterprise value of a company.

        Which is the total value of a company, including its equity and debt.
        Assess a company's overall value and compare it to its peers.

        Args:
            symbol (str): The company’s ticker symbol.
            period (str, optional): "annual" or "quarterly". Default is "annual".
            limit (int, optional): The number of results to return. Default is 140

        Returns: [
            {
                "symbol": "AAPL",
                "date": "2023-07-01",
                "stockPrice": 193.97,
                "numberOfShares": 15697614000,
                "marketCapitalization": 3044866187580,
                "minusCashAndCashEquivalents": 28408000000,
                "addTotalDebt": 109280000000,
                "enterpriseValue": 3125738187580
            }
        ]
        """
        return self.api.get(
            ENTERPRISE_VALUES_ENDPOINT,
            params={"symbol": symbol, "period": period, "limit": limit},
        )

STOCK_LIST_ENDPOINT = "v3/stock/list"
ETF_LIST_ENDPOINT = "v3/etf/list"
FINANCIAL_STATEMENT_SYMBOLS_LIST_ENDPOINT = "v3/financial-statement-symbol-lists"
TRADEABLE_SEARCH_ENDPOINT = "v3/available-traded/list"
COMMITMENT_OF_TRADERS_REPORT_ENDPOINT = "v4/commitment_of_traders_report/list"
CIK_LIST_ENDPOINT = "v3/cik_list"
EURONEXT_SYMBOLS_ENDPOINT = "v3/symbol/available-euronext"
SYMBOL_CHANGES_ENDPOINT = "v4/symbol_change"
EXCHANGE_SYMBOLS_ENDPOINT = "v3/exchange/{exchange}"
AVAILABLE_INDEXES_ENDPOINT = "v3/symbol/available-indexes"


class StockList:
    def __init__(self, api):
        self.api = api

    def stock_list(self):
        """The FMP Stock List endpoint provides a list of all stocks. The list includes the symbol, name, and exchange information for each stock.

        Returns: [
            {
                "symbol": "PWP",
                "exchange": "NASDAQ Global Select",
                "exchangeShortName": "NASDAQ",
                "price": "8.13",
                "name": "Perella Weinberg Partners"
            }
        ]
        """
        return self.api.get(STOCK_LIST_ENDPOINT)

    def etf_list(self):
        """The FMP ETF List endpoint provides a list of all ETFs. The list includes the symbol, name, and exchange information for each ETF.

        Returns: [
            {
                "symbol": "SPPR.F",
                "exchange": "Frankfurt",
                "exchangeShortName": "EURONEXT",
                "price": 26.541,
                "name": "SPDR Bloomberg SASB Euro Corporate ESG UCITS ETF"
            }
        ]
        """
        return self.api.get(ETF_LIST_ENDPOINT)

    def financial_statement_symbols_list(self):
        """The FMP Financial Statement Symbols List endpoint provides a list of all symbols for companies with financial statements available on the FMP API. The list includes the symbol, name, and exchange information for each company.

        Returns: [
            "GOGN",
            "SNCM.TA",
            "000540.SZ",
            "603931.SS",
            "JMG.L",
            "ERM.L",
            "LVCLY",
            "SBFMW",
            "JGLE.JK",
            "SMWN.DE",
            "CYBN",
            "0440.HK"
        ]
        """
        return self.api.get(FINANCIAL_STATEMENT_SYMBOLS_LIST_ENDPOINT)

    def tradeable_search(self):
        """The FMP Tradable Search endpoint provides a list of all actively traded stocks. The list includes the symbol, name, price, and exchange information for each company.

        Returns: [
            {
                "symbol": "0Y9S.L",
                "name": "Check Point Software Technologies Ltd.",
                "exchange": "London Stock Exchange",
                "exchangeShortName": "LSE",
                "price": 116.96
            }
        ]
        """
        return self.api.get(TRADEABLE_SEARCH_ENDPOINT)

    def commitment_of_traders_report(self):
        """The FMP Commitment of Traders Report endpoint provides a list of all Commitment of Traders Reports. The list includes the report's name, date, and the exchange it was released on.

        Returns: [
            {
                "trading_symbol": "NG",
                "short_name": "Natural Gas (NG)"
            }
        ]
        """
        return self.api.get(COMMITMENT_OF_TRADERS_REPORT_ENDPOINT)

    def cik_list(self):
        """The FMP CIK List endpoint provides a list of all CIK numbers for SEC-registered entities. The list includes the CIK number and the name of the entity.

        Returns: [
            {
                "cik": "0000002230",
                "name": "ADAMS DIVERSIFIED EQUITY FUND, INC."
            }
        ]
        """
        return self.api.get(CIK_LIST_ENDPOINT)

    def euronext_symbols(self):
        """The FMP Euronext Symbols endpoint provides a list of all symbols for stocks traded on Euronext exchanges. The list includes the symbol, name, price, and exchange information for each company.

        Returns: [
            {
                "symbol": "533.SI",
                "name": "ABR Holdings Limited",
                "currency": "SGD",
                "stockExchange": "SES",
                "exchangeShortName": "EURONEXT"
            }
        ]
        """
        return self.api.get(EURONEXT_SYMBOLS_ENDPOINT)

    def symbol_changes(self):
        """The FMP Symbol Changes endpoint provides a list of all symbol changes. The list includes the old symbol, new symbol, and the date of the change.

        Returns: [
            {
                "date": "2023-03-01",
                "name": "Zevra Therapeutics, Inc. Common Stock",
                "oldSymbol": "KMPH",
                "newSymbol": "ZVRA"
            }
        ]
        """
        return self.api.get(SYMBOL_CHANGES_ENDPOINT)

    def exchange_symbols(self, exchange):
        """The FMP Exchange Symbols endpoint provides a list of all symbols for a specific exchange. The list includes the symbol, name, currency, stock exchange, and exchange short name.

        Args:
            exchange: string - The exchange to search

        Returns: [
            {
                "symbol": "SRDX",
                "name": "Surmodics, Inc.",
                "price": 22.1,
                "changesPercentage": 0.7752,
                "change": 0.17,
                "dayLow": 21.76,
                "dayHigh": 22.3,
                "yearHigh": 45.85,
                "yearLow": 21.61,
                "marketCap": 312162500,
                "priceAvg50": 30.0696,
                "priceAvg200": 33.5478,
                "exchange": "NASDAQ",
                "volume": 51517,
                "avgVolume": 72111,
                "open": 21.76,
                "previousClose": 21.93,
                "eps": -2.23,
                "pe": -9.91,
                "earningsAnnouncement": "2023-04-25T12:30:00.000+0000",
                "sharesOutstanding": 14125000,
                "timestamp": 1677789927
            }
        ]
        """
        return self.api.get(
            EXCHANGE_SYMBOLS_ENDPOINT.format(exchange=exchange)
        )

    def available_indexes(self):
        """The FMP Available Indexes endpoint provides a list of all available indexes. The list includes the index's symbol, name, and exchange.

        Returns: [
            {
                "symbol": "XU100.IS",
                "name": "BIST 100",
                "currency": "TRY",
                "stockExchange": "Istanbul",
                "exchangeShortName": "INDEX"
            }
        ]
        """
        return self.api.get(AVAILABLE_INDEXES_ENDPOINT)

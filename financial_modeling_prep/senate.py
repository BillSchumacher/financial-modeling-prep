SENATE_TRADING_ENDPOINT = "v4/senate-trading"
SENATE_TRADING_RSS_FEED_ENDPOINT = "v4/senate-trading-rss-feed"
HOUSE_DISCLOSURE_ENDPOINT = "v4/senate-disclosure"
HOUSE_DISCLOSURE_RSS_FEED_ENDPOINT = "v4/senate-disclosure-rss-feed"


class Senate:
    def __init__(self, api):
        self.api = api

    def senate_trading(self, symbol):
        """Track the trading activity of US Senators and identify potential conflicts of interest with the FMP Senate Trading endpoint. This endpoint provides a list of all the trades that have been made by US Senators, including the date of the trade, the asset traded, the amount traded, and the price per share.

        Args:
            symbol (str): [description]

        Returns: [
            {
                "firstName": "Daniel S",
                "lastName": "Sullivan",
                "office": "Sullivan, Dan (Senator)",
                "link": "https://efdsearch.senate.gov/search/view/ptr/f9252211-a695-4c37-869a-0e223fce8d88/",
                "dateRecieved": "2023-09-21",
                "transactionDate": "2023-08-22",
                "owner": "Joint",
                "assetDescription": "Apple Inc",
                "assetType": "Stock",
                "type": "Sale (Full)",
                "amount": "$15,001 - $50,000",
                "comment": "Sale part of investment strategy of 3rd party investment professional to exchange individual stocks received after death of filer’s parents for EIFs.",
                "symbol": "AAPL"
            }
        ]
        """
        return self.api.get(SENATE_TRADING_ENDPOINT, symbol=symbol)

    def senate_trading_rss_feed(self, page=0):
        """Stay up-to-date on the trading activity of US Senators and identify potential conflicts of interest with the FMP Senate Trading RSS Feed. This feed provides real-time updates on all the trades that are made by US Senators, including the same information as the Senate Trading endpoint.

        Args:
            page (int, optional): [description]. Defaults to 0.

        Returns: [
            {
                "firstName": "Sheldon",
                "lastName": "Whitehouse",
                "office": "Whitehouse, Sheldon (Senator)",
                "link": "https://efdsearch.senate.gov/search/view/ptr/d798a094-353b-4186-aa90-8122dd5960d1/",
                "dateRecieved": "2023-10-02",
                "transactionDate": "2023-08-24",
                "owner": "Spouse",
                "assetDescription": "Johnson & Johnson Common Stock (Exchanged) Kenvue Inc. Common Stock (Received)",
                "assetType": "Stock",
                "type": "Exchange",
                "amount": "$1,001 - $15,000",
                "comment": "--",
                "symbol": "JNJ"
            }
        ]
        """
        return self.api.get(SENATE_TRADING_RSS_FEED_ENDPOINT, page=page)

    def house_disclosure(self, symbol):
        """Track the financial interests of House Representative and identify potential conflicts of interest with the FMP House Disclosure endpoint. This endpoint provides a list of all the financial disclosures that have been made by House Representative, including the date of the disclosure, the transaction date, the owner, the asset, the type of transaction, the amount, the representative, the district, and a link to the disclosure document.

        Args:
            symbol (str): [description]

        Returns: [
            {
                "disclosureYear": "2023",
                "disclosureDate": "2023-08-23",
                "transactionDate": "2023-08-07",
                "owner": "self",
                "ticker": "AAPL",
                "assetDescription": "Apple Inc.",
                "type": "purchase",
                "amount": "$1,001 - $15,000",
                "representative": "Michael Patrick Guest",
                "district": "MS03",
                "link": "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2023/20023442.pdf",
                "capitalGainsOver200USD": "False"
            }
        ]
        """
        return self.api.get(HOUSE_DISCLOSURE_ENDPOINT, symbol=symbol)

    def house_disclosure_rss_feed(self, page=0):
        """Stay up-to-date on the financial interests of House Representative and identify potential conflicts of interest with the FMP House Disclosure RSS Feed. This feed provides real-time updates on all the financial disclosures that are made by House Representative, including the same information as the House Disclosure endpoint.

        Args:
            page (int, optional): [description]. Defaults to 0.

        Returns: [
            {
                "disclosureYear": "2023",
                "disclosureDate": "2023-10-04",
                "transactionDate": "2023-09-13",
                "owner": "joint",
                "ticker": "EMR",
                "assetDescription": "Emerson Electric Company",
                "type": "purchase",
                "amount": "$1,001 - $15,000",
                "representative": "John Curtis",
                "district": "UT03",
                "link": "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2023/20023799.pdf",
                "capitalGainsOver200USD": "False"
            }
        ]
        """
        return self.api.get(HOUSE_DISCLOSURE_RSS_FEED_ENDPOINT, page=page)

"""WebSocket clients.

For interacting with the Company, Crypto, and Forex WebSocket servers.
"""
import json
import threading

import websocket

COMPANY_WEBSOCKET_ENDPOINT = "wss://websockets.financemodelingprep.com"
CRYPTO_WEBSOCKET_ENDPOINT = "wss://crypto.financemodelingprep.com"
FOREX_WEBSOCKET_ENDPOINT = "wss://forex.financemodelingprep.com"


class _WSClient:
    """
    A WebSocket client for interacting with a WebSocket server.

    Methods:
        connect():
            Establishes a connection to the WebSocket server
             and handles various WebSocket events.

        login():
            Sends login data to authenticate with the WebSocket server.

        start():
            Starts a new thread to connect to the WebSocket server.

        stop():
            Closes the WebSocket connection.

        subscribe(ticker):
            Subscribes to updates for a specific ticker.

        unsubscribe(ticker):
            Unsubscribes from updates for a specific ticker.
    """

    ENDPOINT = None

    def __init__(self, api_key, callback):
        """Initializes a WebSocket client.

         With the provided URL, API key, and callback function.

        Args:
            api_key (str): The API key for authentication.
            callback (function): The callback function to handle incoming messages.

        Returns:
            None
        """
        self.ws_url = self.ENDPOINT
        self.api_key = api_key
        self.callback = callback
        self.ws = None
        self.thread = None
        self.lock = threading.Lock()

    def connect(self):
        """Establishes a connection to the WebSocket server.

        Returns:
            None
        """

        def on_message(_, message):
            """Calls the callback function with the received message.

            Args:
                _: The websocket object.
                message: The message received from the websocket.

            Returns:
                None
            """
            self.callback(message)

        def on_error(_, error):
            """Prints the error message received from the websocket.

            Args:
                _: The websocket object.
                error: The error message received from the websocket.

            Returns:
                None
            """
            print(f"Error: {error}")

        def on_close(_, *__):
            """Prints a message indicating that the connection has been closed.

            Args:
                _: The websocket object.
                *__: Additional arguments passed to the function.

            Returns:
                None
            """
            print("Connection closed.")

        def on_open(_):
            """Initiates the login process when the WebSocket connection is opened.

            Args:
                _: The websocket object.

            Returns:
                None
            """
            self.login()

        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_open=on_open,
        )

        self.ws.run_forever()

    def login(self):
        """Sends login data with the API key to authenticate with the WebSocket server.

        Returns:
            None
        """
        login_data = {"event": "login", "data": {"apiKey": self.api_key}}
        self.ws.send(json.dumps(login_data))

    def start(self):
        """Starts a new thread to connect to the WebSocket server.

        Returns:
            None
        """
        with self.lock:
            self.thread = threading.Thread(target=self.connect)
            self.thread.start()

    def stop(self):
        """Closes the WebSocket connection.

        Returns:
            None
        """
        with self.lock:
            self.ws.close()

    def subscribe(self, ticker):
        """Subscribes to updates for a specific ticker.

        Args:
            ticker (str): The ticker symbol to subscribe to.

        Returns:
            None
        """
        subscribe_data = {"event": "subscribe", "data": {"ticker": ticker}}
        self.ws.send(json.dumps(subscribe_data))

    def unsubscribe(self, ticker):
        """Unsubscribes from updates for a specific ticker.

        Args:
            ticker (str): The ticker symbol to unsubscribe from.

        Returns:
            None
        """
        unsubscribe_data = {"event": "unsubscribe", "data": {"ticker": ticker}}
        self.ws.send(json.dumps(unsubscribe_data))


class CompanyWSClient(_WSClient):
    """A WebSocket client for interacting with the Company WebSocket server.

    Methods:
        connect():
            Establishes a connection to the WebSocket server
            and handles various WebSocket events.

        login():
            Sends login data to authenticate with the WebSocket server.

        start():
            Starts a new thread to connect to the WebSocket server.

        stop():
            Closes the WebSocket connection.

        subscribe(ticker):
            Subscribes to updates for a specific ticker.

        unsubscribe(ticker):
            Unsubscribes from updates for a specific ticker.

    Response:
        s: Ticker related to the asset.
        t: Timestamp
        type: Trade type
        (Communicates what type of price update this is.
         Will always be 'T' for last trade message,
        'Q' for top-of-book update message,
        and 'B' for trade break messages.)
        ap: The current lowest ask price.
          Only available for Quote updates, null otherwise.
        as: The number of shares at the ask price.
          Only available for Quote updates, null otherwise.
        bs: The number shares at the bid price.
          Only available for Quote updates, null otherwise.
        bp: The current highest bid price.
          Only available for Quote updates, null otherwise.
        lp: The last price the last trade was executed at.
          Only available for Trade and Break updates, null otherwise.
        ls: The amount of shares (volume) traded at the last price.
          Only available for Trade and Break updates, null otherwise.

    Example:
    {
        "s": "spot",
        "t": 1645216790788174600,
        "type": "Q",
        "ap": 152.46,
        "as": 200,
        "bp": 152.31,
        "bs": 100,
        "lp": 152.17,
        "ls": 100
    }
    """

    ENDPOINT = COMPANY_WEBSOCKET_ENDPOINT


class CryptoWSClient(_WSClient):
    """A WebSocket client for interacting with the Crypto WebSocket server.

    Methods:
        connect():
            Establishes a connection to the WebSocket server
             and handles various WebSocket events.

        login():
            Sends login data to authenticate with the WebSocket server.

        start():
            Starts a new thread to connect to the WebSocket server.

        stop():
            Closes the WebSocket connection.

        subscribe(ticker):
            Subscribes to updates for a specific ticker.

        unsubscribe(ticker):
            Unsubscribes from updates for a specific ticker.

    Response:
        s: Ticker related to the asset.
        t: Timestamp
        type: Trade type
        (Communicates what type of price update this is.
         Will always be 'T' for last trade message,
        'Q' for top-of-book update message,
        and 'B' for trade break messages.)
        ap: The current lowest ask price.
          Only available for Quote updates, null otherwise.
        as: The number of shares at the ask price.
          Only available for Quote updates, null otherwise.
        bs: The number shares at the bid price.
          Only available for Quote updates, null otherwise.
        bp: The current highest bid price.
          Only available for Quote updates, null otherwise.
        lp: The last price the last trade was executed at.
          Only available for Trade and Break updates, null otherwise.
        ls: The amount of shares (volume) traded at the last price.
          Only available for Trade and Break updates, null otherwise.

    Example:
    {
        "s": "btcusd",
        "t": 16487238632060000000,
        "e": "binance",
        "type": "Q",
        "bs": 0.00689248,
        "bp": 47244.8,
        "as": 1.72784126,
        "ap": 47244.9
    }
    """

    ENDPOINT = CRYPTO_WEBSOCKET_ENDPOINT


class ForexWSClient(_WSClient):
    """A WebSocket client for interacting with the Forex WebSocket server.

    Provides a Real-time feed of forex price and quote data.

    Methods:
        connect():
            Establishes a connection to the WebSocket server
            and handles various WebSocket events.

        login():
            Sends login data to authenticate with the WebSocket server.

        start():
            Starts a new thread to connect to the WebSocket server.

        stop():
            Closes the WebSocket connection.

        subscribe(ticker):
            Subscribes to updates for a specific ticker.

        unsubscribe(ticker):
            Unsubscribes from updates for a specific ticker.

    Response:
        s: Ticker related to the asset.
        t: Timestamp
        type: Trade type
        (Communicates what type of price update this is.
         Will always be 'T' for last trade message,
        'Q' for top-of-book update message,
        and 'B' for trade break messages.)
        ap: The current lowest ask price.
          Only available for Quote updates, null otherwise.
        as: The number of shares at the ask price.
          Only available for Quote updates, null otherwise.
        bs: The number shares at the bid price.
          Only available for Quote updates, null otherwise.
        bp: The current highest bid price.
          Only available for Quote updates, null otherwise.
        lp: The last price the last trade was executed at.
          Only available for Trade and Break updates, null otherwise.
        ls: The amount of shares (volume) traded at the last price.
          Only available for Trade and Break updates, null otherwise.

    Example:
    {
        "s": "eurusd",
        "t": 1701958248213,
        "type": "Q",
        "ap": 1.07865,
        "as": 1000000,
        "bp": 1.07856,
        "bs": 1000000
    }
    """

    ENDPOINT = FOREX_WEBSOCKET_ENDPOINT

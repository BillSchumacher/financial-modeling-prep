import requests


def make_api_request(endpoint):
    return requests.get(
        f"https://financialmodelingprep.com/api/{endpoint}")

import requests


def get_price_from_bybit(symbol):
    url = f"https://api.bybit.com/v5/market/tickers?category=spot&symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return data



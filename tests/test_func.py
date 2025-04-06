from get_data import get_price_from_bybit
import pytest

TICKERS = ['BTCUSDT','ETHUSDT','ATOMUSDT','ARBUSDT']
@pytest.mark.parametrize('symbol',TICKERS)
def test_response_code(symbol):
    response = get_price_from_bybit(symbol)
    assert response['retCode'] == 0
@pytest.mark.parametrize('symbol',TICKERS)
def test_tickers_bybit(symbol):
    ticker = get_price_from_bybit(symbol)
    assert ticker['result']['list'][0]['symbol'] == symbol
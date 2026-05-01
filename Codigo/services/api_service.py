import requests

def get_crypto_price():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data["bpi"]["USD"]["rate"]
    except Exception:
        return None
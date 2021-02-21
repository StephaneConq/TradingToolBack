import hmac
import time

from requests import Request, Session

from config import CONFIG

FTX_API_secret = CONFIG['FTX_API_secret']
FTX_API = CONFIG['FTX_API']


def get_price(market_name):
    return create_request(f"https://ftx.com/api/markets/{market_name}")


def list_markets():
    return create_request(f"https://ftx.com/api/markets")


def get_funding(market_name):
    return create_request(f"https://ftx.com/api/funding_rates?future={market_name}")


def create_request(url):
    s = Session()

    ts = int(time.time() * 1000)
    request = Request('GET', url)
    prepared = request.prepare()
    signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
    signature = hmac.new(FTX_API_secret.encode(), signature_payload, 'sha256').hexdigest()

    prepared.headers['FTX-KEY'] = FTX_API
    prepared.headers['FTX-SUBACCOUNT'] = CONFIG['FTX-SUBACCOUNT']
    request.headers['FTX-SIGN'] = signature
    request.headers['FTX-TS'] = str(ts)

    prepped = request.prepare()

    resp = s.send(prepped)
    return resp.json()

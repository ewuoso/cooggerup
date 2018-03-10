# py
import json
import requests

def price():
    btc_api = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    ltc_api = "https://api.coinmarketcap.com/v1/ticker/litecoin/"
    steem_api = "https://api.coinmarketcap.com/v1/ticker/steem/"
    sbd_api = "https://api.coinmarketcap.com/v1/ticker/steem-dollars/"
    ethereum = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    coins = {}
    for r_api in [btc_api,ltc_api,steem_api,sbd_api,ethereum]:
        coin_info = json.loads(requests.get(r_api).text)
        coins[coin_info[0]["symbol"]] = coin_info[0]["price_usd"]
    return coins

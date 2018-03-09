# steem
from steem import Steem
from steem.amount import Amount
steem = Steem(nodes=['https://api.steemit.com'])

# bot
from tbot.post import PostDetail
# py
import json
import requests

def price():
    btc_api = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    ltc_api = "https://api.coinmarketcap.com/v1/ticker/litecoin/"
    steem_api = "https://api.coinmarketcap.com/v1/ticker/steem/"
    sbd_api = "https://api.coinmarketcap.com/v1/ticker/steem-dollars/"
    coins = {}
    for r_api in [btc_api,ltc_api,steem_api,sbd_api]:
        coin_info = json.loads(requests.get(r_api).text)
        coins[coin_info[0]["symbol"]] = coin_info[0]["price_usd"]
    return coins

class Pending:
    def __init__(self,username):
        self.sbd_in_account = Amount(steem.get_account(username)['sbd_balance']).amount
        price_sbd = float(price()["SBD"])
        self.usd_in_account = self.sbd_in_account * price_sbd
        self.total_sbd = self.sbd_in_account
        self.posts = {}
        for ppi in PostDetail.pending_payout(username):
            money = round(ppi["payout"],6)
            title = ppi["title"]
            self.total_sbd += money
            self.posts[money] = title
        self.total_usd = self.total_sbd * price_sbd

from steem.account import Account
from steem import Steem
from steem.amount import Amount
steem = Steem(nodes=['https://api.steemit.com'])

#
from easysteem.marketcap import price
from easysteem.post import PostDetail

class EasyAccount:
    def __init__(self,username):
        self.username = username
        self.price_sbd = float(price()["SBD"])
        self.sbd_in_account = Amount(steem.get_account(username)['sbd_balance']).amount
        self.usd_in_account = self.sbd_in_account * self.price_sbd

    def total_sbd(self):
        total_sbd = self.sbd_in_account
        for pp in PostDetail.pending_payout(self.username):
            total_sbd += pp["sbd"]
        return total_sbd

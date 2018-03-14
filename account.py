from steem.amount import Amount

# settings
from settings import STEEM

#
from marketcap import price
from post import PostDetail

class EasyAccount:
    def __init__(self,username):
        self.username = username
        self.price_sbd = float(price()["SBD"])
        self.sbd_in_account = Amount(STEEM.get_account(username)['sbd_balance']).amount
        self.usd_in_account = self.sbd_in_account * self.price_sbd

    def total_sbd(self):
        total_sbd = self.sbd_in_account
        for pp in PostDetail.pending_payout(self.username):
            total_sbd += pp["sbd"]
        return total_sbd

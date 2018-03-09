# steemit
from steem import Steem
steem = Steem(nodes=['https://api.steemit.com'])

# python
import requests
import re
import json

# bot
from tbot.money import Pending,price
from tbot.transfer import Blocktrades,Koinim


class Text:
    def __init__(self):
        self.text_check_username = "Make sure you write the correct {} user is not on steemit.com"
        self.text_follow = "follower count : {},\n\nfollowing count : {},\n\nthose who do not follow you : {},\n\nyou did not follow : {}"
        self.text_sbd = "{} amount of sbd in account {}"
        self.text_price = "BTC : {} USD,\nLTC : {} USD,\nSBD : {} USD,\nSTEEM : {} USD\n"
        self.text_transfer = "Total value of BTC in your account\n- {} BTC,\nTotal value of money in your account\n- {} ₺,\nTotal value of pending payout post in your account\n- {} ₺,\nKoinim change rate\n{}"

class Tbot(Text):

    def check_username(self, username):
        if steem.lookup_account_names([username]) == [None]:
            return self.text_check_username.format(username)

    def follow(self, username):
        self.check_username(username)
        list_followers = [] # seni takip edenler
        list_following = [] # senin takip ettklerin
        d_follow = []       # seni takip etmeyenler
        d_following = []    # senin takip ettiklerin
        get_followers = steem.get_followers(username, 'abit', 'blog', 1000)
        get_following = steem.get_following(username, 'abit', 'blog', 100)
        follow_count = steem.get_follow_count(username)
        follower_count = follow_count["follower_count"]
        following_count = follow_count["following_count"]
        for i in get_followers:
            list_followers.append(i["follower"])
        for i in get_following:
            list_following.append(i["following"])
        for i in list_following:
            if i not in list_followers:
                d_follow.append(i)
        for i in list_followers:
            if i not in list_following:
                d_following.append(i)
        context = self.text_follow.format(follower_count,following_count,d_follow,d_following)
        return context

    def sbd(self, username):
        self.check_username(username)
        sbd = steem.get_account(username)['sbd_balance']
        return self.text_sbd.format(username,sbd)

    def price(self):
        coin = price()
        return self.text_price.format(coin["BTC"],coin["LTC"],coin["SBD"],coin["STEEM"])

    def payout(self, username):
        self.check_username(username)
        context = ""
        payout_info = Pending(username)
        cont = "\n {}\t:\t{}"
        money_title = payout_info.posts
        for i in money_title:
            context += cont.format("{}$".format(i),money_title[i])
        sbd_in_account = str(payout_info.sbd_in_account)
        #usd_in_account = str(payout_info.usd_in_account)
        total_sbd = str(payout_info.total_sbd)
        #total_usd = str(payout_info.total_usd)
        context += cont.format("Amount of SBD in your account ",sbd_in_account)
        #context += cont.format("amount of USD in your account ",usd_in_account+" $")
        context += cont.format("Total Payout","{}$".format(total_sbd))
        #context += cont.format("total USD from in your account","{} $".format(total_usd))
        return context

    def transfer(self, username):
        self.check_username(username)
        b = Blocktrades(username)
        k = Koinim()
        buy = k.buy()
        hmuch_btc_in_account = b.account()
        change_rate = k.change_rate()
        hmuch_try = hmuch_btc_in_account * buy
        if hmuch_try != 0:
            hmuch_try = hmuch_try - 3
        total = b.total() * buy
        return self.text_transfer.format(hmuch_btc_in_account,hmuch_try, round(total,6), change_rate)

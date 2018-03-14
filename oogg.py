from settings import STEEM, Keys, COOGGERUP_REPLY, TODAY

# python
import requests
import re
import json

# bot
from marketcap import price
from transfer import Blocktrades,Koinim
from post import PostDetail
from account import EasyAccount

#steem
from steem.steem import Commit
from steem.post import Post

class Text:
    def __init__(self):
        self.text_check_username = "Make sure you write the correct {} user is not on steemit.com"
        self.text_follow = "follower count : {},\n\nfollowing count : {},\n\nthose who do not follow you : {},\n\nyou did not follow : {}"
        self.text_sbd = "{} amount of sbd in account {}"
        self.text_price = "BTC : {} USD,\nLTC : {} USD,\nSBD : {} USD,\nSTEEM : {} USD,\nETHEREUM : {} USD\n"
        self.text_transfer = "Total value of BTC in your account\n- {} BTC,\nTotal value of money in your account\n- {} ₺,\nTotal value of pending payout post in your account\n- {} ₺,\nKoinim change rate\n{}"

class Oogg(Text):
    "cooggerup botunun ana işlemleri"

    def check_username(self, username):
        if STEEM.lookup_account_names([username]) == [None]:
            return self.text_check_username.format(username)

    def follow(self, username):
        self.check_username(username)
        follow_count = STEEM.get_follow_count(username)
        follower_count = follow_count["follower_count"]
        following_count = follow_count["following_count"]
        get_followers = STEEM.get_followers(username, 'abit', 'blog',limit = 1000)
        get_following = STEEM.get_following(username, 'abit', 'blog',limit = 100)
        list_followers = [i["follower"] for i in get_followers]
        list_following = [i["following"] for i in get_following]
        d_follow = [i for i in list_following if i not in list_followers]
        d_following = [i for i in list_followers if i not in list_following]
        context = self.text_follow.format(follower_count,following_count,d_follow,d_following)
        return context

    def sbd(self, username):
        self.check_username(username)
        sbd = STEEM.get_account(username)['sbd_balance']
        return self.text_sbd.format(username,sbd)

    def price(self):
        coin = price()
        return self.text_price.format(coin["BTC"],coin["LTC"],coin["SBD"],coin["STEEM"],coin["ETH"])

    def transfer(self, username):
        self.check_username(username)
        b = Blocktrades(username)
        k = Koinim()
        buy = k.buy()
        hmuch_btc_in_account = b.account()
        change_rate = k.change_rate()
        hmuch_try = hmuch_btc_in_account * buy
        if hmuch_try > 3:
            hmuch_try = hmuch_try - 3
        total = b.total() * buy
        return self.text_transfer.format(hmuch_btc_in_account,hmuch_try, round(total,6), change_rate)

    @staticmethod
    def upvote(url):
        post = Post(post = url, steemd_instance = STEEM)
        # title = post.permlink / post.title
        voters_list = Oogg.voters(url)
        voted = {}
        for account in Keys.accounts:
            username = account["username"]
            weight = float(account["weight"])
            if username in voters_list:
                yield {"username":username,"status":False,"note":"already voted"}
            else:
                try:
                    post.vote(weight,username)
                    yield {"username":username,"status":True, "weight":weight, "note":"voted"}
                except:
                    yield {"username":username,"status":False,"note":"Unknown"}
        if "coogger" not in Oogg.get_replies_list(post):
            Oogg.reply(title = None,body = COOGGERUP_REPLY, author = "coogger", identifier = post.identifier)

    @staticmethod
    def voters(identify):
        author,permlink = identify.split("/")[4:]
        return [i["voter"] for i in STEEM.get_active_votes(author.replace("@",""), permlink)]

    @staticmethod
    def reply(title, body, author, identifier):
        Commit(steem=STEEM).post(
        title = title,
        body = body,
        author = author,
        permlink = None,
        reply_identifier = identifier,
        json_metadata = None,
        comment_options = None,
        community = None,
        tags = None,
        beneficiaries = None,
        self_vote = False
        )

    @staticmethod
    def post(title, body, author, identifier):
        Commit(steem=STEEM).post(
        title = title,
        body = body,
        author = author,
        permlink = None,
        reply_identifier = None,
        json_metadata = None,
        comment_options = None,
        community = None,
        tags = "coogger cooggerup tr",
        beneficiaries = None,
        self_vote = True
        )

    @staticmethod
    def get_replies_list(post):
        return [str(i.author) for i in post.get_replies()]

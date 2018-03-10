from steem import Steem
from steem.account import Account
from steem.post import Post
from steem.amount import Amount
from dateutil.parser import parse
from datetime import datetime, timedelta
steem = Steem(nodes=['https://api.steemit.com'])

class PostDetail:
    
    @staticmethod
    def pending_payout(username):
        for post in steem.get_blog(username, 0, 500):
            post = Post(post["comment"])
            if post.is_main_post() and post.author == username:
                if datetime(1970, 1, 1, 0, 0) == post.last_payout:
                    payout = Amount(post.pending_payout_value).amount
                    if payout == 0:
                        payout = (Amount(post.total_payout_value).amount + Amount(post.curator_payout_value).amount)
                    yield dict(
                    title = post.title,
                    payout = round(payout,4),
                    sp = round(payout*0.15,4),
                    sbd = round(payout*0.75/2,4),
                    )
                else:
                    break

    @staticmethod
    def votes_by_rshares(url):
        author,permlink = url.split("/")[4:]
        identify = author+"/"+permlink
        reward_fund = steem.get_reward_fund()
        reward_balance = Amount(reward_fund["reward_balance"]).amount
        recent_claims = float(reward_fund["recent_claims"])
        reward_share = reward_balance / recent_claims
        base = Amount(steem.get_current_median_history_price()["base"]).amount
        post = Post(identify)
        votes = []
        for vote in post["active_votes"]:
            if len(votes) < 30:
                votes.append(vote)
            else:
                break
        for vote in sorted(votes, key = lambda x: float(x["rshares"]), reverse=True):
            yield dict(
            voter = vote["voter"],
            rshares = str(float(vote["rshares"]) * reward_share * base)[:5],
            percent = vote["percent"] / 100,
            )

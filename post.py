from steem.post import Post
from steem.amount import Amount
from datetime import datetime

# settings
from settings import STEEM

class PostDetail:

    @staticmethod
    def pending_payout(username):
        for post in STEEM.get_blog(username, 0, 500):
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
        reward_fund = STEEM.get_reward_fund()
        reward_balance = Amount(reward_fund["reward_balance"]).amount
        recent_claims = float(reward_fund["recent_claims"])
        reward_share = reward_balance / recent_claims
        base = Amount(STEEM.get_current_median_history_price()["base"]).amount
        post = Post(identify)
        votes = []
        for vote in post["active_votes"]:
            if len(votes) < 30:
                votes.append(vote)
            else:
                break
        for vote in sorted(votes, key = lambda x: float(x["rshares"]), reverse=True):
            rshares = float(vote["rshares"]) * reward_share * base
            sbd_sp = PostDetail.calculate_sbd_sp(rshares)
            if rshares != 0:
                yield dict(
                voter = vote["voter"],
                rshares = round(rshares,4),
                percent = vote["percent"] / 100,
                sp = sbd_sp["sp"],
                sbd = sbd_sp["sbd"],
                )

    @staticmethod
    def calculate_sbd_sp(payout):
        return dict(
        sp = round(payout * 0.15,4),
        sbd = round(payout * 0.75/2,4),
        )

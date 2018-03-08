from steem import Steem
from steem.post import Post

# cooggerup keys
from up.keys import Keys

class Upvote(Keys):

    def __init__(self):
        self.s = Steem(keys = self.keys_list)

    def upvote(self, weight, identify):
        post = Post(post = identify, steemd_instance = self.s)
        voters_list = self.voters(identify)
        voted = {}
        for username in self.keys_username:
            try:
                post.vote(weight,username)
                voted[username] = {"status":True, "weight":weight, "not":"voted"}
            except:
                if username in voters_list:
                    voted[username] = {"status":False, "weight":weight, "not":"already voted"}
                else:
                    voted[username] = {"status":False, "weight":weight ,"not":"Unknown"}
        return voted

    def voters(self, identify):
        author,permlink = identify.split("/")[4:]
        return [i["voter"] for i in self.s.get_active_votes(author.replace("@",""), permlink)]

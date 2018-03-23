# steemit
from steem.post import Post

# settings
from settings import STEEM,UP_PERMISSION,COOGGERUP_REPLY
up_permission_ids = [i["discord_id"] for i in UP_PERMISSION]

#python
import asyncio
import re

from oogg import Oogg,EasyFollow,EasyAccount,PostDetail
oogg = Oogg()

class MainInit:
    def __init__(self, message, client):
        self.message = message
        self.client = client
        self.mschannel = message.channel
        self.mscontent = message.content.lower()
        self.mscs = self.mscontent.replace("$","").split()
        self.sendms = client.send_message
        self.editms = client.edit_message
        self.author = str(message.author.id)

class Cooggerup(MainInit):

    async def run(self):
        if self.author in up_permission_ids:
            await self.sendms(self.mschannel, 'Postunuz oylanıyor... ')
            count = 0
            for upvote_result in oogg.upvote(url = self.mscs[1]):
                if upvote_result["status"]:
                    count += 1
                await self.sendms(self.mschannel, upvote_result)
            await self.sendms(self.mschannel, "Oylama bitti {} kişi tarafından oy atıldı <@{}>".format(count,self.author))
        else:
            await self.sendms(self.mschannel, "Bu özellik sadece yetkili kişiler tarafından kullanılabilir. <@{}>".format(self.author))

class Coogger(MainInit):

    async def follow(self):
        follow_class = EasyFollow(username = self.mscs[1])
        follower_count = follow_class.get_follower_count()
        following_count = follow_class.get_following_count()
        not_follow_you = follow_class.not_follow_you()
        not_follow = follow_class.not_follow()
        context = "\nfollower_count : {}\nfollowing_count : {}\nnot_follow_you : {}\nnot_follow : {}\n".format(follower_count,following_count,not_follow_you,not_follow)
        try:
            await self.sendms(self.mschannel,str(context)+" <@{}>".format(self.author))
        except:
            context = "Fazla karakterden dolayı sonuç gösteremiyorum http://www.coogger.com/apps/steemitapp/search/?username={} bu adresi kullanarak sonuçları görüntüleyebilirsiniz.".format(self.mscs[1])
            await self.sendms(self.mschannel,str(context)+" <@{}>".format(self.author))
    async def post(self):
        count_rshares = 0.0
        for votes_result in PostDetail.votes_by_rshares(url = self.mscs[1]):
            count_rshares += float(votes_result["rshares"])
            votes_result = "{} -- {}% -- ${} -- ${}.SP -- ${}.SBD".format(
            votes_result["voter"],
            votes_result["percent"],
            votes_result["rshares"],
            votes_result["sp"],
            votes_result["sbd"]
            )
            await self.sendms(self.mschannel, votes_result)
        await self.sendms(self.mschannel, "**---- Total ----**")
        sbd_sp = PostDetail.calculate_sbd_sp(float(count_rshares))
        await self.sendms(self.mschannel, "**${}  --  ${}.SP  --  ${}.SBD**".format(round(count_rshares,4), sbd_sp["sp"],sbd_sp["sbd"]))
        await self.sendms(self.mschannel, "sonuçlar bitti <@{}>".format(self.author))

    async def sbd(self):
        context = oogg.sbd(username = self.mscs[1])
        await self.sendms(self.mschannel,str(context)+" <@{}>".format(self.author))

    async def price(self):
        context = oogg.price()
        await self.sendms(self.mschannel,str(context)+" <@{}>".format(self.author))

    async def payout(self):
        ea = EasyAccount(self.mscs[1])
        sbd_in_account = ea.sbd_in_account
        total_sbd = sbd_in_account
        for pp in PostDetail.pending_payout(self.mscs[1]):
            await self.sendms(self.mschannel, pp)
            total_sbd += pp["sbd"]
        context = dict(
        sbd_in_account = round(sbd_in_account,4),
        total_sbd = round(total_sbd,4),
        usd_in_account = round(ea.usd_in_account,4),
        total_usd = round(total_sbd * ea.price_sbd,4),
        )
        await self.sendms(self.mschannel, context)
        await self.sendms(self.mschannel, "sonuçlar bitti <@{}>".format(self.author))

    async def transfer(self):
        context = oogg.transfer(username = self.mscs[1])
        await self.sendms(self.mschannel,str(context)+" <@{}>".format(self.author))

    async def calculate(self):
        sbd_sp = PostDetail.calculate_sbd_sp(float(self.mscs[1]))
        await self.sendms(self.mschannel, "sonuçlar bitti <@{}> ${}.sbd   ${}.sp".format(self.author,sbd_sp["sbd"],sbd_sp["sp"]))


class Follow(MainInit):

    ms_is = False
    ms = """\nMerhaba <@{}> bu kanal sadece steemit profil adresinizi paylaşabileceğiniz
    \nbir kanaldır örneğin:https://steemit.com/@coogger bu yüzden başka bir şey paylaşmaya çalışmayın, paylaşılan hesapları takip edin
    \nbaşkalarıda sizi takip etsin bu kadar kolay."""

    async def run(self):
        re_find = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.mscontent)
        if re_find == []:
            self.ms_is = True
        for must_be_user_url in re_find:
            if must_be_user_url.startswith("https://steemit.com/@"):
                username = must_be_user_url.split("@")[1]
                if STEEM.lookup_account_names([username]) == [None]:
                    self.ms_is = True
                    break
                else:
                    self.ms_is = False
                    break
            else:
                self.ms_is = True
                break
        if self.ms_is:
            await self.client.delete_message(self.message)
            await self.sendms(self.mschannel, self.ms.format(self.author))

class PostShare(MainInit):

    ms_is = False
    ms = """\nMerhaba <@{}> bu kanal sadece {} etiketi bulunan postların
    \npaylaşılması ve yardımlaşması içindir, lütfen sevdiğiniz gönderi varsa
    \nupvote atarak arkadaşlarınızı destekleyin onlarda sizi desteklesin
    \nbakın bu kadar basit.
    """

    async def run(self,tag):
        re_find = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.mscontent)
        if re_find == []:
            self.ms_is = True
        for must_be_steemit_url in re_find:
            if must_be_steemit_url.startswith("https://steemit.com/"):
                try:
                    author,permlink = must_be_steemit_url.split("/")[4:]
                    identify = author+"/"+permlink
                    if tag not in Post(post = identify, steemd_instance = STEEM).tags:
                        self.ms_is = True
                        break
                except:
                    self.ms_is = True
                    break
            else:
                self.ms_is = True
                break
        if self.ms_is:
            await self.client.delete_message(self.message)
            await self.sendms(self.mschannel, self.ms.format(self.author,tag))

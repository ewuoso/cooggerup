# steemit
from steem.post import Post

# settings
from settings import STEEM,UP_PERMISSION,COOGGERUP_REPLY
up_permission_ids = [i["discord_id"] for i in UP_PERMISSION]

#python
import asyncio
import re

# first my bot telegram bot
from post import PostDetail
from account import EasyAccount
from oogg import Oogg
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

    async def cooggerup(self):
        if self.author in up_permission_ids:
            await self.sendms(self.mschannel, 'Postunuz oylanıyor... ')
            count = 0
            for upvote_result in oogg.upvote(identify = self.mscs[1]):
                if upvote_result["status"]:
                    count += 1
                await self.sendms(self.mschannel, upvote_result)
            await self.sendms(self.mschannel, "Oylama bitti {} kişi tarafından oy atıldı <@{}>".format(count,self.author))
        else:
            await self.sendms(self.mschannel, "Bu özellik sadece yetkili kişiler tarafından kullanılabilir. <@{}>".format(self.author))

    async def follow(self):
        tmp = await self.sendms(self.mschannel, 'Takip bilgileriniz hazırlanıyor... ')
        context = oogg.follow(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def post(self):
        await self.sendms(self.mschannel, 'Post bilgileriniz hazırlanıyor... ')
        count_rshares = 0.0
        for votes_result in PostDetail.votes_by_rshares(url = self.mscs[1]):
            count_rshares += float(votes_result["rshares"])
            votes_result = "{}  --  {}%  --  ${}  --  ${}.SP  --  ${}.SBD".format(
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
        tmp = await self.sendms(self.mschannel, 'Hesabınızdaki toplam sbd miktarı.. ')
        context = oogg.sbd(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def price(self):
        tmp = await self.sendms(self.mschannel, 'coinlerin dolar cinsinden değeri.. ')
        context = oogg.price()
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def payout(self):
        tmp = await self.sendms(self.mschannel, 'Ödeme bekleyen gönderi bilgileri... ')
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
        tmp = await self.sendms(self.mschannel, 'Blocktrades ve koinim transfer bilgileriniz... ')
        context = oogg.transfer(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def calculate(self):
        tmp = await self.sendms(self.mschannel, 'Girdiğiniz değerin sbd ve steem powerı hesaplanıyor... ')
        sbd_sp = PostDetail.calculate_sbd_sp(float(self.mscs[1]))
        await self.sendms(self.mschannel, "sonuçlar bitti <@{}> ${}.sbd   ${}.sp".format(self.author,sbd_sp["sbd"],sbd_sp["sp"]))

class Coogger(MainInit):

    ms_is = False
    ms = """\nMerhaba <@{}> bu kanal sadece coogger etiketi bulunan postların
    \npaylaşılması ve yardımlaşması içindir ayrıca ben içerik seçerken buraya arada uğrarım
    \nlütfen coogger etiketi olmayan içerik atmayın sohbet için mesaj atmış
    \niseniz lütfen <#419852543368101891> kanalını kullanın.
    """

    async def has(self):

        for must_be_steemit_url in self.mscontent.split():
            if must_be_steemit_url.startswith("https://steemit.com/"):
                try:
                    author,permlink = must_be_steemit_url.split("/")[4:]
                    identify = author+"/"+permlink
                except:
                    self.ms_is = True
                    break
                if "coogger" not in  Post(post = identify, steemd_instance = STEEM).tags:
                    await self.client.delete_message(self.message)
                    self.ms_is = True
                    break
            else:
                await self.client.delete_message(self.message)
                self.ms_is = True
                break
        if self.ms_is:
            await self.sendms(self.mschannel, self.ms.format(self.author))


class Follow(MainInit):

    ms_is = False
    ms = """\nMerhaba <@{}> bu kanal sadece steemit profil adresinizi paylaşabileceğiniz
    \nbir kanaldır örneğin:https://steemit.com/@coogger/ bu yüzden başka bir şey paylaşmaya çalışmayın, paylaşılan hesapları takip edin
    \nbaşkalarıda sizi takip etsin bu kadar kolay."""

    async def is_user(self):
        username = self.mscontent.split("@")
        if len(username) == 2:
            if STEEM.lookup_account_names([username[1]]) == [None]:
                self.ms_is = False
            else:
                self.ms_is = True
        else:
            self.ms_is = True
        if self.ms_is:
            await self.sendms(self.mschannel, self.ms.format(self.author))

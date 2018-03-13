# steemit
from steem.post import Post
from steem import Steem
steem = Steem(nodes=['https://api.steemit.com'])

import asyncio
import re


# first my bot telegram bot
from easysteem.post import PostDetail
from easysteem.account import EasyAccount
from easysteem.bot import Tbot
Tbot = Tbot()

# cooggerup bot
from up.cooggerup import Upvote
cooggerup = Upvote()

hakancelik_discord_id = "403671940507631618"
sedatcelik_discord_id = "411540871960330241"

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
        if self.author == hakancelik_discord_id or self.author == sedatcelik_discord_id:
            await self.sendms(self.mschannel, 'Postunuz oylanıyor... ')
            count = 0
            for upvote_result in cooggerup.upvote(identify = self.mscs[1]):
                if upvote_result["status"]:
                    count += 1
                await self.sendms(self.mschannel, upvote_result)
            await self.sendms(self.mschannel, "Oylama bitti {} kişi tarafından oy atıldı <@{}>".format(count,self.author))
        else:
            await self.sendms(self.mschannel, "Bu özellik sadece <@{}> ve <@{}> tarafından kullanılabilir. <@{}>".format(hakancelik_discord_id,sedatcelik_discord_id,self.author))

    async def follow(self):
        tmp = await self.sendms(self.mschannel, 'Takip bilgileriniz hazırlanıyor... ')
        context = Tbot.follow(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def post(self):
        await self.sendms(self.mschannel, 'Post bilgileriniz hazırlanıyor... ')
        count_rshares = 0.0
        for votes_result in PostDetail.votes_by_rshares(url = self.mscs[1]):
            count_rshares += float(votes_result["rshares"])
            votes_result = "{0:16}  voted for ${1} --  {2:>5}%".format(
            votes_result["voter"],
            votes_result["rshares"],
            votes_result["percent"]
            )
            await self.sendms(self.mschannel, votes_result)
        await self.sendms(self.mschannel, "---- Total ----")
        await self.sendms(self.mschannel, "${}".format(count_rshares))
        await self.sendms(self.mschannel, "sonuçlar bitti <@{}>".format(self.author))

    async def sbd(self):
        tmp = await self.sendms(self.mschannel, 'Hesabınızdaki toplam sbd miktarı.. ')
        context = Tbot.sbd(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def price(self):
        tmp = await self.sendms(self.mschannel, 'coinlerin dolar cinsinden değeri.. ')
        context = Tbot.price()
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
        usd_in_account = round(ea.usd_in_account,4),
        total_sbd = round(total_sbd,4),
        total_usd = round(total_sbd * ea.price_sbd,4),
        )
        await self.sendms(self.mschannel, context)
        await self.sendms(self.mschannel, "sonuçlar bitti <@{}>".format(self.author))

    async def transfer(self):
        tmp = await self.sendms(self.mschannel, 'Blocktrades ve koinim transfer bilgileriniz... ')
        context = Tbot.transfer(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

class Coogger(MainInit):

    async def is_has(self):
        ms_is = False
        ms = """\nMerhaba <@{}> bu kanal sadece coogger etiketi bulunan postlar için
        \nyardımlaşma ve ben içerik seçerken buraya arada uğrarım lütfen coogger etiketi olmayan
        \niçerik atmayın sohbet için mesaj atmış iseniz lütfen <#419852543368101891> kanalını
        \nkullanın."""
        for must_be_steemit_url in self.mscontent.split():
            if must_be_steemit_url.startswith("https://steemit.com/"):
                try:
                    author,permlink = must_be_steemit_url.split("/")[4:]
                    identify = author+"/"+permlink
                except:
                    ms_is = True
                    break
                if "coogger" not in  Post(post = identify, steemd_instance = steem).tags:
                    await self.client.delete_message(self.message)
                    ms_is = True
                    break
            else:
                await self.client.delete_message(self.message)
                ms_is = True
                break
        if ms_is:
            await self.sendms(self.mschannel, ms.format(self.author))


class Follow(MainInit):

    async def is_user(self):
        if re.match("https://steemit.com/@.*/$",self.mscontent):
            pass
        else:
            await self.client.delete_message(self.message)
            ms = """\nMerhaba <@{}> bu kanal sadece steemit profil adresinizi paylaşabileceğiniz
            \nbir kanaldır örneğin:https://steemit.com/@coogger/ bu yüzden başka bir şey paylaşmaya çalışmayın, paylaşılan hesapları takip edin
            \nbaşkalarıda sizi takip etsin bu kadar kolay."""
            await self.sendms(self.mschannel, ms.format(self.author))

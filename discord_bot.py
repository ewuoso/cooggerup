import asyncio
Bot_ID = "420911621846859776"

# cooggerup bot
from up.cooggerup import Upvote
cooggerup = Upvote()

# first my bot telegram bot
from tbot.bot import Tbot
from tbot.post import PostDetail
Tbot = Tbot()

# 3.
import discord
Client_ID = "TOKEN"
client = discord.Client()
discord_user = discord.User()


class DiscordBot:

    def __init__(self, message):
        self.mschannel = message.channel
        self.mscontent = message.content.lower()
        self.mscs = self.mscontent.split()
        self.sendms = client.send_message
        self.editms = client.edit_message
        self.author = str(message.author.id)

    async def cooggerup(self):
        if self.author != "403671940507631618":
            await self.sendms(self.mschannel, "Bu özellik sadece hakancelik tarafından kullanılabilir. <@{}>".format(self.author))
        if self.author == "403671940507631618":
            await self.sendms(self.mschannel, 'Postunuz oylanıyor... ')
            count = 0
            for upvote_result in cooggerup.upvote(weight = 100, identify = self.mscs[1]):
                if upvote_result["status"]:
                    count += 1
                await self.sendms(self.mschannel, upvote_result)
            await self.sendms(self.mschannel, "Oylama bitti {} kişi tarafından oy atıldı <@{}>".format(count,self.author))

    async def follow(self):
        tmp = await self.sendms(self.mschannel, 'Takip bilgileriniz hazırlanıyor... ')
        context = Tbot.follow(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def post(self):
        await self.sendms(self.mschannel, 'Post bilgileriniz hazırlanıyor... ')
        det = PostDetail.general(url = self.mscs[1])
        await self.sendms(self.mschannel, det)
        count_rshares = 0.0
        for votes_result in PostDetail.votes_by_rshares(url = self.mscs[1]):
            count_rshares += float(votes_result["rshares"])
            votes_result = "{0:16} {2:>5}% voted for ${1}".format(votes_result["voter"],votes_result["percent"],votes_result["rshares"])
            await self.sendms(self.mschannel, votes_result)
        await self.sendms(self.mschannel, "---- Total ----")
        await self.sendms(self.mschannel, "{4}".format(count_rshares))
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
        context = Tbot.payout(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def transfer(self):
        tmp = await self.sendms(self.mschannel, 'Blocktrades ve koinim transver bilgileriniz... ')
        context = Tbot.transfer(username = self.mscs[1])
        await self.editms(tmp, str(context)+" <@{}>".format(self.author))

    async def help(self):
        ms = """
        \nMerhaba <@{}> sana yapabildiğim bir kaç özellikten bahsetmeme izin ver
        \n- hesap takip bilgilerini follow steemit_kullanıcı_adın şeklinde yazarak sonuçları görebilirsin.
        \n- post bilgilerini post steemit_post_adresi şeklinde yazarak sonuçları görebilirsin.
        \n- hesabındaki toplam sbd miktarını sbd steemit_kullanıcı_adı şeklinde yazarak sonuçları görebilirsin.
        \n- bitcoin litecoin sbd ve steem gibi coinlerin dolar cinsinden değerini görmek için price yazman yeterli
        \n- ödeme bekleyen gönderi bilgisi vs için payout steemit_kullanıcı_adı şeklinde yazman yeterli.
        \n- eğer coinlerini bloctras aracılığı ile bitcoine ve koinim aracılığı ile tl ye dönültüreceksen
        \ntransfer steemit_kullanıcı_adı şeklinde yazdığında sana kesintiler ile birlikte kaç tl alacağını
        \ngösterebilirim.
        \n- cooggerup steemit_post_adresi ile upvote atılıyor fakat şuan için bu özellik sadece kurucu tarafından
        \n belirli postlara yönelik kullanılmakta.
        """
        await self.sendms(self.mschannel, ms.format(self.author))

# commands
commands = ["cooggerup","follow","post","sbd","price","payout","transfer","help"]

@client.event
async def on_message(message):
    mschannel = message.channel
    mscontent = message.content.lower()
    mscs = mscontent.split()
    author = str(message.author.id)
    discord_bot = DiscordBot(message = message)
    if str(mschannel) == "cooggerup" or str(mschannel) == "test" and author != Bot_ID:
        if mscs[0] in commands:
            await eval("discord_bot."+mscs[0]+"()")

    elif str(mschannel) == "hoşgeldin":
        if author != Bot_ID and mscontent == "":
            ms = """
            \nMerhaba <@{}> seni aramızda görmekten büyük mutluluk duyduğumuzu söylemek istiyorum
            \n- coogger projesi
            \n- coogger discord kanalı
            \n- kurallar ve
            \n- cooggerup botu hakkında öğrenmen gereken bütün bilgileri
            \n<#421086987571822592> kanalında bulabilirsin,
            \nlütfen ilk ziyaret edeceğin yer burası olsun daha sonra coogger topluluğunda ki
            \nkullanıcılar ile takipleşmek için <#421390753881653248> kanalını ziyaret edebilirsin
            \nbenim yani cooggerup botunun diğer hünerlerini
            \ngörmek istersen seni mutlaka <#420741092070129685> kanalına bekliyorum help yazman yeterli
            \nsponsor olan kişilerin kanalı hemen burası <#421085667653713930> sende sponsor olabilirsin
            \nbunun için <@403671940507631618>'e özelden mesaj at.
            \nsponsorlar keşfettiği güzel içerikler <#421393050904952842> bu kanaldan paylaşır ve yetkili kişiler
            \ninceledikten sonra cooggerup botu çalıştırılır ve cooggerup desteği alır.
            \ndeveloperlar burada toplanır <#421392663678550024> arge, tartışma vb eğer sende developer isen yine hakancelik'e
            \nözelden yazabilirsin veya developer olan biri ile konuşabilirsin.
            \nve son olarak sohbet muhabbet aşkına <#419852543368101891> kanalına geçebilirsin
            \ntekrar görüşmek üzere.
            """
            await client.send_message(mschannel, ms.format(author))

client.run(Client_ID)

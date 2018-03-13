# channels
from channels import Cooggerup, Coogger, Follow

# 3.
import discord
import asyncio
Client_ID = "token"
client = discord.Client()
discord_user = discord.User()
#############
hakancelik_discord_id = "403671940507631618"
sedatcelik_discord_id = "411540871960330241"
Bot_ID = "420911621846859776"
# commands
commands = ["cooggerup","follow","post","sbd","price","payout","transfer"]
channels = ["Cooggerup"]

async def cooggerup_help(message):
    ms = """
    \nMerhaba <@{}> sana yapabildiğim bir kaç özellikten bahsetmeme izin ver
    \n- hesap takip bilgilerini $follow steemit_kullanıcı_adın şeklinde yazarak sonuçları görebilirsin.
    \n- post bilgilerini $post steemit_post_adresi şeklinde yazarak sonuçları görebilirsin.
    \n- hesabındaki toplam sbd miktarını $sbd steemit_kullanıcı_adı şeklinde yazarak sonuçları görebilirsin.
    \n- bitcoin litecoin sbd ve steem gibi coinlerin dolar cinsinden değerini görmek için $price yazman yeterli
    \n- ödeme bekleyen gönderi bilgisi vs için $payout steemit_kullanıcı_adı şeklinde yazman yeterli.
    \n- eğer coinlerini bloctras aracılığı ile bitcoine ve koinim aracılığı ile tl ye dönültüreceksen
    \n$transfer steemit_kullanıcı_adı şeklinde yazdığında sana kesintiler ile birlikte kaç tl alacağını
    \ngösterebilirim.
    \n- $cooggerup steemit_post_adresi ile upvote atılıyor fakat şuan için bu özellik sadece kurucu ve sedatcelik tarafından
    \n belirli postlara yönelik kullanılmakta.
    """
    await client.send_message(message.channel, ms.format(str(message.author.id)))

async def welcome(message):
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
    \ngörmek istersen seni mutlaka <#420741092070129685> kanalına bekliyorum $help yazman yeterli
    \nsponsor olan kişilerin kanalı hemen burası <#421085667653713930> sende sponsor olabilirsin
    \nbunun için <@403671940507631618>'e özelden mesaj at.
    \nsponsorlar keşfettiği güzel içerikler <#421393050904952842> bu kanaldan paylaşır ve yetkili kişiler
    \ninceledikten sonra cooggerup botu çalıştırılır ve cooggerup desteği alır.
    \ndeveloperlar burada toplanır <#421392663678550024> arge, tartışma vb eğer sende developer isen yine hakancelik'e
    \nözelden yazabilirsin veya developer olan biri ile konuşabilirsin.
    \nve son olarak sohbet muhabbet aşkına <#419852543368101891> kanalına geçebilirsin
    \ntekrar görüşmek üzere.
    """
    await client.send_message(message.channel, ms.format(str(message.author.id)))

@client.event
async def on_message(message):
    mschannel = message.channel
    mscontent = message.content.lower()
    mscs = mscontent.split()
    author = str(message.author.id)
    command = mscs[0].replace("$","")
    if author != Bot_ID:
        if mscontent.startswith("$"):
            if command == "help":
                await cooggerup_help(message)
            elif str(mschannel) == "cooggerup" or str(mschannel) == "test":
                cooggerup_channel = Cooggerup(message = message, client = client)
                if command in commands:
                    await eval("cooggerup_channel."+command+"()")
        elif str(mschannel) == "coogger":
            coogger_channel = Coogger(message = message, client = client)
            await coogger_channel.is_has()
        elif str(mschannel) == "takip":
            follow_channel = Follow(message = message, client = client)
            await follow_channel.is_user()
        elif str(mschannel) == "hoşgeldin":
             if mscontent == "":
                 await welcome(message)

client.run(Client_ID)

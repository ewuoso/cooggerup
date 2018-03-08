import discord
import asyncio
Client_ID = "token"
client = discord.Client()
discord_user = discord.User()

# cooggerup bot
from up.cooggerup import Upvote
cooggerup = Upvote()

# first my bot telegram bot
from tbot.bot import Tbot
Tbot = Tbot()

@client.event
async def on_message(message):
    mschannel = message.channel
    mscontent = message.content.lower()
    mscs = mscontent.startswith
    sendms = client.send_message
    editms = client.edit_message
    author = message.author.id
    if str(mschannel) == "cooggerup" and author != "420911621846859776":
        if mscs('cooggerup'):
            if str(author) != "403671940507631618":
                await sendms(mschannel, "Bu özellik sadece hakancelik tarafından kullanılabilir. <@{}>".format(author))
            if str(author) == "403671940507631618":
                tmp = await sendms(mschannel, 'Postunuz oylanıyor... <@{}>'.format(author))
                url = mscontent.replace("cooggerup ","")
                upvote_result = cooggerup.upvote(100, url)
                await editms(tmp, str(upvote_result)+" <@{}>".format(author))

        elif mscs('follow'):
            tmp = await sendms(mschannel, 'Takip bilgileriniz hazırlanıyor... <@{}>'.format(author))
            username = mscontent.replace("follow ","")
            context = Tbot.follow(username)
            await editms(tmp, str(context)+" <@{}>".format(author))

        elif mscs('post'):
            tmp = await sendms(mschannel, 'Post bilgileriniz hazırlanıyor... <@{}>'.format(author))
            url = mscontent.replace("follow ","")
            context = Tbot.post_detail(url)
            await editms(tmp, str(context)+" <@{}>".format(author))

        elif mscs('sbd'):
            tmp = await sendms(mschannel, 'Hesabınızdaki toplam sbd miktarı.. <@{}>'.format(author))
            username = mscontent.replace("sbd ","")
            context = Tbot.sbd(username)
            await editms(tmp, str(context)+" <@{}>".format(author))

        elif mscs('price'):
            tmp = await sendms(mschannel, 'coinlerin dolar cinsinden değeri.. <@{}>'.format(author))
            context = Tbot.price()
            await editms(tmp, str(context)+" <@{}>".format(author))

        elif mscs('payout'):
            tmp = await sendms(mschannel, 'Ödeme bekleyen gönderi bilgileri... <@{}>'.format(author))
            username = mscontent.replace("payout ","")
            context = Tbot.payout(username)
            await editms(tmp, str(context)+" <@{}>".format(author))

        elif mscs('transfer'):
            tmp = await sendms(mschannel, 'Blocktrades ve koinim transver bilgileriniz... <@{}>'.format(author))
            username = mscontent.replace("transfer ","")
            context = Tbot.transfer(username)
            await editms(tmp, str(context)+" <@{}>".format(author))

        elif mscs('hi coogger') or mscs('hi'):
            await sendms(mschannel, 'ih <@{}>'.format(author))

        elif mscs('sa coogger') or mscs('sa'):
            await sendms(mschannel, 'as <@{}>'.format(author))

        elif mscs('help'):
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
            await sendms(mschannel, ms.format(author))

    elif str(mschannel) == "hoşgeldin":
        if author != "420911621846859776" and mscontent == "":
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
            await sendms(mschannel, ms.format(author))

client.run(Client_ID)

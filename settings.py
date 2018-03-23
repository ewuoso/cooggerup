# python
# from datetime import datetime
# TODAY = datetime.today()
# TODAY = str(TODAY.year)+"-"+str(TODAY.month)+"-"+str(TODAY.day)

# steem
from steem import Steem

# 3.
import discord

class Keys:
    accounts = [
    {"username":"hakancelik","weight":100,"posting_key":"key"},

    ]
    keys = [account["posting_key"] for account in accounts]
    users = [account["username"] for account in accounts]
    weight = [account["weight"] for account in accounts]

STEEM = Steem(nodes=['https://api.steemit.com'],keys = Keys.keys)

CLIENT = discord.Client()

CLIENT_ID = "key"

BOT_ID = "420911621846859776"

COMMANDS = ["follow","post","sbd","price","payout","transfer","help","calculate"] # coogger kanalı için komutlar

POSTSHARE = ["coogger","feronio","dmania","dlive","dtube","utopian","dsound","steepshot"] # kanallar için

UP_PERMISSION = [
    dict(
    username = "hakancelik",discord_id = "403671940507631618",
    ),
]

HELP_MS = """
    \nMerhaba <@{}> sana yapabildiğim bir kaç özellikten bahsetmeme izin ver
    \n- $follow steemit_kullanıcı_adın  hesap takip bilgilerini gösterir.
    \n- $post steemit_post_adresi post bilgilerini gösterir.
    \n- $sbd steemit_kullanıcı_adı hesabındaki toplam sbd miktarını gösterir.
    \n- $price coinlerin dolar cinsinden değerlerini gösterir.
    \n- $payout steemit_kullanıcı_adı ödeme bekleyen gönderi bilgilerini gösterir.
    \n- $transfer steemit_kullanıcı_adı eğer coinlerini bloctras aracılığı ile bitcoine ve koinim aracılığı ile tl ye dönültüreceksen şeklinde yazdığında sana kesintiler ile birlikte kaç tl alacağını gösterebilirim.
    \n- $calculate 40 şeklinde yazarsan sana $40 değerin %50/%50 olarak ayarlandığını varsayarak ödeme sonunda kaç sbd kaç sp
    \n alacagınızı gösterebilirim.
    \n- cooggerup kanalında $cooggerup steemit_post_adresi ile upvote atılıyor fakat şuan için bu özellik sadece hakancelik ve sedatcelik tarafından
    \n  belirli postlara yönelik kullanılmakta.
    \n made by @hakancelik
"""

WELCOME_MS = """
    \nMerhaba <@{}> seni aramızda görmekten büyük mutluluk duyduğumuzu söylemek istiyorum
    \n- coogger projesi, coogger discord kanalı, cooggerup botu hakkında öğrenmen gereken bütün bilgileri
    \n<#421086987571822592> kanalında bulabilirsin,
    \nlütfen ilk ziyaret edeceğin yer burası olsun daha sonra coogger topluluğunda ki
    \nkullanıcılar ile takipleşmek için <#421390753881653248> kanalını ziyaret edebilirsin
    \nbenim yani cooggerup botunun diğer hünerlerini
    \ngörmek istersen seni mutlaka <#424979369820160012> kanalına bekliyorum $help yazman yeterli
    \nsponsor olan kişilerin kanalı hemen burası <#421085667653713930> sende sponsor olabilirsin
    \nbunun için <@403671940507631618>'e özelden mesaj at.
    \ndeveloperların arge, tartışma vb kanalları vardır eğer sende developer isen ve coogger'da rol olmak istersen yine hakancelik'e
    \nözelden yazabilirsin veya developer olan biri ile konuşabilirsin.
    \nve son olarak sohbet muhabbet aşkına <#419852543368101891> kanalına geçebilirsin
    \ntekrar görüşmek üzere.
    \nBütün kanalların ne için açıldığı vb bilgiler kanal başlığında yazar.
"""

COOGGERUP_REPLY = """------------------
- İçeriğiniz coogger projesi tarafından seçilmiş olup<strong> {} </strong>hesap
tarafından upvote atılmıştır içeriğinize upvote atan cooggerup botu hakkında ve
bu oluşum hakkında detaylı bilgileri aşağıdaki adrese tıklayarak öğrenebilirsiniz.
https://steemit.com/coogger/@coogger/cooggerup-nedir-ve-discord-kanalimiz

- Bizimle discord üzerinden iletişime geçebilirsiniz.
Discord : https://discord.gg/QC5B3GX

- {}


<center>Sende bu oluşumun bir parçası olabilir, destek verebilir veya alabilirsin; discord kanalımıza bekleriz. </center>
"""
COOGGERUP_TAG_REPLY = COOGGERUP_REPLY.format(len(Keys.users),"coogger etiketini kullanıp bizleri desteklediğiniz için teşekkürler.")

COOGGERUP_REPLY = COOGGERUP_REPLY.format(len(Keys.users),"Bir dahaki sefere sizi daha hızlı bulabilmemiz için coogger etiketini kullanabilirsiniz.")

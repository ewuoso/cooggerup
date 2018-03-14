# python
from datetime import datetime
TODAY = datetime.today()
TODAY = str(TODAY.year)+"-"+str(TODAY.month)+"-"+str(TODAY.day)

# steem
from steem import Steem

# 3.
import discord

class Keys:
    accounts = [
    {"username":"hakancelik","weight":75,"posting_key":"key"},
    ]
    keys = [account["posting_key"] for account in accounts]
    users = [account["username"] for account in accounts]
    weight = [account["weight"] for account in accounts]

STEEM = Steem(nodes=['https://api.steemit.com'],keys = Keys().keys)

CLIENT = discord.Client()

CLIENT_ID = "token"

BOT_ID = "420911621846859776"

COMMANDS = ["cooggerup","follow","post","sbd","price","payout","transfer","help","calculate"]

UP_PERMISSION = [
    dict(
    username = "hakancelik",discord_id = "403671940507631618",
    ),
    dict(
    username = "sedatcelik",discord_id = "11540871960330241",
    )
]

# CHANNELS_INFO = [
#     dict(
#     category = "genel", name = "sohbet",discord_id = "419852543368101891",
#     ),
#     dict(
#     category = "genel", name = "mining",discord_id = "421980283131133952",
#     ),
#     dict(
#     category = "sponsors", name = "sohbet",discord_id = "421085667653713930",
#     ),
#     dict(
#     category = "sponsors", name = "arge",discord_id = "421393704411070484",
#     ),
#     dict(
#     category = "bots", name = "cooggerup",discord_id = "420741092070129685",
#     ),
#     dict(
#     category = "bots", name = "postup",discord_id = "421393050904952842",
#     ),
#     dict(
#     category = "bots", name = "önerr",discord_id = "422821057318092803",
#     ),
#     dict(
#     category = "bots", name = "test",discord_id = "421461920625983488",
#     ),
#     dict(
#     category = "yardımlaşma", name = "post-paylaşımı",discord_id = "421391092890730497",
#     ),
#     dict(
#     category = "yardımlaşma", name = "takip",discord_id = "421390753881653248",
#     ),
#     dict(
#     category = "yardımlaşma", name = "kurasyon-avı",discord_id = "422695781082988544",
#     ),
#     dict(
#     category = "yardımlaşma", name = "coogger",discord_id = "422746357472690189",
#     ),
#     dict(
#     category = "developers", name = "arge",discord_id = "421392663678550024",
#     ),
#     dict(
#     category = "developers", name = "sohbet",discord_id = "421396625936875531",
#     ),
#     dict(
#     category = "yeni üyeler", name = "hoşgeldin",discord_id = "421044641429717010",
#     ),
#     dict(
#     category = "yeni üyeler", name = "sss",discord_id = "421086987571822592",
#     ),
# ]

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
    \n- $cooggerup steemit_post_adresi ile upvote atılıyor fakat şuan için bu özellik sadece kurucu ve sedatcelik tarafından
    \n  belirli postlara yönelik kullanılmakta.
"""

WELCOME_MS = """
    \nMerhaba <@{}> seni aramızda görmekten büyük mutluluk duyduğumuzu söylemek istiyorum
    \n- coogger projesi, coogger discord kanalı, cooggerup botu hakkında öğrenmen gereken bütün bilgileri
    \n<#421086987571822592> kanalında bulabilirsin,
    \nlütfen ilk ziyaret edeceğin yer burası olsun daha sonra coogger topluluğunda ki
    \nkullanıcılar ile takipleşmek için <#421390753881653248> kanalını ziyaret edebilirsin
    \nbenim yani cooggerup botunun diğer hünerlerini
    \ngörmek istersen seni mutlaka <#420741092070129685> kanalına bekliyorum $help yazman yeterli
    \nsponsor olan kişilerin kanalı hemen burası <#421085667653713930> sende sponsor olabilirsin
    \nbunun için <@403671940507631618>'e özelden mesaj at.
    \nsponsorlar keşfettiği güzel içerikler <#421393050904952842> bu kanaldan paylaşır ve yetkili kişiler
    \ninceledikten sonra cooggerup botu çalıştırılır ve cooggerup desteği alır.
    \ndeveloperlar burada toplanır <#421392663678550024> arge, tartışma vb eğer sende developer isen ve coogger'da rol olmak istersen yine hakancelik'e
    \nözelden yazabilirsin veya developer olan biri ile konuşabilirsin.
    \nve son olarak sohbet muhabbet aşkına <#419852543368101891> kanalına geçebilirsin
    \ntekrar görüşmek üzere.
"""

COOGGERUP_REPLY = """
    --------------------------------------------------------
    - İçeriğiniz coogger projesi tarafından seçilmiş olup<strong> {} </strong>hesap
    tarafından upvote atılmıştır içeriğinize upvote atan cooggerup botu hakkında ve
    bu oluşum hakkında detaylı bilgileri aşağıdaki adrese tıklayarak öğrenebilirsiniz.
    https://steemit.com/coogger/@coogger/cooggerup-nedir-ve-discord-kanalimiz

    - Bizimle discord üzerinden iletişime geçebilirsiniz.
    Discord : https://discord.gg/QC5B3GX

    - Bir dahaki sefere sizi daha hızlı bulabilmemiz için coogger etiketini kullanabilirsiniz.

    - [Seçilen diğer içeriklere buradan ulaşabilirsiniz.](https://steemit.com/coogger/@coogger/{}-coogger-projesi-tarafindan-secilen-icerikler)

    <center>Sende bu oluşumun bir parçası olabilir, destek verebilir veya alabilirsin; discord kanalımıza bekleriz. </center>
""".format(len(Keys.users),TODAY)

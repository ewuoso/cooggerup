# settings
import settings
from settings import CLIENT, CLIENT_ID, BOT_ID, COMMANDS, POSTSHARE

# channels
from channels import Cooggerup, Coogger, Follow, PostShare

# python
import asyncio

@CLIENT.event
async def on_message(message):
    mschannel = message.channel
    mscontent = message.content.lower()
    mscs = mscontent.split()
    author = str(message.author.id)
    command = mscs[0].replace("$","")
    if author != BOT_ID:
        if mscontent.startswith("$") and str(mschannel) == "coogger" or str(mschannel) == "test":
            if command == "help":
                await CLIENT.send_message(message.channel, settings.HELP_MS.format(str(message.author.id)))
            else:
                cooggerup_channel = Coogger(message = message, client = CLIENT)
                if command in COMMANDS:
                    await eval("cooggerup_channel."+command+"()")
        elif str(mschannel) == "cooggerup":
            if command == "cooggerup":
                await Cooggerup(message = message, client = CLIENT).run()
        elif str(mschannel) == "hoşgeldin": # mesaj yazımına yetkisi olmaması gerek kimsenin bu kanala
            await CLIENT.send_message(message.channel, settings.WELCOME_MS.format(str(message.author.id)))
        ############# kanal kuralları ###############
        elif str(mschannel) == "coogger-etiketli-postlar":
            await Coogger(message = message, client = CLIENT).run()
        elif str(mschannel) == "takip":
            await Follow(message = message, client = CLIENT).run()
        elif str(mschannel) in POSTSHARE:
            await PostShare(message = message, client = CLIENT).run(tag = str(mschannel))

CLIENT.run(CLIENT_ID)

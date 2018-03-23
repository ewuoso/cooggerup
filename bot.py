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
    if author != BOT_ID:
        if mscontent.startswith("$") and str(mschannel) == "bot" or str(mschannel) == "test":
            command = mscs[0].replace("$","")
            if command == "help":
                await CLIENT.send_message(mschannel, settings.HELP_MS.format(author))
            else:
                cooggerup_channel = Coogger(message = message, client = CLIENT)
                if command in COMMANDS:
                    await eval("cooggerup_channel."+command+"()")
        elif str(mschannel) == "hoşgeldin" and mscontent == "":
            await CLIENT.send_message(mschannel, settings.WELCOME_MS.format(author))
        elif str(mschannel) == "cooggerup":
            if command == "cooggerup":
                await Cooggerup(message = message, client = CLIENT).run()
        ############# kanal kuralları ###############
        elif str(mschannel) == "takip":
            await Follow(message = message, client = CLIENT).run()
        elif str(mschannel) in POSTSHARE:
            await PostShare(message = message, client = CLIENT).run(tag = str(mschannel))

CLIENT.run(CLIENT_ID)

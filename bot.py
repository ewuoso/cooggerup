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
    try:
        command = mscs[0].replace("$","")
    except:
        command = ""
    if author != BOT_ID:
        if str(mschannel) == "hoşgeldin" and mscontent == "":
            await CLIENT.send_message(mschannel, settings.WELCOME_MS.format(author))
        if str(mschannel) == "bot" or str(mschannel) == "test":
            if command == "help":
                await CLIENT.send_message(mschannel, settings.HELP_MS.format(author))
            else:
                cooggerup_channel = Coogger(message = message, client = CLIENT)
                if command in COMMANDS:
                    await eval("cooggerup_channel."+command+"()")
        if str(mschannel) == "cooggerup":
            if command == "cooggerup":
                await Cooggerup(message = message, client = CLIENT).run()
        if str(mschannel) == "takip":
            await Follow(message = message, client = CLIENT).run()
        if str(mschannel) in POSTSHARE:
            await PostShare(message = message, client = CLIENT).run(tag = str(mschannel))

CLIENT.run(CLIENT_ID)

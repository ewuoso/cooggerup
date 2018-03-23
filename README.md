[![Licence](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/coogger/discord.bot/blob/master/LICENSE.txt)

Discord and vote bot for coogger which is steemit account
====================


Before
-
- pip install -r requirements.txt

Open [settings](https://github.com/coogger/discord.bot/blob/master/settings.py)
and write your discord app cliet id in here CLIENT_ID = "token",
write in here your bot id BOT_ID

These commands COMMANDS = 
```python
["follow","post","sbd","price","payout","transfer","help","calculate"]
```
in settings is main command and run named coogger channel

this bot supervisor at discord channel,
example no one can't write something unlike https://steemit.com/@hakancelik this adrese on follow channel, 
if it does, bot will delete message and give a warning message.

![](https://steemitimages.com/0x0/https://i.hizliresim.com/qGaAlV.png)

POSTSHARE = ["dmania","dlive","dtube","utopian","dsound","zappl","steepshot"] 
this list looks at the contents of the relevant channels to see if they are appropriate, 
eg you can just put the dmania address in the dmania channel otherwise the bot will delete and warn you.

```python
UP_PERMISSION = [
    dict(
    username = "hakancelik",discord_id = "403671940507631618",
    ),
    dict(
    username = "sedatcelik",discord_id = "11540871960330241",
    )
]
```
This list is id of the discord members who will use the $cooggerup command


This class
```python
class Keys:
    accounts = [
    {"username":"hakancelik","weight":50,"posting_key":"key"},
    ]
    keys = [account["posting_key"] for account in accounts]
    users = [account["username"] for account in accounts]
    weight = [account["weight"] for account in accounts]
```
list in this class is the posting keys of steemit users

ex:
```python
accounts = [
    {"username":"hakancelik","weight":50,"posting_key":"key"},
    {"username":"user","weight":100,"posting_key":"key"},
    {"username":"lalala","weight":50,"posting_key":"key"},
    ]
```

--------

WHAT CAN YOU DO  WİTH COOGGERUP BOT

- $ follow steemit_name shows account follow information.
- $ post steemit_post_address shows post information.
- $ sbd steemit_ Displays the total amount of sbd in the username account.
- $ price shows the dollar values ​​of the coins.
- $ payout steemit_username shows shipping information pending payment.
- $ transfer steemit_username If you convert your coins to blocktrades via bitcoine and bitoin to try, I can show you how many tl will get you with interrupts.
- $ calculate 40, assuming you set the $ 40 value to 50% / 50%, how many sbd how many sp
  I can show you.
  $ cooggerup can upvote with steemit_post_address.
- After the $cooggerup command, I add a comment on coogger formation to the supported posts (edited)

Ex:

![](https://steemitimages.com/0x0/https://i.hizliresim.com/EPBmyg.png)
![](https://steemitimages.com/0x0/https://i.hizliresim.com/LbXlNb.png)
![](https://steemitimages.com/0x0/https://i.hizliresim.com/kOa9Q7.png)
![](https://steemitimages.com/0x0/https://i.hizliresim.com/8Y3ayQ.png)
 
**before**

![](https://steemitimages.com/0x0/https://i.hizliresim.com/1J3pVp.png)

**after**

![](https://steemitimages.com/0x0/https://i.hizliresim.com/nOabG5.png)
cooggerup's repply in settings.py named COOGGERUP_REPLY you can edit it

channel name should be cooggerup for this $cooggerup command run

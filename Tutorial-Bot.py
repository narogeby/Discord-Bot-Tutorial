import discord
import json
import random
import time
import datetime
from discord.ext import tasks

colors = ['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.sB7oAgOuL9mBm8PiFvb_nQHaEo%26pid%3DApi&f=1&ipt=9e4b75b300b02bb86e11a57172a187c6ed21b888d55eb39c640f1dfd43441219&ipo=images',
          'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.bavnPo93SaXTdsRdg163BAHaEK%26pid%3DApi&f=1&ipt=ab44e36e40cc49cdc7c98f7b4ecdb5253072c2c4d2e8a481eaed3fbd54ef460f&ipo=images',
          'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.aZ2fL4vj64QQHlIStpUiFgHaFv%26pid%3DApi&f=1&ipt=d6f42429834fb0e8655f318fe5cebc58ff7aaabae0e12f45d011860e2a78acd3&ipo=images']

cats = ['https://media.discordapp.net/attachments/1040793692035887184/1102330597109669989/rapidsave.com_jeaklf0k30xa1.gif?ex=671aadde&is=67195c5e&hm=1749ac20ca5e32a2aec780a263d42dc182702191dbdf5c6f879c27b11565d17f&',
        'https://tenor.com/view/wtff-cat-confused-orange-gif-25858653', 'https://tenor.com/view/cat-underwater-gif-922906369727670801']

interval = 7200
first_time = 1

prefix = '!'

client = discord.Client

@tasks.loop(seconds=interval)
async def on_interval():
    global first_time
    channel = client.get_channel(1298799488542183478)
    if(first_time != 1):
        await channel.send("It has been {} seconds".format(interval))
    first_time = 2

class MyClient(discord.Client):

    async def on_ready(self):
        print(self.user, " is running...")
        channel = client.get_channel(1298799488542183478)
        await channel.send("I am here...")
        on_interval.start()

    async def on_message(self, message):
        message_content = message.content.lower()
        channel = message.channel
        if message.author == self.user:
            return
        if 'hello tutorial bot' in message.content.lower():
            await message.channel.send("Hello {}".format(message.author.name))
        if (prefix + 'color') in message_content:
            await channel.send(random.choice(colors))
        if (prefix + 'cat') in message_content:
            await channel.send(random.choice(cats))
        if (prefix + 'set interval') in message_content:
            global interval
            global first_time
            interval = int(message_content[14:])
            first_time = 1
            on_interval.change_interval(seconds = interval)
            

token_file = open(r"C:\Users\natha\Discord Bot Tutorial\Discord-Bot-Tutorial\token.txt")
token = token_file.read()
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
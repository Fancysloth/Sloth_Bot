"""git add  .
git commit -m "your message here"
git push"""""
import SLOTHBOT_KEY
import discord
from discord.ext.commands import Bot
from discord.ext import commands


Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await client.kick(userName)

client.run(SLOTHBOT_KEY.key)
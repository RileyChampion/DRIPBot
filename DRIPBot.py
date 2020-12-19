import discord
from discord.ext import commands
from discord.utils import get
from Config import Config as config
import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
})

bot = commands.Bot(command_prefix="!")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     # if message.author == client.user:
#     #     return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# @bot.event
# async def on_message(message):
#     print(message.author)
#     # if message.author == bot:
#     #     print('here')
#     #     await message.add_reaction(":white_check_mark:")

@bot.command(name='drip')
async def drip(ctx):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    # msg = await say(embed=embedVar)
    # await msg.add_reaction(msg, ":white_check_mark:")
    msg = await ctx.send(embed=embedVar)
    # emoji1 = get(ctx.server.emojis, name="")
    await msg.add_reaction("789818259787612170")
    await msg.add_reaction('\N{smirking face}')

# bot.add_command(fucuuck)

bot.run(config.DISCORD_TOKEN)
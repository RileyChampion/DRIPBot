import discord
from discord.ext import commands
from discord.utils import get
from Config import Config as config
import requests
from bs4 import BeautifulSoup
import time
import asyncio
from test import scrap_site

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
})

bot = commands.Bot(command_prefix="!")

currency = "€£₽$¥"
size = ['XS', 'S','M','L','XL','XXL']

# @bot.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

@bot.command(name='drip_help')
async def drip_help(ctx):
    await ctx.send("```!drip {url to website} {price = optional} {size = optional}```")

@bot.command(name='drip')
async def drip(ctx, url="", price="", size=""):
    if(url == ""):
        await ctx.send("```!drip {url to website} {price = optional} {size = optional}```")
    else:
        item_tuple = await scrap_site(url)

        embedVar = discord.Embed(title=f"♨️SOME NEW HEAT IN THE CHAT♨️", description=f"**DRIP FROM:** {ctx.author.mention}", color=0xF6EB07)
        embedVar.set_image(url=f"{item_tuple[1]}")
        embedVar.add_field(name="Item", value=f"{item_tuple[0]}\n{'Price: **{}**'.format(price) if price != '' else ''}\n{'Size: **{}**'.format(size) if size != '' else ''}", inline=True)
        msg = await ctx.send(embed=embedVar)

        await msg.add_reaction('🔥')
        await msg.add_reaction('🤮')

        await asyncio.sleep(10)
        
        count_reactions = await ctx.channel.fetch_message(msg.id)

        max_reaction_text = ("🔥YO! That's fire cop it!🔥" if count_reactions.reactions[0].count >= count_reactions.reactions[1].count else "🤮Nah wtf is that shit?🤮")

        if(max_reaction_text == "🔥YO! That's fire cop it!🔥"):
            embedVar.color=0xF67407
        else:
            embedVar.color=0x439C3D

        embedVar.set_footer(text=max_reaction_text)
        await msg.edit(embed=embedVar)

bot.run(config.DISCORD_TOKEN)
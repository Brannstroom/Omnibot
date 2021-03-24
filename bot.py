import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("Hei botten har starta bro")

@bot.command(aliases=['vs'])
async def versus(ctx):
    author = ctx.message.author
    channel = author.voice.channel

    members_in_vc = ""

    for member in channel.members:
        members_in_vc += member.mention + '\n'

    tms = str(members_in_vc)

    embed=discord.Embed(title="Versus", color=0x0e87f1)
    embed.add_field(name="Settings", value="1️⃣ - Antall lag \n\n ❌ - Lås kanalen for motstandere \n\n 👪 - Inkluder alle på servern", inline=True)
    embed.add_field(name="Status", value="2 \n\n NEI \n\n NEI", inline=True)
    embed.add_field(name="Spillere", value=tms, inline=False)
    message = await ctx.send(embed=embed)

    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '❌', '👪']
    for emoji in emojis:
        await message.add_reaction(emoji)

bot.run('ODI0MzQ3NDkyMjQxODk5NTUy.YFuDbQ.O7k6dU3U5w7nU-FpTqD8n-xrVKU')
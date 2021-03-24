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

    embed=discord.Embed(title="Versus", color=0x0e87f1)
    embed.add_field(name="Settings", value="1️⃣ - Antall lag: 2 \n ❌ - Lås kanalen for motstandere: NEI \n 👪 - Inkluder alle på servern: NEI ", inline=False)
    embed.add_field(name="Spillere", value="1234 \n 1234 \n 1234 \n 1234 \n 1234 \n 1234", inline=True)
    message = await ctx.send(embed=embed)

    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '❌', '👪']
    for emoji in emojis:
        await message.add_reaction(emoji)

@bot.event
async def on_reaction_add():
    


bot.run('ODI0MzQ3NDkyMjQxODk5NTUy.YFuDbQ.O7k6dU3U5w7nU-FpTqD8n-xrVKU')
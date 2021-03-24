import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("Hei botten har starta bro")

@bot.command()
async def test(ctx, arg):
    max = random.randint(1,int(arg))
    await ctx.send("Du fikk " + str(max))

@bot.command(aliases=['vs'])
async def versus(ctx):

    


bot.run('ODI0MzQ3NDkyMjQxODk5NTUy.YFuDbQ.O7k6dU3U5w7nU-FpTqD8n-xrVKU')
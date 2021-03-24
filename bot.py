import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Hei botten har starta bro")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')

client.run('ODI0MzQ3NDkyMjQxODk5NTUy.YFuDbQ.O7k6dU3U5w7nU-FpTqD8n-xrVKU')
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
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '❌', '👪']
    num_teams = 0
    bool_lock = False
    bool_alle = False

    async def updateEmbed(num_teams, bool_lock, bool_alle):
        members_in_vc = ""

        for member in channel.members:
            members_in_vc += member.mention + '\n'

        tms = str(members_in_vc)

        embed=discord.Embed(title="Versus", color=0x0e87f1)
        embed.add_field(name="Settings", value="1️⃣ - Antall lag \n\n ❌ - Lås kanalen for motstandere \n\n 👪 - Inkluder alle på servern", inline=True)
        embed.add_field(name="Status", value= f"{num_teams} \n\n {bool_lock} \n\n {bool_alle}", inline=True)
        embed.add_field(name="Spillere", value=tms, inline=False)
        message = await ctx.send(embed=embed)

        for emoji in emojis:
            await message.add_reaction(emoji)

    await updateEmbed(num_teams, bool_lock, bool_alle)

    @bot.event
    async def on_reaction_add(reaction, user):
        
        if user == author:
            i = 0
            for emoj in emojis:
                if str(reaction) == emojis[i] and i < 4:
                    global num_teams
                    num_teams = i+1
                    print(num_teams)
                elif str(reaction) == emojis[4]:
                    global bool_lock
                    bool_lock = True
                elif str(reaction) == emojis[5]:
                    global bool_alle
                    bool_alle = True
                i += 1
        print(num_teams)
        await updateEmbed(num_teams, bool_lock, bool_alle)

        

        
                


bot.run('ODI0MzQ3NDkyMjQxODk5NTUy.YFuDbQ.O7k6dU3U5w7nU-FpTqD8n-xrVKU')
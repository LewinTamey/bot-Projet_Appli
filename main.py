from random import randint
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "")

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def nomg(ctx):
    with open("garcon.txt", "r") as fichier:
        lines = fichier.readlines()
        element = lines[randint(0, len(lines)-1)]
        await ctx.send(element)

@bot.command()
async def nomf(ctx):
    with open("fille.txt", "r") as fichier:
        lines = fichier.readlines()
        element = lines[randint(0, len(lines)-1)]
        await ctx.send(element)

bot.run("process.env.TOKEN")

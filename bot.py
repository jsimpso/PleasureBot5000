#!/usr/bin/env python

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='^', description='Not a Hookerbot.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.cmmands()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
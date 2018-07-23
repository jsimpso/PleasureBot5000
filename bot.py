#!/usr/bin/env python

import discord
import asyncio
from discord.ext import commands
import requests
import os

bot_token = os.environ['bot_token']
cat_token = os.environ['cat_token']

bot = commands.Bot(command_prefix='^', description='Not a Hookerbot.')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def cat(ctx):
    payload = {'api_key': cat_token}
    img = requests.get('http://thecatapi.com/api/images/get', json=payload)
    await ctx.send(img.url)


bot.run(bot_token)

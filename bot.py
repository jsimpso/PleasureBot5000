#!/usr/bin/env python

from discord.ext import commands
from twython import Twython
from io import BytesIO
import requests
import os
import urllib

bot_token = os.environ['bot_token']
cat_token = os.environ['cat_token']
consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter.verify_credentials()

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

@bot.command()
async def dog(ctx):
    img = requests.get('https://dog.ceo/api/breeds/image/random')
    await ctx.send(img.json()['message'])


@bot.command()
async def pups(ctx):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    print(r.json())
    url = r.json()['message']
    await ctx.send(url)


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')
    
    
@bot.command()
async def nancy(ctx):
    await ctx.send("https://i.imgur.com/PCn05.jpg") 


@bot.command()
async def nancytweet(ctx):
    url = 'https://i.imgur.com/PCn05.jpg'
    r = requests.get(url)
    image = BytesIO(r.content)
    message = "@Seeeeeeeev"
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    twitter.update_status(status=message, media_ids=media_id)
    await ctx.send("Tweeted: %s" % message)


bot.run(bot_token)

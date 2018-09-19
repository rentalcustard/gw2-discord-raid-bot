#!/usr/bin/env python3

import discord
import os

try:
    TOKEN = os.environ['DISCORD_TOKEN']
except KeyError:
    print("DISCORD_TOKEN environment variable not found. Please set it and run again!")
    exit(1)

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in")

@client.event
async def on_message(message):
    #the bot shouldn't reply to itself
    if message.author.id == client.user.id:
        return

    if message.content == "!test":
        await message.channel.send("HELLO {0.author.mention}. I AM READY TO SERVE.".format(message))


client.run(TOKEN)

#!/usr/bin/env python3

import discord
import os
import lib.builds as Builds

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
        await client.send_message(message.channel, "HELLO {0.author.mention}. I AM READY TO SERVE.".format(message))

    if message.content.startswith("!build"):
        parts = message.content.split(" ")
        build_link = Builds.get_build(parts[1], parts[2])
        await client.send_message(message.channel, build_link)


client.run(TOKEN)

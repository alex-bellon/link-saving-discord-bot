#! /bin/python3
import discord, os
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

archive_id = 985292956112158773

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author != client.user: 
        await message.add_reaction('✅')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '✅' and user != client.user and reaction.message.channel != archive_id:
        await reaction.message.delete()
        await client.get_channel(archive_id).send(reaction.message.content)

client.run(TOKEN)


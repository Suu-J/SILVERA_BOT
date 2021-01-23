import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
from itertools import cycle
import firebase_admin
from firebase_admin import credentials
import asyncio
from asyncio import sleep

firebase_key=os.path.join(os.path.dirname(__file__),'./firebase_key.json')
cred = credentials.Certificate(firebase_key)
firebase_admin.initialize_app(cred)


client = commands.Bot(command_prefix ='.', help_command=None)
status = cycle(['Work in progress','.help for more'])

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    change_status.start()
    print('ONLINE!')
    #await client.change_presence(status = discord.Status.idle,activity = discord.Game('Work In Progress'))

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))   

'''
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

'''
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run(DISCORD_TOKEN)
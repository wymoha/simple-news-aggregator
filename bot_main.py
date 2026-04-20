
import discord
import discord.ext
from dotenv import load_dotenv
import os
import logging
load_dotenv()
TOKEN = os.getenv('TOKEN')
handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Sucessfully logged in as {client.user}")
   

client.run(token=TOKEN)
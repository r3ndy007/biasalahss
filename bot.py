import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

messages = [
    "HALO GES SELAMAT GRINDING",
    "NGOPI NGOPI GES",
    "Yuk gaskan lah ah, walawe walawe",
    "Kasih paham, kasih JP nya jg gasss",
    "KOWKWKOWOKKWKOWKOW"
]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("Channel tidak ditemukan. Cek ID-nya.")
        return

    while True:
        for message in messages:
            await channel.send(message)
            await asyncio.sleep(10)  # tiap 10 detik

client.run(TOKEN)

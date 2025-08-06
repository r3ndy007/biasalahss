import discord
import asyncio

TOKEN = MTQwMjU2Mzg0NzU2NjM5MzQwNA.GjTsX_.E-9kqMq-o8_jxFHJ1g8TxZp1bal-Y4RLRKa-fA
CHANNEL_ID = 1400757543021838357  # Sudah kamu dapat

pesan_list = [
    "HALO GES SELAMAT GRINDING",
    "NGOPI NGOPI GES",
    "Yuk gaskan lah ah, walawe walawe",
    "Kasih paham, kasih JP nya jg gasss",
    "KOWKWKOWOKKWKOWKOW"
]

delay = 10  # detik

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot aktif sebagai {client.user}')
    channel = client.get_channel(CHANNEL_ID)

    index = 0
    while True:
        pesan = pesan_list[index]
        await channel.send(pesan)
        index = (index + 1) % len(pesan_list)
        await asyncio.sleep(delay)

client.run(TOKEN)

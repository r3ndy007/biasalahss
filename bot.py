import requests
import time
import os
from dotenv import load_dotenv

# Load dari .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

messages = [
    "HALO GES SELAMAT GRINDING",
    "NGOPI NGOPI GES",
    "Yuk gaskan lah ah, walawe walawe",
    "Kasih paham, kasih JP nya jg gasss",
    "KOWKWKOWOKKWKOWKOW"
]

headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

def kirim_pesan():
    for msg in messages:
        payload = {
            "content": msg
        }
        response = requests.post(
            f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages",
            headers=headers,
            json=payload
        )
        if response.status_code == 200:
            print(f"✔️ Terkirim: {msg}")
        else:
            print(f"❌ Gagal kirim: {msg} | Status: {response.status_code}")
        time.sleep(5)

if __name__ == "__main__":
    kirim_pesan()

import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

message = "Salom Nozanin! Bugungi darslar va maqsadlarni bajarish esdan chiqmasin! 🚀"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, json=payload)
print(response.json())

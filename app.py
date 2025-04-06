from flask import Flask, request
import requests
import logging
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = '7559752691:AAHdzZZ0pXq2CacIRx7SSD79fFE1YliIQkw'
CHAT_ID = '580021764'

# Logger sozlamasi
logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', '⚠️ Xabar topilmadi')

    # Telegramga yuborish
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, json=payload)

    # Logga yozish
    logging.info(f"Yuborilgan signal: {message}")

    return 'OK', 200

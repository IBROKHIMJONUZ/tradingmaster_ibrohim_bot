import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = '7559752691:AAHdzZZ0pXq2CacIRx7SSD79fFE1YliIQkw'
CHAT_ID = '580021764'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.data.decode('utf-8')
    send_telegram_message(f"📈 Yangi Signal keldi:\n\n🔔 {data}")
    return "✅ Signal yuborildi"

if __name__ == '__main__':
    app.run(port=5000)

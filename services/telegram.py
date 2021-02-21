from config import CONFIG
import requests


def send_message(username, message):
    token = CONFIG['TELEGRAM_APP_TOKEN']
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.post(url).json()
    chat_id = None
    for chat in res['result']:
        if chat['message']['chat']['username'] == username:
            chat_id = chat['message']['chat']['id']

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data).json()
    return


def verify_username(username):
    token = CONFIG['TELEGRAM_APP_TOKEN']
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    res = requests.post(url).json()
    for chat in res['result']:
        if chat['message']['chat']['username'] == username:
            return {"exists": True}

    return {"exists": False}

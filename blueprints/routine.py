from flask import Blueprint, jsonify

from services.firestore import list_users
from services.ftx import get_funding
from services.telegram import send_message

routine_bp = Blueprint('routine_bp', __name__)


@routine_bp.route('')
def run():
    users = list_users()

    for user in users:
        for stock in user['watchlist']:
            funding = get_funding(stock['symbol'])
            if funding['result'][0]['rate'] >= stock['limit']:
                message = f"Value {stock['symbol']} is above limit. Limit was set to {stock['limit']}, and is {funding['result'][0]['rate']} from {funding['result'][0]['time'].split('+')[0].replace('T', ' ')}"
                send_message(user['telegram'], message)
    return "ok"

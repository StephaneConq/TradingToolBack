from flask import Blueprint, jsonify

from services.telegram import verify_username

telegram_bp = Blueprint('telegram_bp', __name__)


@telegram_bp.route('<username>')
def check_username(username):
    return jsonify(verify_username(username))

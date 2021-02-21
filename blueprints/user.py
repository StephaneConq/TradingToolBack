from flask import Blueprint, jsonify, request

from services.firestore import get_user, set_user

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/me')
def get_current_user():
    return jsonify(get_user(request.headers.get('X-Goog-Authenticated-User-Email')))


@user_bp.route('/me', methods=['PATCH'])
def update_current_user():
    return jsonify(set_user(request.headers.get('X-Goog-Authenticated-User-Email'), request.json))

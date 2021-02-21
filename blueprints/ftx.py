from flask import Blueprint, jsonify

from services.ftx import list_markets, get_price

ftx_bp = Blueprint('ftx_bp', __name__)


@ftx_bp.route('')
def list_market():
    stocks = list_markets()
    return jsonify(stocks['result'])


@ftx_bp.route('<market>')
def get_market(market):
    market = market.replace('---', '/')
    stock = get_price(market)
    return jsonify(stock['result'])

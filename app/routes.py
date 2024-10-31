from flask import render_template, request, jsonify, current_app
from . import db  # Directly import db
from .models import Stock, Portfolio, Transaction
from .simulator import simulate_stock_price_changes, trigger_random_event

@current_app.route('/')
def index():
    portfolio = Portfolio.query.first()
    stocks = Stock.query.all()
    return render_template('index.html', portfolio=portfolio, stocks=stocks)

@current_app.route('/buy', methods=['POST'])
def buy_stock():
    stock_id = request.json.get('stock_id')
    shares = request.json.get('shares')
    # Process the transaction logic here
    return jsonify({'message': 'Stock bought successfully'})

@current_app.route('/sell', methods=['POST'])
def sell_stock():
    stock_id = request.json.get('stock_id')
    shares = request.json.get('shares')
    # Process the transaction logic here
    return jsonify({'message': 'Stock sold successfully'})

@current_app.route('/market', methods=['GET'])
def market_conditions():
    event = trigger_random_event()
    return jsonify({'event': event})

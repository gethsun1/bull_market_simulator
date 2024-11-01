import requests
from flask import Blueprint, render_template, request, jsonify, current_app

# Define the blueprint
bp = Blueprint('main', __name__)

# Initialize portfolio with dummy cash balance
portfolio = {
    'cash_balance': 10000,  # Dummy balance of $10,000
    'stocks': {}
}

# NSE API configuration
API_URL = "https://nairobi-stock-exchange-nse.p.rapidapi.com/stocks"
API_HEADERS = {
    'x-rapidapi-host': 'nairobi-stock-exchange-nse.p.rapidapi.com',
    'x-rapidapi-key': '64e5499d05mshf4c762192029b45p14a558jsndd98c5a2f1a0'  # Replace with your actual API key
}


def load_stock_data():
    try:
        response = requests.get(API_URL, headers=API_HEADERS)
        response.raise_for_status()
        data = response.json()

        # Parse the data into the format needed for the app
        stocks = []
        for item in data:
            stock = {
                'name': item.get('name', 'Unknown Company'),
                'ticker': item.get('ticker', 'N/A'),
                'price': float(item.get('price', '0').replace(',', '')),  # Remove commas before converting
                'volume': item.get('volume', '0'),
                'change': item.get('change', '0')
            }
            stocks.append(stock)
        return stocks
    except requests.RequestException as e:
        print(f"Error fetching data from NSE API: {e}")
        return []

# Homepage route
@bp.route('/')
def index():
    stocks_data = load_stock_data()
    return render_template('index.html', portfolio=portfolio, stocks=stocks_data)

# Function to buy stocks
@bp.route('/buy', methods=['POST'])
def buy_stock():
    stock_id = request.json.get('stock_id')
    stock_name = request.json.get('stock_name')
    stock_price = request.json.get('stock_price')
    shares = int(request.json.get('shares'))

    # Calculate the total cost
    total_cost = stock_price * shares

    # Check if the user has enough cash
    if portfolio['cash_balance'] >= total_cost:
        portfolio['cash_balance'] -= total_cost
        if stock_name in portfolio['stocks']:
            portfolio['stocks'][stock_name]['shares'] += shares
        else:
            portfolio['stocks'][stock_name] = {
                'stock_price': stock_price,
                'shares': shares
            }

        return jsonify({'message': f'Successfully bought {shares} shares of {stock_name}', 'cash_balance': portfolio['cash_balance']})
    else:
        return jsonify({'message': 'Insufficient balance', 'cash_balance': portfolio['cash_balance']}), 400

# Function to sell stocks
@bp.route('/sell', methods=['POST'])
def sell_stock():
    stock_name = request.json.get('stock_name')
    shares = int(request.json.get('shares'))

    if stock_name in portfolio['stocks'] and portfolio['stocks'][stock_name]['shares'] >= shares:
        stock_price = portfolio['stocks'][stock_name]['stock_price']
        total_sale = stock_price * shares
        portfolio['cash_balance'] += total_sale
        portfolio['stocks'][stock_name]['shares'] -= shares
        if portfolio['stocks'][stock_name]['shares'] == 0:
            del portfolio['stocks'][stock_name]

        return jsonify({'message': f'Successfully sold {shares} shares of {stock_name}', 'cash_balance': portfolio['cash_balance']})
    else:
        return jsonify({'message': 'Not enough shares to sell', 'cash_balance': portfolio['cash_balance']}), 400

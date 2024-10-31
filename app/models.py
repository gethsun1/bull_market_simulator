from app import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
  

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cash_balance = db.Column(db.Float, nullable=False, default=100000)  # Starting cash

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(4), nullable=False)  # "BUY" or "SELL"
    

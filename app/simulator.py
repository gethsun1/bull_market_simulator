from app.models import Stock, db
import random

# Define random events
EVENTS = [
    "The company has been bombed completely...",
    "Seismologists have reported strong and long earthquakes...",
    # Add all other events
]

def simulate_stock_price_changes():
    stocks = Stock.query.all()
    for stock in stocks:
        stock.price += random.uniform(-10, 10)  # Random price fluctuation
        db.session.commit()

def trigger_random_event():
    event = random.choice(EVENTS)
    # Logic to determine how the event affects stocks
    return event

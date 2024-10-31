from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy without binding it to an app initially
db = SQLAlchemy()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Register routes and create the database tables within the app context
    with app.app_context():
        from . import routes, models  # Import routes and models
        db.create_all()  # Create database tables

    return app

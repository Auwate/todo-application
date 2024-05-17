from flask import Flask
from database import db, init_db
from routes import register_routes

# Setup
app = Flask(__name__)

# Initialize DB
init_db(app)

# Register routes in routes.py
register_routes(app)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)

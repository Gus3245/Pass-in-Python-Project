from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from src.main.routes.event_routes import event_route_bp
app.register_blueprint(event_route_bp)
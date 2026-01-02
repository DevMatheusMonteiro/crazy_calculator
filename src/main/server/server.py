from flask import Flask
from src.main.routes.calculators import CalculatorsRoutes

app = Flask(__name__)
app.register_blueprint(CalculatorsRoutes.calc_route_bp)
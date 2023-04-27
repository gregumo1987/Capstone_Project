from flask import Flask, render_template, jsonify, request
import json
from app.ml_model import fetch_data, process_kpi_data
from app.route import route

def create_app():
    app = Flask(__name__)
    app.register_blueprint(route)

    return app

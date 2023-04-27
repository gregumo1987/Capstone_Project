from flask import Flask, render_template, jsonify, request

from flask import Blueprint, jsonify, request
import json
from app.ml_model import fetch_data, process_kpi_data

route = Blueprint('route', __name__)

@route.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@route.route("/api/data", methods=["POST"])
def get_data():
    data = request.get_json()
    company_name = data["company_name"]
    raw_data = fetch_data(company_name)
    kpi_data, chart_data = process_kpi_data(raw_data)

    return jsonify({
        "kpiData": kpi_data,
        "chartData": chart_data
    })

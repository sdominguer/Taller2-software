from flask import Blueprint, jsonify, render_template
import random
from .data import pokeneas, container_id

app_routes = Blueprint("app_routes", __name__)

@app_routes.route("/json")
def random_pokenea_json():
    pokenea = random.choice(pokeneas)
    pokenea['container_id'] = container_id
    return jsonify(pokenea)

@app_routes.route("/imagen")
def imagen_frase():
    pokenea = random.choice(pokeneas)
    return render_template("imagen.html", imagen=pokenea["imagen"], frase=pokenea["frase"], container_id=container_id)

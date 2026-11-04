from flask import Blueprint
from app.productos.models import Producto  # importa el modelo para que se detecte en las migraciones

bp_productos = Blueprint("bp_productos", __name__, template_folder="templates")

@bp_productos.route("/")
def index():
    return "<h3>Módulo de productos</h3>"
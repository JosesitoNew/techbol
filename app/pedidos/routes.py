from flask import Blueprint
from app.pedidos.models import Pedido  # importa el modelo para que se detecte en las migraciones

bp_pedidos = Blueprint("bp_pedidos", __name__, template_folder="templates")

@bp_pedidos.route("/")
def index():
    return "<h3>Módulo de pedidos</h3>"
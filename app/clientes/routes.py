from flask import Blueprint
from app.clientes.models import Cliente  # importa el modelo para que se detecte en las migraciones

bp_clientes = Blueprint("bp_clientes", __name__, template_folder="templates")

@bp_clientes.route("/")
def index():
    return "<h3>Módulo de clientes</h3>"
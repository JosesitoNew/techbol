from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()       # instancia global, se importa en modelos y rutas
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder="templates")

    # SQLite: el archivo se crea dentro de instance/
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bd_techbol.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # 1. Importar
    from app.clientes.routes import bp_clientes
    from app.productos.routes import bp_productos
    from app.pedidos.routes import bp_pedidos

    # 2. Registrar con su prefijo
    app.register_blueprint(bp_clientes, url_prefix="/clientes")
    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")

    return app



    
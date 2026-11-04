from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.pedidos.models import Pedido
from app.clientes.models import Cliente
from app.productos.models import Producto

bp_pedidos = Blueprint("bp_pedidos", __name__, template_folder="templates")

@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template("pedido/index.html", pedidos=pedidos)

@bp_pedidos.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        clientes = Cliente.query.all()
        productos = Producto.query.all()
        return render_template(
            "pedido/create.html", pedido=None, clientes=clientes, productos=productos
        )

    cliente_id = int(request.form.get("cliente_id"))
    producto = db.get_or_404(Producto, int(request.form.get("producto_id")))
    # El monto es el precio del producto elegido
    pedido = Pedido(cliente_id=cliente_id, producto_id=producto.id, monto=producto.precio)
    db.session.add(pedido)
    db.session.commit()
    flash("Pedido agregado correctamente", "success")
    return redirect(url_for("bp_pedidos.index"))

@bp_pedidos.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    pedido = db.get_or_404(Pedido, id)
    if request.method == "GET":
        clientes = Cliente.query.all()
        productos = Producto.query.all()
        return render_template(
            "pedido/create.html", pedido=pedido, clientes=clientes, productos=productos
        )

    producto = db.get_or_404(Producto, int(request.form.get("producto_id")))
    pedido.cliente_id = int(request.form.get("cliente_id"))
    pedido.producto_id = producto.id
    pedido.monto = producto.precio  # se recalcula con el producto elegido
    db.session.commit()
    flash("Pedido actualizado", "success")
    return redirect(url_for("bp_pedidos.index"))

@bp_pedidos.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    pedido = db.get_or_404(Pedido, id)
    db.session.delete(pedido)
    db.session.commit()
    flash("Pedido eliminado", "success")
    return redirect(url_for("bp_pedidos.index"))
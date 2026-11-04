from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.productos.models import Producto

bp_productos = Blueprint("bp_productos", __name__, template_folder="templates")

@bp_productos.route("/")
def index():
    productos = Producto.query.all()
    return render_template("producto/index.html", productos=productos)

@bp_productos.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("producto/create.html", producto=None)

    nombre = request.form.get("nombre")
    precio = float(request.form.get("precio"))
    stock = int(request.form.get("stock") or 0)
    producto = Producto(nombre=nombre, precio=precio, stock=stock)
    db.session.add(producto)
    db.session.commit()
    flash("Producto agregado correctamente", "success")
    return redirect(url_for("bp_productos.index"))

@bp_productos.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    producto = db.get_or_404(Producto, id)
    if request.method == "GET":
        return render_template("producto/create.html", producto=producto)

    producto.nombre = request.form.get("nombre")
    producto.precio = float(request.form.get("precio"))
    producto.stock = int(request.form.get("stock") or 0)
    db.session.commit()
    flash("Producto actualizado", "success")
    return redirect(url_for("bp_productos.index"))

@bp_productos.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    producto = db.get_or_404(Producto, id)
    # No se elimina si está en algún pedido
    if producto.pedidos:
        flash("No se puede eliminar: el producto está en pedidos", "danger")
        return redirect(url_for("bp_productos.index"))
    db.session.delete(producto)
    db.session.commit()
    flash("Producto eliminado", "success")
    return redirect(url_for("bp_productos.index"))
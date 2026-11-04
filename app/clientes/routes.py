from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.clientes.models import Cliente

bp_clientes = Blueprint("bp_clientes", __name__, template_folder="templates")

@bp_clientes.route("/")
def index():
    clientes = Cliente.query.all()
    return render_template("cliente/index.html", clientes=clientes)

@bp_clientes.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("cliente/create.html", cliente=None)

    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")
    cliente = Cliente(nombre=nombre, telefono=telefono)
    db.session.add(cliente)
    db.session.commit()
    flash("Cliente agregado correctamente", "success")
    return redirect(url_for("bp_clientes.index"))

@bp_clientes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cliente = db.get_or_404(Cliente, id)
    if request.method == "GET":
        return render_template("cliente/create.html", cliente=cliente)

    cliente.nombre = request.form.get("nombre")
    cliente.telefono = request.form.get("telefono")
    db.session.commit()
    flash("Cliente actualizado", "success")
    return redirect(url_for("bp_clientes.index"))

@bp_clientes.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    cliente = db.get_or_404(Cliente, id)
    # No se elimina si tiene pedidos asociados
    if cliente.pedidos:
        flash("No se puede eliminar: el cliente tiene pedidos", "danger")
        return redirect(url_for("bp_clientes.index"))
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente eliminado", "success")
    return redirect(url_for("bp_clientes.index"))
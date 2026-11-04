from app import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)

    # Un producto puede estar en muchos pedidos
    pedidos = db.relationship("Pedido", back_populates="producto")

    def __repr__(self):
        return f"Producto: {self.nombre} - {self.precio}"

        
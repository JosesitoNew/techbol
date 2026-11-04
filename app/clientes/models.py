from app import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String)

    # Un cliente tiene muchos pedidos
    pedidos = db.relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"Cliente: {self.nombre} - {self.telefono}"
        
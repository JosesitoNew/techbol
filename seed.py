from app import create_app, db
from app.clientes.models import Cliente
from app.productos.models import Producto
from app.pedidos.models import Pedido

app = create_app()

with app.app_context():
    # Evita duplicar datos si se ejecuta dos veces
    if Cliente.query.first():
        print("La base ya tiene datos")
        raise SystemExit

    c1 = Cliente(nombre="Ana Pérez", telefono="70000001")
    c2 = Cliente(nombre="Luis Gómez", telefono="70000002")
    c3 = Cliente(nombre="María Rojas", telefono="70000003")

    p1 = Producto(nombre="Teclado mecánico", precio=45.50, stock=20)
    p2 = Producto(nombre="Mouse inalámbrico", precio=18.00, stock=35)
    p3 = Producto(nombre="Monitor 24 pulgadas", precio=120.00, stock=8)
    p4 = Producto(nombre="Auriculares", precio=30.00, stock=15)

    db.session.add_all([c1, c2, c3, p1, p2, p3, p4])

    # El monto es el precio del producto
    pedidos = [
        Pedido(cliente=c1, producto=p1, monto=p1.precio),
        Pedido(cliente=c1, producto=p2, monto=p2.precio),
        Pedido(cliente=c2, producto=p3, monto=p3.precio),
        Pedido(cliente=c3, producto=p4, monto=p4.precio),
    ]
    db.session.add_all(pedidos)
    db.session.commit()
    print("Datos de prueba insertados")
    
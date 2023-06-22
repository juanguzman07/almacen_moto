from Modelos.Productos import Productos

from Repositorios.RepositorioProductos import RepositorioProductos


class ControladorProductos():

    def __init__(self):
        self.repositorioProductos = RepositorioProductos()

        print("Creando Controlador Productos")

    def index(self):
        print("Listar Los Productos")
        return self.repositorioProductos.findAll()

    def create(self, elProductos):
        print("Creando Producto")
        nuevoProducto = Productos(elProductos)
        return self.repositorioProductos.save(nuevoProducto)

    def show(self, id):
        print("Mostrando Producto Con id ", id)
        elProductos = Productos(self.repositorioProductos.findById(id))
        return elProductos.__dict__

    def update(self, id, elProductos):
        print("Actualizando Producto con id ", id)
        ProductosActual = Productos(self.repositorioProductos.findById(id))
        ProductosActual.Nombre = elProductos["Nombre"]
        ProductosActual.Codigo = elProductos["Codigo"]
        ProductosActual.Descripcion = elProductos["Descripcion"]
        ProductosActual.Cantidad = elProductos["Cantidad"]
        ProductosActual.Precio = elProductos["Precio"]
        return self.repositorioProductos.save(ProductosActual)

    def delete(self, id):
        print("Elimiando Producto con id ", id)
        return self.repositorioProductos.delete(id)
from Modelos.Proveedor import Proveedor

from Repositorios.RepositorioProveedor import RepositorioProveedor


class ControladorProveedor():

    def __init__(self):
        self.repositorioProveedor = RepositorioProveedor()

        print("Creando Controlador Proveedor")

    def index(self):
        print("Listar Los Proveedor")
        return self.repositorioProveedor.findAll()

    def create(self, elProveedor):
        print("Creando Proveedor")
        nuevoProveedor = Proveedor(elProveedor)
        return self.repositorioProveedor.save(nuevoProveedor)

    def show(self, id):
        print("Mostrando Proveedor Con id ", id)
        elProveedor = Proveedor(self.repositorioProveedor.findById(id))
        return elProveedor.__dict__

    def update(self, id, elProveedor):
        print("Actualizando Proveedor con id ", id)
        ProductosActual = Proveedor(self.repositorioProveedor.findById(id))
        ProductosActual.Nit = elProveedor["Nit"]
        ProductosActual.Nombre = elProveedor["Nombre"]
        ProductosActual.Telefono = elProveedor["Telefono"]
        ProductosActual.Email = elProveedor["Email"]
        return self.repositorioProveedor.save(ProductosActual)

    def delete(self, id):
        print("Elimiando Proveedor con id ", id)
        return self.repositorioProveedor.delete(id)
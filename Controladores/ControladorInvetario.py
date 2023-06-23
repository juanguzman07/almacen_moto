from Modelos.Inventario import Inventario
from Modelos.Productos import Productos
from Modelos.Proveedor import Proveedor
from Repositorios.RepositorioInventario import RepositorioInventario
from Repositorios.RepositorioProductos import RepositorioProductos
from Repositorios.RepositorioProveedor import RepositorioProveedor


class ControladorInventario():
    def __init__(self):
        self.repositorioInventario = RepositorioInventario()
        self.repositorioProductos = RepositorioProductos()
        self.repositorioProveedor = RepositorioProveedor()

    def index(self):
        return self.repositorioInventario.findAll()

    """
    Asignacion estudiante y materia a inscripción
    """

    def create(self, infoInventario, id_productos, id_proveedor):
        nuevoInventario = Inventario(infoInventario)
        elProductos = Productos(self.repositorioProductos.findById(id_productos))
        elProveedor = Proveedor(self.repositorioProveedor.findById(id_proveedor))
        nuevoInventario.Productos = elProductos
        nuevoInventario.Proveedor = elProveedor
        return self.repositorioInventario.save(nuevoInventario)

    def show(self, id):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        return elInventario.__dict__

    """
    Modificación de inventario (producto y proveedor)
    """

    def update(self, id, infoInventario, id_productos, id_proveedor):
        laInventario = Inventario(self.repositorioInventario.findById(id))
        laInventario.anio = infoInventario["año"]
        laInventario.semestre = infoInventario["semestre"]
        laInventario.notaFinal = infoInventario["nota_final"]
        elProductos = Productos(self.repositorioEstudiantes.findById(id_productos))
        laProveedor = Proveedor(self.repositorioMaterias.findById(id_proveedor))
        laInventario.Productos = elProductos
        laInventario.Proveedor = laProveedor
        return self.repositorioInventario.save(laInventario)

    def delete(self, id):
        return self.repositorioInventario.delete(id)
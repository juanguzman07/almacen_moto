from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorAdministrador import ControladorAdministrador
from Controladores.ControladorProductos import ControladorProductos
from Controladores.ControladorProveedor import ControladorProveedor
from Controladores.ControladorInvetario import ControladorInventario

app = Flask(__name__)
cors = CORS(app)

miControladorAdministrador = ControladorAdministrador()
miControladorProductos = ControladorProductos()
miControladorProveedor = ControladorProveedor()
miControladorInventario = ControladorInventario()

########################### Servicio Administrador #####################3
@app.route("/administradores", methods=['GET'])
def getAdministradores():
    json = miControladorAdministrador.index()
    return jsonify(json)


@app.route("/administradores", methods=['POST'])
def crearAdministrador():
    data = request.get_json()
    json = miControladorAdministrador.create(data)
    return jsonify(json)


@app.route("/admnistradores/<string:id>", methods=['GET'])
def getAdministrador(id):
    json = miControladorAdministrador.show(id)
    return jsonify(json)


@app.route("/administradores/<string:id>", methods=['PUT'])
def modificarAdministrador(id):
    data = request.get_json()
    json = miControladorAdministrador.update(id, data)
    return jsonify(json)


@app.route("/administradores/<string:id>", methods=['DELETE'])
def eliminarAdministrador(id):
    json = miControladorAdministrador.delete(id)
    return jsonify(json)


############################## Servicio Producto ######################
@app.route("/productos", methods=['GET'])
def getProductos():
    json = miControladorProductos.index()
    return jsonify(json)


@app.route("/productos", methods=['POST'])
def crearProducto():
    data = request.get_json()
    json = miControladorProductos.create(data)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['GET'])
def getProducto(id):
    json = miControladorProductos.show(id)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json = miControladorProductos.update(id, data)
    return jsonify(json)


@app.route("/productos/<string:id>", methods=['DELETE'])
def eliminarProducto(id):
    json = miControladorProductos.delete(id)
    return jsonify(json)


########################### Servicio Proveedor ##########################3
@app.route("/proveedores", methods=['GET'])
def getProveedores():
    json = miControladorProveedor.index()
    return jsonify(json)


@app.route("/proveedores", methods=['POST'])
def crearProveedor():
    data = request.get_json()
    json = miControladorProveedor.create(data)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['GET'])
def getProveedor(id):
    json = miControladorProveedor.show(id)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['PUT'])
def modificarProveedor(id):
    data = request.get_json()
    json = miControladorProveedor.update(id, data)
    return jsonify(json)


@app.route("/proveedores/<string:id>", methods=['DELETE'])
def eliminarProveedor(id):
    json = miControladorProveedor.delete(id)
    return jsonify(json)

################################### Servicio Inventario ###############################

@app.route("/Inventario", methods=['GET'])
def getInventarios():
    json = miControladorInventario.index()
    return jsonify(json)


@app.route("/Inventario/<string:id>", methods=['GET'])
def getInventario(id):
    json = miControladorInventario.show(id)
    return jsonify(json)


@app.route("/Inventario/Productos/<string:id_Productos>/Proveedor/<string:id_Proveedor>", methods=['POST'])
def crearInventario(id_Productos, id_Proveedor):
    data = request.get_json()
    json = miControladorInventario.create(data, id_Productos, id_Proveedor)
    return jsonify(json)


@app.route("/Inventario/<string:id>/Productos/<string:id_Productos>/Proveedor/<string:id_Proveedor>", methods=['PUT'])
def modificarInventario(id, id_Productos, id_Proyecto):
    data = request.get_json()
    json = miControladorInventario.update(id, id_Productos, id_Proyecto)
    return jsonify(json)


@app.route("/Inventario/<string:id>", methods=['DELETE'])
def eliminarInventario(id):
    json = miControladorInventario.delete(id)
    return jsonify(json)




@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
    Se crea la instancia del servidor con la url del backend y puerto especificado 
    en el archivo de configuración.
    """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

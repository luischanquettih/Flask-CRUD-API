from flask import Flask, request, jsonify
from flask_cors import CORS # importa la extension cors

app = Flask(__name__)
CORS(app)  # Aplica CORS a todas las rutas de la aplicación
stored_data = []  # Lista para almacenar los datos

# Ruta para el método GET
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'data': stored_data})

# Ruta para el método POST
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()

    # Almacena los datos en la lista
    stored_data.append(data)

    return jsonify({'message': 'Datos enviados y almacenados correctamente'})

# Ruta para actualizar valores específicos
@app.route('/api/update', methods=['PUT'])
def update_data():
    update_info = request.get_json()

    # Actualiza los valores correspondientes
    for item in stored_data:
        for key, value in update_info.items():
            if key in item:
                item[key] = value

    return jsonify({'message': 'Datos actualizados correctamente'})

# Ruta para eliminar una clave específica
@app.route('/api/delete', methods=['DELETE'])
def delete_key():
    delete_info = request.get_json()

    # Elimina la clave especificada de los datos almacenados
    for item in stored_data:
        for key in delete_info.get('keys', []):
            item.pop(key, None)

    # Elimina elementos vacíos de la lista
    stored_data[:] = [item for item in stored_data if item]

    return jsonify({'message': 'Claves eliminadas correctamente'})

if __name__ == '__main__':
    app.run(debug=True)

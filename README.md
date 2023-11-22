# Flask-CRUD-API
Este proyecto presenta una sencilla API CRUD (Create, Read, Update, Delete) construida con Flask, un framework web para Python. La aplicación permite realizar operaciones básicas en una lista de datos almacenados en memoria, accesibles a través de solicitudes HTTP.

## Requerimientos
- Flask: Framework web ligero para Python
- Flask-CORS: Extensión para manejar solicitudes de origen cruzado (CORS) en Flask

## Instalación de dependencias
```bash
pip install Flask Flask-CORS
```
## Ejecución
1. Ejecutar el script api_crud.py
2. Acceder a las siguientes rutas para realizar operaciones CRUD.
     
    GET: /api/data (Obtener todos los datos)
    ```bash
    curl -X GET https://luisalechh.onrender.com/api/data
    ```
    POST: /api/data (Agregar nuevos datos)
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"clave": "valor"}' https://luisalechh.onrender.com/api/data
    ``` 
    PUT: /api/update (Actualizar valores específicos)
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"clave": "nuevo_valor"}' https://luisalechh.onrender.com/api/update
    ``` 
    DELETE: /api/delete (Eliminar claves específicas)
    ```bash
    curl -X DELETE -H "Content-Type: application/json" -d '{"keys": ["clave1", "clave2"]}' https://luisalechh.onrender.com/api/delete
    ```
## Ejemplos de Uso
Aquí hay algunos ejemplos de cómo interactuar con la API utilizando la libreria 'requests' de python.
Obtener todos los datos (GET):
```bash
import requests

url = 'https://luisalechh.onrender.com/api/data'

# Realizar la solicitud GET
response = requests.get(url)

# Imprimir la respuesta
print(response.json())
```
Agregar nuevos datos (POST):
```bash
import requests

url = 'https://luisalechh.onrender.com/api/data'
cuerpo_solicitud = {
    "temperatura": "25"
}

# Realizar la solicitud POST
response = requests.post(url, json=cuerpo_solicitud)

# Imprimir la respuesta
print(response.json())
```
Actualizar valores específicos(PUT):
```bash
import requests

url = 'https://luisalechh.onrender.com/api/update'
cuerpo_solicitud = {
    "temperatura": "26"
}

# Realizar la solicitud PUT
response = requests.put(url, json=cuerpo_solicitud)

# Imprimir la respuesta
print(response.json())
```
Eliminar claves específicas(DELETE):
```bash
import requests

url = 'https://luisalechh.onrender.com/api/delete'
cuerpo_solicitud = {
    "keys": ["temperatura"]
}
# Realizar la solicitud DELETE
response = requests.delete(url, json=cuerpo_solicitud)

# Imprimir la respuesta
print(response.json())

```

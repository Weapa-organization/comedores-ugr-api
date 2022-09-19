# Comedores UGR API

Projecto para mejorar el uso de FastAPI y obtener el menu de comedores de la Universidad de Granada.

## Tecnologías involucradas

El lenguaje en este caso es Python 3.9, utilizando el framework de FastAPI, ya que permite la creación de manera rápida
de una API para el tratamiento de diferentes datos.

Como base de datos se va a utilizar MongoDB, desplegado en una Raspberry Pi mediante Docker.

La estructura a almacenar es como la mostrada en el archivo [example-menu.json](example-menu.json).

## Preparación

Para poder desplegar el siguiente repositorio, es necesario instalar los paquetes indicados en el requirements.txt.

Es recomendable antes de nada generar un entorno virtual, ya sea con `python venv` o con Anaconda.

Además es necesario por último generar en la raíz un archivo `.env`, utilizado en [config.py](app/core/config.py)
para establecer las variables de entorno:
- PROJECT_NAME="Comedores Ugr"
- BACKEND_CORS_ORIGINS=["http://localhost:8000",...]
- MONGODB_URL="mongodb://user:pass@uri:port"

### Despliegue en Docker

Se ha dejado adjunto un archivo [Dockerfile](Dockerfile) donde viene definida una imagen de python 3.9 version alpine.
Para su construcción y despliegue se pueden usar los siguientes comandos:

```bash
# Generar una imagen
docker build -t comedores .

# Lanzar el contenedor
docker run -d --name comedores -p 80:80 myimage

```

### Enlaces de interés

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [MongoDB Docs](https://www.mongodb.com/docs/)
- [Docker Docs](https://docs.docker.com/)
- [Getting started with FastAPI and MongoDB](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/)
# Comedores UGR API

Projecto para mejorar el uso de FastAPI y obtener el menu de comedores de la Universidad de Granada.

## Tecnologías involucradas

El lenguaje en este caso es Python 3.9, utilizando el framework de FastAPI, ya que permite la creación de manera rápida
de una API para el tratamiento de diferentes datos.

Como base de datos se va a utilizar MongoDB, desplegado en una Raspberry Pi mediante Docker.

La estructura a almacenar es como la mostrada en el archivo [example-menu.json](example-menu.json).

El acceso a Swagger de la API es mediante [http://localhost:80/docs](http://localhost:80/docs).

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

### Desplegar Docker Compose (FastAPI junto a MongoDB)

Al igual que en el anterior caso, se ha adjuntado un archivo [docker-compose.yml](./docker-compose.yml) donde se declaran
las imagenes de Mongo y Mongo Express, para poder lanzar todo el conjunto con un único comando:

```bash
# Generar la imágen correspondiente a la api
docker-compose build

# Lanzar y desplegar los contenedores
docker-compose up -d

# Parar los contenedores
docker-compose stop
```

El puerto actual para este caso es el 80:80, y es necesario una vez generado, crear una Base de Datos en Mongo llamada
`ComedoresUGR`, y a su vez dentro una collection llamada `menus`.

### Script para alimentar la Base de Datos

En el repo se encuentra un script llamado [scrapping.py](./scrapping.py). Este obtiene los datos de la url de [Comedores UGR](https://scu.ugr.es/pages/menu/comedor),
lo estructura y se lo envía a la API para que se encargue de almacenar esta información.

Para poder ejecutarlo, es necesario instalar las dependencias almacenadas en [requirements-scrapping.txt](./requirements-scrapping.txt).
Tras esto se podrá lanzar con `python scrapping.py`

### Bot realizado para publicar en Telegram los mensajes

Hay un fichero [bot.py](./bot.py) que contiene el código para desplegar un bot de Telegram, el cuál
recibe el comando `/hoy` y devuelve el menú del día, solicitando está información a toda la aplicación que se ha ido desarrollando
en el proyecto.

Este necesita los paquetes almacenados en [requirements-bot.txt](./requirements-bot.txt), que es en concreto pyTelegramBotAPI. 

### Enlaces de interés

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [MongoDB Docs](https://www.mongodb.com/docs/)
- [Docker Docs](https://docs.docker.com/)
- [Getting started with FastAPI and MongoDB](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/)
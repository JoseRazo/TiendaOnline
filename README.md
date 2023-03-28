# TiendaOnline

Tienda Online

## Pre-requisitos

- Instalar [Docker.](https://www.docker.com/get-started)
- Instalar [Docker Compose.](https://docs.docker.com/compose/install/)

## Instalación

- Clonar repositorio `git clone https://github.com/JoseRazo/TiendaOnline.git`
- Abrir proyecto con editor de codigo y configurar archivo **`.env`**
- Abrir terminal y entrar a la carpeta del proyecto `~/dev/django/TiendaOnline$`
- Generar imagen docker y contenedores con **`docker-compose build`** y **`docker-compose up -d`**
- Crear migraciones `docker compose run web python manage.py makemigrations`
- Ejecutar migraciones `docker compose run web python manage.py migrate`
- Crear superusuario **`docker compose run web python manage.py createsuperuser`**

## Abrir proyecto

Abrir navegador y entrar a URL [127.0.0.1:8888](http://127.0.0.1:8001)

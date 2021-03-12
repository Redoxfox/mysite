# mysite

Repositorio proyecto personal (portafolio).

Este repositorio es una iniciativa personal la cual tiene como finalidad la concentracion de una serie de proyectos personales los cuales en conjunto corresponde a mi portafolio de tecnologias web que manejo  frontend y backend en el momento las tecnolgias utilizadas para el proyecto son las siguientes.

Tecnologias frontend:

HTML
Javascript
CSS

Tecnologias backend:

Frameword Flask (python)
Python

Bases de datos:

Mysql

Sistema operativo 

Linux (distribucion Centos 7-Server Linux Ubuntu)

Estructura del proyecto:

* /mysite  "Carpeta raiz del proyecto".  
    * app/                         "Carpeta aplicacion". 
        - ## /config               * Carpeta con archivos de configuración. *
            - __init__.py          "Archivo para validar carpeta como paquete".
            - config.json          "Archivo  configuracion innorado en repositorio por - seguridad".
        - ** /model                   "Carpeta con modelos de la base de datos".
            - __init__.py          "Archivo para validar carpeta como paquete".
            - modeldb.py           "Archivo para modelos y consultas a base de datos".
        - /routes                  "Carpeta para configuracion de rutas y carpetas con diferentes rutas".
            - __init__.py          "Archivo para cofiguracion de acceso rutas".
            - /admin               "Carpeta con rutas para administrar el proyecto".
                - __init__.py     "Archivo para validar carpeta como paquete".
                - admin.py        "Archivo con metodos para administracion del proyecto".
                - login.py        "Archivo con metodos para logeo al proyecto".
                - registro.py     "Archivo con metodos para manejo de registros del proyecto".
                - validar.py      "Archivo con metodos para validacioes del proyecto".
                - view.py         "Archivo con metodos para gestionar vistas para admin proyecto".
            - /blog               "Carpeta con rutas para gestion de blog en el proyecto".
                - __init__.py     "Archivo para validar carpeta como paquete".
                - sopa_letras.py  "Archivo gestion de aplicacion entrada blog".
            - /project             "Carpeta con rutas para gestion de proyectos".
                - __init__.py      "Archivo para validar carpeta como paquete".
                - gastos.py        "Archivo gestion aplicacion gastos personales".
                - lavasplah.py     "Archivo gestion aplicacion de lavado ecologico de autos".
        - /static                  "Carpeta para gestion de estilos, js y librerias proyecto".
        - /css
        - /imgs
        - /js
        - /lib
        - /media 
    * run.py                        

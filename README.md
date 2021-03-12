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

Mysql (En este proyecto no se utiliza ORM se crea en su lugar un modelo personalizado de consultas solo como practica).

Sistema operativo 

Linux (distribucion Centos 7-Server Linux Ubuntu)

Estructura del proyecto:

* __/mysite__                          "Carpeta raiz del proyecto".  
    * __app/__                         "Carpeta aplicacion". 
        - __/config__                  "Carpeta con archivos de configuración."
            - __init__.py              "Archivo para validar carpeta como paquete".
            - __config.json__          "Archivo  configuracion innorado en repositorio por - seguridad".
        - __/model__                   "Carpeta con modelos de la base de datos".
            - __init__.py              "Archivo para validar carpeta como paquete".
            - __modeldb.py__           "Archivo para modelos y consultas a base de datos".
        - __/routes__                  "Carpeta para configuracion de rutas y carpetas con diferentes rutas".
            - __init__.py              "Archivo para cofiguracion de acceso rutas".
            - __/admin__               "Carpeta con rutas para administrar el proyecto".
                - __init__.py          "Archivo para validar carpeta como paquete".
                - __admin.py__         "Archivo con metodos para administracion del proyecto".
                - __login.py__         "Archivo con metodos para logeo al proyecto".
                - __registro.py__      "Archivo con metodos para manejo de registros del proyecto".
                - __validar.py__       "Archivo con metodos para validacioes del proyecto".
                - __view.py__          "Archivo con metodos para gestionar vistas para admin proyecto".
            - __/blog__                "Carpeta con rutas para gestion de blog en el proyecto".
                - __init__.py          "Archivo para validar carpeta como paquete".
                - __sopa_letras.py__   "Archivo gestion de aplicacion entrada blog".
            - __/project__             "Carpeta con rutas para gestion de proyectos".
                - __init__.py          "Archivo para validar carpeta como paquete".
                - __gastos.py__        "Archivo gestion aplicacion gastos personales".
                - __lavasplah.py__     "Archivo gestion aplicacion de lavado ecologico de autos".
        - __/static__                  "Carpeta para gestion de estilos, js y librerias proyecto".
        - __/css__
        - __/imgs__
        - __/js__
        - __/lib__
        - __/media__ 
    * __run.py__                       "Archivo arranque del proyecto". 

El proyecto se encuentra aun desarrollo porque los ultimos meses lo he abandonado un poco y me he dedicado a un proyecto de emprendimiento personal. Por ese motivo Aplicaciones como la de finanzas personales solo cuenta con un calendario sin embargo este calendario es generado automaticamente por el sistema sin la necesidad de una libreria externa como es habitual. Y la Aplicacion de geolocalizacion aun falta hacerla mas dinamica  este es link del proyecto en desplegado en pythonanywhere.

___
[Proyecto Personal Portafolio](https://redoxfox1.pythonanywhere.com/) 

Y este es link de mi otro gran proyecto personal desplegado en DigitalOcean

[Proyecto Personal Emprendimiento](https://www.sandyvitalstore.com/) 



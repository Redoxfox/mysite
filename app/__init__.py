from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

#Rutas de administracion 
from app.routes.admin import view
from app.routes.admin import admin
from app.routes.admin import login
from app.routes.admin import registro
from app.routes.admin import validar

#Rutas de proyectos portafolio
from app.routes.project import lavasplah
from app.routes.project import gastos

#Rutas de entradas blog portafolio
from app.routes.blog import sopa_letras

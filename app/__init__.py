from flask import Flask,render_template,request

app = Flask(__name__)

#Rutas de administracion 
from app.routes.admin import view
from app.routes.admin import admin
from app.routes.admin import login
from app.routes.admin import validar

from app.routes.project import lavasplah
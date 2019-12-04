from flask import Flask, render_template, Blueprint, request, redirect, url_for
import pymysql.cursors
from app.model.modeldb import Model
from app.config import config
from app.model.modeldb import Model
from app.config.config import urldirection
from app.model.validaciones import Validar
import json
app = Flask(__name__)
f =open("./app/config/config.json","r")
file=f.read()
CONFIG = json.loads(file)
URLBASE = CONFIG['DEFAULT']['URLBASE']

#Rutas de administracion 
from app.routes.admin import view
from app.routes.admin import admin
from app.routes.admin import login
from app.routes.admin import validar

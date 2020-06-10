from app import app, request
from app import app, render_template
from app.model.modeldb import Model
from app.static.lib import validaciones
import os
import json
from datetime import datetime, date
import re
from flask import jsonify

dir_act = os.getcwd()
route_file_config = dir_act 
route_exist = route_file_config.find("mysite")
if route_exist > 0:
    route_file_config = dir_act + "/app/config/config.json"
else:
    route_file_config = dir_act + "/mysite/app/config/config.json"

f =open(route_file_config,"r")
file=f.read()
CONFIG = json.loads(file)
MODODESARROLLO = 'DEFAULT'
URLBASE = CONFIG['DEFAULT']['URLBASE']


""" @app.route("/validar", methods=["GET", "POST"])
def validar():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    if request.method == "POST":
        nick = request.form["username"]
        password = request.form["password"]
    
    wid = nick
    TSWusers = dict()
    TSWusers = {'TABLE': 'users',
        'Col1': 'nick',
        'Col2': 'password',
        'Col3': 'salt',
        'Col4': 'tipo_user',
        'Whe5': 'nick=%s'
        }
         
    Data = (wid,)
    DatosUsers = connect.SW_TABLE(username,TSWusers, Data)
    
    if DatosUsers:
        password_userbd = DatosUsers[0]['password']
        salt_userbd = DatosUsers[0]['salt']
        tipo_user = DatosUsers[0]['tipo_user']
        hash= validaciones.Validar()
        h2=hash.check_password(password_userbd, password, salt_userbd)

        if h2 == True and tipo_user=="admin":
            return render_template("/admin/principal.html")
        else:
            return render_template("/registro/login.html") 
    else:
        return render_template("/registro/login.html") """
        
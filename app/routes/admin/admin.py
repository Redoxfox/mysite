from app import app, request, url_for, redirect
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
    server = "local"
else:
    route_file_config = dir_act + "/mysite/app/config/config.json"
    server = "server"

f = open(route_file_config , "r")
file = f.read()
CONFIG = json.loads(file)
MODODESARROLLO = 'DEFAULT'
URLBASE = CONFIG['DEFAULT']['URLBASE']

@app.route("/admin/", methods=["GET", "POST"])
def admin():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    return render_template("/admin/principal.html")

@app.route("/tablas/", methods=["GET", "POST"])
def tablas():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username) 
    tablas = connect.SHOW_TABLES(username)
    print(tablas)
    nom_server = {}
    nom_server["server"] = server 
    tablas.append(nom_server)
    result = json.dumps(tablas)

    return (result)

@app.route("/validar", methods=["GET", "POST"])
def validar():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username) 
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
    DatosUsers = connect.SW_TABLE(username, TSWusers, Data)
    password_userbd = DatosUsers[0]['password']
    salt_userbd = DatosUsers[0]['salt']
    tipo_user = DatosUsers[0]['tipo_user']
    hash = validaciones.Validar()
    #myhash=[]
    #myhash=hash.hash_password(password)
    #salt=myhash[0]
    #myhash1=myhash[1]
    h2 = hash.check_password(password_userbd, password, salt_userbd)
    
    if h2 is True and tipo_user == "admin":
        return redirect(url_for('admin'))
    else:
        return render_template("/registro/login.html")

@app.route("/Estructura_tabla/", methods=["POST"])
def Estructura_tabla():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username)   
    req = request.get_json()
    nombreTabla = req["nombreTabla"]
    campos_tabla = connect.DESCRIBE_TABLES(username,  nombreTabla)
    print (nombreTabla)
    estructura = json.dumps(campos_tabla)
    #print(type(result))
    #res = make_response(jsonify({"message": "OK"}), 200) 
    #result1 = "hola"
    
    return (estructura)

@app.route("/add_topico/", methods=["POST"])
def add_topico():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username)   
    req = request.get_json()
    result = {}
    wid = req["topico"]
    topico = wid
    nombre_id = "id"
    nombre_tabla = "grupo"
    id = None
    Insert_ofgrupo = dict()
    Insert_ofgrupo = {'TABLE':'grupo',
            'Col1':'id',
            'Col2':'topico',
            'Val3':'%s',
            'Val4':'%s'
    }
    Data = [id, topico]
    result["new_topico"] = wid 
    res_insert = connect.IT_TABLE(username, Insert_ofgrupo , Data) 
    
    return result

@app.route("/add_palabra/", methods=["POST"])
def add_palabra():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username)   
    req = request.get_json()
    result = {}
    id = None
    english = req["english"].upper()
    spanish = req["spanish"].upper() 
    grupo = req["grupo"] 
    ejemplos = req["ejemplos"]
    
    
    wid = english
    TSWVocabulary = dict()
    TSWVocabulary = {'TABLE': 'vocabulary', 
        'Col1': 'english',
        'Whe2': 'english=%s'
    }
         
    Data = (wid,)
    DatosVocabulary = connect.SW_TABLE(username, TSWVocabulary, Data)

    if DatosVocabulary:
        result["new_topico"] = "Ya se encuentra registrado " + english + " en BD"
    else:
        Insert_ofvocabulary = dict()
        Insert_ofvocabulary = {'TABLE':'vocabulary',
            'Col1':'id',
            'Col2':'english',
            'Col3':'spanish',
            'Col4':'grupo',
            'Col5':'ejemplos',
            'Val6':'%s',
            'Val7':'%s',
            'Val8':'%s',
            'Val9':'%s',
            'Val10':'%s'
        }
        Data = [id,  english, spanish,  grupo, ejemplos]
        result["new_topico"] = "Registro exitoso"
        res_insert = connect.IT_TABLE(username,  Insert_ofvocabulary, Data) 
        
        
    
    return result

@app.route("/grupos/")
def grupos():
    urlrev = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    
    Tabla_All_Grupos = dict()
    Tabla_All_Grupos = {'TABLE':'grupo',
        'Col1':'id',
        'Col2':'topico'
    }
   
    DatosAllGrupos = connect.SSP_TABLE(username, Tabla_All_Grupos)

    DatosAllGrupos_json = json.dumps(DatosAllGrupos) 
    
    return (DatosAllGrupos_json)


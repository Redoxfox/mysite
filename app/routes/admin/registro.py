from app import app, request
from app import app, render_template
from app.model.modeldb import Model
from app.static.lib import validaciones
import os
import json


dir_act = os.getcwd()
route_file_config = dir_act 
route_exist = route_file_config.find("mysite")
if route_exist > 0:
    route_file_config = dir_act + "/app/config/config.json"
else:
    route_file_config = dir_act + "/mysite/app/config/config.json"

f = open(route_file_config, "r")
file = f.read()
CONFIG = json.loads(file)
MODODESARROLLO = 'DEFAULT'
URLBASE = CONFIG['DEFAULT']['URLBASE']


@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render_template("/registro/registro.html")

@app.route("/singup", methods=["GET", "POST"])
def singup():
    urlrev = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username)  
    if request.method == "POST":
        id = None
        nick = request.form['nick']
        nombre = request.form['name']
        email = request.form['Email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        password = request.form['password']
        Insert_users = dict()
        Insert_users = {'TABLE': 'users',
                        'Col1': 'id',
                        'Col2': 'nick',
                        'Col3': 'nombre',
                        'Col4': 'email',
                        'Col5': 'direccion',
                        'Col6': 'telefono',
                        'Col7': 'password',
                        'Col8': 'salt',
                        'Val9': '%s',
                        'Val10': '%s',
                        'Val11': '%s',
                        'Val12': '%s',
                        'Val13': '%s',
                        'Val14': '%s'}

        hash = validaciones.Validar()
        pass_hash = []
        pass_hash = hash.hash_password(password)
        salt = pass_hash[0]
        password_hash = pass_hash[1]
        Data = [id, nick, nombre, email, direccion, telefono, password_hash, salt]
        connect.IT_TABLE(username, Insert_users, Data) 

    return render_template("/registro/login.html", url = urlrev)

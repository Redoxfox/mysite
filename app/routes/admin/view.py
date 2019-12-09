from app import app, render_template
from app.model.modeldb import Model
import os
import json
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

print(dir_act)
print(os.path.isfile(route_file_config))
print(os.path.isdir('app/config'))

@app.route("/")
def index():

    Sql="ddasddf"
    lista = URLBASE
    connect=Model("root")   
    username = CONFIG['TYPE_USER']['ROOT']
    Nick = "Redoxfox"
    TSWusers = dict()
    TSWusers = {'TABLE':'users',
        'Col1':'nick',
        'Col2':'password',
        'Col3':'salt',
        'Whe4':'nick=%s'
        }
    Data = (Nick,)
    DatosUsers = connect.SW_TABLE(username,TSWusers,Data)
    return render_template("index.html", sql = Sql, lista = DatosUsers)
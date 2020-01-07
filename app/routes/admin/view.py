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
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username)   
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

    '''  TCliente = dict()
    TCliente = {'TABLE':'elementos2',
        'id':'INT AUTO_INCREMENT',
        'id_servicio':'INT NOT NULL',
        'id_cliente':'INT NOT NULL',
        'PK':'id'
    }

    createtable = connect.CT_TABLE(username, TCliente)  

    #print(createtable)
    #print(DatosUsers)

    #Insertar datos forma simple
    id = None
    id_servicio = "3"
    id_cliente = "3"
    Data = [id, id_servicio, id_cliente]
    Insert_client= dict()
    Insert_client= {'TABLE':'elementos2',
            'Col1':'id',
            'Col2':'id_servicio',
            'Col3':'id_cliente',
            'Val4':'%s',
            'Val5':'%s',
            'Val6':'%s'   
        }
    
    insertsimple = connect.IT_TABLE(username, Insert_client, Data) 

    print(insertsimple)'''

    '''#Consultar datos de forma simple
    TSSClient = dict()
    TSSClient = {'TABLE':'clientes',
    'Col1':'id',
    'Col2':'nombre',
    'Col3':'direccion',
    'Col4':'telefono',
    'Col5':'nit',
    'Col6':'email',
    'Col7':'web'
        }
    DatosUsers = connect.SSP_TABLE(username,TSSClient)

    print (DatosUsers)

    #Eliminar fila de acuerdo a una condicion.
    id = "2"
    id2 = "4"
    delete_ofservicio = dict()
    delete_ofservicio = {'TABLE':'elementos2',
            'Whe1':'id>' + id +' and  id < ' + id2 
        }
    delete = connect.DELWT_TABLE(username, delete_ofservicio)

    print(delete)'''

    '''id = "4"
    id_servicio = "5"
    id_cliente = "5"
    Data = [id_servicio, id_cliente, id]
    Update_ofIngreso= {'TABLE':'elementos2',
            'Val1':'id_servicio=%s',
            'Val2':'id_cliente=%s',
            'Whe3':'id= %s'
        }

    insertsimple = connect.UPWT_TABLE(username, Update_ofIngreso, Data)

    print(insertsimple)'''
    
    return render_template("index.html", sql = Sql, lista = DatosUsers)
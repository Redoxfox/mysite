from app import app, request
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


@app.route("/lavasplash/index_ls")
def index_ls():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username)   
    #urlrev = URLBASE
    TSSServicioPtado  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        }
    DatosServicioPtado = connect.SSP_TABLE(username,TSSServicioPtado)
    return render_template("home_ls.html", url= Urlbase, servicios = DatosServicioPtado)

#Consultar servicios prestados
@app.route('/reg_prestado/<id>/', methods=['POST', 'GET'])
def reg_prestado(id):
    urlrev = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    wid = id
    TSSServicioPtado = dict()
    TSSServicioPtado  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        'Whe4':'id=%s'
        }
    Data = (wid,)
    DatosServicioPtado = connect.SW_TABLE(username,TSSServicioPtado, Data)
    
    TSSClient = dict()
    TSSClient = {'TABLE':'clientes',
    'Col1':'id',
    'Col2':'nombre'
        }
    DatosClient = connect.SSP_TABLE(username,TSSClient)

    return render_template("form_registro_servicio.html", url = urlrev, servicios = DatosServicioPtado, 
    clientes=DatosClient) 

#Insertar nuevo servicio prestado
@app.route("/InsertNewServicioPtdo", methods=["GET", "POST"])
def InsertNewServicioPtdo(): 
    urlrev = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    if request.method == "POST":
        id = None
        id_servicio = request.form['idservicio']
        id_cliente = request.form['cliente']
        costo = request.form['costo']
        fecha = request.form['fecha']
        costo_descuento = request.form['costo_descuento']
        obs = request.form['obs']

        porc_descuento = float(costo_descuento)/float(costo)
        costo_total = float(costo) * porc_descuento
        if costo_total == 0:
             costo_total = float(costo)
        else:
            costo_total = costo_total
            
        descuento = float(costo) - costo_total

        Insert_ofservicioPtdo = dict()
        Insert_ofservicioPtdo = {'TABLE':'servicios',
            'Col1':'id',
            'Col2':'id_servicio',
            'Col3':'id_cliente',
            'Col4':'descuento',
            'Col5':'costo_total',
            'Col6':'costo_desc',
            'Col7':'fecha',
            'Col8':'observacion',
            'Val9':'%s',
            'Val10':'%s',
            'Val11':'%s',
            'Val12':'%s', 
            'Val13':'%s',
            'Val14':'%s',
            'Val15':'%s',
            'Val16':'%s' 
        }
        Data = [id, id_servicio, id_cliente, porc_descuento, costo_total, descuento, fecha, obs]
        res_insert = connect.IT_TABLE(username, Insert_ofservicioPtdo, Data) 
        

        TSSServicioPtado = dict()
        TSSServicioPtado  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        }
        DatosServicioPtado = connect.SSP_TABLE(username,TSSServicioPtado)
    
    return render_template("home_ls.html", url = urlrev, servicios = DatosServicioPtado)

#Lista de servicios ofertados.
@app.route("/ListaOfServicios", methods=["GET", "POST"])
def ListaOfServicios():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    TSSOfServicio = dict()
    TSSOfServicio  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        'Col4':'detalles'
        }
    '''TSOfSevicio = Model(TSSOfServicio)
    sql = TSOfSevicio.SSP_TABLE()
    cursor = db1.cursor()
    cursor.execute(sql)
    DatosOfServicio = cursor.fetchall()'''
    DatosOfServicio = connect.SSP_TABLE(username,TSSOfServicio)

    return render_template("ListaOfServicios.html", url = urlrev, Oferta_Servicio = DatosOfServicio)

#Editar servicio ofertado
@app.route('/ActualizarServicio/', methods=['POST', 'GET'])
def ActualizarServicio():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    if request.method == "POST":
        id = request.form['id']
        tipo = request.form['tipo']
        costo = request.form['costo']
        obs = request.form['obs']
    Update_ofservicio = dict()
    Update_ofservicio = {'TABLE':'servicio',
            'Val1':'tipo=%s',
            'Val2':'costo=%s',
            'Val3':'detalles=%s',
            'Whe4':'id='+ id
        }
    Data = [tipo, costo, obs]
    '''Update_TOServicio= Model(Update_ofservicio)
    sql = Update_TOServicio.UPT_TABLE()
    cursor = db1.cursor()
    cursor.execute(sql, (tipo, costo, obs))
    cursor.close()
    db1.commit()'''

    res_update = connect.UPWT_TABLE(username, Update_ofservicio, Data)

    TSSOfServicio = dict()
    TSSOfServicio  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        'Col4':'detalles'
        }
    DatosOfServicio = connect.SSP_TABLE(username,TSSOfServicio)
    return render_template("ListaOfServicios.html", url = urlrev, Oferta_Servicio = DatosOfServicio)

#Nueva oferta servicio
@app.route("/NewOfServicio", methods=["GET", "POST"])
def NewOfServicio():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    TSSOfServicio = dict()
    TSSOfServicio  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        'Col4':'detalles'
        }
    DatosOfServicio = connect.SSP_TABLE(username,TSSOfServicio)
    return render_template("form_new_servicio.html", url = urlrev, Oferta_Servicio = DatosOfServicio)  


#Nuevo servicio prestado
@app.route("/NewServicioPtado", methods=["GET", "POST"])
def NewServicioPtado():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    TSSServicioPtado = dict()
    TSSServicioPtado  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        }
    DatosServicioPtado = connect.SSP_TABLE(username,TSSServicioPtado)
    return render_template("form_new_servicios.html", url = urlrev, servicios = DatosServicioPtado)  

#Editar servicio ofertado
@app.route('/VerDetallesServicio/<id>/', methods=['POST', 'GET'])
def VerDetallesServicio(id):
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    TSSOfServicio = dict()
    wid = id
    TSSOfServicio  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        'Col4':'detalles',
        'Whe5':'id=%s'
        }
    Data = (wid,)
    DatosOfServicio = connect.SW_TABLE(username,TSSOfServicio, Data)
    return render_template("ActualizarServicio.html", url = urlrev,  Oferta_Servicio = DatosOfServicio) 

#Eliminar servicio ofertado
@app.route('/EliminarServicio/<id>/', methods=['POST', 'GET'])
def EliminarServicio(id):
    urlrev = URLBASE 
    delete_ofservicio = dict()
    delete_ofservicio = {'TABLE':'servicio',
            'Whe1':'id=' + id
        }
    Del_TOServicioPtdo= Model(delete_ofservicio)
    sql = Del_TOServicioPtdo.DELWT_TABLE()
    cursor = db1.cursor()
    cursor.execute(sql)
    cursor.close()
    db1.commit()
    TSSOfServicio = dict()
    TSSOfServicio  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        'Col4':'detalles'
        }
    TSOfSevicio = Model(TSSOfServicio)
    sql = TSOfSevicio.SSP_TABLE()
    cursor = db1.cursor()
    cursor.execute(sql)
    DatosOfServicio = cursor.fetchall()

    return render_template("ListaOfServicios.html", url = urlrev, Oferta_Servicio = DatosOfServicio)



from app import app, request
from app import app, render_template
from app.model.modeldb import Model
from app.static.lib import procesar_fechas
import os
import json
from datetime import datetime, date
import re
from flask import jsonify
import numpy as np


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

##################################################
# Gestion de servicios prestados
##################################################
##################################################
# Operacion con servicios prestados
##################################################
#Calculo de gastos
@app.route('/ProcesarServicios/', methods=['POST', 'GET'])
def ProcesarServicios( ):
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    
    lista = dict()
    lista = {'view':'ListaOfServicios'
        }
    detalle = []
    servicio_mes = []
    gasto_mes = []
    #Lista de servicios ofertados.
    TSSOfServicioOftado = dict()
    TSSOfServicioOftado  = {'TABLE':'servicios order by fecha',
        'Col1':'id',
        'Col2':'costo_total',
        'Col3':'fecha'
        }
    DatosOfServicioOftado= connect.SSP_TABLE(username,TSSOfServicioOftado)

    return render_template("saldo.html", url = urlrev, lista=lista, total = detalle, Softado=DatosOfServicioOftado)

##################################################
# Operacion con servicios prestados
##################################################
#Consulta de servicios prestados por dia mes  
@app.route('/mes/<string:dia_mes>', methods=['POST', 'GET'])
def mes(dia_mes):
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    lista = dict()
    lista = {'view':'ListaOfServicios'
        }
    detalle = []
    servicio_mes = []
    gasto_mes = []
    #Lista de servicios ofertados.
    TSSOfServicioOftado = dict()
    TSSOfServicioOftado  = {'TABLE':'servicios order by fecha',
        'Col1':'id',
        'Col2':'costo_total',
        'Col3':'fecha'
        }
    DatosOfServicioOftado= connect.SSP_TABLE(username,TSSOfServicioOftado)
    
    mis_servicios = {}
    fecha_recibida = procesar_fechas.proc_fecha()
    day_init = fecha_recibida.first_day_year(dia_mes)
    
    #print(day_init)
    #listfecha = fecha_recibida.datosdb(dia_mes)
    cont = 0
    
    #print(listfecha)

    year_res = fecha_recibida.year_fecha(dia_mes)
    mes_res = fecha_recibida.month_fecha(dia_mes)
    dia_res = fecha_recibida.day_fecha(dia_mes)
    nom_mes = fecha_recibida.nombre_mes(dia_mes)


    for rows in DatosOfServicioOftado:
        id = rows["id"]
        costo_total = rows["costo_total"]
        fecha = str(rows["fecha"])

        year = fecha_recibida.year_fecha(fecha)
        mes = fecha_recibida.month_fecha(fecha)
        dia = fecha_recibida.day_fecha(fecha)

        cont += 1
        

        if mes == mes_res and  year == year_res and  dia == dia_res:
            servicio_mes.append(costo_total)
            mis_servicios[cont]= {"_id":id, 
                "costo_total":costo_total,
                "fecha": fecha,
                "dia": dia,
                "url": urlrev,
                "mes": nom_mes
            }
            
    return (mis_servicios)

#Consulta de servicios prestados por  mes  
@app.route('/mes_year/<string:mes_year>', methods=['POST', 'GET'])
def mes_year(mes_year):
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    lista = dict()
    lista = {'view':'ListaOfServicios'
        }
    detalle = []
    servicio_mes = []
    gasto_mes = []
    #Lista de servicios ofertados.
    TSSOfServicioOftado = dict()
    TSSOfServicioOftado  = {'TABLE':'servicios order by fecha',
        'Col1':'id',
        'Col2':'costo_total',
        'Col3':'fecha'
        }
    DatosOfServicioOftado= connect.SSP_TABLE(username,TSSOfServicioOftado)
    
    mis_servicios = {}
    fecha_recibida = procesar_fechas.proc_fecha()
   
    cont = 0

    year_res = fecha_recibida.year_fecha(mes_year)
    mes_res = fecha_recibida.month_fecha(mes_year)
    dia_res = fecha_recibida.day_fecha(mes_year)
    nom_mes = fecha_recibida.nombre_mes(mes_year)


    for rows in DatosOfServicioOftado:
        id = rows["id"]
        costo_total = rows["costo_total"]
        fecha = str(rows["fecha"])

        year = fecha_recibida.year_fecha(fecha)
        mes = fecha_recibida.month_fecha(fecha)
        dia = fecha_recibida.day_fecha(fecha)

        cont += 1
        

        if mes == mes_res and  year == year_res:
            servicio_mes.append(costo_total)
            mis_servicios[cont]= {"_id":id, 
                "costo_total":costo_total,
                "fecha": fecha,
                "dia": dia,
                "url": urlrev,
                "mes": nom_mes
            }
            
    return (mis_servicios)


#Consulta de servicios prestados por  mes  
@app.route('/between_date/<string:day_ini>/<string:day_end>/', methods=['POST', 'GET'])
def betwwen_date(day_ini, day_end):
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    lista = dict()
    lista = {'view':'ListaOfServicios'
        }
    detalle = []
    servicio_mes = []
    gasto_mes = []
    datos_fechas = []
    #Lista de servicios ofertados.
    TSSOfServicioOftado = dict()
    TSSOfServicioOftado  = {'TABLE':'servicios order by fecha',
        'Col1':'id',
        'Col2':'costo_total',
        'Col3':'fecha'
        }
    DatosOfServicioOftado= connect.SSP_TABLE(username,TSSOfServicioOftado)
    
    mis_servicios = {}
    data = {}
    
    
    fecha_recibida = procesar_fechas.proc_fecha()
    datos_fechas = fecha_recibida.date_between(day_ini, day_end)
    fecha_ini = fecha_recibida.Numero_dias(day_ini)
    fecha_end = fecha_recibida.Numero_dias(day_end)


    for rows in DatosOfServicioOftado:
        id = rows["id"]
        costo_total = rows["costo_total"]
        fecha = str(rows["fecha"])
        year_db = fecha_recibida.year_fecha(fecha)
        result = data.get(year_db)
        numero_day_fecha = fecha_recibida.Numero_dias(fecha)
     
      
        if(result == None):
            servicios_mes = {}
            servicios_mes["Enero"] = []
            servicios_mes["Febrero"] = []
            servicios_mes["Marzo"] = []
            servicios_mes["Abril"] = []
            servicios_mes["Mayo"] = []
            servicios_mes["Junio"] = []
            servicios_mes["Julio"] = []
            servicios_mes["Agosto"] = []
            servicios_mes["Septiembre"] = []
            servicios_mes["Octubre"] = []
            servicios_mes["Noviembre"] = []
            servicios_mes["Diciembre"] = [] 
            data[year_db] = servicios_mes
           
            if numero_day_fecha >= fecha_ini and numero_day_fecha <= fecha_end:
               
                year = fecha_recibida.year_fecha(fecha)
                mes = fecha_recibida.month_fecha(fecha)
                dia = fecha_recibida.day_fecha(fecha)
                nom_mes = fecha_recibida.nombre_mes(fecha)
                
                servicio_mes.append(costo_total)
                data[year_db][nom_mes].append({"_id":id, 
                        "costo_total":costo_total,
                        "fecha": fecha,
                        "dia": dia,
                        "url": urlrev,
                        "mes": nom_mes,
                        "year":year
                        })  
        else:
            if numero_day_fecha >= fecha_ini and numero_day_fecha <= fecha_end:
                year = fecha_recibida.year_fecha(fecha)
                mes = fecha_recibida.month_fecha(fecha)
                dia = fecha_recibida.day_fecha(fecha)
                nom_mes = fecha_recibida.nombre_mes(fecha)
            
            
                data[year_db][nom_mes].append({"_id":id, 
                        "costo_total":costo_total,
                        "fecha": fecha,
                        "dia": dia,
                        "url": urlrev,
                        "mes": nom_mes,
                        "year":year
                        })  

    meses_json = json.dumps(data)    
                             
    return (meses_json)

@app.route('/Clientes/', methods=['POST', 'GET'])
def Clientes():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    TSSOfServicioOftado = dict()
    TSSOfServicioOftado  = {'TABLE':'clientes order by id',
        'Col1':'id',
        'Col2':'nombre',
        'Col3':'direccion',
        'Col4':'telefono',
        'Col5':'nit',
        'Col6':'email',
        'Col7':'web',
        'Col8':'image',
        }
    DatosOfServicioOftado= connect.SSP_TABLE(username,TSSOfServicioOftado)
    
    return render_template("users.html", url = urlrev, Oferta_Servicio = DatosOfServicioOftado)

''' @app.route('/Clientes/Users/', methods=['POST', 'GET'])
def Clientes_users():
    urlrev = URLBASE 
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username) 
    direction = ["Cl 56 # 45-15",
    "Cra 34 # 17-14",
    "Cl 84 # 88-14",
    "Cl 43 # 65-19",
    "Cra 33a # 12-14",
    "Cl 16K # 24-26",
    "Cra 83 # 33-23",
    "Cl 14 # 64-26",
    "Cll 22 # 33-62",
    "Cll 10 # 44-26"
     ]
    req = request.get_json()
    cont = 0
    idc = 9
    for item in req:
        idx = idc + 1
        id = str(idx) 
        print(item["name"])
        nombre=item["company"]["name"]
        direccion=direction [cont]
        telefono=item["phone"]
        nit = item["address"]["zipcode"]
        email = item["email"]
        web = item["website"]
        Insert_client= dict()
        Insert_client= {'TABLE':'clientes',
            'Val1':'nombre=%s',
            'Val2':'direccion=%s',
            'Val3':'telefono=%s',
            'Val4':'nit=%s',
            'Val5':'email=%s',
            'Val6':'web=%s',
            'Whe7':'id='+ id
        } 
        Data = [nombre, direccion, telefono, nit, email, web]
        res_update = connect.UPWT_TABLE(username, Insert_client, Data)
        idc+=1
        cont+=1
    
    
    #req
    #print(req[0]["address"]["street"])
   
        
    res = {"messaje":"JSON received"}
    meses_json = json.dumps(res) 
    #res_update = connect.UPWT_TABLE(username, Update_ofservicio, Data)

    return  res  '''


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


@app.route("/gastos/index_gp")
def index_gp():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username)   
    TSSServicioPtado  = {'TABLE':'servicio',
        'Col1':'id',
        'Col2':'tipo',
        'Col3':'costo',
        }
    DatosServicioPtado = connect.SSP_TABLE(username,TSSServicioPtado)
  
    today = date.today()
    year_req = today.year
    month_req = today.month 

    month_next = month_req + 1
    month_back = month_req - 1

    if month_next == 13:
       month_next = 1
       year_req =  year_req + 1

    if month_next == 0:
       month_back = 12
       year_req =  year_req - 1

    meses = {1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
    }

    Datos_function = {}

    

    Datos_function["num_month_ant"] = "mes_anterior(" + str(month_back) + "," + str(year_req) + ")"
    Datos_function["num_month_act"] = "mes_actual(" + str(month_req) + "," + str(year_req) + ")"
    Datos_function["num_month_sig"] = "mes_siguiente(" + str(month_next) + "," + str(year_req) + ")"
    Datos_function["name_month_ant"] = meses[month_back] + "-" + str(year_req) 
    Datos_function["name_month_act"] = meses[month_req]  + " " + str(year_req) 
    Datos_function["name_month_sig"] = meses[month_next] + "-" + str(year_req) 


    fecha_recibida = procesar_fechas.proc_fecha()
    day_month = fecha_recibida.days_month(year_req,month_req) 
    num_day_first_week = {"domingo":1,
        "lunes": 2,
        "martes":3,
        "miercoles":4,
        "jueves":5,
        "viernes":6,
        "sabado":7
        }  

    day_weekx = {1:"sem1_d1",
        2: "sem1_d2",
        3:"sem1_d3",
        4:"sem1_d4",
        5:"sem1_d5",
        6:"sem1_d6",
        7:"sem1_d7",
        8:"sem2_d1",
        9:"sem2_d2",
        10:"sem2_d3",
        11:"sem2_d4",
        12:"sem2_d5",
        13:"sem2_d6",
        14:"sem2_d7",
        15:"sem3_d1",
        16:"sem3_d2",
        17:"sem3_d3",
        18:"sem3_d4",
        19:"sem3_d5",
        20:"sem3_d6",
        21:"sem3_d7",
        22:"sem4_d1",
        23:"sem4_d2",
        24:"sem4_d3",
        25:"sem4_d4",
        26:"sem4_d5",
        27:"sem4_d6",
        28:"sem4_d7",
        29:"sem5_d1",
        30:"sem5_d2",
        31:"sem5_d3",
        32:"sem5_d4",
        33:"sem5_d5",
        34:"sem5_d6",
        35:"sem5_d7",
        }  
    day_of_week = {}

    first_day = num_day_first_week[day_month[1]]
    for item in day_month:
        name_number_week = day_weekx[first_day]
        day_of_week[name_number_week]= item
        first_day +=  1

 
    return render_template("/gastos/gestion_gastos.html", url= Urlbase, servicios = DatosServicioPtado, 
    month = day_of_week, datos = Datos_function)

@app.route("/mes_calendar/<string:month>/<string:year>/")
def mes_calendar(month, year):
    fecha_recibida = procesar_fechas.proc_fecha()
    year_req = int(year) 
    month_req = int(month)
    day_month = fecha_recibida.days_month(year_req,month_req) 
    num_day_first_week = {"domingo":1,
        "lunes": 2,
        "martes":3,
        "miercoles":4,
        "jueves":5,
        "viernes":6,
        "sabado":7
        }  

    day_weekx = {1:"sem1_d1",
        2: "sem1_d2",
        3:"sem1_d3",
        4:"sem1_d4",
        5:"sem1_d5",
        6:"sem1_d6",
        7:"sem1_d7",
        8:"sem2_d1",
        9:"sem2_d2",
        10:"sem2_d3",
        11:"sem2_d4",
        12:"sem2_d5",
        13:"sem2_d6",
        14:"sem2_d7",
        15:"sem3_d1",
        16:"sem3_d2",
        17:"sem3_d3",
        18:"sem3_d4",
        19:"sem3_d5",
        20:"sem3_d6",
        21:"sem3_d7",
        22:"sem4_d1",
        23:"sem4_d2",
        24:"sem4_d3",
        25:"sem4_d4",
        26:"sem4_d5",
        27:"sem4_d6",
        28:"sem4_d7",
        29:"sem5_d1",
        30:"sem5_d2",
        31:"sem5_d3",
        32:"sem5_d4",
        33:"sem5_d5",
        34:"sem5_d6",
        35:"sem5_d7",
        36:"sem6_d1",
        37:"sem6_d2",
        38:"sem6_d3",
        39:"sem6_d4",
        40:"sem6_d5",
        41:"sem6_d6",
        42:"sem6_d7" 
      
        }  

   
    day_of_week = {}
    first_day = num_day_first_week[day_month[1]]
    for item in day_month:
        name_number_week = day_weekx[first_day]
        day_of_week[name_number_week]= item
        first_day +=  1 
    
    for item in day_weekx:
        x = day_weekx[item]
        if day_of_week.get(x) == None:
           day_of_week[x] = "" 
        
    return (day_of_week)
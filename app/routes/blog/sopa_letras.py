from app import app, request
from app import app, render_template
from app.model.modeldb import Model
from app.static.lib import sopa_letras
import os
import json
from datetime import datetime, date
import re
from flask import jsonify, make_response
import numpy as np
from random import *


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

@app.route("/blog/sopa_letters/<string:id_topic>")
def sopa_letters(id_topic):
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username)   
    #urlrev = URLBASE
    num_palabras = 0
    TSSTopico  = {'TABLE':'grupo',
        'Col1':'id',
        'Col2':'topico'
        }
    DatosTopico = connect.SSP_TABLE(username,TSSTopico)

    wid = id_topic
    TSSVocabulary  = {'TABLE':'vocabulary',
        'Col1':'id',
        'Col2':'english',
        'Col3':'spanish',
        'Col4':'grupo',
        'Col5':'ejemplos',
        'Whe6':'grupo=%s'
        }
    Data = (wid,)
    PalabrasCrucigrama = connect.SW_TABLE(username,TSSVocabulary, Data)
    list_palabras = []
    list_id = []
    Palabras_in_Crucigrama = []
    for items in PalabrasCrucigrama:
        list_id.append(items["id"])

    

    acierto = 0
    num_palabras = 0
    while num_palabras < 15:
        value_palabra = randint(0, len(list_id)-1)
        palabra_select = PalabrasCrucigrama[value_palabra]["english"]
        palabra_select = re.sub(r"\s+", "", palabra_select, flags=re.UNICODE)
        num_letras = len(palabra_select)
        nueva_palabra = {}
        if acierto == 0 and num_letras > 10 and num_letras < 13:
            if palabra_select not in list_palabras:
                list_palabras.append(palabra_select)
                nueva_palabra["spanish"] = PalabrasCrucigrama[value_palabra]["spanish"]
                nueva_palabra["english"] = palabra_select
                Palabras_in_Crucigrama.append(nueva_palabra)
                num_palabras += 1
                acierto = 1
        else:
            if palabra_select not in list_palabras:
                list_palabras.append(palabra_select)
                nueva_palabra["spanish"] = PalabrasCrucigrama[value_palabra]["spanish"]
                nueva_palabra["english"] = palabra_select
                Palabras_in_Crucigrama.append(nueva_palabra)
                num_palabras += 1


    resultados_crucigrama = sopa_letras.llenar_palabra()
    result_crucigrama = resultados_crucigrama.generar_crucigrama(list_palabras)
    data = result_crucigrama[0]
    palabras = result_crucigrama[1]
    nombre_id = "id"
    nombre_tabla = "crucigrama"
    id_max = connect.MAX_ID_TABLE(username, nombre_tabla  , nombre_id) 
    proximo_id = id_max[0]["max_id"] + 1
    id = str(proximo_id)
    grupo = "1"
    Insert_ofCrucigrama = dict()
    Insert_ofCrucigrama  = {'TABLE':'crucigrama',
            'Col1':'id',
            'Col2':'grupo',
            'Col3':'palabras',
            'Val4':'%s',
            'Val5':'%s',
            'Val6':'%s',
    }
    Data = [id, grupo, palabras] 
    res_insert = connect.IT_TABLE(username, Insert_ofCrucigrama , Data)   

    return render_template("/blog/sopa.html", url = Urlbase, data = data,
    palabras_crucigrama = Palabras_in_Crucigrama, id_crucigrama = proximo_id, DatosTopico= DatosTopico)

@app.route("/palabra/", methods=["POST"])
def palabra():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect = Model(username)   
    req = request.get_json()
    wid = req["nro_crucigrama"]
    #wid = "1"
    TSSPalabras = {'TABLE':'crucigrama',
        'Col1':'palabras',
        'Whe2':'id=%s'
        }
    Data = (wid,)
    EnCrucigrama = connect.SW_TABLE(username, TSSPalabras, Data)
    
    cx = "*"
    Total_palabras = EnCrucigrama[0]["palabras"]
    palabra = req["palabra"]
    cx += palabra
    acierto = True
    for item in req["coordenadas"]:
        coord = req["coordenadas"][item]
        cx += coord
     
    mtrix_palabras = Total_palabras.split("*")
    palabras_in_crucigrama = ""
    x_palabra = cx.strip("*")
    if x_palabra in mtrix_palabras:
        acierto = True
    else:
        acierto = False


                  
    if (acierto):        
        result = {"palabra": req["palabra"],
            "coordenadas": req["coordenadas"],
            "acierto":True
        }  
    else:
        result = {"palabra": req["palabra"],
            "coordenadas": req["coordenadas"],
            "acierto":False
        }  


    res = make_response(jsonify({"message": "OK"}), 200)
    
    return result
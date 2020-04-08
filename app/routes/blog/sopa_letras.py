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

@app.route("/blog/sopa_letters")
def sopa_letters():
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

    wid = "1"
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
    for items in PalabrasCrucigrama:
        list_palabras.append(items["english"])

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
        

    ''' id = "1"
    Update_crucigrama = dict()
    Update_crucigrama = {'TABLE':'crucigrama',
            'Val1':'palabras=%s',
            'Whe2':'id='+ id
        }
    Data = [palabras]
   
    res_update = connect.UPWT_TABLE(username, Update_crucigrama, Data) '''
    
    ''' id_max = connect.MAX_ID_TABLE(username, nombre_tabla  , nombre_id) 
    print(id_max[0]["max_id"]) '''

    return render_template("sopa.html", url= Urlbase, servicios = DatosServicioPtado, data = data,
    palabras_crucigrama = PalabrasCrucigrama, id_crucigrama = proximo_id)

@app.route("/palabra/", methods=["POST"])
def palabra():
    Urlbase = URLBASE
    username = CONFIG['TYPE_USER']['ROOT']
    connect=Model(username)   
    req = request.get_json()
    wid = req["nro_crucigrama"]
    #wid = "1"
    TSSPalabras = {'TABLE':'crucigrama',
        'Col1':'palabras',
        'Whe2':'id=%s'
        }
    Data = (wid,)
    EnCrucigrama = connect.SW_TABLE(username,TSSPalabras, Data)
    
    cx = "*"
    Total_palabras = EnCrucigrama[0]["palabras"]
    palabra = req["palabra"]
    cx += palabra
    acierto = True
    for item in req["coordenadas"]:
        coord = req["coordenadas"][item]
        cx += coord
        #x_palabra = Total_palabras.find(palabra)
        #indice = Total_palabras.find(coord)
        
        #print(cx)
        ''' print(cx)
        print(mtrix_palabras)
        
        if indice == -1 and x_palabra == -1:
            acierto = False '''

    mtrix_palabras = Total_palabras.split("*")
    palabras_in_crucigrama = ""
    x_palabra = cx.strip("*")
    if x_palabra in mtrix_palabras:
        acierto = True
    else:
        acierto = False


    """ for item_palabra in mtrix_palabras:
        #num_letters = len(item_palabra)-1
        #palabras_in_crucigrama = palabras_in_crucigrama[1:num_letters]
        
        x_palabra = cx.strip("*")
        print(item_palabra)
        print(x_palabra)
        if x_palabra ==  item_palabra:
            for item_coord in req["coordenadas"]:
                coord = req["coordenadas"][item]
                indice = Total_palabras.find(coord)
                if indice == -1:
                    acierto = False
        else:
            acierto = False """
                  
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
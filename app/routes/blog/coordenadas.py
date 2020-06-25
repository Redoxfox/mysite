from app import app, request   #libreria app y request(permite la manipulacion de peticiones HTTP)
from app import app, render_template 
from flask import jsonify, make_response #Librerias jsonify, make_response para manipulacion de tipos datos json



#Vista principal de la aplicación
@app.route("/blog/coordenadas/", methods=["GET"])
def coordenadas():
    #Ruta para mostrar vista coordenadas
    return render_template("/blog/coordenadas.html")

#Ruta con metodo POST para recepcion de coodenadas consumidas desde la API    
@app.route("/blog/ver_coordenadas/", methods=["POST"])
def ver_coordenadas():
    req = request.get_json() #Conversion de datos tipos json a lenguaje python (diccionario/lista)
    print(req)
    lista_coordenadas = req["coordenadas"] #Extraer los datos como lista python
    print(lista_coordenadas)
    for item in lista_coordenadas:
        print(lista_coordenadas[0])
     
    #Diccionario con lista de coordenadas se enviara a la vista    
    result = {"array":lista_coordenadas}
    #Respuesta de exito de peticion.
    #No se como tienes los datos de coordenadas almacenadas pero un ejemplo de modelo de objeto
    # que puede entender json es este. Son varios diccionarios con latitud y longitud y estos dentro de una lista
    # algo asi similar te deberia devolver una consulta de la base de datos y ese array lo guardas en un diccionario
    # con clave coordenadas. Yo no tengo base de datos asi que solo simulo la lectura con datos traidos desde la vista
    """  {'coordenadas': [{'lat': 4.443581, 'lng': -75.230992}, 
    {'lat': 4.445581, 'lng': -75.231992}, 
    {'lat': 4.446581, 'lng': -75.232992}, 
    {'lat': 4.447581, 'lng': -75.233992}, 
    {'lat': 4.448581, 'lng': -75.234992}, 
    {'lat': 4.449581, 'lng': -75.235992}, 
    {'lat': 4.440581, 'lng': -75.236992}, 
    {'lat': 4.441581, 'lng': -75.237992}, 
    {'lat': 4.442581, 'lng': -75.238992}, 
    {'lat': 4.447581, 'lng': -75.239992}]
    } """
    res = make_response(jsonify({"message": "OK"}), 200)
    
    """Nota: Los print y el for comentados permiten ver los datos en consola pero como se muestran en 
       servidor WEB no se pueden ver a menos que se implemente desde cero la APP"""
    return result


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
    #print(req)
    lista_coordenadas = req["coordenadas"] #Extraer los datos como lista python
    #print(lista_coordenadas)
    #for item in lista_coordenadas:
    #    print(item)
    

    #Diccionario con lista de coordenadas se enviara a la vista    
    result = {"array":lista_coordenadas}
    #Respuesta de exito de peticion.
    res = make_response(jsonify({"message": "OK"}), 200)
    
    """Nota: Los print y el for comentados permiten ver los datos en consola pero como se muestran en 
       servidor WEB no se pueden ver a menos que se implemente desde cero la APP"""
    return result
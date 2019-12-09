from app import app, render_template
import pymysql.cursors 
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
URLBASE = CONFIG['DEFAULT']['URLBASE']

class Model:
    def __init__(self,usuario):
        self.usuario = usuario

    def con(self):
        #f =open("./app/config/config.json","r")
        #file=f.read()
        #config = json.loads(file)

        self.connection = pymysql.connect(host = CONFIG["DEFAULT"]["DB_HOST"],
                             user=self.usuario,
                             password = CONFIG['DEFAULT']['DB_PASSWORD'],
                             db = CONFIG['DEFAULT']['DB_NAME'],
                             charset = CONFIG['DEFAULT']['DB_CRARSET'],
                             cursorclass=pymysql.cursors.DictCursor
                             )
        return self.connection
    
    def SW_TABLE(self, type_user, datos_table, *args):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
        self.Datos_table = datos_table
        list_column = []
        list_table = []
        list_where = []
        cont=0
        list_column.append("SELECT ")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + " "
                list_table.append(Cadena)
            else:
                cont+=1
                num_col="Col" + str(cont)
                num_whe="Whe" + str(cont)
                if items == num_col:
                    Cadena = valor + ","
                    list_column.append(Cadena)
                if items == num_whe:
                    Cadena = valor
                    list_where.append(Cadena)


        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + " FROM "
        else:
           Colunm = Colunm + " FROM "

        Values= ' '.join(list_table)

        Wheres= ' '.join(list_where)
        lenWheres= len(Wheres)
        ultimaVal = Wheres[lenWheres-1]
        if ultimaVal == ",":
           Wheres=Wheres[0:lenWheres-1]
           Wheres= Wheres + ";"
        else:
           Wheres = Wheres + ";"

        result = Colunm + Values + "WHERE " + Wheres
        print(result)
        sql = result
        cursor = con.cursor()
        cursor.execute(sql, (args))
        DatosUsers = cursor.fetchall()
        TotalEquipos = cursor.fetchall() 

        return  DatosUsers 

        #return result
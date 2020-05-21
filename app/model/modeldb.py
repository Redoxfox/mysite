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
    #Metodo constructor clase Model############################################ 
    def __init__(self,usuario):
        self.usuario = usuario

    #Metodo de conexion a la base de datos############################################ 
    def con(self):
        self.connection = pymysql.connect(host = CONFIG["DEFAULT"]["DB_HOST"],
                             user=self.usuario,
                             password = CONFIG['DEFAULT']['DB_PASSWORD'],
                             db = CONFIG['DEFAULT']['DB_NAME'],
                             charset = CONFIG['DEFAULT']['DB_CRARSET'],
                             cursorclass=pymysql.cursors.DictCursor
                             )
        return self.connection

    #Consulta con combinacion de SELECT and WHERE############################################ 
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
        sql = result
        cursor = con.cursor()
        cursor.execute(sql, (args))
        Allresuls = cursor.fetchall()
        con.close()
        return  Allresuls 

    #Consulta para la creacion de tablas############################################
    def CT_TABLE(self, type_user, Datos_table):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
        list_table = []
        for items in Datos_table:
            valor = Datos_table[items]
            if items=="TABLE":
                Cadena = "CREATE TABLE IF NOT EXISTS " + valor + "("
                list_table.append(Cadena)
            else:
                if items != "PK":
                    Cadena = items + " " + valor + ","
                    list_table.append(Cadena)
                    

            if items=="PK":
                Cadena = "PRIMARY KEY " + "(" + valor + ")"
                list_table.append(Cadena)
                result = ' '.join(list_table)
                longitud = len(result)
                ultima = result[longitud-1] 
                if ultima == ",":
                    result=result[0:longitud-1]
                    result = result + ");"
                else:
                    result = result + ");"

        try:
            sql = result
            cursor = con.cursor()
            cursor.execute(sql)
            create = True
        except:
            create = False
        
        con.close() 

        return create

    #Consulta para la insertar elementos############################################ 
    def IT_TABLE(self, type_user, datos_table, args):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
        list_column = []
        list_values = []
        cont=0
        list_column.append("INSERT INTO ")
        list_values.append(" VALUES(")
        self.Datos_table = datos_table
       
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + "("
                list_column.append(Cadena)
            else:
                cont+=1
                num_col="Col" + str(cont)
                num_value="Val" + str(cont)
                if items == num_col:
                    Cadena = valor + ","
                    list_column.append(Cadena)
                if items == num_value:
                    Cadena = valor + ","
                    list_values.append(Cadena)

        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + ")"
        else:
           Colunm = Colunm + ")"

        Values= ' '.join(list_values)
        lenValues = len(Values)
        ultimaVal = Values[lenValues-1]
        if ultimaVal == ",":
           Values=Values[0:lenValues-1]
           Values = Values + ");"
        else:
           Values = Values + ");"

        result = Colunm + Values
        

        try:
            sql = result
            cursor = con.cursor()
            cursor.execute(sql, args)
            con.commit() 
            cursor.close()
            create = True
        except:
            create = False

        con.close()  

        return create 

    #Consulta SELECT simple 
    def SSP_TABLE(self, type_user, datos_table):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
        list_column = []
        list_table = []
        cont = 0
        list_column.append("SELECT ")
        self.Datos_table = datos_table
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items == "TABLE":
                Cadena = valor + ";"
                list_table.append(Cadena)
            else:
                cont+=1
                num_col="Col" + str(cont)
                if items == num_col:
                    Cadena = valor + ","
                    list_column.append(Cadena)

        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + " FROM "
        else:
           Colunm = Colunm + " FROM "

        Values= ' '.join(list_table)
        result = Colunm + Values

        sql = result
        cursor = con.cursor()
        cursor.execute(sql)
        Allresuls = cursor.fetchall()
        con.close()

        return  Allresuls

    #Eliminar fila de tabla
    def DELWT_TABLE(self, type_user, datos_table):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
        list_column = []
        list_table = []
        list_where = []
        cont=0
        self.Datos_table = datos_table
        list_column.append("DELETE FROM ")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + " " 
                list_table.append(Cadena)
            else:
                cont+=1
                num_whe="Whe" + str(cont)
                if items == num_whe:
                    Cadena = valor
                    list_where.append(Cadena)


        Colunm= ' '.join(list_column)
        lenColunm = len(Colunm)
        ultimaCol = Colunm[lenColunm-1]
        Values= ' '.join(list_table)
        Wheres= ' '.join(list_where)
        lenWheres= len(Wheres)
        ultimaVal = Wheres[lenWheres-1]
        if ultimaVal == ",":
           Wheres=Wheres[0:lenWheres-1]
           Wheres= Wheres + ";"
        else:
           Wheres = Wheres + ";"

        result = Colunm +  Values + "WHERE " + Wheres

        try:
            sql = result
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit() 
            cursor.close()
            delete = True
        except:
            delete = False
        
        con.close()  

        return delete 

    #Actualizacion de tabla (UPDATE with WHERE)
    def UPWT_TABLE(self,type_user, datos_table, args_up):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
        list_column = []
        list_values = []
        list_where = []
        cont=0
        self.Datos_table = datos_table
        list_column.append("UPDATE ")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
                Cadena = valor + " SET "
                list_column.append(Cadena)
            else:
                cont+=1
                num_value="Val" + str(cont)
                num_whe="Whe" + str(cont)
                if items == num_value:
                    Cadena = valor + ","
                    list_values.append(Cadena)
                if items == num_whe:
                    Cadena = valor
                    list_where.append(Cadena) 

        Colunm = ' '.join(list_column)
        Values = ' '.join(list_values)
        Wheres = ' '.join(list_where)
        lenValues = len(Values)
        lenWheres = len(Wheres)
        ultimaVal = Wheres[lenWheres-1]
        ultimaValue = Values[lenValues-1]

        if ultimaVal == ",":
           Wheres=Wheres[0:lenWheres-1]
           Wheres= Wheres + ";"
        else:
           Wheres = Wheres + ";"
        
        if ultimaValue == ",":
            Values = Values[0:lenValues-1]
        else:
           Values = Values 

        result = Colunm + Values + " WHERE " + Wheres

        
        try:
            sql = result
            cursor = con.cursor()
            cursor.execute(sql, args_up)
            con.commit() 
            cursor.close()
            print(args_up)

            update = True
        except:
            update = False
        
        con.close()  

        return   update

    #Maximo id de la tabla
    def MAX_ID_TABLE(self, type_user, datos_table, id):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
       
        result = "SELECT  " + "max(" + id + ")" + "as max_id FROM  " + datos_table + ";"

        sql = result
        cursor = con.cursor()
        cursor.execute(sql)
        Allresuls = cursor.fetchall()
        con.close()

        return  Allresuls

    #Mostrar tablas de la base de datos.
    def SHOW_TABLES(self, type_user):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
       
        sql  = "SHOW TABLES;"

        cursor = con.cursor()
        cursor.execute(sql)
        Allresuls = cursor.fetchall()
        con.close()

        return  Allresuls

    #Mostrar tablas de la base de datos.
    def DESCRIBE_TABLES(self, type_user, datos_table):
        MyObjModel = Model(type_user)
        con = MyObjModel.con();
       
        sql  = "DESCRIBE  " + datos_table + ";"

        cursor = con.cursor()
        cursor.execute(sql)
        Allresuls = cursor.fetchall()
        con.close()

        return  Allresuls

    

    
    


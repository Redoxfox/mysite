import pymysql.cursors 
import configparser
import json
class Model:
    def __init__(self,usuario):
        self.usuario = usuario

    def con(self):
        f =open("./app/config/config.json","r")
        file=f.read()
        config = json.loads(file)
        self.connection = pymysql.connect(host=config["DEFAULT"]["DB_HOST"],
                             user=self.usuario,
                             password=config['DEFAULT']['DB_PASSWORD'],
                             db=config['DEFAULT']['DB_NAME'],
                             charset=config['DEFAULT']['DB_CRARSET'],
                             cursorclass=pymysql.cursors.DictCursor
                             )
        return self.connection
    
    
    def CT_TABLE(self,datos_table):
        
        list_table = []
        for items in self.Datos_table:
            valor = self.Datos_table[items]
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
        if ultima==",":
           result=result[0:longitud-1]
           result = result + ");"
        else:
           result = result + ");"""

        return result

    def SSP_TABLE(self, datos_table, ):
        #con =Model("root")
        list_column = []
        list_table = []
        cont=0
        list_column.append("SELECT ")
        for items in self.Datos_table:
            valor = self.Datos_table[items]
            if items=="TABLE":
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

        #TSEquipos = Model(TSSEquipos)
        sql = result
        cursor = con.cursor()
        cursor.execute(sql)
        TotalEquipos = cursor.fetchall() 

        return TotalEquipos

    def SW_TABLE(self, con, datos_table, *args):
        MyObjModel = Model("root")
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
        

    


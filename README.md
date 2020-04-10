# mysite

Repositorio proyecto personal (portafolio).

Este repositorio es ua iniciativa personal la cual tiene como finalidad la concentracion de una serie de proyectos personales los cuales en conjunto corresponde a mi portafolio de tecnologias web que manejo  frontend y backend en el momento las tecnolgias utilizadas para el proyecto son las siguientes.

Tecnologias frontend:

HTML
Javascript
CSS

Tecnologias backend:

Frameword Flask (python)
Python

Bases de datos:

Mysql

Sistema operativo 

Linux (distribucion Centos 7)

Estructura del proyecto:

-/mysite                         "Carpeta raiz del proyecto".
    -app/                        "Carpeta aplicacion".
       -/config                  "Carpeta con archivos de configuración".
           -__init__.py          "Archivo para validar carpeta como paquete".
           -config.json          "Archivo con datos de configuracion innorado en repositorio por seguridad".
       -/model                   "Carpeta con modelos de la base de datos".
           -__init__.py          "Archivo para validar carpeta como paquete".
           -modeldb.py           "Archivo para modelos y consultas a base de datos".
       -/routes                  "Carpeta para configuracion de rutas y carpetas con diferentes rutas".
           -__init__.py          "Archivo para validar carpeta como paquete y con cofiguracion de acceso -rutas".
           -/admin               "Carpeta con rutas para administrar el proyecto".
               - __init__.py     "Archivo para validar carpeta como paquete".
                -admin.py        "Archivo con metodos para administracion del proyecto".
                -login.py        "Archivo con metodos para logeo al proyecto".
                -registro.py     "Archivo con metodos para manejo de registros del proyecto".
                -validar.py      "Archivo con metodos para validacioes del proyecto".
                -view.py         "Archivo con metodos para gestionar vistas para administracion del proyecto".
            -/blog               "Carpeta con rutas para gestion de blog en el proyecto".
               - __init__.py     "Archivo para validar carpeta como paquete".
                -sopa_letras.py  "Archivo gestion de aplicacion entrada blog".
            -/project            "Carpeta con rutas para gestion de proyectos".
               - __init__.py     "Archivo para validar carpeta como paquete".
                -gastos.py       "Archivo gestion aplicacion gastos personales".
                -lavasplah.py    "Archivo gestion aplicacion de lavado ecologico de autos".
        -/static                 "Carpeta para gestion de estilos, js y librerias proyecto".
            -/css

                 
            






def IT_TABLE(self):
        list_column = []
        list_values = []
        cont=0
        list_column.append("INSERT INTO ")
        list_values.append(" VALUES(")
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

        return result


    def SSP_TABLE(self):
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

        return result

    def SW_TABLE(self):
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

        return result

    def DELWT_TABLE(self):
        list_column = []
        list_table = []
        list_where = []
        cont=0
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
        """if ultimaCol==",":
           Colunm=Colunm[0:lenColunm-1]
           Colunm = Colunm + " SET "
        else:
           Colunm = Colunm + " SET " """

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

        return result


    def UPT_TABLE(self):
        list_column = []
        list_values = []
        list_where = []
        cont=0
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

        print(Values)
       
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

        return result

        #return result

        CREATE TABLE crucigrama (id INT PRIMARY KEY,  grupo INT NOT NULL, palabras TEXT);
        INSERT INTO crucigrama (id, grupo, palabras) VALUES (1, 1,""); 

        CREATE TABLE vocabulary (id INT PRIMARY KEY,  english VARCHAR(50) NOT NULL, spanish VARCHAR(50) NOT NULL, grupo INT NOT NULL, ejemplos TEXT);

        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (1, "LIVINGROOM", "SALA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (2, "KITCHEN", "COCINA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (3, "BED", "CAMA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (4, "GARAGE", "GARAGE", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (5, "ATTIC", "ATICO", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (6, "DRESSER", "MESANOCHE", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (7, "FLOOR", "PISO", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (8, "SOAP", "JABÓN", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (9, "CAN", "LATA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (10, "SINK", "LAVAPLATOS", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (11, "SOFA", "SOFA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (12, "TABLE", "MESA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (13, "CHAIR", "SILLA", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (14, "STOOL", "BANCO", 1,""); 
        INSERT INTO vocabulary (id, english, spanish, grupo, ejemplos) VALUES (15, "BOWL", "TAZON", 1,""); 
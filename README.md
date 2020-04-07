# mysite


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
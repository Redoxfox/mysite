class proc_fecha:

    def year_fecha(self, fecha):
        fecha = fecha
        list_fecha = fecha.split("-")
        year = list_fecha
        year_int = year[0]
        
        return  year_int

    def month_fecha(self, fecha):
        fecha = fecha
        list_fecha = fecha.split("-")
        month = list_fecha
        month_int = month[1]
        
        return  month_int
       

    def day_fecha(self, fecha):
        fecha = fecha
        list_fecha = fecha.split("-")
        day = list_fecha
        day_int = day[2]
        
        return  day_int

    def nombre_mes(self, fecha):
        fecha = fecha
        list_fecha = fecha.split("-")
        month = list_fecha
        month_int = int(month[1])
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

        nom_mes =  meses[month_int]
        
        
        return  nom_mes

    def esBisiesto(self, fecha):
        fecha = fecha
        list_fecha = fecha.split("-")
        year = list_fecha
        year_ini = int(year[0])
        if(year_ini%4 == 0 and year_ini%100 != 0 or 
        (year_ini%4 == 0 and year_ini%100 == 0 and  year_ini%400 == 0)):
           return True
        else:
           return False 

    def Numero_dias(self, fecha):
        depurar_date = proc_fecha()
        list_fecha = fecha.split("-")
        month = list_fecha
        year_ini = int(month[0]) 
        num_day = 0
        #x = []
        year = 0
        for dias in range(0, year_ini):
            year += 1
            fecha_i = str(year) + "-" + "01" + "01"
            #x.append(depurar_date.esBisiesto(fecha_i))
            if(depurar_date.esBisiesto(fecha_i)):
                num_day += 366
            else:
                num_day += 365

        numero_day_month = depurar_date.day_restantes(fecha)
        

        if depurar_date.esBisiesto(fecha):
           dias_faltantes = 366 - numero_day_month
        else: 
           dias_faltantes = 365 - numero_day_month
        
        total_day_date = num_day - dias_faltantes 
        
        return total_day_date
        #return x 


    def day_restantes(self, fecha):
        depurar_date = proc_fecha()
        fecha = fecha
        list_fecha = fecha.split("-")
        month = list_fecha
        year_ini = int(month[0])
        month_int = int(month[1]) 
        day_ini = int(month[2])
        meses = {1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
        }
        cont = 0
        x = 0
        for value in range(0,month_int):
            cont += 1
            
            if cont == month_int:
                x -=  meses[cont] - day_ini
                   
            if (depurar_date.esBisiesto(fecha)==True and cont == 2):
                x += meses[cont] + 1
            else:
                x += meses[cont] 

             

            total_dias = x 

            

        return x
   
    def valor_fechas(self, fecha_ini):
        depurar_date = proc_fecha()
        year_ini = int(depurar_date.year_fecha(fecha_ini))
        month_ini = int(depurar_date.month_fecha(fecha_ini)) * 10
        day_ini = int(depurar_date.day_fecha(fecha_ini))
        value = year_ini + month_ini + day_ini 
        return  value 

    def date_between(self, fecha_ini, fecha_end):
        #Array de fechas 
        fechas = []
        #Instancia de objeto 
        depurar_date = proc_fecha()
        #Depuracion de fecha inicial
        year_ini = int(depurar_date.year_fecha(fecha_ini)) 
        month_ini = int(depurar_date.month_fecha(fecha_ini))
        day_ini = int(depurar_date.day_fecha(fecha_ini))
        #Depuracion de fecha final
        year_end = int(depurar_date.year_fecha(fecha_end)) + 1
        month_end = int(depurar_date.month_fecha(fecha_end))
        day_end = int(depurar_date.day_fecha(fecha_end))

        num_year = year_end - year_ini
        num_month_year_ini = month_ini
        num_month_year_end = month_end

        fechas.append(str(year_ini))
        fechas.append(str(month_ini))
        fechas.append(str(day_ini))
        fechas.append(str(year_end))
        fechas.append(str(month_end))
        fechas.append(str(day_end))
        fechas.append(year_ini)
        fechas.append(year_end)
        fechas.append(num_month_year_ini)
        fechas.append(num_month_year_end)

        return fechas








        


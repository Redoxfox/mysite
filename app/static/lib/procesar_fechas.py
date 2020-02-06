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


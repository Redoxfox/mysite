class Model:
    import pymysql.cursors
    
    def __init__(self,datos_table):
         self.Datos_table = datos_table

    def con(self,user):
        from app.config.config import urldirection, conexion
        myconeccion=conexion(self.user)
        CONFIG_DB = myconeccion.datosdb()
        connection = pymysql.connect(host=CONFIG_DB['HOST'],
                             user=CONFIG_DB['USERNAME'],
                             password=CONFIG_DB['PASSWORD'],
                             db=CONFIG_DB['DATABASENAME'],
                             charset=CONFIG_DB['CRARSET'],
                             cursorclass=pymysql.cursors.DictCursor)
        return connection

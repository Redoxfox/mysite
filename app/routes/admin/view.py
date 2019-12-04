from app import app, render_template
from app.model.modeldb import Model
from app.config.config import urldirection
myurls = urldirection()
CONFIG_URL = myurls.datosUrl()
URLBASE = CONFIG_URL['URLBASE']
AMBIENTE = CONFIG_URL['MODO_DESARROLLO']

@app.route("/")
def index():
    Sql="ddasddf"
    lista ="lista"
    urlrev = URLBASE 


    """titulo = "Home!"
    urlrev = URLBASE 
    lista = ["footer", "header", "info"]
    TCliente = dict()
    TCliente = {'TABLE':'servicios',
        'id':'INT AUTO_INCREMENT',
        'id_servicio':'INT NOT NULL',
        'id_cliente':'INT NOT NULL',
        'descuento':'DOUBLE NOT NULL',
        'costo_total':'DOUBLE  NOT NULL',
        'costo_desc':'DOUBLE  NOT NULL',
        'fecha':'DATE NOT NULL',
        'observacion':'TEXT NOT NULL',
        'PK':'id'
    }
    TCliente = Model(TCliente)
    Sql = TCliente.CT_TABLE()
    #print(titulo)
    #urlrev = titulo
    #print(urlrev)"""
    return render_template("index.html", sql=Sql, lista=lista, url = urlrev)
from app import app, render_template, request ,redirect, url_for
from app.model.modeldb import Model
from app.config import config
from app.model.modeldb import Model
from app.config.config import urldirection
from app.model.validaciones import Validar
import json
f =open("./app/config/config.json","r")
file=f.read()
CONFIG = json.loads(file)
URLBASE = CONFIG['DEFAULT']['URLBASE']

"""db1 = UserDb("root")

db1 = UserDb("redoxfox1")"""

@app.route("/validar", methods=["GET", "POST"])
def validar():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    TSWusers = dict()
    TSWusers = {'TABLE':'users',
        'Col1':'nick',
        'Col2':'password',
        'Col3':'salt',
        'Whe4':'nick=%s'
        }

    connect=Model("root")   
    '''  TUsers= Model(username)
    sql = TUsers.SW_TABLE()
    cursor = TUsers.con(TSWusers)
    cursor.execute(sql, (username))
    DatosUsers = cursor.fetchall() '''

    Data = (username,)
    DatosUsers = connect.SW_TABLE(connect,TSWusers,Data)
    password_userbd = DatosUsers[0]['password']
    salt_userbd = DatosUsers[0]['salt']

    print (password_userbd)
    print (salt_userbd)
    hash= Validar()
    h2=hash.check_password(password_userbd, password, salt_userbd)
    if h2:
        urlrev = URLBASE 
        #return render_template("principal.html", url = urlrev)
        
        return redirect(url_for('admin_user'))
    else:
        urlrev = URLBASE 
        return redirect(url_for('index'))
    
    urlrev= URLBASE

    return render_template("login.html", url = urlrev)
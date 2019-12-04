from app import app
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

@app.route("/admin/passw")
def passw():
    return "Hello word"

@app.route("/admin/admin_user")
def admin_user():
    urlrev = URLBASE
    return render_template("principal.html", url = urlrev)
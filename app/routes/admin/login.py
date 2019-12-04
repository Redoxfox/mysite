from app import app, render_template
import json
f =open("./app/config/config.json","r")
file=f.read()
CONFIG = json.loads(file)

#app.config.from_object("config.DevelopmentConfig") 
URLBASE = CONFIG['DEFAULT']['URLBASE']
@app.route("/login")
def login():
    urlrev = URLBASE 
    return render_template("login.html", url = urlrev)
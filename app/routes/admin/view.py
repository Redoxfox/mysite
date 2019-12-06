from app import app, render_template
import os
import json
dir_act = os.getcwd()
route_file_config = dir_act 
#+ "/app/config/config.json"
route_exist = route_file_config.find("mysite")
if route_exist > 0:
    route_file_config = dir_act + "/app/config/config.json"
else:
    route_file_config = dir_act + "/mysite/app/config/config.json"

print(dir_act)
print(os.path.isfile(route_file_config))
print(os.path.isdir('app/config'))

@app.route("/")
def index():
    Sql="ddasddf"
    lista = route_file_config 
    return render_template("index.html", sql=Sql, lista=lista)
from app import app
from app import app, render_template


@app.route("/lavasplash/index_ls")
def index_ls():
    #urlrev = URLBASE
    return render_template("home_ls.html")


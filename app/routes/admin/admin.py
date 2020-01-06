from app import app
from app import app, render_template


@app.route("/admin/passw")
def passw():
    return "Hello word"

@app.route("/admin/admin_user")
def admin_user():
    #urlrev = URLBASE
    return render_template("principal.html")
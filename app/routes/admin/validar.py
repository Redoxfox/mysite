from app import app, render_template

@app.route("/validar", methods=["GET", "POST"])
def validar():
    return render_template("login.html")
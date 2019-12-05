from app import app, render_template
import json

@app.route("/login")
def login():
    return render_template("login.html")
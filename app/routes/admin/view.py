from app import app, render_template


@app.route("/")
def index():
    Sql="ddasddf"
    lista ="lista"
    return render_template("index.html", sql=Sql, lista=lista)
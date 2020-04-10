from app import app, request
from app import app, render_template
from app.model.modeldb import Model
from app.static.lib import validaciones
import os
import json
from datetime import datetime, date
import re
from flask import jsonify


@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render_template("/registro/registro.html")

@app.route("/singup", methods=["GET", "POST"])
def singup():
    if request.method == "POST":
        id = None
        nick = request.form['nick']
        nombre = request.form['name']
        email = request.form['Email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        password = request.form['password']
        passwordc = request.form['passwordc']
        Insert_users= dict()
        Insert_users= {'TABLE':'users',
            'Col1':'id',
            'Col2':'nick',
            'Col3':'nombre',
            'Col4':'email',
            'Col5':'direccion',
            'Col6':'telefono',
            'Col7':'password',
            'Col8':'salt',
            'Val9':'%s',
            'Val10':'%s',
            'Val11':'%s',
            'Val12':'%s',
            'Val13':'%s',
            'Val14':'%s',
            'Val15':'%s',
            'Val16':'%s'
        }
        Inst_TUsers= Model(Insert_users)
        sql = Inst_TUsers.IT_TABLE()
        hash= validaciones.Validar()
        pass_hash=[]
        pass_hash=hash.hash_password(password)
        salt=pass_hash[0]
        password_hash=pass_hash[1]

        cursor = db1.cursor()
        cursor.execute(sql, (id, nick, nombre, email, direccion, telefono, password_hash, salt))
        cursor.close()
        db1.commit()

        return render_template("login.html", clave=sql)
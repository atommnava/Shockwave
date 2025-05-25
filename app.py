#!urs/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from sqlhelpers import *
from forms import *

app = Flask(__name__)

# Configuration for all our setting from MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USERNAME'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'CRYPTO'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    return render_template('register.html')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = 'secret256'
    app.run(debug=True)

#!urs/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration for all our setting from MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USERNAME'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DATABASE'] = 'CRYPTO'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = 'secret256'
    app.run(debug=True)


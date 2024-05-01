from flask import Flask, redirect, render_template, request, session, jsonify, flash, url_for, g
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import sqlite3
import datetime
import os

#   Configure Application
app = Flask(__name__)
DATABASE = "app.db"

#   Configure the database
def get_db():
    db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#   Row Factory Function
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


@app.route('/', methods=["GET", "POST"])
def home():
    #   Serve the default home page
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)
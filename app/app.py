"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
from flask import Flask, request, render_template, session, redirect, jsonify, g
import numpy as np
import pandas as pd
import sqlalchemy as db
import sqlite3

app = Flask(__name__)
engine = db.create_engine('sqlite:///users.db')
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('users', metadata, autoload=True, autoload_with=engine)
#print(users.columns.keys())
#print(repr(metadata.tables['users']))
query = db.select([users])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
#print(ResultSet)
df = pd.DataFrame(ResultSet)
df.columns = ResultSet[0].keys()
#print(df)
#df.to_html('pandas.html')
#print(df)
@app.route('/users/list', methods=("POST", "GET"))
def html_table():

    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/api/v1/users/', methods=("POST", "GET"))
def get_json():
    #result = connection.execute(users)
    return jsonify(tables=[df.to_html(classes='data')])

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

"""
Routes and views for the flask application.
"""
#Import libraries
from datetime import datetime
from flask import render_template, jsonify
from ApiFullStack import app
import pandas as pd
import sqlalchemy as db

#Main function to get database as a pd table
def Database():
    engine = db.create_engine('sqlite:///users.db')

    #Se conecta
    connection = engine.connect()
    metadata = db.MetaData()

    #Se "refleja" o copia los datos de la BD para poder usarlos
    users = db.Table('users', metadata, autoload=True, autoload_with=engine)
    query = db.select([users])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    #Se definen los datos de la BD en pandas para mostrarlos de manera mas ordenada
    df = pd.DataFrame(ResultSet)
    df.columns = ResultSet[0].keys()
    return df

#Get database table
df=Database()

#Main route or home also this list the data of the database obtained
@app.route('/')
@app.route('/home')
@app.route('/users/list')
#Function to render the home page and the table of the database
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        tables=[df.to_html(classes='data')], 
        titles=df.columns.values
    )


#Route contact
@app.route('/contact')
#Main function to render contact page
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Please refer to the following information.'
    )


#Route about
@app.route('/about')
#Main function to render about page
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Hello, i see you´ve got here, well, this is just a simple flask application'
    )


#Route to ask for jason
@app.route('/api/v1/users/')
#main function to render jason
def get_json():
    return jsonify(tables=[df.to_html(classes='data')])
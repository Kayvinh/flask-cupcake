import os
from flask import Flask, jsonify, request
from models import Cupcake, db, connect_db
"""Flask app for Cupcakes"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

connect_db(app)

@app.get('/')
def display_cupcakes():
    """ Lists all cupcakes """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]


    return jsonify(cupcakes=serialized)


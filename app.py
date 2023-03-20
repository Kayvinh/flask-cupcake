import os
from flask import Flask, jsonify, request
from models import Cupcake, db, connect_db, DEFAULT_IMG
"""Flask app for Cupcakes"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

connect_db(app)

@app.get('/api/cupcakes')
def list_cupcakes():
    """ Returns JSON {'cupcakes': [{id, flavor, size}, ...]} """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<cupcake_id>')
def list_cupcake(cupcake_id):
    """ Return JSON {'cupcake: {id, flavor, ...}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """ Create cupcake from posted JSON data and return it. 
    
    Returns JSON {'cupcake': {id, flavor, size ...}}"""


    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    if image == '':
        image = DEFAULT_IMG

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)






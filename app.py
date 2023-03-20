import os
from flask import Flask, jsonify, request, render_template
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
    """ Returns JSON for all cupcakes: {'cupcakes': [{id, flavor, size, rating, image}, ...]} """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:cupcake_id>')
def list_cupcake(cupcake_id):
    """ Return JSON for single cupcake: {'cupcake: {id, flavor, size, rating, image}} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post('/api/cupcakes')
def create_cupcake():
    """ Create cupcake from posted JSON data and return it. 
    
    Returns JSON {'cupcake': {id, flavor, size, rating, image}}
    
    Adds cupcake to the database 'cupcakes'. """


    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    if image == '':
        image = None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch('/api/cupcakes/<int:cupcake_id>')
def patch_cupcake(cupcake_id):
    """ Return updated cupcake JSON
        {'cupcake': {id, flavor, size, rating, image}}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    # If they send empty string for image, assign default image

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    if cupcake.image == '':
        cupcake.image = DEFAULT_IMG

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.delete('/api/cupcakes/<int:cupcake_id>')
def delete_cupcake(cupcake_id):
    """ Delete cupcake JSON and from database """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted=cupcake_id)

@app.get




# GET /
# This should return an HTML page (via render_template). 
# This page should be entirely static (the route should just render the template,
# without providing any information on cupcakes in the database). 
# It should show simply have an empty list where cupcakes should appear and a 
# form where new cupcakes can be added.
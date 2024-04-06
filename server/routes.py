from flask import jsonify, request
from app import app
from model import Restaurant, Pizza, RestaurantPizza, db

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
    })

@app.route('/restaurants/<int:id>', methods=['PATCH'])
def update_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    data = request.json
    if 'name' in data:
        restaurant.name = data['name']
    if 'address' in data:
        restaurant.address = data['address']
    db.session.commit()
    return jsonify({'message': 'Restaurant updated successfully'}), 200

# Other routes...

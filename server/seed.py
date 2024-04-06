from app import app, db
from model import Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        # Create initial data
        pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
        pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
        db.session.add_all([pizza1, pizza2])
        db.session.commit()

        restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
        restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
        restaurant1.pizzas.append(pizza1)
        restaurant1.pizzas.append(pizza2)
        db.session.add_all([restaurant1, restaurant2])
        db.session.commit()

if __name__ == '__main__':
    seed_data()

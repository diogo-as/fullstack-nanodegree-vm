#!/home/vagrant/python-env/env/bin python
# This Python file uses the following encoding: utf-8
from flask import Flask, render_template, url_for

app = Flask(__name__)

#Fake Restaurants
#restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
one_item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree', 'id':'1'}

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    #return "this page will show all restaurants"
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurants/new')
def newRestaurants():
    #return "this page will be for create new restaurants"
    return render_template('newRestaurant.html', restaurants = restaurants)

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurants(restaurant_id):
    #return "this page will be to edit restaurants %s" % restaurant_id
    restaurant_selected = restaurants[restaurant_id]
    return render_template('editRestaurants.html', restaurant = restaurant_selected)

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurants(restaurant_id):
    #return "this page will show all restaurants %s" % restaurant_id
    restaurant_selected = restaurants[restaurant_id]
    return render_template('deleteRestaurants.html', restaurant = restaurant_selected)

@app.route('/restaurants/<int:restaurant_id>')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant_selected = restaurants[restaurant_id]
    #return "this page will show menu of restaurants %s" % restaurant_id
    return render_template('menu.html', restaurant = restaurant_selected, items = items)

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    #return "this page will create a menu item for restaurants %s" % restaurant_id
    restaurant_selected = restaurants[restaurant_id]
    return render_template('newMenuItem.html', restaurant = restaurant_selected, restaurant_id = restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenu(restaurant_id, menu_id):
    #return "this page will edit menu item of restaurants %s" % menu_id
    restaurant_selected = restaurants[restaurant_id]
    return render_template('editMenuItem.html', restaurant = restaurant_selected, restaurant_id = restaurant_id, menu_id = menu_id, item = one_item)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenu(restaurant_id, menu_id):
    #return "this page will show menu of restaurants %s" % menu_id
    restaurant_selected = restaurants[restaurant_id]
    return render_template('deleteMenuItem.html', restaurant = restaurant_selected, restaurant_id = restaurant_id, menu_id = menu_id, item = one_item)



if __name__ == '__main__':
    app.secret_key = "secret"
    app.debug = True
    app.run(host='192.168.0.15', port=8000)

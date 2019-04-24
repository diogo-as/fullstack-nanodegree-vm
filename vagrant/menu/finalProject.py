#!/home/vagrant/python-env/env/bin python
# This Python file uses the following encoding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "this page will show all restaurants"

@app.route('/restaurant/new')
def newRestaurants():
    return "this page will be for create new restaurants"

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurants(restaurant_id):
    return "this page will be to edit restaurants %s" % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurants(restaurant_id):
    return "this page will show all restaurants %s" % restaurant_id

@app.route('/restaurants/<int:restaurant_id>')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu():
    return "this page will show menu of restaurants %s" % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem():
    return "this page will create a menu item for restaurants %s" % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenu():
    return "this page will edit menu item of restaurants %s" % menu_id

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenu():
    return "this page will show menu of restaurants %s" % menu_id



if __name__ == '__main__':
    app.secret_key = "secret"
    app.debug = True
    app.run(host='192.168.0.15', port=8000)

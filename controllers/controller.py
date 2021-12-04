from flask import render_template, request, redirect
from app import app
from models.items import *

@app.route('/shopping_list')
def index():
    return render_template('index.html', title = 'Home', items = items)

@app.route('/shopping_list', methods=['POST'])
def add_item():
  add_new_item(Item(request.form['name'], request.form['price'], request.form['quantity'], False ))
  return redirect('/shopping_list')
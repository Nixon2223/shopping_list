from flask import render_template, request, redirect
from app import app
from models.items import *

@app.route('/shopping_list')
def index():
  t = total_price(items)
  l = len(items)
  return render_template('index.html', title = 'Home', items = items, t=t, l=l)

@app.route('/shopping_list', methods=['POST'])
def add_item():
  add_new_item(Item(request.form['name'], request.form['price'], request.form['quantity'], False ))
  return redirect('/shopping_list')

@app.route('/shopping_list/remove<int:i>')
def order_remove(i):
    items.pop(i)
    return redirect('/shopping_list')

@app.route('/shopping_list/bought<int:i>')
def order_bought(i):
    items[i].bought = not items[i].bought
    return redirect('/shopping_list')

@app.route('/shopping_list/bought_filter<string:i>')
def order_bought_filter(i):
  new_items = filter_bought(items, i)
  t = total_price(new_items)
  l = len(new_items)
  if i == "T" or i == "F":
    return render_template('index.html', title = 'Home', items = new_items, t=t, l=l)
  return redirect('/shopping_list')
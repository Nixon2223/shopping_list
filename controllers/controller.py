from flask import render_template, request, redirect
from app import app
from models.items import *

@app.route('/list')
def index():
    return render_template('index.html', title = 'Home', items = items)
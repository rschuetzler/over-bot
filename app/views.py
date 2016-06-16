from flask import render_template
from app import app, db
from .models import Hero, Map, Player
from datetime import datetime

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.djhtml',
                           title = 'Home')

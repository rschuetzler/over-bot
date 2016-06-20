from flask import render_template, flash, redirect, session, url_for
from app import app, db
from .models import Hero, Map, Player
from .forms import HeroCreateForm
from datetime import datetime

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.djhtml',
                           title = 'Home')

@app.route('/hero/<id>')
def hero(id):
    hero = Hero.query.filter_by(id=id).first()
    if hero == None:
        flash('Hero %s not found' % id)
        return redirect(url_for('index'))
    return render_template('hero.djhtml',
                           hero = hero,
                           title = hero.name)
    
@app.route('/hero/create', methods = ['GET', 'POST'])
def hero_create():
    form = HeroCreateForm()
    if form.validate_on_submit():
        print('attempting to create hero')
        hero = Hero(name = form.name.data,
                    description = form.description.data,
                    image = form.image.data,
                    role = form.role.data,
                    specialty = form.specialty.data)
        db.session.add(hero)
        db.session.commit()
        print('hero created')
        flash('hero %s created' % form.name.data)
        return redirect(url_for('hero_create'))
    return render_template('hero_create.djhtml',
                           title = 'Create hero',
                           form = form)
    

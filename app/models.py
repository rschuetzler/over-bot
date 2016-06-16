from app import db

# "Counter" counters "countered"
counters = db.Table('counters',
                    db.Column('counter_id', db.Integer, db.ForeignKey('hero.id')),
                    db.Column('countered_id', db.Integer, db.ForeignKey('hero.id')),
                    db.Column('details', db.String(255)))

class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tag = db.Column(db.String(64), index = True)
    bnet = db.Column(db.String(64), index = True, unique = True)
    updated = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<Player %r>' % (self.bnet)
    
class Hero(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    description = db.Column(db.String(255))
    class = db.Column(db.String(64), index = True)
    role = db.Column(db.String(64), index = True)
    countered_by = db.relationship('Hero',
                                   secondary = counters,
                                   primaryjoin = (counters.c.countered_id == id),
                                   secondaryjoin = (counters.c.counter_id == id),
                                   backref = db.backref('counters', lazy = 'dynamic'),
                                   lazy = 'dynamic')

    def __repr__(self):
        return '<Hero %r>' % (self.name)

class Map(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    description = db.Column(db.String(255))
    type = db.Column(db.String(64), index = True)

    def __repr__(self):
        return '<Map %r>' % (self.name)

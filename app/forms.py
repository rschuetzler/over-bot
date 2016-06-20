from flask_wtf import Form
from wtforms import StringField, RadioField, SelectField
from wtforms.validators import DataRequired

class HeroCreateForm(Form):
    name = StringField('name', validators = [DataRequired()])
    description = StringField('description', validators = [DataRequired()])
    image = StringField('image')
    role = SelectField('role', choices=[('offense', 'Offense'), ('defense', 'Defense'),
                                       ('tank', 'Tank'), ('support', 'Support')],
                      validators = [DataRequired()])
    specialty = RadioField('specialty', choices=[('flanker', 'Flanker'),
                                                 ('sniper', 'Sniper'),
                                                 ('builder', 'Builder')])

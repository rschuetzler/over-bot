from flask_wtf import Form
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired

class HeroCreate(Form):
    name = StringField('name', validators = [DataRequired()])
    description = StringField('description', validators = [DataRequired()])
    role = RadioField('role', choices=['Offense', 'Defense', 'Tank', 'Support'],
                      validators = [DataRequired()])
    specialty = RadioField('specialty', choices=['Flanker', 'Sniper', 'Builder'])

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class HitsForm(FlaskForm):
    hit_count = IntegerField('Hits', validators=[DataRequired()], default=3)
    submit = SubmitField('Generate')

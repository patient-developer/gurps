from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class HitsForm(FlaskForm):
    damage_dice_count = IntegerField(
        'Damage Dice',
        validators=[
            DataRequired(),
            NumberRange(1, 30)
        ],
        default=5)

    damage_bonus = IntegerField(
        'Damage Bonus',
        validators=[
            NumberRange(-50, 50)
        ],
        default=0)

    hit_count = IntegerField(
        'Hits',
        validators=[
            DataRequired(),
            NumberRange(1, 50)],
        default=3)

    submit = SubmitField('Generate')

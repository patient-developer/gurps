import random
from datetime import datetime

import random_hit_location
import weapon_damage
from . import blueprint
from flask import render_template

from .forms import HitsForm


@blueprint.route('/', methods=['POST', 'GET'])
def hits():
    hits_form = HitsForm()
    if hits_form.validate_on_submit():
        random.seed(datetime.now())
        hit_count = int(hits_form.hit_count.data)
        damage_dice_count = int(hits_form.damage_dice_count.data)
        damage_bonus = int(hits_form.damage_bonus.data)
        hit_locations = random_hit_location.provide_random_hit_locations(hit_count, random)
        hit_results = []
        for hit_location in hit_locations:
            damage = weapon_damage.provide_weapon_damage(damage_dice_count, damage_bonus, random)
            hit_results.append({'location': hit_location,
                                'damage': str(damage)})
        return render_template('hits.html', form=hits_form, hit_results=hit_results)
    return render_template('hits.html', form=hits_form)

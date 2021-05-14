import random_hit_location
from . import blueprint
from flask import render_template

from .forms import HitsForm

MAX_HIT_COUNT = 20


@blueprint.route('/', methods=['POST', 'GET'])
def hits():
    hits_form = HitsForm()
    if hits_form.validate_on_submit():
        hit_count = min(int(hits_form.hit_count.data), MAX_HIT_COUNT)
        hit_locations = random_hit_location.provide_random_hit_locations(hit_count)
        return render_template('hits.html', form=hits_form, hit_locations=hit_locations)
    return render_template('hits.html', form=hits_form)

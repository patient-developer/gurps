from flask import Blueprint

blueprint = Blueprint('hits', __name__, template_folder='templates')

from . import forms, views

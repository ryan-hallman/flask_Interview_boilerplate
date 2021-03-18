from flask import render_template, jsonify, flash, redirect, url_for
from flask_login import login_required

from app import app, logger
import random

from app.models import Widgets


@app.route('/')
@app.route('/index')
def index():
    logger.info("Some text for console and log file")
    return render_template('index.html', title='Home')


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/make_widgets')
@login_required
def make_widgets(number_of_widgets=5):
    Widgets.make_widgets(number_of_widgets)
    flash("Made %s widgets" % number_of_widgets, 'positive')
    return redirect(url_for('index'))


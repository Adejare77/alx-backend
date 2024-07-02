#!/usr/bin/env python3
""" Mock logging in """
from flask import Flask, request, g, render_template
from flask_babel import Babel, _
import pytz
from pytz import timezone
from datetime import datetime


class Config:
    """ create language class attribute """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as=None):
    """ Get user database """
    if login_as and users.get(int(login_as)):
        return users[int(login_as)]
    return None


@app.before_request
def before_request():
    """ Get user info """
    user_id = request.args.get('login_as', None)
    user = get_user(user_id)
    g.user = None
    g.user_locale = None
    if user:
        g.user = user["name"]
        g.user_locale = user.get('locale')
        g.user_timezone = user.get('timezone')


@babel.localeselector
def get_locale():
    """ Select the best match locale for the user """
    if request.args.get('locale'):
        lang = request.args.get('locale')
    elif g.user_locale:
        lang = g.user_locale
    elif request.headers.get("Accept-Language"):
        lang = request.headers.get("Accept-Language")
    else:
        lang = app.config["BABEL_DEFAULT_LOCALE"]

    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Select the timezone for the user """
    if request.args.get('timezone'):
        zone = request.args.get('timezone')
    elif g.user_timezone:
        zone = g.user
    else:
        zone = app.config["BABEL_DEFAULT_TIMEZONE"]

    try:
        timezone(zone)
        return zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route('/')
def index():
    """ index page """
    home_title = _('home_title')  # MessageID is enclose in ()
    home_header = _('home_header')
    return render_template('7-index.html', home_header=home_header,
                           home_title=home_title, user=g.user)


if __name__ == '__main__':
    app.run()

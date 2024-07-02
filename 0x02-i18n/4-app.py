#!/usr/bin/env python3
""" Parametrize templates """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ create language class attribute """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Select the best match locale for the user """
    lang = request.args.get('locale', None)
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ index page """
    home_title = _('home_title')  # MessageID is enclose in ()
    home_header = _('home_header')
    return render_template('4-index.html', home_header=home_header,
                           home_title=home_title)


if __name__ == '__main__':
    app.run()

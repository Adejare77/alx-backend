#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ create language class attribute """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# create a flask instance
app = Flask(__name__)
# load class/object configuration
app.config.from_object(Config)
# Create a babel instance
babel = Babel(app)


@app.route('/')
def index():
    """ index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)

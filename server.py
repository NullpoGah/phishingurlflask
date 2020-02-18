from index import phishng_detection
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("getInput.html")

@app.route('/result')
def result():
    urlname  = request.args['name']
    result  = phishng_detection(urlname)
    return result

if __name__ == '__main__':
    app.run(debug=True)

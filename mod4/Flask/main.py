from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('enternew.html')

@app.route('/list')
def list():
    return 'List Hospital App Users'

@app.route('/results')
def results():
    return 'Results'

if __name__ == '__main__':
    app.debug = True
    app.run()
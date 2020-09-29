import os
from flask import Flask, render_template, flash, redirect, url_for, session, request

import psycopg2, psycopg2.extras

# DB connection
conn = psycopg2.connect(dbname='Book', user='root', password='root')

app = Flask(__name__)

# Init redirect
@app.route('/')
def index():
    return redirect(url_for('home'))


# Home page
@app.route('/home', methods=['GET', 'POST'])
def home():
    # POST (probably a search)
    if request.method == 'POST':
        pass

    # GET method
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
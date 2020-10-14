import os, tool
from flask import Flask, render_template, flash, redirect, url_for, session, request

import psycopg2, psycopg2.extras

# DB connection
#conn = psycopg2.connect(dbname='Book', user='root', password='root')

app = Flask(__name__)


# Init redirect
@app.route('/')
def index():
    return redirect(url_for('home'))


# Home page
@app.route('/index')
def home():
    # Method should query DB for a group of books (~25, 5 rows of 5?) and then pass the information to home.html
    books = [tool.genbook() for i in range(25)]

    return render_template('index.html', books=books)


# Page for specific book
@app.route('/book/<string:isbn>')
def book(isbn):
    # Grab info for book based on isbn

    b = tool.genbook()

    return render_template('book.html', book=b, isbn=isbn)


# DB search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    # Result of search (present seperate space beneath the search space to display results, rather than redirect?)
    if request.method == 'POST':
        # Probably grab info from HTML form
        return render_template('search.html')

    # GET method, display search and search options
    else:
        return render_template('search.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()

import os, tool
from flask import Flask, render_template, flash, redirect, url_for, session, request
import mysql.connector


# DB connection
conn = mysql.connector.connect(user='root', password='root', host="localhost", database="book")
cur = conn.cursor(dictionary=True)

app = Flask(__name__)


# Init redirect
@app.route('/')
def index():
    return redirect(url_for('home'))


# Home page
@app.route('/index')
def home():
    # Method should query DB for a group of books (~25, 5 rows of 5?) and then pass the information to home.html
    # books = [tool.genbook() for i in range(25)]
    books = tool.db_get_n_books(cur, 25)
    return render_template('index.html', books=books)


# Page for specific book
@app.route('/book/<string:isbn>')
def book(isbn):
    # Grab info for book based on isbn
    books = tool.db_get_n_books(cur, 25)

    for b in books:
        if b['BIsbn'] == isbn:
            return render_template('book.html', book=b, isbn=isbn)

   # if the book is not found then create a random book to show
    newBook = tool.genbook()
    return render_template('book.html', book=newBook, isbn=isbn)





# DB search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    books = tool.db_get_n_books(cur, 25)

    # Result of search (present seperate space beneath the search space to display results, rather than redirect?)
    if request.method == 'POST':
        # Probably grab info from HTML form
        return render_template('search.html')

    # GET method, display search and search options
    else:
        return render_template('search.html')


if __name__ == '__main__':

    # Creating database tables and populating courses table, then adding 50 books into the Books table
    tool.db_setup(conn, cur, "sqlcommands v1.sql")
    tool.db_insert_random_books(conn, cur, 50)

    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()

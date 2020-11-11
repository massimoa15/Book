import os, tool
from flask import Flask, render_template, flash, redirect, url_for, session, request
import mysql.connector
import random as rm

# DB connection
conn = mysql.connector.connect(user='root', password='root', host="localhost", database="book")

app = Flask(__name__)


# Init redirect
@app.route('/')
def index():
    return redirect(url_for('login'))


# Home page
@app.route('/home')
def home():
    cur = conn.cursor(dictionary=True)

    # Fetch some number of books from DB to display
    cur.execute("select * from books limit %s", [25])
    books = cur.fetchall()

    cur.close()
    return render_template('home.html', books=books)


# Page for specific book
@app.route('/book/<string:isbn>')
def book(isbn):
    cur = conn.cursor(dictionary=True)

    # Grab info for book based on isbn
    cur.execute("select * from books where BISBN = %s", [isbn])

    # Try to fetch book info from DB
    b = cur.fetchone()
    cur.close()

    # Only load page if book was found
    if b:
        return render_template('book.html', book=b)
    # if the book is not found then display error page
    else:
        return redirect(url_for('index'))


# DB search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = "MATH-1730"
    # Result of search
    if request.method == 'POST' or query:
        cur = conn.cursor(dictionary=True)

        # Grab info from HTML form
        # method = request.form.get('method')
        # query = request.form.get('query')

        cur.execute("select * from books where BCourseID = %s", [query])
        books = cur.fetchall()

        # Add random price
        for b in books:
            b['price'] = "$" + str(rm.randrange(600)) + "." + str(rm.randrange(100)).zfill(2)

        cur.close()
        return render_template('search.html', books=books, numResults=len(books))

    # GET method, display search and search options
    else:
        return render_template('search.html', numResults=0)


# DB login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["exampleInputEmail1"]
        password = request.form["exampleInputPassword1"]

        if tool.userLogin(email, password, conn):
            return redirect(url_for('index'))

    return render_template("login.html")


# DB signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form["exampleInputEmail1"]
        username = request.form["userName1"]
        password = request.form["exampleInputPassword1"]
        confirm_password = request.form["exampleInputPassword2"]

        if password == confirm_password:
            # attempting to create account, if account creation fails, returns False and reason is printed
            if tool.register(username, password, email, conn):
                return redirect(url_for('index'))

    return render_template("signup.html")


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()

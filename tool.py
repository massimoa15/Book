# This file exists to provide tool functions for the main python script (app.py)
import names
import random as rm
from coolname import generate
import constants


def genbook():
    '''
    Generates book information
    Title randomly generated from coolname
    Author randomly generated from names library
    ISBN is randomly generated 12 digit number
    CourseID is a randomly chosen id based off of known Ids
    :return: Dictionary containing a title, author, and ISBN-13
    '''
    title = ' '.join(generate(3)).title()

    author = names.get_full_name()

    # Generate ISBN with proper checksum
    isbn = ''.join([str(rm.randrange(10)) for i in range(12)])
    check = sum([int(i) * 3 if isbn.index(i) % 2 != 0 else int(i) for i in isbn]) % 10
    digit = check if check == 0 else 10 - check

    isbn += str(digit)
    courseID = rm.choice(constants.courseIds)
    # print(title,author, isbn)
    return {'title': title, 'author': author, 'isbn': isbn, 'courseID': courseID}


# DB setup
def db_setup(connection, cursor, filename):
    """ Creates the tables of the database and inserts course data into Courses table"""

    if connection is not None:
        with open(filename, "r") as f:
            sqlfile = f.read()
            commands = sqlfile.split(";")

            for c in commands:
                try:
                    if c.strip() != "":
                        cursor.execute(c)
                except:
                    pass

        connection.commit()

    else:
        print("Connection is None")


# adds a book to the database
def db_add_book(connection, cursor, book_course_id, book_title, book_author, book_isbn):
    if connection is not None:

        insertion_command = f"INSERT INTO `Books` (`BCourseID`, `BTitle`,`BAuthor`, `BIsbn`) VALUES " \
                            f"('{book_course_id}','{book_title}', '{book_author}', '{book_isbn}')"
        cursor.execute(insertion_command)

        connection.commit()

    else:
        print("Connection is None")


# Acts as wrapper function for db_add_book to automatically insert randomly generated books
def db_insert_random_books(connection, cursor, numberOfBooks):
    if connection is not None:
        for i in range(numberOfBooks):
            book = genbook()
            db_add_book(connection, cursor, book['courseID'], book['title'], book['author'], book['isbn'])

    else:
        print("Connection is not None")


# fetches n books stored in the db from top to bottom
def db_get_n_books(cursor, numberOfBooks):
    if cursor is not None:
        cursor.execute(f"select * from books limit {numberOfBooks}")
        return cursor.fetchall()

    else:
        print("Cursor is None")


if __name__ == '__main__':
    genbook()

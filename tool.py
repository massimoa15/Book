# This file exists to provide tool functions for the main python script (app.py)
import names
import random as rm
from coolname import generate

def genbook():
    '''
    Generates book information
    Title randomly generated from coolname
    Author randomly generated from names library
    ISBN is randomly generated 12 digit number
    :return: Dictionary containing a title, author, and ISBN-13
    '''
    title = ' '.join(generate(3)).title()

    author = names.get_full_name()

    # Generate ISBN with proper checksum
    isbn = ''.join([str(rm.randrange(10)) for i in range(12)])
    check = sum([int(i) * 3 if isbn.index(i) % 2 != 0 else int(i) for i in isbn]) % 10
    digit = check if check == 0 else 10 - check

    isbn += str(digit)

    #print(title,author, isbn)
    return {'title': title, 'author': author, 'isbn': isbn}


if __name__ == '__main__':
    genbook()
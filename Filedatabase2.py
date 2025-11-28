#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Concerned with storing and retrieving books from a Database with
context management example.
"""

from database_connection2 import DatabaseConnection

def create_book_table():
    """ context management example """
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)''')


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES( ?, ?, 0)', (name, author))


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
    
        books = [{
            'name': book[0],
            'author': book[1],
            'read': book[2]
        } for book in cursor.fetchall()]
    return books


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
        #(name,)in ordet to say that is a tuple with one element


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name = ?', (name,))



        


#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Concerned with storing and retrieving books from a Database

"""
import sqlite3

def create_book_table():
    try:
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)''')
        connection.commit()
        connection.close()

    except FileExistsError:
        pass #El fichero ya existe, no pasa nada
    except OSError as e:
        print(f"Error al crear el fichero: {e}")        
    
def add_book(name, author):
    # ", 0); DROP TABLE books; --"
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    
    #basicamente inseguro:
    #cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')

    #SQL Injection Attack Example:
    #cursor.execute(f'INSERT INTO books VALUES("{name}", "", 0); DROP TABLE books;", 0')

    #con una lista de tuplas
    #cursor.execute(f'INSERT INTO books VALUES(?, ?, ?)', (book['name'], book['author'], int(book['read'])))

    cursor.execute('INSERT INTO books VALUES( ?, ?, 0)', (name, author))

    connection.commit()
    connection.close()
    

def get_all_books():
    """ 
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM books')
    books_from_db = cursor.fetchall()
    connection.close()

    books = []
    for book in books_from_db:
        books.append({
            'name': book[0],
            'author': book[1],
            'read': True if book[2] == 1 else False
        })
    return books
    """
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM books')
    """
    books = cursor.fetchall()# Tupla de tuplas [(name, author, read), (name, author, read)]
    """
    books = [{
        'name': book[0],
        'author': book[1],
        'read': book[2]
    } for book in cursor.fetchall()]

    connection.close()
    return books


def mark_book_as_read(name):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    
    cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
    #(name,)in ordet to say that is a tuple with one element

    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    
    cursor.execute('DELETE FROM books WHERE name = ?', (name,))

    connection.commit()
    connection.close()
   

        


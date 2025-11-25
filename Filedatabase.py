#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Concerned with storing and retrieving books from a 

"""
import sqlite3

books_file = 'books.json'

def create_book_table():
    try:
        connection = sqlite3.connect('books.db?)')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books(name text, author text, read integer)''')
        connection.commit()
        connection.close()


    except FileExistsError:
        pass #El fichero ya existe, no pasa nada
    except OSError as e:
        print(f"Error al crear el fichero: {e}")


def _save_all_books(bonoks): #el simbolo _ quiere decir que es una funcion privada por convencion
    connection = sqlite3.connect('books.db?)')
    cursor = connection.cursor()
    #cursor.execute(f'INSERT INTO books VALUES(?, ?, ?)', (book['name'], book['author'], int(book['read'])))
    cursor.execute(f'SELECT * FROM books')

    connection.commit()
    connection.close()
        
    
def add_book(name, author):
    # ", 0); DROP TABLE books; --"
    connection = sqlite3.connect('books.db?)')
    cursor = connection.cursor()
    
    #basicamente inseguro:
    cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)')

    #SQL Injection Attack Example:
    #cursor.execute(f'INSERT INTO books VALUES("{name}", "", 0); DROP TABLE books;", 0')

    #con una lista de tuplas
    #cursor.execute(f'INSERT INTO books VALUES(?, ?, ?)', (book['name'], book['author'], int(book['read'])))

    cursor.execute(f'INSERT INTO books VALUES( ?, ?, 0)', (name, author))

    connection.commit()
    connection.close()
    

def get_all_books():
    try:
        with open(books_file, 'r') as file:
            return json.load(file)
   
    except FileNotFoundError:
        print("El fichero no existe todavía, devolviendo lista vacía.")
        return []
    except Exception as e:
        print(f"Error al leer el fichero: {e}")
        return []


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
   books = get_all_books()
   books = [book for book in books if book['name'] != name]
   _save_all_books(books)

        


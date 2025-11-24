#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
"""
Concerned with storing and retrieving books from a 

"""
import sqlite3

books_file = 'books.json'

def create_book_table():
    try:
        with open(books_file, 'w') as file:
            pass #No hacemos nada, solo crear el fichero
    except FileExistsError:
        pass #El fichero ya existe, no pasa nada
    except OSError as e:
        print(f"Error al crear el fichero: {e}")


def _save_all_books(books): #el simbolo _ quiere decir que es una funcion privada por convencion
    try:
        with open(books_file, 'w') as file:
            json.dump(books, file)
                
    except OSError as e:
        print(f"Error al guardar los libros: {e}")
        
    
def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


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

        


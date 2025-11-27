
import sqlite3

class DatabaseConnection:
   """ def __init__(self, db_name='books.db'):
        self.db_name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.connection.commit()
        self.connection.close()
    """
   
   def __init__():
       pass
   
   def __enter__(self):
       return sqlite3.connect('books.db')
   
   def __exit__(self, exc_type, exc_value, traceback):
       pass
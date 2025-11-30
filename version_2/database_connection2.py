
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
   
   def __init__(self, host):
       self.connection = None
       self.host = host
   
   def __enter__(self):
       self.connection = sqlite3.connect(self.host)
       return self.connection
   
   def __exit__(self, exc_type, exc_value, exc_traceback):
        #if exc_type or exc_value or exc_traceback:
        if exc_type is not None or exc_value is not None or exc_traceback is not None:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close
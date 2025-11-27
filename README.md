# Serie Bases de Datos con Python
## Sqlite


En el fichero Filedatabase.py creamos la base de datos y la tabla que vamos a utilizar
> connection = sqlite3.connect('books.db')

 > cursor = connection.cursor()

>cursor.execute('''CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)''')

>connection.commit()

>connection.close()


Como vemos solo hace falta el fichero que maneja la base de datos, que en este caso es un fichero de texto.
El fichero de la aplicacion app.py, practicamente no hace falta modificarlo a excepcion de esta sentencia:

 > read = 'YES' if book_return['read'] else 'NO'
 
Esta tambien:
> books = [book for book in books if book['name'] != name]

Hay dos versiones, los ficheros que llevan el numero 2 pertenecen a una version mas
avanzada pues se les aplica *"context management"*, osea se le aplica otra capa mas
separando la apetura y cierre de la conexion en otro fichero llamado **database_connection2.py**

Para ver paso a paso como se desarrolla visitar el este video de youtube
https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p

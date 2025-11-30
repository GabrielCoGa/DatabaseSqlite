# Serie Bases de Datos con Python
## Sqlite SQL
## Sqlite ORM - SQLAlchemy

Hay dos versiones, la primera version es inciaria, la segunda es una version mas
avanzada pues se les aplica *"context management"*, osea se le aplica otra capa mas
separando la apetura y cierre de la conexion en otro fichero llamado **database_connection2.py**

En el fichero Filedatabase.py o en el fichero database_connection2.py creamos la base de datos,
segun la version, y la tabla que vamos a utilizar

> connection = sqlite3.connect('books.db')

 > cursor = connection.cursor()

> cursor.execute('''CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)''')

> connection.commit()

> connection.close()


Como vemos solo hace falta modificar el fichero que maneja la base de datos o bien crear uno nuevo, si 
le añadimos una capa mas de aislamiento de cada cometido.

El fichero de la aplicacion app.py, practicamente no hace falta modificarlo a excepcion de esta sentencia:

 > read = 'YES' if book_return['read'] else 'NO'
 
Para ver paso a paso como se desarrolla visitar el este video de youtube:
https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p


Para ver paso a paso como se desarrolla la version 3 visitar el este video de youtube:
https://youtu.be/xr7vDSFXjW0?si=bMK_uNbwnIbvztuO

Para crear el entorno virtual para instalar SQLAlchemy visitar el capitulo de este video de youtube:
https://youtu.be/eGwuHtRaFrM?si=J8kX7POTs43mG80Q


> python3 -m pip install --user --upgrade pip

> python3 -m pip install --user virtualenv

> python3 -m venv version_3

> cd version_3

> source bin/activate

>  pip3 install sqlalchemy

Se puede desativar el entorno virtual con:

>  deactivate

Para volverlo a activar:

> source bin/activate
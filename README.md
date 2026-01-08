# Serie Bases de Datos con Python
## Sqlite SQL
## Sqlite ORM - SQLAlchemy
## Sqlite - SQLModel
>----------------------------------------------------------------------------------------------
### Sqlite SQL
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

### Sqlite ORM - SQLAlchemy
Para visitar el sitio oficial: https://www.sqlalchemy.org/

Para ver paso a paso como se desarrolla la version 3 visitar el este video de youtube:
https://youtu.be/xr7vDSFXjW0?si=bMK_uNbwnIbvztuO

En el fichero **main.py** tenemos el codigo de creacion de la base de datos y una tabla:

>from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
>from sqlalchemy.orm import declarative_base, relationship, sessionmaker

>engine  = create_engine('sqlite:///orm.db')

>Session = sessionmaker( bind=engine)
>session = Session()

>Base = declarative_base()

>class User(Base):
 >   __tablename__ = 'users'
 >  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
 >   name = Column(String(50))
 >   email = Column(String(50))

>Base.metadata.create_all(engine)

En el fichero **mainrelationships.py** tenemos como montar una relacion entre dos tablas de la base de datos:

>class User(Base):
 >   __tablename__ = 'users'
 >  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
 >   name = Column(String(50))
 >   email = Column(String(50))

 >   posts = relationship('Post', back_populates='user')

>class Post(Base):
 >   __tablename__ = 'posts'
 >   id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
 >   title = Column(String(100))
 >   content = Column(String(500))
 >   user_id = Column(Integer, ForeignKey('users.id'))

 >   user = relationship('User', back_populates='posts')


Para crear el ***entorno virtual*** para instalar SQLAlchemy visitar el capitulo de este video de youtube:
https://youtu.be/eGwuHtRaFrM?si=J8kX7POTs43mG80Q

Instalamos y activamos el entorno virutal:
> python3 -m pip install --user --upgrade pip

> python3 -m pip install --user virtualenv

> python3 -m venv version_3

> cd version_3

> source bin/activate

Instalamos SQLAlchemy:
>  pip3 install sqlalchemy

Se puede desativar el entorno virtual con:
>  deactivate

Para volverlo a activar:
> source bin/activate

### Sqlite - SQLModel
para visitar el sitio oficial: https://sqlmodel.tiangolo.com/

SqlModel es la mezcla de ORM SQLAlchemy y Pydantic.

Pydantic is the most widely used data validation and parsing library for Python. As of 2026, it remains a cornerstone of the Python ecosystem, utilized for ensuring data integrity by leveraging native Python type hints.
Para visital el sitio oficial: https://docs.pydantic.dev/latest/

Ejemplo:
>from pydantic import BaseModel

>class User(BaseModel):
 >   id: int
 >   name: str
 >   is_active: bool = True  # Default value

>#Validation and Parsing
>user = User(id="123", name="John Doe") 
>print(user.id)  # Output: 123 (automatically converted from string to int)


Para ver paso a paso como se desarrolla la version 4 visitar el este video de youtube:
https://youtu.be/RU6Fk6bmBk8?si=xM1OxX_l1tjDNvG5

Dentro del directorio de trabajo activamos el entorno virtual, como ya vimos anteriormente:
> python3 -m venv version_4

> cd version_4

> source bin/activate

Instalamos SQLModel:
>  pip3 install sqlmodel



Otro ejemplo paso a paso:
https://betterstack.com/community/guides/scaling-python/sqlmodel-orm/
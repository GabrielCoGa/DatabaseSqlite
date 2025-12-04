# SQLAlchemy Tutorial for Beginners
#https://youtu.be/xr7vDSFXjW0?si=wcwI5RPNsaNZVpJC
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine  = create_engine('sqlite:///orm.db')

Session = sessionmaker( bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    #id = column(Integer, Sequence('user_id_seq'), primary_key=True)
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

Base.metadata.create_all(engine)

user1 = User(name='Alice', email='alice@example.com')
user2 = User(name='Bob', email=' bob@example.com')

session.add_all([user1, user2])
session.commit()


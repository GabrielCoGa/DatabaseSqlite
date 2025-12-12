# SQLAlchemy Tutorial for Beginners
#https://youtu.be/xr7vDSFXjW0?si=wcwI5RPNsaNZVpJC
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine  = create_engine('sqlite:///orm_relationships.db')

Session = sessionmaker( bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String(100))
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

    user = relationship('User', back_populates='posts')

Base.metadata.create_all(engine)

user1 = User(name='Alice', email='alice@example.com')
user2 = User(name='Bob', email='bob@example.com')

#insert data:
session.add_all([user1, user2])
session.commit()

#query data:
user = session.query(User).filter_by(name=('Alice')).first()
if user is not None:
    print(f'User: {user.name}, Email: {user.email}')

#delete data:
    session.delete(user)
    session.commit()

#verify deletion
user = session.query(User).filter_by(name='Alice').first()
if user is None:
    print('User Alice has been deleted.')
else:
    print(f'User: {user.name}, Email: {user.email}')

#update data:
session.query(User).filter(User.name == 'Bob').update(
    {User.email: 'bob_new@example.com'}
)

session.commit()

#verify update
user = session.query(User).filter_by(name='Bob').first()
if user is not None:
    print(f'User: {user.name}, Email: {user.email}')


session.close()

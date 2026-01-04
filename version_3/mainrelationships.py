# SQLAlchemy Tutorial for Beginners
#https://youtu.be/xr7vDSFXjW0?si=wcwI5RPNsaNZVpJC
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

#engine  = create_engine('sqlite:///orm_relationships.db')

#show SQL statements with echo=True
engine  = create_engine('sqlite:///orm_relationships.db', echo=True)

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

Base.metadata.create_all(engine)

user1 = User(name='Alice', email='alice@example.com')
user2 = User(name='Bob', email='bob@example.com')
post1 = Post(title='Alice First Post', content='This is the content of the Alice first post.', user=user1)
post2 = Post(title='Bob First Post', content='This is the content of the Bob first post.', user=user2)
post3 = Post(title='Alice Second Post', content='This is the content of the Alice second post.', user=user1)
  
#insert data:
session.add_all([user1, user2, post1, post2, post3])
session.commit()

#query data:
posts_with_user = session.query(Post, User).join(User).all()

for post, user in posts_with_user:
    print(f'Post Title: {post.title}, Author: {user.name}, Email: {user.email}')

alice = session.query(User).filter(User.name == 'Alice').first()
for post in alice.posts:
    print(f'\nAlice Post Title: {post.title}, Content: {post.content}') 

alice_posts = session.query(Post).join(User).filter(User.name == 'Alice').all()
print("\nPosts by Alice:")
for post in alice_posts:
    print(f'Post Title: {post.title}, Content: {post.content}')

# Close the session
session.close()

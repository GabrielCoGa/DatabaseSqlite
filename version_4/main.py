from sqlmodel import SQLModel, create_engine, Session, select, Relationship, Field

engine = create_engine("sqlite:///orm.db", echo=True)

class Author(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=50, unique=True)

    books: list["Book"] = Relationship(back_populates="author")

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str
    author_id: int | None = Field(default=None, foreign_key="author.id")
    
    author: Author = Relationship(back_populates="books")
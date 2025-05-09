# Create a new database and manipulate table using Python library - SQLAlchemy.
#
# 1. Create a script to set up the database named films_db; and create table named films with following columns:
# id (integer, primary key)
# title (string)
# director (string)
# release year (integer)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# set up for db connection
engine = create_engine('sqlite:///films_db.sqlite', echo=True)
Base = declarative_base()

# film class that represents a table in the db
class Film(Base):
    # film table attributes
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

    def __repr__(self):
        return f"----------\n{self.id}: {self.title}\n{self.director} - {self.release_year}\n----------"

#generates database
Base.metadata.create_all(engine)
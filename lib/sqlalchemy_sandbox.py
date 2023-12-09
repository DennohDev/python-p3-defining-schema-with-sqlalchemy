#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# declarative_base() combines a container for table metadata as well as a group of methods that act as mappers between Python and our SQL database
# Inheritance From Base allows us to avoid rewritting code
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db', echo=True)
    Base.metadata.create_all(engine)
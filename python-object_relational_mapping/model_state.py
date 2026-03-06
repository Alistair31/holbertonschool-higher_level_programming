#!/usr/bin/python3
"""
This module defines the State class which maps
to the 'states' table in the database.
It uses SQLAlchemy's declarative base to create
the mapping between the class and the table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """State class that maps to the 'states' table in the database."""
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)

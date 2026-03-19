#!/usr/bin/python3
"""
This module defines the City class which maps
to the 'cities' table in the database.
It uses SQLAlchemy's declarative base to create
the mapping between the class and the table."""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """City class that maps to the 'cities' table in the database."""
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

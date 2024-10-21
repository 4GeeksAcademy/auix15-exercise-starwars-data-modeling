
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#relación muchos-a-muchos entre usuario y planetas favoritos
favorite_planet = Table('favorite_planet', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True)
)

# relación muchos-a-muchos entre usuario y personajes favoritos
favorite_character = Table('favorite_character', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
    # Relación muchos-a-muchos con planetas y personajes
    favorite_planets = relationship('Planet', secondary=favorite_planet, backref='favorited_by_users')
    favorite_characters = relationship('Character', secondary=favorite_character, backref='favorited_by_users')

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)

class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

# Generar el diagrama UML
render_er(Base, 'diagram.png')

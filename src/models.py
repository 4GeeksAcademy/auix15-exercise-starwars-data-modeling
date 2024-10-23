
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
    # Relación muchos-a-muchos con planetas y personajes
    favorite = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)

    favorited_by = relationship('Favorite', back_populates='planet')
    
class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

    favorited_by = relationship('Favorite', back_populates='character')

class Favorite(Base):
    __tablename__= 'favorite'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    
    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet')
    character = relationship('Character')

    def to_dict(self):
        return {}

# Generar el diagrama UML
print("Generating diagram...")
render_er(Base, 'diagram.png')
print("Diagram generated as diagram.png")

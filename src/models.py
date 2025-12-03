import os 
import sys 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, declarative_base 
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    is_active = Column(Boolean(), nullable=False)

class Planet(Base):
    __tablename__ = "planet"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    climate = Column(String(120))
    terrain = Column(String(120))
    population = Column(String(120))

    residents = relationship("Character", back_populates="homeworld")

class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    homeworld_id = Column(Integer, ForeignKey("planet.id"), nullable=False)

    homeworld = relationship("Planet", back_populates="residents")

class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character_id = Column(Integer, ForeignKey("character.id"))

    user = relationship("User")
    planet = relationship("Planet")
    character = relationship("Character")

render_er(Base, 'diagram.png')


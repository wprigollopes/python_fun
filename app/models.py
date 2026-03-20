from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    abbreviation = Column(String(2), nullable=False, unique=True)
    region = Column(String(20), nullable=False)
    size = Column(Integer)

    def __repr__(self):
        return f"<State(name='{self.name}', abbreviation='{self.abbreviation}')>"


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    state = Column(String(2), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    population = Column(Integer)

    def __repr__(self):
        return f"<City(name='{self.name}', state='{self.state}')>"

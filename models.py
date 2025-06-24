<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

libro_genero = Table(
    'libro_genero', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libros.id'), primary_key=True),
    Column('genero_id', Integer, ForeignKey('generos.id'), primary_key=True)
)

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    libros = relationship("Libro", back_populates="autor")

class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    libros = relationship("Libro", secondary=libro_genero, back_populates="generos")

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    autor = relationship("Autor", back_populates="libros")
=======
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

libro_genero = Table(
    'libro_genero', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libros.id'), primary_key=True),
    Column('genero_id', Integer, ForeignKey('generos.id'), primary_key=True)
)

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    libros = relationship("Libro", back_populates="autor")

class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    libros = relationship("Libro", secondary=libro_genero, back_populates="generos")

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    autor = relationship("Autor", back_populates="libros")
>>>>>>> 223ecc28ee676c2d7eec23a6ed56a088e7526074
    generos = relationship("Genero", secondary=libro_genero, back_populates="libros")
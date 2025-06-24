<<<<<<< HEAD
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Autor, Libro, Genero

class BibliotecaController:
    def __init__(self):
        self.db = SessionLocal()

    def crear_autor(self, nombre: str):
        autor = Autor(nombre=nombre)
        self.db.add(autor)
        self.db.commit()
        self.db.refresh(autor)
        return autor

    def obtener_autores(self):
        return self.db.query(Autor).all()

    def actualizar_autor(self, autor_id: int, nuevo_nombre: str):
        autor = self.db.query(Autor).filter(Autor.id == autor_id).first()
        if autor:
            autor.nombre = nuevo_nombre
            self.db.commit()
            return True
        return False

    def eliminar_autor(self, autor_id: int):
        autor = self.db.query(Autor).filter(Autor.id == autor_id).first()
        if autor:
            self.db.delete(autor)
            self.db.commit()
            return True
        return False

    def crear_genero(self, nombre: str):
        genero = Genero(nombre=nombre)
        self.db.add(genero)
        self.db.commit()
        self.db.refresh(genero)
        return genero

    def obtener_generos(self):
        return self.db.query(Genero).all()

    def crear_libro(self, titulo: str, autor_id: int, generos_ids: list):
        libro = Libro(titulo=titulo, autor_id=autor_id)
        generos = self.db.query(Genero).filter(Genero.id.in_(generos_ids)).all()
        libro.generos.extend(generos)
        self.db.add(libro)
        self.db.commit()
        return libro

    def obtener_libros(self):
        return self.db.query(Libro).all()

    def eliminar_libro(self, libro_id: int):
        libro = self.db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            self.db.delete(libro)
            self.db.commit()
            return True
=======
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Autor, Libro, Genero

class BibliotecaController:
    def __init__(self):
        self.db = SessionLocal()

    def crear_autor(self, nombre: str):
        autor = Autor(nombre=nombre)
        self.db.add(autor)
        self.db.commit()
        self.db.refresh(autor)
        return autor

    def obtener_autores(self):
        return self.db.query(Autor).all()

    def actualizar_autor(self, autor_id: int, nuevo_nombre: str):
        autor = self.db.query(Autor).filter(Autor.id == autor_id).first()
        if autor:
            autor.nombre = nuevo_nombre
            self.db.commit()
            return True
        return False

    def eliminar_autor(self, autor_id: int):
        autor = self.db.query(Autor).filter(Autor.id == autor_id).first()
        if autor:
            self.db.delete(autor)
            self.db.commit()
            return True
        return False

    def crear_genero(self, nombre: str):
        genero = Genero(nombre=nombre)
        self.db.add(genero)
        self.db.commit()
        self.db.refresh(genero)
        return genero

    def obtener_generos(self):
        return self.db.query(Genero).all()

    def crear_libro(self, titulo: str, autor_id: int, generos_ids: list):
        libro = Libro(titulo=titulo, autor_id=autor_id)
        generos = self.db.query(Genero).filter(Genero.id.in_(generos_ids)).all()
        libro.generos.extend(generos)
        self.db.add(libro)
        self.db.commit()
        return libro

    def obtener_libros(self):
        return self.db.query(Libro).all()

    def eliminar_libro(self, libro_id: int):
        libro = self.db.query(Libro).filter(Libro.id == libro_id).first()
        if libro:
            self.db.delete(libro)
            self.db.commit()
            return True
>>>>>>> 223ecc28ee676c2d7eec23a6ed56a088e7526074
        return False
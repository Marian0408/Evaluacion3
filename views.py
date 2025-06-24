class BibliotecaView:
    def __init__(self, controller):
        self.controller = controller

    def mostrar_menu(self):
        while True:
            print("\n--- SISTEMA DE BIBLIOTECA ---")
            print("1. Gestión de Autores")
            print("2. Gestión de Géneros")
            print("3. Gestión de Libros")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_autores()
            elif opcion == "2":
                self.menu_generos()
            elif opcion == "3":
                self.menu_libros()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def menu_autores(self):
        while True:
            print("\n--- GESTIÓN DE AUTORES ---")
            print("1. Crear autor")
            print("2. Listar autores")
            print("3. Actualizar autor")
            print("4. Eliminar autor")
            print("5. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del autor: ")
                self.controller.crear_autor(nombre)
                print("Autor creado exitosamente!")
            elif opcion == "2":
                autores = self.controller.obtener_autores()
                print("\n--- LISTA DE AUTORES ---")
                for autor in autores:
                    print(f"ID: {autor.id} | Nombre: {autor.nombre}")
            elif opcion == "3":
                autor_id = int(input("ID del autor a actualizar: "))
                nuevo_nombre = input("Nuevo nombre: ")
                if self.controller.actualizar_autor(autor_id, nuevo_nombre):
                    print("Autor actualizado exitosamente!")
                else:
                    print("No se encontró el autor")
            elif opcion == "4":
                autor_id = int(input("ID del autor a eliminar: "))
                if self.controller.eliminar_autor(autor_id):
                    print("Autor eliminado exitosamente!")
                else:
                    print("No se encontró el autor")
            elif opcion == "5":
                break
            else:
                print("Opción no válida")

    def menu_generos(self):
        while True:
            print("\n--- GESTIÓN DE GÉNEROS ---")
            print("1. Crear género")
            print("2. Listar géneros")
            print("3. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del género: ")
                self.controller.crear_genero(nombre)
                print("Género creado exitosamente!")
            elif opcion == "2":
                generos = self.controller.obtener_generos()
                print("\n--- LISTA DE GÉNEROS ---")
                for genero in generos:
                    print(f"ID: {genero.id} | Nombre: {genero.nombre}")
            elif opcion == "3":
                break
            else:
                print("Opción no válida")

    def menu_libros(self):
        while True:
            print("\n--- GESTIÓN DE LIBROS ---")
            print("1. Crear libro")
            print("2. Listar libros")
            print("3. Actualizar libro")
            print("4. Eliminar libro")
            print("5. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                titulo = input("Título del libro: ")
                autor_id = int(input("ID del autor: "))
                generos = self.controller.obtener_generos()
                print("Géneros disponibles:")
                for g in generos:
                    print(f"ID: {g.id} | {g.nombre}")
                generos_ids = list(map(int, input("IDs de géneros (separados por coma): ").split(',')))
                self.controller.crear_libro(titulo, autor_id, generos_ids)
                print("Libro creado exitosamente!")
            elif opcion == "2":
                libros = self.controller.obtener_libros()
                print("\n--- LISTA DE LIBROS ---")
                for libro in libros:
                    generos = ", ".join([g.nombre for g in libro.generos])
                    print(f"ID: {libro.id} | Título: {libro.titulo} | Autor: {libro.autor.nombre} | Géneros: {generos}")
            elif opcion == "3":
                libro_id = int(input("ID del libro a actualizar: "))
                print("Actualización de libro (implementar)")
            elif opcion == "4":
                libro_id = int(input("ID del libro a eliminar: "))
                if self.controller.eliminar_libro(libro_id):
                    print("Libro eliminado exitosamente!")
                else:
                    print("No se encontró el libro")
            elif opcion == "5":
                break
            else:
                print("Opción no válida")
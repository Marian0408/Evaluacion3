#<<<<<<< HEAD
from controllers import BibliotecaController
from views import BibliotecaView
from database import init_db

def main():
    init_db()
    
    controller = BibliotecaController()
    view = BibliotecaView(controller)
    
    view.mostrar_menu()  
if __name__ == "__main__":
#=======
    from controllers import BibliotecaController
    from views import BibliotecaView
    from database import init_db

def main():
    init_db()
    
    controller = BibliotecaController()
    view = BibliotecaView(controller)
    
    view.mostrar_menu()  
if __name__ == "__main__":
#>>>>>>> 223ecc28ee676c2d7eec23a6ed56a088e7526074
    main()
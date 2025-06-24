from controllers import BibliotecaController
from views import BibliotecaView
from database import init_db

def main():
    init_db()
    
    controller = BibliotecaController()
    view = BibliotecaView(controller)
    
    view.mostrar_menu()  
if __name__ == "__main__":
    main()
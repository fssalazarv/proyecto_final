from controller.menu import *git add controller/function.py controller/function.py
from config.app import *
from controller.function import *
if __name__ == "__main__":
    app=App('./datux.db')
    menu(app)
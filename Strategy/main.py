from tkinter import Tk
from Controller.juego_controller import JuegoController
from View.interfaz_juego import InterfazJuego

def main():
    root = Tk()

    controller = JuegoController()
    app = InterfazJuego(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
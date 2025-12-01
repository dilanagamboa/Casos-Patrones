from .Visual.gui_tk import SandwichApp
from .Model.sandwich import *

def main():
    gui = SandwichApp()
    gui.mainloop()


if __name__ == "__main__":
    main()
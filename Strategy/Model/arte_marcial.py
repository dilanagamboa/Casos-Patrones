from abc import ABC, abstractmethod

class ArteMarcial(ABC):
    def __init__(self, nombre, nombre_imagen):
        self.nombre = nombre
        self.nombre_imagen = nombre_imagen
        self.golpes = []
    
    # lista de golpes del arte marcial
    @abstractmethod
    def obtener_golpes(self):
        pass
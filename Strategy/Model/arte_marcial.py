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
    
    # cada arte marcial define cómo genera su combo, entonces acá se aplica Strategy
    @abstractmethod
    def ejecutar_combo(self, num_golpes):
        pass
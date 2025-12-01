from enum import Enum
from .sandwich import SandwichSize
class Ingredients(Enum):
    #PROTEINAS
    PAVO = {
        "nombre": "Pavo",
        "tipo": "Proteina",
        "precio": lambda size: { SandwichSize.SMALL: 12.0, SandwichSize.BIG: 18.0 }[size],
    }
    ITALIANO = {
        "nombre": "Italiano",
        "tipo": "Proteina",
        "precio": lambda size: { SandwichSize.SMALL: 9.0, SandwichSize.BIG: 16.0 }[size],
    }
    BEEF = {
        "nombre": "Beef",
        "tipo": "Proteina",
        "precio": lambda size: { SandwichSize.SMALL: 10.0, SandwichSize.BIG: 16.0 }[size],
    }
    VEGGIE = {
        "nombre": "Veggie",
        "tipo": "Proteina",
        "precio": lambda size: { SandwichSize.SMALL: 18.0, SandwichSize.BIG: 14.0 }[size],
    }
    ATUN = {
        "nombre": "Atun",
        "tipo": "Proteina",
        "precio": lambda size: { SandwichSize.SMALL: 11.0, SandwichSize.BIG: 17.0 }[size],
    }
    POLLO = {
        "nombre": "Pollo",
        "tipo": "Proteina",
        "precio": lambda size: { SandwichSize.SMALL: 12.0, SandwichSize.BIG: 18.0 }[size],
    }

    #EXTRAS

    AGUACATE = {
        "nombre": "Aguacate",
        "tipo": "Extra",
        "precio": lambda size: { SandwichSize.SMALL: 1.5, SandwichSize.BIG: 2.5 }[size],
    }
    Doble_PROTEINA = {
        "nombre": "Doble Proteina",
        "tipo": "Extra",
        "precio": lambda size: { SandwichSize.SMALL: 4.5, SandwichSize.BIG: 8.0 }[size],
    }
    HONGOS = {
        "nombre": "Hongos",
        "tipo": "Extra",
        "precio": lambda size: { SandwichSize.SMALL: 0.85, SandwichSize.BIG: 1.45 }[size],
    }
    REFRESCO = {
        "nombre": "Refresco",
        "tipo": "Extra",
        "precio": lambda size: { SandwichSize.SMALL: 1.0, SandwichSize.BIG: 1.0 }[size],
    }
    SOPA = {
        "nombre": "Sopa",
        "tipo": "Extra",
        "precio": lambda size: { SandwichSize.SMALL: 4.2, SandwichSize.BIG: 4.2 }[size],
    }
    POSTRE = {
        "nombre": "Postre",
        "tipo": "Extra",
        "precio": lambda size: { SandwichSize.SMALL: 3.5, SandwichSize.BIG: 3.5 }[size],
    }


    def nombre(self):
        return self.value["nombre"]

    def precio(self, size):
        p = self.value["precio"]
        if callable(p):
            return p(size)
        return p
    
    def tipo(self):
        return self.value["tipo"]


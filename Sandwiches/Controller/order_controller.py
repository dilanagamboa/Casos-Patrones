from ..Model.sandwich import BaseSandwich, SandwichSize
from ..Services.builder import SandwichBuilder
from ..Model.ingredients import Ingredients

class OrderController:
    def __init__(self):
        self.orders = []  # lista de Sandwich (objetos)
        # builder se crea cuando empieza un nuevo sandwich
        self.builder = None

    def start_new(self, size: SandwichSize):
        base = BaseSandwich(_description="", _price=0.0, _size=size)
        self.builder = SandwichBuilder(base)
        return self.builder

    def add_ingredient(self, ingredient: Ingredients, qty: int = 1):
        if not self.builder:
            raise RuntimeError("No hay sandwich en construcción")
        self.builder.add(ingredient, qty)

    def remove_ingredient(self, ingredient: Ingredients, qty: int = 1):
        if not self.builder:
            raise RuntimeError("No hay sandwich en construcción")
        self.builder.remove(ingredient, qty)

    def finalize_current(self):
        if not self.builder:
            return None
        sandwich_obj = self.builder.build()
        self.orders.append(sandwich_obj)
        self.builder = None
        return sandwich_obj

    def get_orders(self):
        return self.orders

    def clear_orders(self):
        self.orders = []
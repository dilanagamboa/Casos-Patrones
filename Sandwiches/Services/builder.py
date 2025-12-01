from ..Model.sandwich import *
from ..Model.decorators import SandwichDecoratorIngredients
from ..Model.ingredients import Ingredients
from typing import Dict
class SandwichBuilder:
    def __init__(self, base : BaseSandwich):
        self.base = base
        self.ings: Dict[Ingredients, int] = {}
    
    def add(self, ing: Ingredients, can : int = 1):
        if can <=0:
            return self
        self.ings[ing] = self.ings.get(ing, 0) + can
        return self
    
    def remove(self, ing: Ingredients, can: int = 1):
        if ing not in self.ings:
            return self
        self.ings[ing] = max(0, self.ings[ing] - int(can))
        if self.ings[ing] == 0:
            del self.ings[ing]
        return self

    def clear(self):
        """Limpia todos los ingredientes añadidos."""
        self.ings.clear()
        return self

    def build(self) -> Sandwich:
        s = self.base
        for ing, qty in self.ings.items():
            price = Ingredients.precio(ing, s.size())
            s = SandwichDecoratorIngredients(s, ing, price, cantidad=qty)
        return s
    

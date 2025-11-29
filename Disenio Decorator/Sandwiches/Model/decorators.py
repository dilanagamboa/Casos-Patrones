from Sandwiches.Model.sandwich import Sandwich
from Sandwiches.Model.ingredients import Ingredients
from typing import Any

class SandwichDecoratorIngredients(Sandwich):
    def __init__(self, sandwich : Sandwich, ingredient : Ingredients, unit_price : float, cantidad : int = 1):
        self._sandwich = sandwich
        self._ingredient = ingredient
        self._unit_price = unit_price
        self._cantidad = max(0, int(abs(cantidad)))
        self._typ = self._ingredient.tipo()
        self._name = self._ingredient.nombre()

    def description(self):
        qty = f" x{self._cantidad}" if self._cantidad > 1 else ""
        total_ing = self.unitary_price() * self._cantidad
        if self._typ == "Proteina":
            return f"{self._sandwich.description()}{self._name}{qty} de {self.size().value} ({total_ing:.2f})"
        return f"{self._sandwich.description()} + {self._name}{qty} ({total_ing:.2f})"
    
    def size(self):
        return self._sandwich.size()
    
    def unitary_price(self):
        if callable(self._unit_price):
            return float(self._unit_price(self.size()))
        return float(self._unit_price)
    
    def price(self):
        return self._sandwich.price() + self.unitary_price()*self._cantidad
    
    def ingredient_summary(self):
        """
        Retorna una lista de ingredientes desde la base hasta este decorador.
        Cada ingrediente tiene: nombre, cantidad, precio unitario, subtotal y tipo.
        """
        summary = self._sandwich.ingredient_summary()

        unit = self.unitary_price()
        subtotal = unit * self._cantidad

        summary.append({
            "name": self._name,
            "qty": self._cantidad,
            "unit": unit,
            "total": subtotal,
        })

        return summary


from .Model.decorators import SandwichDecoratorIngredients
from .Model.ingredients import Ingredients
from .Services.builder import SandwichBuilder
from .Model.sandwich import *

def main():
    # Crear vista
    base = BaseSandwich("", 0.0, SandwichSize.BIG)

    s = base

    s = SandwichBuilder(s).add(Ingredients.BEEF, can=1).add(Ingredients.HONGOS, can=1).add(Ingredients.AGUACATE, can=1).build()

    x = s.ingredient_summary()

    for i in x:
        print(i)
    
    print(s.description(), s.price())

    print(base.size(), type(base.size()))


if __name__ == "__main__":
    main()
from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod

class SandwichSize(Enum):
    SMALL = "15"
    BIG = "30"

class Sandwich(ABC):
    @abstractmethod
    def description(self):
        raise NotImplementedError
    @abstractmethod
    def size(self):
        raise NotImplementedError
    @abstractmethod
    def price(self):
        raise NotImplementedError

@dataclass
class BaseSandwich(Sandwich):
    def __init__(self, _description : str = "", _price : float = 0.0, _size : SandwichSize = SandwichSize.SMALL):
        self._description = _description
        self._size = _size
        self._price = _price
    
    def description(self):
        return self._description
    
    def size(self):
        return self._size
    
    def price(self):
        return float(self._price)
    
    def ingredient_summary(self):
        return []
    

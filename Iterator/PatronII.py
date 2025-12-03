# iterators.py
from abc import ABC, abstractmethod
from collections.abc import Iterator as PyIterator
from typing import Any, Iterable, List, Optional

#Clase Iterator
class Iterator(ABC, PyIterator):
    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...

    def has_next(self) -> bool:
        try:
            return True
        except StopIteration:
            return False

    def reset(self):
        raise NotImplementedError("Reset no implementado para este iterador")


#Lista
class ArrayIterator(Iterator):
    def __init__(self, data: Iterable[Any]):
        self._data = list(data)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        val = self._data[self._index]
        self._index += 1
        return val

    def has_next(self) -> bool:
        return self._index < len(self._data)

    def reset(self):
        self._index = 0


class ArrayAggregate:
    def __init__(self, data: Iterable[Any]):
        self._data = list(data)

    def get_iterator(self) -> ArrayIterator:
        return ArrayIterator(self._data)


#Matriz
class MatrixIterator(Iterator):
    def __init__(self, matrix: List[List[Any]]):
        self._matrix = matrix
        self._r = 0
        self._c = 0
        self._advance_to_next_valid()

    def _advance_to_next_valid(self):
        while self._r < len(self._matrix) and self._c >= len(self._matrix[self._r]):
            self._r += 1
            self._c = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._r >= len(self._matrix):
            raise StopIteration
        val = self._matrix[self._r][self._c]
        self._c += 1
        self._advance_to_next_valid()
        return val

    def has_next(self) -> bool:
        return self._r < len(self._matrix)

    def reset(self):
        self._r = 0
        self._c = 0
        self._advance_to_next_valid()


class MatrixAggregate:
    def __init__(self, matrix: List[List[Any]]):
        self._matrix = matrix

    def get_iterator(self) -> MatrixIterator:
        return MatrixIterator(self._matrix)


# Arbol Binario
class TreeNode:
    def __init__(self, value: Any, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTreeIterator(Iterator):
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self._stack: List[TreeNode] = []
        self._current = None
        self._init_stack()

    def _init_stack(self):
        self._stack = []
        node = self.root
        while node is not None:
            self._stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stack:
            raise StopIteration
        node = self._stack.pop()
        val = node.value
        # procesar el subárbol derecho: bajar por las izquierdas
        right = node.right
        while right is not None:
            self._stack.append(right)
            right = right.left
        return val

    def has_next(self) -> bool:
        return len(self._stack) > 0

    def reset(self):
        self._init_stack()


class BinaryTreeAggregate:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def get_iterator(self) -> BinaryTreeIterator:
        return BinaryTreeIterator(self.root)


#pruebas
def pruebas():
    print("Array/tupla:")
    arr = ArrayAggregate((1, 2, 3, 4))
    it = arr.get_iterator()
    while True:
        try:
            print(next(it), end=" ")
        except StopIteration:
            break
    print("\n---")

    print("Matriz (row-major):")
    mat = MatrixAggregate([[1,2,3],[4,5],[6]])
    itm= mat.get_iterator()
    while True:
        try:
            print(next(itm), end=" ")
        except StopIteration:
            break
    print("\n---")

    # crear árbol:
    #      4
    #     / \
    #    2   6
    #   / \ / 
    #  1  3 5
    root = TreeNode(4,
                    left=TreeNode(2, TreeNode(1), TreeNode(3)),
                    right=TreeNode(6, TreeNode(5), None))
    tree = BinaryTreeAggregate(root)
    itt=tree.get_iterator()
    while True:
        try:
            print(next(itt), end=" ")
        except StopIteration:
            break

if __name__ == "__main__":
    pruebas()

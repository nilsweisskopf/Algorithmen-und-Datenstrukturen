"""
Implementing SearchTree, but with a Stopper Dummy.
~Nils Weißkopf 01. August 2025
"""

import doctest
from typing import Any


class Node:
    """Knoten with key, and knowledge about their sons."""

    def __init__(self, key: int, value: Any):
        self.left_son = None
        self.right_son = None
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return (
            f"({self.key}, {self.value!r}, "
            f"{self.left_son!r}, {self.right_son!r})"
        )


class SearchTree:
    """SearchTree, implemented with Zeiger."""

    def __init__(self):
        self.root = None

    def __repr__(self) -> str:
        return repr(self.root)

    def insert(self, key: int, value: Any) -> None:
        """
        Inserts an element with the given key and value.
        If the key already exists, the value is overwritten.

        >>> bst = SearchTree()
        >>> bst.insert(5, 'e')
        >>> bst.insert(1, 'a')
        >>> bst.insert(6, 'f')
        >>> bst.insert(7, 'g')
        >>> bst
        (5, 'e', (1, 'a', None, None), (6, 'f', None, (7, 'g', None, None)))

        >>> bst2 = SearchTree()
        >>> bst2.insert(2, 'b')
        >>> bst2.insert(1, 'a')
        >>> bst2.insert(0, ' ')
        >>> bst2.insert(3, 'c')
        >>> bst2
        (2, 'b', (1, 'a', (0, ' ', None, None), None), (3, 'c', None, None))

        >>> bst2.insert(3, 'd')
        >>> bst2.insert(1, 'e')
        >>> bst2.insert(2, 'f')
        >>> bst2
        (2, 'f', (1, 'e', (0, ' ', None, None), None), (3, 'd', None, None))
        """
        if self.root is None:
            self.root = Node(key, value)
            return

        node = self.root
        while True:
            if key < node.key:
                if node.left_son is None:
                    node.left_son = Node(key, value)
                    return
                node = node.left_son
            elif key > node.key:
                if node.right_son is None:
                    node.right_son = Node(key, value)
                    return
                node = node.right_son
            else:
                node.value = value
                return

    def look_recursive(self, key: int, node: Node) -> Node | None:
        """
        Searches recursively for a node with the given key.

        >>> bst = SearchTree()
        >>> bst.insert(2, 'b')
        >>> bst.insert(1, 'a')
        >>> bst.insert(3, 'c')
        >>> bst.insert(4, 'd')
        >>> bst.look_recursive(2, bst.root).key
        2
        >>> bst.look_recursive(4, bst.root).value
        'd'
        >>> bst.look_recursive(99, bst.root) is None
        True
        """
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.look_recursive(key, node.left_son)
        return self.look_recursive(key, node.right_son)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
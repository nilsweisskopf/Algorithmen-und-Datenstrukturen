""" one_sort algortihm ~Nils Weißkopf. """

import doctest
import sys


def one_sort(lst: list[int], i: int):
    """
    sorting one element int o a already sorted list.
    >>> lst = [1, 2, 3, 0, 5, 6, 9]
    >>> one_sort(lst, 3)
    >>> lst
    [0, 1, 2, 3, 5, 6, 9]
    """
    n = len(lst)
    while 0 < i < n - 1:
        while i > 0 and lst[i] <= lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
        while i < n - 1 and lst[i] >= lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i += 1


if __name__ == "__main__":
    doctest.run_docstring_examples(one_sort, globals())

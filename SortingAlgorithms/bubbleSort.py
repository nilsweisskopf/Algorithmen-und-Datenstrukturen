"""
Exam Implementation of Bubble Sort.
"""

import doctest


def bubble_sort(lst: list[int]) -> None:
    """
    Sorts a list in-place using bubble sort (descending fixed).

    >>> lst = [3, 1, 4, 1, 5]
    >>> bubble_sort(lst)
    >>> lst
    [1, 1, 3, 4, 5]
    """
    upper = len(lst) - 1
    for i in range(upper):
        for k in range(i, upper):
            if lst[k] > lst[k + 1]:  # Bugfix: war < statt >
                lst[k + 1], lst[k] = lst[k], lst[k + 1]


def sort_one(lst: list[int], i: int) -> None:
    """
    Sorts one misplaced element at index i into the correct position.

    >>> lst = [1, 2, 3, 4, 9, 6, 7, 20]
    >>> sort_one(lst, 4)
    >>> lst
    [1, 2, 3, 4, 6, 7, 9, 20]

    >>> lst = [1, 3, 4, 2, 6, 7, 20]
    >>> sort_one(lst, 3)
    >>> lst
    [1, 2, 3, 4, 6, 7, 20]
    """
    while i < len(lst) - 1 and lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        i += 1
    while i > 0 and lst[i] < lst[i - 1]:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
        i -= 1


if __name__ == "__main__":
    doctest.testmod(verbose=True)

"""
Sortieren durch Auswahl (Selection Sort)
Sorting a list by repeatedly finding the minimum element.
~Nils Weißkopf
"""

import sys
from time import monotonic


def sort(lst: list[int]) -> None:
    """
    Sorts a list in-place by repeatedly selecting the smallest element.

    >>> lst = [3, 5, 6, 4, 2, 5]
    >>> sort(lst)
    >>> lst
    [2, 3, 4, 5, 5, 6]

    >>> lst = []
    >>> sort(lst)
    >>> lst
    []

    >>> lst = [3, 4, 5, 6, 7, 8, 9]
    >>> sort(lst)
    >>> lst
    [3, 4, 5, 6, 7, 8, 9]
    """
    length = len(lst)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def main() -> None:
    """Perform test sortings and print runtimes."""
    iterations = 5

    for n in range(500, 10001, 500):
        timing = 0.0
        for _ in range(iterations):
            values = list(range(n, -1, -1))
            start = monotonic() * 1000
            sort(values)
            timing += (monotonic() * 1000) - start

        print(f"{n}\t{timing / iterations:.2f}ms")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
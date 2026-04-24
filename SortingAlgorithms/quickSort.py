"""
    QuickSort algorithm, quickest..

    Explanation:

    -> list is getting splitted into two halves
    -> choosing a pivotelement p
    -> sorting every element e ∈ lst by it's pivot element
    -> e < p → listA := ∀e ∈ lst < p
    -> e > p → listB := ∀e ∈ lst > p
"""

import time


def splittingList(lst: list[int], anfang: int, ende: int) -> int:
    """
    Vorgang einer QuickSort Iteration
    """
    pivot = lst[(anfang + ende) // 2]
    i, j = anfang - 1, ende + 1
    
    while True:
        i += 1
        while lst[i] < pivot:
            i += 1
        
        j -= 1
        while lst[j] > pivot:
            j -= 1
        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]


def quick_Sort(lst: list[int], anfang: int, ende: int) -> None:
    """
    recursive algorithm
    Doctests for Quicksort algorithm:
    """
    while anfang < ende:
        newPivot = splittingList(lst, anfang, ende)
        if newPivot - anfang < ende - (newPivot + 1):
            quick_Sort(lst, anfang, newPivot)
            links = newPivot + 1
        else:
            quick_Sort(lst, newPivot + 1, ende)
            ende = newPivot


def quickSort(lst: list[int]) -> None:
    """
    wrapper function, damit man nicht die werte links und rechts eingeben muss

    >>> lst = []
    >>> quickSort(lst); lst
    []
    >>> lst = [1]
    >>> quickSort(lst); lst
    [1]
    >>> lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> quickSort(lst); lst
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> lst = [23, 65, 8, 12, 23, 1, 3, 6, 100, 120, 0]
    >>> quickSort(lst); lst
    [0, 1, 3, 6, 8, 12, 23, 23, 65, 100, 120]
    """
    if lst:
        quick_Sort(lst, 0, len(lst) - 1)


if __name__ == "__main__":
    lst = [23, 65, 8, 12, 23, 1, 3, 6, 100, 120, 0]
    start_time = time.time()
    quickSort(lst)
    end_time = time.time()
    print(f"Sorted list: {lst}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
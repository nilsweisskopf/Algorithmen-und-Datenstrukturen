import time

"Coded by Nils"

def merge(lst: list[int], left: int, middle: int, right: int):
    """
    Merge lst[left:middle] and lst[middle:right], overwriting lst[left:right]
    with the result. Use the algorithm explained in Vorlesung 1.

    TIP: First copy the two parts from lst to two separate lists and then merge
    these copies and overwrite lst with the result. Merging "in-place" (without
    using separate lists for the input and the output) is very hard.

    >>> lst = [4, 3, 2, 1]
    >>> merge(lst, 0, 1, 2) # sublists: [4], [3], with [2, 1] remaining in lst
    >>> lst
    [3, 4, 2, 1]
    >>> merge(lst, 2, 3, 4) # sublists: [2], [1]
    >>> lst
    [3, 4, 1, 2]
    >>> merge(lst, 0, 2, 4) # sublists: [3, 4], [1, 2]
    >>> lst
    [1, 2, 3, 4]
    >>> lst = [4, 2, 3, 1]
    >>> merge(lst, 0, 1, 2) # sublists: [4], [2], with [3, 1] remaining in lst
    >>> lst
    [2, 4, 3, 1]
    >>> merge(lst, 2, 3, 4) # sublists: [3], [1]
    >>> lst
    [2, 4, 1, 3]
    >>> merge(lst, 0, 2, 4) # sublists: [2, 4], [1, 3]
    >>> lst
    [1, 2, 3, 4]
    """
    listA = lst[left:middle]
    listB = lst[middle:right]

    i = 0
    j = 0

    lenB = len(listB)
    lenA = len(listA)

    while i < lenA or j < lenB:
        if i < lenA:
            if j == lenB or listA[i] <= listB[j]:
                lst[left + j + i] = listA[i]
                i += 1
        if j < lenB:
            if i == lenA or listB[j] <= listA[i]:
                lst[left + j + i] = listB[j]
                j += 1


def merge_sort(lst: list[int]):
    """
    Sort the input list lst using the *iterative* MergeSort algorithm, as
    explained in Vorlesung 1.

    >>> lst = []
    >>> merge_sort(lst)
    >>> lst
    []

    >>> lst = [1]
    >>> merge_sort(lst)
    >>> lst
    [1]

    >>> lst = [1, 4, -3]
    >>> merge_sort(lst)
    >>> lst
    [-3, 1, 4]

    >>> lst = [1, 2, 3, 4]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> lst = [4, 3, 2, 1]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> lst = [1, 4, 2, 3]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> import random, copy
    >>> random.seed(42)
    >>> lst = [random.randint(-1000, 1000) for _ in range(0, 63)]
    >>> lst_copy = copy.deepcopy(lst)
    >>> merge_sort(lst)
    >>> sorted(lst_copy) == lst
    True

    """

    # man hat eine Liste die man erst mit left middle right durch geht welche eine 
    # sublistst in Größe 1 erdtellen

    n = len(lst)
    sizeOfSublist = 1

    while sizeOfSublist < n:
        for i in range(0, n, 2 * sizeOfSublist):
            middle = i + sizeOfSublist
            right = i + 2 * sizeOfSublist
            merge(lst, i, middle, right)
        sizeOfSublist *= 2


def merge_sort_blockoptimized(lst: list[int],  beg: int = 0, end: int = -1, B: int = 1):
    """
    Sort the input list lst using the *iterative* MergeSort algorithm, as
    explained in Vorlesung 1.

    >>> lst = []
    >>> merge_sort(lst)
    >>> lst
    []

    >>> lst = [1]
    >>> merge_sort(lst)
    >>> lst
    [1]

    >>> lst = [1, 4, -3]
    >>> merge_sort(lst)
    >>> lst
    [-3, 1, 4]

    >>> lst = [1, 2, 3, 4]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> lst = [4, 3, 2, 1]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> lst = [1, 4, 2, 3]
    >>> merge_sort(lst)
    >>> lst
    [1, 2, 3, 4]

    >>> import random, copy
    >>> random.seed(42)
    >>> lst = [random.randint(-1000, 1000) for _ in range(0, 63)]
    >>> lst_copy = copy.deepcopy(lst)
    >>> merge_sort(lst)
    >>> sorted(lst_copy) == lst
    True

    """

    # man hat eine Liste die man erst mit left middle right durch geht welche eine 
    # sublistst in Größe 1 erdtellen

    n = len(lst)
    if n < 2:
        return
    
    arraySize = B

    if B > 1:
        for i in range(0, n, B):
            merge_sort_blockoptimized(lst, i, min(i + B, n), 1)

    while array_size < n:
        # ... sort all non-overlapping subarrays with size array_size.
        for left in range(beg, end, 2 * array_size):
            # Calculate middle and right indices, make sure they are not out of
            # bounds and remember right sides are exclusive!
            middle = left + array_size
            right = min(left + 2 * array_size, end)

            # Merge the elemements from `left` to `right` and show only those.
            merge(lst, left, middle, right)
            print(
                " ".join(
                    [
                        f"{lst[i]:2}" if left <= i < right else "  "
                        for i in range(len(lst))
                    ]
                )
            )

        # Double size of the subarrays for the next iteration
        array_size *= 2
        print()


if __name__ == "__main__":

    # Laufzeit messen
    for n in range(500, 10001, 500):
        array = [n - k for k in range(n)]
        startTime = time.monotonic()
        merge_sort(array)
        endTime = time.monotonic()
        duration_ms = (endTime - startTime) * 1000
        print(f"{n}\t{duration_ms:.2f}", flush=True)

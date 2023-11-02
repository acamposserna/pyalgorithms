# -*- coding: utf-8 -*-
def bubble_sort(list):
    """
    Bubble sort, sometimes referred to as sinking sort, is a simple sorting
    algorithm that repeatedly steps through the list, compares adjacent
    elements and swaps them if they are in the wrong order. The pass through
    the list is repeated until the list is sorted. The algorithm, which is a
    comparison sort, is named for the way smaller or larger elements "bubble"
    to the top of the list.

    More info: https://en.wikipedia.org/wiki/Bubble_sort

    Args:
        list (list): numbers to be sorted.

    Returns:
        list: the same list sorted by ascending.

    Examples:
        >>> bubble_sort([3, 5, 1, 4, 2])
        >>> [1, 2, 3, 4, 5]
    """

    # If list is empty, return empty
    if (list == []):
        return []

    # Get number of items
    length = len(list)

    # Passed through the list is repeated until the list is sorted
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if (list[j] > list[j + 1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    return list

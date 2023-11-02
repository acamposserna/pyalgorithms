# -*- coding: utf-8 -*-
def merge_sort(list):
    """
    Merge sort is a sorting algorithm based on the divide-and-conquer paradigm
    that works as follows:
    1. Divide the unsorted list into n sublists, each containing one element.
    2. Repeatedly merge sublists to produce new sorted sublists until there
       is only one sublist remaining. This will be the sorted list.

    More info: https://en.wikipedia.org/wiki/Merge_sort

    Args:
        list (list): numbers to be sorted.

    Returns:
        list: the same list sorted by ascending.
    """
    if (len(list) < 2):
        return list

    index_mid = len(list) // 2

    return _merge(
        left=merge_sort(list[:index_mid]),
        right=merge_sort(list[index_mid:])
    )


def _merge(left, right):
    """
    Merge two sublists to produce new sorted sublist that is returned.

    Args:
        left (list): First sublist.
        right (list): Second sublist.

    Returns:
        list: combined list sorted by ascending.
    """
    if (left == []):
        return right

    if (right == []):
        return left

    sorted = []
    index_left = index_right = 0

    while len(sorted) < len(left) + len(right):
        if (left[index_left] <= right[index_right]):
            sorted.append(left[index_left])
            index_left += 1
        else:
            sorted.append(right[index_right])
            index_right += 1

        if (index_right == len(right)):
            sorted += left[index_left:]
            break

        if (index_left == len(left)):
            sorted += right[index_right:]
            break

    return sorted

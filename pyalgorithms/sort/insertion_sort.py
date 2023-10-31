# -*- coding: utf-8 -*-
def insertion_sort(list):
    """
    Insertion sort iterates, consuming one input element each repetition,
    and grows a sorted output list. At each iteration, insertion sort
    removes one element from the input data, finds the location it belongs
    within the sorted list, and inserts it there. It repeats until no input
    elements remain.

    More info: https://en.wikipedia.org/wiki/Insertion_sort

    Args:
        list (list): numbers to be sorted.

    Returns:
        list: the same list sorted by ascending.
    """
    # If list is empty, return empty
    if (list == []):
        return []
    
    # Get number of items
    length = len(list)

    # Run the elements of the list
    for i in range(1, length):
        # Get the current element
        item = list[i]

        # Run through the left portion of the list and find the correct
        # position of the item. Do this only if item is smaller than its
        # adjacent values.
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = item
    
    return list
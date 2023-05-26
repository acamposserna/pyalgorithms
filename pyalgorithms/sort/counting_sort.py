# -*- coding: utf-8 -*-
def countingSort(list):
    """
    In computer science, counting sort is an algorithm for sorting a collection
    of objects according to keys that are small integers; that is, it is an
    integer sorting algorithm. It operates by counting the number of objects
    that have each distinct key value, and using arithmetic on those counts to
    determine the positions of each key value in the output sequence. 
    
    More info: https://en.wikipedia.org/wiki/Counting_sort
    
    :param list: numbers to be sorted.
    :return: the same list sorted by ascending.
    
    Examples:
    >>> countingSort([3, 5, 1, 4, 2])
    >>> [1, 2, 3, 4, 5]
    """
    
    # If list is empty, return empty
    if (list == []):
        return []
    
    # Get data about the list
    length = len(list)
    maxVal = max(list)
    minVal = min(list)
    
    # Creates de counting array
    array_length = maxVal + 1 - minVal
    array = [0] * array_length
    
    # Counting the number of any value in the list
    for value in list:
        array[value - minVal] += 1
        
    # Sum each position with its predecessors.
    # This calculates how many elements <= i has in the array.
    for i in range(1, array_length):
        array[i] = array[i] + array[i - 1]
        
    # Creates output array
    sorted = [0] * length
    
    # Place the values to output array
    for i in reversed(range(0, length)):
        sorted[array[list[i] - minVal] - 1] = list[i]
        array[list[i] - minVal] -= 1
        
    return sorted
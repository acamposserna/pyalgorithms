# -*- coding: utf-8 -*-
def bubbleSort(list):
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through
    the list, compares adjacent elements and swaps them if they are in the
    wrong order. The pass through the list is repeated until the list is
    sorted. The algorithm, which is a comparison sort, is named for the way
    smaller or larger elements "bubble" to the top of the list.
    """
    for i in range(len(list)):
        j = len(list) - 1
        while (j >= i):
            if (list[j] < list[j-1]):
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
            j-=1
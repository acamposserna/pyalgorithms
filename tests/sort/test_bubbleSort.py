# -*- coding: utf-8 -*-
import unittest

from pyalgorithms.sort.bubble_sort import bubbleSort

class bubbleSortTest(unittest.TestCase):
    def test_bubbleSort(self):
        list = [3, 5, 1, 4, 2]
        bubbleSort(list)
        self.assertEqual(
            list,
            [1, 2, 3, 4, 5]
        )
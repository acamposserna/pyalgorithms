# -*- coding: utf-8 -*-
import unittest

from pyalgorithms.sort.insertion_sort import insertion_sort

class insertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        list = [3, 5, 1, 4, 2]
        sorted = insertion_sort(list)
        self.assertEqual(
            sorted,
            [1, 2, 3, 4, 5]
        )
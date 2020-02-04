# -*- coding: utf-8 -*-
import unittest

from pyalgorithms.sort.counting_sort import countingSort

class countingSortTest(unittest.TestCase):
    def test_countingSort(self):
        list = [3, 5, 1, 4, 2]
        sorted = countingSort(list)
        self.assertEqual(
            sorted,
            [1, 2, 3, 4, 5]
        )

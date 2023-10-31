# -*- coding: utf-8 -*-
import unittest

from pyalgorithms.sort.counting_sort import counting_sort

class countingSortTest(unittest.TestCase):
    def test_counting_sort(self):
        list = [3, 5, 1, 4, 2]
        sorted = counting_sort(list)
        self.assertEqual(
            sorted,
            [1, 2, 3, 4, 5]
        )

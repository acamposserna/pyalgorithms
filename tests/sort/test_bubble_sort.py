# -*- coding: utf-8 -*-
import unittest

from pyalgorithms.sort.bubble_sort import bubble_sort


class bubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        list = [3, 5, 1, 4, 2]
        sorted = bubble_sort(list)
        self.assertEqual(
            sorted,
            [1, 2, 3, 4, 5]
        )

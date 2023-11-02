# -*- coding: utf-8 -*-
import unittest

from pyalgorithms.sort.merge_sort import merge_sort


class mergeSortTest(unittest.TestCase):
    def test_merge_sort(self):
        list = [3, 5, 1, 4, 2]
        sorted = merge_sort(list)
        self.assertEqual(
            sorted,
            [1, 2, 3, 4, 5]
        )

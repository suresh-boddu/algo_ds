import unittest

from algo.sorting.mergesort import *
from algo.sorting.heapsort import *
from algo.sorting.quicksort import *


class TestSort(unittest.TestCase):

    def test_merge_sort(self):
        input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
        mergesort(input_arr, 0, len(input_arr) - 1)
        self.assertEqual(input_arr, [ -45, -10, -1, 0, 2, 4, 5, 8, 12, 32 ])

    def test_quick_sort(self):
        input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
        quicksort(input_arr, 0, len(input_arr) - 1)
        self.assertEqual(input_arr, [ -45, -10, -1, 0, 2, 4, 5, 8, 12, 32 ])

    def test_heap_sort(self):
        input_arr = [12, 4, 2, 8, -10, 5, 32, -1, 0, -45]
        heapsort(input_arr)
        self.assertEqual(input_arr, [ -45, -10, -1, 0, 2, 4, 5, 8, 12, 32 ])


if __name__ == '__main__':
    unittest.main()
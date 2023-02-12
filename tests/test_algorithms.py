"""
Module for algorithms.py tests.
"""
import unittest

import algorithms


class TestSortingAlgorithms(unittest.TestCase):
    """
    Tests for sorting algorithms in algorithms.py.
    """
    def test_quicksort(self):
        """
        Assert that quicksort function correctly sorts a list.
        """
        test_list = [10, 40, 30, 20, 60, 50]

        self.assertEqual(algorithms.quicksort(test_list, 0, len(test_list))[0],
                         sorted(test_list))

    def test_quicksort_empty_list(self):
        """
        Assert that quicksort function correctly sorts an empty list.
        """
        test_list = []

        self.assertEqual(algorithms.quicksort(test_list, 0, len(test_list))[0],
                         test_list)

    def test_merge_sort(self):
        """
        Assert that merge_sort function correctly sorts a list.
        """
        test_list = [10, 40, 30, 20, 60, 50]

        self.assertEqual(algorithms.merge_sort(test_list),
                         sorted(test_list))

    def test_merge_sort_empty_list(self):
        """
        Assert that merge_sort function correctly sorts an empty list.
        """
        test_list = []

        self.assertEqual(algorithms.merge_sort(test_list), test_list)


if __name__ == '__main__':
    unittest.main()

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

        self.assertEqual(algorithms.quicksort(test_list, 0, len(test_list) - 1)[0],
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


class TestSearchingAlgorithms(unittest.TestCase):
    """
    Tests for searching algorithms in algorithms.py.
    """

    def test_linear_search(self):
        """
        Assert that linear_search function finds a value within a list.
        """
        test_list = [10, 40, 30, 20, 60, 50]

        self.assertEqual(algorithms.linear_search(test_list, 30), 2)

    def test_linear_search_value_not_found(self):
        """
        Assert that linear_search function does not find value that is not in list.
        """
        test_list = [10, 40, 30, 20, 60, 50]

        self.assertEqual(algorithms.linear_search(test_list, 70), None)

    def test_linear_search_empty_list(self):
        """
        Assert that linear_search function does not find value in empty list.
        """
        test_list = []

        self.assertEqual(algorithms.linear_search(test_list, 30), None)

    def test_binary_search(self):
        """
        Assert that binary_search function finds a value within a list.
        """
        test_list = [10, 40, 30, 20, 60, 50]

        self.assertEqual(algorithms.binary_search(test_list, 30, algorithms.MERGE_SORT), 2)

    def test_binary_search_value_not_found(self):
        """
        Assert that binary_search function does not find value that is not in list.
        """
        test_list = [10, 40, 30, 20, 60, 50]

        self.assertEqual(algorithms.binary_search(test_list, 70, algorithms.MERGE_SORT), None)

    def test_binary_search_empty_list(self):
        """
        Assert that binary_search function does not find value in empty list.
        """
        test_list = []

        self.assertEqual(algorithms.binary_search(test_list, 30, algorithms.MERGE_SORT), None)


if __name__ == '__main__':
    unittest.main()

"""
Contains the searching and sorting algorithms used in the program.
"""
import math
import time

# Sorting types.
MERGE_SORT = 1
QUICKSORT = 2


def quicksort(data):
    """
    Demonstration of the quick sort algorithm

    :param data: the data to be sorted.
    :return: data and time in nanoseconds to perform the sort.
    """
    start_time = time.time_ns()

    run_time = time.time_ns() - start_time

    return data, run_time


def merge_sort(data):
    """
    Demonstration of the merge sort algorithm

    :param data: the data to be sorted.
    :return: data and time in nanoseconds to perform the sort.
    """
    start_time = time.time_ns()

    run_time = time.time_ns() - start_time

    return data, run_time


def linear_search(list_of_data, data):
    """
    Demonstration of linear search algorithm.

    :param list_of_data: to be searching.
    :param data: the data being searched for.
    :return: index of the data or None and time in nanoseconds to perform
    the search.
    """
    start_time = time.time_ns()

    for i in list_of_data:
        if list_of_data[i] is data:
            # Found, return its index and the run time.
            return i, time.time_ns() - start_time

    # Not found.
    return None, time.time_ns() - start_time


def binary_search(list_of_data, data, sort_type):
    """
    Demonstration of binary search algorithm.

    :param list_of_data: to be searching.
    :param data: the data being searched for.
    :param sort_type: the sort algorithm to be used.
    :return: index of the data or None and time in nanoseconds to perform
    the search.
    """
    start_time = time.time_ns()

    sorted_data = list_of_data

    # Check the type of sorting to use.
    if sort_type == MERGE_SORT:
        sorted_data = merge_sort(list_of_data)[0]

    if sort_type == QUICKSORT:
        sorted_data = quicksort(list_of_data)[0]

    # Get the indexes of the start, end, and middle of the list.
    start = 0
    end = sorted_data.len()
    middle = math.floor(sorted_data.len() / 2)

    while start != end:
        # Check the first value or character of data.
        if data[0] < sorted_data[middle][0]:
            # Data is within first half, if it exists in the list.
            end = middle
            middle = math.floor(end / 2)
        else:
            # Data is within second half, if it exists in the list.
            start = middle
            middle = math.floor((start + end) / 2)

    if sorted_data[start] is data:
        # Found, return the index and the run time.
        return start, time.time_ns() - start_time
    else:
        # Not found.
        return None, time.time_ns() - start_time

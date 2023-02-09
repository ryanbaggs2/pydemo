"""
Contains the searching and sorting algorithms used in the program.
"""
import math
import time

# Sorting types.
MERGE_SORT = 1
QUICKSORT = 2


def quicksort_and_runtime(data, start, end):
    """
    Demonstration of the quick sort algorithm with runtime.

    :param data: the data to be sorted.
    :param start: the start element of the data.
    :param end: the end element of the data.
    :return: data and time in nanoseconds to perform the sort.
    """
    start_time = time.time_ns()

    data = quicksort(data, start, end)

    run_time = time.time_ns() - start_time

    return data, run_time


def quicksort(data, start, end):
    """
    Demonstration of the quick sort algorithm, recursively called.

    :param data: the data or partition of data to be sorted.
    :param start: the start of the data or partition of data.
    :param end: the end of the data or partition of data.
    :return: data, start element, and end element.
    """
    # Recursively go until smallest partitions achieved.
    if start < end:
        # Get the previous pivot index and the updated data.
        pivot_index, data = move_elem_across_pivot(data, start, end)

        # Partition the data, continue quicksort.
        quicksort(data, start, pivot_index)
        quicksort(data, pivot_index + 1, end)

    return data, start, end


def move_elem_across_pivot(data, start, end):
    """
    Moves elements across a pivot value. Lower value elements moved to
    positions in front of pivot and higher value elements moved to
    positions behind pivot.

    :param data: to move elements within.
    :param start: of the partition of data.
    :param end: of the partition of data.
    :return: the pivot index and the updated data.
    """
    # Get the pivot value.
    pivot = data[start]

    i = start + 1
    j = end

    # Loop until in pivot location.
    while i < j:
        # Loop until value that should be swapped across pivot found.
        while data[i] <= pivot:
            i += 1

        # Loop until value that should be swapped across pivot found.
        while data[j] > pivot:
            j -= 1

        # Check that not in pivot location.
        if i < j:
            data = swap_values(data, i, j)

    # Move the pivot into its correct position.
    swap_values(data, start, j)

    return j, data


def swap_values(data, i, j):
    """
    Swaps two values in a list.

    :param data: list that has elements to be swapped.
    :param i: index of first element to be swapped.
    :param j: index of second element to be swapped.
    :return: the list with the elements swapped with each other.
    """
    # Create a temporary variable.
    temp = data[i]

    # Swap the values between each other.
    data[i] = data[j]
    data[j] = temp

    # Return the updated list.
    return data


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
        sorted_data = quicksort(list_of_data, 0, list_of_data.len())[0]

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

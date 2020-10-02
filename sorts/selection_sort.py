"""
https://en.wikipedia.org/wiki/Selection_sort
"""


def selection_sort(array):
    """
    Selection sort algorithm.
    :param array: the array to be sorted.
    :return: sorted array
    >>> import random
    >>> array = random.sample(range(-50, 50), 100)
    >>> selection_sort(array) == sorted(array)
    True
    """
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == '__main__':
    from doctest import testmod

    testmod()

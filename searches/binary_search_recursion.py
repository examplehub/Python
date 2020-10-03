"""
https://en.wikipedia.org/wiki/Binary_search_algorithm
"""


def binary_search(array, key) -> int:
    """
    Binary search algorithm.
    :param array: the sorted array to be searched.
    :param key: the key value to be searched.
    :return: index of key value if found, otherwise -1.

    >>> array = list(range(10))
    >>> for index, item in enumerate(array):
    ...     assert index == binary_search(array, item)
    >>> binary_search(array, 10) == -1
    True
    >>> binary_search(array, -1) == -1
    True
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) >> 1
        if key == array[mid]:
            return mid
        elif key > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    from doctest import testmod

    testmod()

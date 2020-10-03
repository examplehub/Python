"""
https://en.wikipedia.org/wiki/Binary_search_algorithm
"""


def binary_search_recursion(array, key, left: int = 0, right: int = None) -> int:
    """
    Binary search algorithm using recursion.
    :param array: the sorted array to be searched.
    :param key: the key value to be searched.
    :param left: the left index of sub array.
    :param right: the right index of sub array.
    :return: index of key value if found, otherwise -1.

    >>> array = list(range(10))
    >>> for index, item in enumerate(array):
    ...     assert index == binary_search_recursion(array, item)
    >>> binary_search_recursion(array, 10) == -1
    True
    >>> binary_search_recursion(array, -1) == -1
    True
    """
    if right is None:
        right = len(array) - 1
    if left > right:
        return -1
    mid = (left + right) >> 1
    if key == array[mid]:
        return mid
    elif key > array[mid]:
        return binary_search_recursion(array, key, mid + 1, right)
    else:
        return binary_search_recursion(array, key, left, mid - 1)


if __name__ == '__main__':
    from doctest import testmod

    testmod()

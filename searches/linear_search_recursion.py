"""
https://en.wikipedia.org/wiki/Linear_search
"""


def linear_search_recursion(array, key, length: int = None, ) -> int:
    """
    Linear search algorithm using recursion.
    :param array: the array to be searched.
    :param length: the length of sub array.
    :param key: the key value to be searched.
    :return: index of key value if found, otherwise -1.

    >>> array = list(range(0, 10))
    >>> for index, key in enumerate(range(0, 10)):
    ...     assert index == linear_search_recursion(array, key)
    >>> linear_search_recursion(array, 10) == -1
    True
    >>> linear_search_recursion(array, -1) == -1
    True
    """
    if length is None:
        length = len(array)
    if length == 0:
        return -1
    elif array[length - 1] == key:
        return length - 1
    else:
        return linear_search_recursion(array, key, length - 1)


if __name__ == '__main__':
    from doctest import testmod

    testmod()

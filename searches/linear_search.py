"""
https://en.wikipedia.org/wiki/Linear_search
"""


def linear_search(array, key) -> int:
    """
    Linear search algorithm.
    :param array: the array to be searched.
    :param key: the key value to be searched.
    :return: index of key value if found, otherwise -1.

    >>> array = list(range(0, 10))
    >>> for index, key in enumerate(range(0, 10)):
    ...     assert index == linear_search(array, key)
    >>> linear_search(array, 10) == -1
    True
    >>> linear_search(array, -1) == -1
    True
    """
    for index, value in enumerate(array):
        if value == key:
            return index
    return -1


if __name__ == "__main__":
    from doctest import testmod

    testmod()

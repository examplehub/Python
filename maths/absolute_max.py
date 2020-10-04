def absolute_max(array):
    """
    Returns absolute max value of a array.
    :param array: the array.
    :return: absolute max value

    >>> absolute_max([1, -2, 5, -8, 7])
    -8
    >>> absolute_max([1, -2, 3, -4, 5])
    5
    """
    return max(array, key=abs)


if __name__ == '__main__':
    from doctest import testmod

    testmod()

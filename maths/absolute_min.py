def absolute_min(array):
    """
    Returns absolute min value of a array.
    :param array: the array.
    :return: absolute min value

    >>> absolute_min([1, -2, 5, -8, 7])
    1
    >>> absolute_min([1, -2, 3, -4, 5])
    1
    """
    return min(array, key=abs)


if __name__ == '__main__':
    from doctest import testmod

    testmod()

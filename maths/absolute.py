"""
https://en.wikipedia.org/wiki/Absolute_value
"""


def absolute(number):
    """ Return the absolute value of the argument.
    >>> absolute(-3.14) == abs(-3.14) and absolute(3.14) == abs(3.14)
    True
    >>> absolute(0) == abs(0)
    True
    >>> absolute(50) == abs(50)
    True
    >>> import random
    >>> all(absolute(number) == abs(number) for number in random.sample(range(-50, 50), 100))
    True
    """
    return -number if number < 0 else number


if __name__ == '__main__':
    from doctest import testmod

    testmod()

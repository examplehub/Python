"""
https://en.wikipedia.org/wiki/Average
"""


def average(numbers):
    """
    Calculate average of a list numbers.
    :param numbers: the number to be calculated.
    :return: average of a list number.

    >>> average([1, 2, 2, 3, 4, 7, 9])
    4.0
    >>> average(range(1, 11))
    5.5
    >>> average(range(1, 101))
    50.5
    """
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

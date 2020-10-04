"""
https://en.wikipedia.org/wiki/Median
"""


def median(numbers):
    """
    Calculate median of a list numbers.
    :param numbers: the numbers to be calculated.
    :return: median value of numbers.

    >>> median([1, 3, 3, 6, 7, 8, 9])
    6
    >>> median([1, 2, 3, 4, 5, 6, 8, 9])
    4.5
    >>> import statistics
    >>> import random
    >>> numbers = random.sample(range(-50, 50), k=100)
    >>> statistics.median(numbers) == median(numbers)
    True
    """
    numbers = sorted(numbers)
    mid_index = len(numbers) // 2
    return (
        (numbers[mid_index] + numbers[mid_index - 1]) / 2
        if mid_index % 2 == 0
        else numbers[mid_index]
    )


if __name__ == "__main__":
    from doctest import testmod

    testmod()

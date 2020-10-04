"""
https://en.wikipedia.org/wiki/Mode_(statistics)
"""


def mode(numbers):
    """
    Calculate mode of a list numbers.
    :param numbers: the numbers
    :return: mode number of the numbers.

    >>> import statistics
    >>> mode([1, 2, 2, 3, 4, 7, 9]) == statistics.mode([1, 2, 2, 3, 4, 7, 9])
    True
    >>> import random
    >>> numbers = random.sample(range(-50, 50), 100)
    >>> mode(numbers) == statistics.mode(numbers)
    True
    """
    max_count = 1
    mode_number = numbers[0]

    for number in numbers:
        count = 0
        for temp in numbers:
            if temp == number:
                count += 1
        if count > max_count:
            max_count = count
            mode_number = number

    return mode_number


if __name__ == "__main__":
    from doctest import testmod

    testmod()

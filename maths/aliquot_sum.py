"""
https://en.wikipedia.org/wiki/Aliquot_sum
"""


def aliquot_sum(number: int) -> int:
    """
    Calculate aliquot sum of a number.
    :param number: the number.
    :return: aliquot sum of given number.
    >>> aliquot_sum(1)
    0
    >>> aliquot_sum(2)
    1
    >>> aliquot_sum(3)
    1
    >>> aliquot_sum(15)
    9
    >>> aliquot_sum(21)
    11
    >>> aliquot_sum(0)
    Traceback (most recent call last):
    ...
    ValueError: number must be positive
    >>> aliquot_sum(-10)
    Traceback (most recent call last):
    ...
    ValueError: number must be positive
    >>> aliquot_sum(10.50)
    Traceback (most recent call last):
    ...
    ValueError: number must be positive
    """
    if number <= 0 or not isinstance(number, int):
        raise ValueError("number must be positive")
    return sum(divisor for divisor in range(1, number // 2 + 1) if number % divisor == 0)


if __name__ == '__main__':
    from doctest import testmod

    testmod()
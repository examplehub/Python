def is_odd(number: int) -> bool:
    """
    Test if a number is a odd number.
    :param number: the number to be checked.
    :return: True if the number is odd, otherwise False.

    >>> is_odd(-1)
    True
    >>> is_odd(-2)
    False
    >>> is_odd(0)
    False
    >>> is_odd(3)
    True
    >>> is_odd(4)
    False
    >>> all([is_odd(i) for i in range(1, 100, 2)])
    True
    """
    return number % 2 != 0


def is_odd_faster(number: int) -> bool:
    """
    Test if a number is a odd number using bit operator.
    :param number: the number to be checked.
    :return: True if the number is odd, otherwise False.

    >>> is_odd_faster(-1)
    True
    >>> is_odd_faster(-2)
    False
    >>> is_odd_faster(0)
    False
    >>> is_odd_faster(3)
    True
    >>> is_odd_faster(4)
    False
    >>> all([is_odd_faster(i) for i in range(1, 100, 2)])
    True
    """
    return number & 1 != 0


if __name__ == "__main__":
    from doctest import testmod

    testmod()

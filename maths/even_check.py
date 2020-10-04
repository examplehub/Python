def is_even(number: int) -> bool:
    """
    Test if a number is a even number.
    :param number: the number to be checked.
    :return: True if the number is even, otherwise False.

    >>> is_even(-1)
    False
    >>> is_even(-2)
    True
    >>> is_even(0)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    >>> all([is_even(i) for i in range(0, 100, 2)])
    True
    """
    return number % 2 == 0


def is_even_faster(number: int) -> bool:
    """
    Test if a number is a even number using bit operator.
    :param number: the number to be checked.
    :return: True if the number is even, otherwise False.

    >>> is_even_faster(-1)
    False
    >>> is_even_faster(-2)
    True
    >>> is_even_faster(0)
    True
    >>> is_even_faster(3)
    False
    >>> is_even_faster(4)
    True
    >>> all([is_even_faster(i) for i in range(0, 100, 2)])
    True
    """
    return number & 1 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod()

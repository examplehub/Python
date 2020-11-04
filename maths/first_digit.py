def first_digit(number: int) -> int:
    """
    >>> first_digit(-123)
    1
    >>> first_digit(0)
    0
    >>> first_digit(123)
    1
    >>> first_digit(123456789)
    1
    """
    number = abs(number)
    while number >= 10:
        number //= 10
    return number


if __name__ == "__main__":
    from doctest import testmod

    testmod()

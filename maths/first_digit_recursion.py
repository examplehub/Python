def first_digit_recursion(number: int) -> int:
    """
    >>> first_digit_recursion(-123)
    1
    >>> first_digit_recursion(0)
    0
    >>> first_digit_recursion(123)
    1
    >>> first_digit_recursion(123456789)
    1
    """
    number = abs(number)
    return number if number < 10 else first_digit_recursion(number // 10)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

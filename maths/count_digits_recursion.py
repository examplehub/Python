def count_digits_recursion(number: int) -> int:
    """
    >>> count_digits_recursion(-123)
    3
    >>> count_digits_recursion(-1)
    1
    >>> count_digits_recursion(0)
    1
    >>> count_digits_recursion(123)
    3
    >>> count_digits_recursion(123456)
    6
    """
    number = abs(number)
    return 1 if number < 10 else 1 + count_digits_recursion(number // 10)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

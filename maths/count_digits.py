def count_digits(number: int) -> int:
    """
    >>> count_digits(-123)
    3
    >>> count_digits(-1)
    1
    >>> count_digits(0)
    1
    >>> count_digits(123)
    3
    >>> count_digits(123456)
    6
    """
    number = abs(number)
    count = 0
    while True:
        number = number // 10
        count = count + 1
        if number == 0:
            break
    return count


if __name__ == "__main__":
    from doctest import testmod

    testmod()

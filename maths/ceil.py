def ceil(number) -> int:
    """
    >>> import math
    >>> numbers = [-3.14, 3.14, -3, 3, 0, 0.0, -0.0, -1234.567, 1234.567]
    >>> all(math.ceil(num) == ceil(num) for num in numbers)
    True
    """
    return int(number) if number - int(number) <= 0 else int(number) + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()

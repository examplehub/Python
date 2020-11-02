def to_integer(number_str: str) -> int:
    """
    >>> to_integer("123")
    123
    >>> to_integer("3.14")
    3
    >>> to_integer("-123")
    -123
    >>> to_integer("-3.14")
    -3
    >>> to_integer("123a")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: '123a'
    """
    return int(float(number_str))


if __name__ == "__main__":
    from doctest import testmod

    testmod()

def subtract(first_number, second_number):
    """
    >>> subtract(1.1, 1.1)
    0.0
    >>> subtract(10, 5)
    5
    >>> subtract(3.14159, 3)
    0.14158999999999988
    """
    return first_number - second_number


if __name__ == "__main__":
    from doctest import testmod

    testmod()

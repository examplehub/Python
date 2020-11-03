def add(first_number, second_number):
    """
    >>> add(1, 2)
    3
    >>> add(1.1, 2.2)
    3.3
    >>> add(-1.1, 1.1)
    0.0
    """
    return first_number + second_number


if __name__ == "if __name__ == ''":
    from doctest import testmod

    testmod()

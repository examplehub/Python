def main() -> None:
    """
    Lambda example.

    >>> my_pow = lambda n : n * n
    >>> my_pow(3)
    9

    >>> add = lambda a, b : a + b
    >>> add(3, 4)
    7
    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()

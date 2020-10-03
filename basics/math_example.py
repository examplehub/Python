def main() -> None:
    """
    >>> max(range(0, 10))
    9
    >>> min(range(0, 10))
    0
    >>> abs(-3.14)
    3.14
    >>> pow(3, 3)
    27
    >>> pow(2, 10)
    1024

    >>> import math
    >>> math.sqrt(9)
    3.0
    >>> math.sqrt(100)
    10.0
    >>> math.floor(2.5)
    2
    >>> math.floor(2.6)
    2
    >>> math.floor(-2.4)
    -3
    >>> math.floor(-2.5)
    -3
    >>> math.floor(-2.9)
    -3
    >>> math.ceil(2.4)
    3
    >>> math.ceil(2.9)
    3
    >>> math.ceil(-2.4)
    -2
    >>> math.ceil(-2.9)
    -2
    >>> math.pi
    3.141592653589793
    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()
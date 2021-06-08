def fibonacci(number: int) -> int:
    """
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(8)
    21
    """
    first_item = 0
    second_item = 1
    for i in range(0, number):
        temp = first_item + second_item
        first_item = second_item
        second_item = temp
    return first_item


if __name__ == "__main__":
    from doctest import testmod

    testmod()

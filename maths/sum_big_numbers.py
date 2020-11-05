def sum_big_numbers(first_number: int, second_number: int):
    """
    >>> sum_big_numbers(1234567891011121314151617181920, 2019181716151413121110987654321)
    3253749607162534435262604836241
    """
    return first_number + second_number


if __name__ == "__main__":
    from doctest import testmod

    testmod()

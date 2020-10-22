"""
https://en.wikipedia.org/wiki/Leap_year
"""


def is_leap_year(year: int) -> bool:
    """
    >>> all(is_leap_year(year) for year in [1600, 2000, 24000])
    True
    >>> all(is_leap_year(year) for year in [1999, 2001, 2002])
    False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod()

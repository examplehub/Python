def main() -> None:
    """
    >>> import datetime
    >>> year = datetime.datetime.now().year
    >>> year >= 2020
    True

    >>> time = datetime.datetime(2100, 10, 5)
    >>> str(time)
    '2100-10-05 00:00:00'
    """
    pass


if __name__ == "__main__":
    from doctest import testmod

    testmod()

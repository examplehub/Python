def main():
    """
    While example.

    >>> i = 1
    >>> while i <= 5:
    ...     print(i, end='')
    ...     i += 1
    12345

    >>> i = 5
    >>> while i >= 1:
    ...     print(i, end='')
    ...     i -= 1
    54321
    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()

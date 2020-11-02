def contains(main_str: str, sub_str: str) -> bool:
    """
    >>> "a" in "abc"
    True
    >>> "bc" in "abc"
    True
    >>> "ac" in "abc"
    False
    >>> "" in "abc"
    True
    >>> "" in ""
    True
    """
    return sub_str in main_str


if __name__ == '__main__':
    from doctest import testmod

    testmod()

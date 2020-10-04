def main() -> None:
    """
    >>> import re
    >>> text = "ExampleHub - Python"
    >>> print(re.findall("[A-Z]", text))
    ['E', 'H', 'P']

    >>> text = "a1b2c3"
    >>> re.findall("\\d", text)
    ['1', '2', '3']

    >>> text = "abc123abd"
    >>> re.findall("a.d", text)
    ['abd']

    >>> text = "abcABabc123abd123"
    >>> re.findall("^abc", text)
    ['abc']

    >>> text = "ExampleHub"
    >>> re.search("Hub$", text) is not None
    True

    >>> text = "ExampleHub Python"
    >>> re.search("Pp*", text) is not None
    True
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()

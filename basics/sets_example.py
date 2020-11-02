def main() -> None:
    """
    >>> languages = {"Python", "Java", "C", "JavaScript", "Python", "C"}
    >>> len(languages)
    4
    >>> "Java" in languages
    True
    >>> "Python" in languages
    True
    >>> "c" in languages
    False
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()

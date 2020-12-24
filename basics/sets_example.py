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
    >>> my_langs = {"Python", "Golang", "C"}
    >>> sorted(list(my_langs & languages))
    ['C', 'Python']
    >>> sorted(list(my_langs | languages))
    ['C', 'Golang', 'Java', 'JavaScript', 'Python']
    >>> sorted(list(my_langs ^ languages))
    ['Golang', 'Java', 'JavaScript']
    >>> sorted(list(my_langs - languages))
    ['Golang']
    >>> sorted(list(languages - my_langs))
    ['Java', 'JavaScript']
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()

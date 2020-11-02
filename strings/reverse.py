def reverse(original: str) -> str:
    """
    >>> reverse("abc")
    'cba'
    >>> reverse('1234')
    '4321'
    >>> reverse("cba321")
    '123abc'
    >>> reverse("")
    ''
    """
    return original[::-1]


def reverse2(original: str) -> str:
    """
    >>> reverse2("abc")
    'cba'
    >>> reverse2('1234')
    '4321'
    >>> reverse2("cba321")
    '123abc'
    >>> reverse2("")
    ''
    """
    original = list(original)
    i, j = 0, len(original) - 1
    while i < j:
        original[i], original[j] = (
            original[j],
            original[i],
        )
        i += 1
        j -= 1
    return "".join(original)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

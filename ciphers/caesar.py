"""
https://en.wikipedia.org/wiki/Caesar_cipher
"""


def encrypt(original: str, steps: int = 3) -> str:
    """
    >>> encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    'DEFGHIJKLMNOPQRSTUVWXYZABC'
    >>> encrypt("abcdefghijklmnopqrstuvwxyz")
    'defghijklmnopqrstuvwxyzabc'
    """
    original = list(original)
    for i in range(0, len(original)):
        if original[i].isupper():
            original[i] = chr(65 + (ord(original[i]) - 65 + steps) % 26)
        elif original[i].islower():
            original[i] = chr(97 + (ord(original[i]) - 97 + steps) % 26)
    return "".join(original)


def decrypt(password: str, steps: int = 3) -> str:
    """
    >>> decrypt("DEFGHIJKLMNOPQRSTUVWXYZABC")
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> decrypt(("defghijklmnopqrstuvwxyzabc"))
    'abcdefghijklmnopqrstuvwxyz'
    """
    password = list(password)
    for i in range(0, len(password)):
        if password[i].isupper():
            password[i] = chr(65 + (ord(password[i]) - 65 - steps + 26) % 26)
        elif password[i].islower():
            password[i] = chr(97 + (ord(password[i]) - 97 - steps + 26) % 26)
    return "".join(password)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

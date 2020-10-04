"""
https://en.wikipedia.org/wiki/Palindrome
"""


def is_palindrome(s: str) -> bool:
    """
    Test if a string is palindrome string.
    :param s: the string to be check.
    :return: True if the string is palindrome, otherwise False.
    >>> is_palindrome("Able was I ere I saw Elba")
    True
    >>> is_palindrome("A man, a plan, a canal – Panama")
    True
    >>> is_palindrome("Madam, I'm Adam")
    True
    >>> is_palindrome("Never odd or even")
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome("      ")
    True
    """
    s = "".join(char for char in s.lower() if s.isalnum())
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def is_palindrome_reverse(s: str) -> bool:
    """
    Test if a string is palindrome string by reversing string.
    :param s: the string to be checked
    :return: True if the string is palindrome, otherwise False.
    >>> is_palindrome_reverse("Able was I ere I saw Elba")
    True
    >>> is_palindrome_reverse("A man, a plan, a canal – Panama")
    True
    >>> is_palindrome_reverse("Madam, I'm Adam")
    True
    >>> is_palindrome_reverse("Never odd or even")
    True
    >>> is_palindrome_reverse("")
    True
    >>> is_palindrome_reverse("      ")
    True
    """
    s = "".join(char for char in s.lower() if s.isalnum())
    return s == s[::-1]


def is_palindrome_reversion(s: str) -> bool:
    """
    Test if a string is palindrome string by reversion.
    :param s: the string to be checked
    :return: True if the string is palindrome, otherwise False.
    >>> is_palindrome_reversion("Able was I ere I saw Elba")
    True
    >>> is_palindrome_reversion("A man, a plan, a canal – Panama")
    True
    >>> is_palindrome_reversion("Madam, I'm Adam")
    True
    >>> is_palindrome_reversion("Never odd or even")
    True
    >>> is_palindrome_reversion("12345")
    False
    >>> is_palindrome_reverse("")
    True
    >>> is_palindrome_reverse("      ")
    True
    """
    s = "".join(char for char in s.lower() if s.isalnum())
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return is_palindrome_reversion(s[1 : len(s) - 1])


if __name__ == "__main__":
    from doctest import testmod

    testmod()

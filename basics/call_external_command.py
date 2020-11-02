def main() -> None:
    """
    >>> import subprocess
    >>> _ = subprocess.run(["ls", "-l"])
    """


if __name__ == "__main__":
    from doctest import testmod

    testmod()

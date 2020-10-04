def open_file(filename: str):
    """
    >>> open_file("hello.txt")
    No such file or directory: hello.txt

    >>> import os
    >>> if os.path.exists("../LICENSE"):
    ...     f = open_file("../LICENSE")
    ...     f is not None
    ...     f.readline().strip() == "Apache License"
    ...     f.readline().strip() == "Version 2.0, January 2004"
    ...     f.close()
    ...     f.closed
    ...     with open("../LICENSE") as f:
    ...         f.readline().strip() == "Apache License"
    ...         f.readline().strip() == "Version 2.0, January 2004"
    True
    True
    True
    True
    True
    True
    """
    try:
        f = open(filename)
        return f
    except FileNotFoundError:
        print(f"No such file or directory: {filename}")


def writefile_append() -> None:
    """
    >>> f = open("temp_file1.txt", "a")
    >>> f is not None
    True
    >>> f.writelines("ExampleHub\\n")
    >>> f.writelines("Python\\n")
    >>> f.close()
    >>> f.closed
    True
    >>>
    """
    pass


def writefile_override() -> None:
    """
    >>> f = open("temp_file2.txt", "w")
    >>> f is not None
    True
    >>> f.writelines("ExampleHub\\n")
    >>> f.writelines("Python\\n")
    >>> f.close()
    >>> f.closed
    True
    """
    pass


def delete_file() -> None:
    """
    >>> import os
    >>> os.path.exists("hello.txt") == False
    True

    >>> if os.path.exists("example_file.txt"):
    ...     os.remove("example_file.txt")

    >>> if os.path.exists("folder_path"):
    ...     os.rmdir("folder_path")
    """
    pass


if __name__ == "__main__":
    from doctest import testmod

    testmod()

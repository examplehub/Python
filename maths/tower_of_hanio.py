"""
https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""


def move(number_of_tower: int, a_place: str, b_place: str, c_place: str) -> None:
    """
    >>> move(0, "A", "B", "C")
    >>> move(1, "A", "B", "C")
    move from A to B
    >>> move(2, "A", "B", "C")
    move from A to C
    move from A to B
    move from C to B
    >>> move(3, "A", "B", "C")
    move from A to B
    move from A to C
    move from B to C
    move from A to B
    move from C to A
    move from C to B
    move from A to B
    >>> move(4, "A", "B", "C")
    move from A to C
    move from A to B
    move from C to B
    move from A to C
    move from B to A
    move from B to C
    move from A to C
    move from A to B
    move from C to B
    move from C to A
    move from B to A
    move from C to B
    move from A to C
    move from A to B
    move from C to B
    """
    if number_of_tower != 0:
        move(number_of_tower - 1, a_place, c_place, b_place)
        print(f"move from {a_place} to {b_place}")
        move(number_of_tower - 1, c_place, b_place, a_place)


if __name__ == "__main__":
    from doctest import testmod

    testmod()

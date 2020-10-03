def main() -> None:
    """
    >>> import json
    >>> json_data = '{ "name":"Jack", "age":23}'
    >>> data = json.loads(json_data)
    >>> data["name"]
    'Jack'
    >>> data["age"]
    23

    >>> student = {"name": "Jack", "age":23, "id": "2020101039"}
    >>> data = json.dumps(student)
    >>> data
    '{"name": "Jack", "age": 23, "id": "2020101039"}'
    """


if __name__ == '__main__':
    from doctest import testmod

    testmod()

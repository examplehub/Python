def allocation(number_of_bytes: int, partitions: int):
    """
    Allocation number of bytes to multi partitions.
    :param number_of_bytes: number of bytes.
    :param partitions: the count of partition.
    :return: allocated partitions.

    >>> allocation(16647, 4)
    ['1-4161', '4162-8322', '8323-12483', '12484-16647']
    >>> allocation(100000, 6)
    ['1-16666', '16667-33332', '33333-49998', '49999-66664', '66665-83330', '83331-100000']
    >>> allocation(1000, 10005)
    Traceback (most recent call last):
    ...
    ValueError: partitions can't be greater or equal to number_of_bytes
    >>> allocation(1000, -1)
    Traceback (most recent call last):
    ValueError: partitions must be positive number
    """
    if partitions <= 0:
        raise ValueError("partitions must be positive number")
    if partitions >= number_of_bytes:
        raise ValueError(
            "partitions can't be greater or equal to number_of_bytes"
        )
    allocations = []
    bytes_per_partition = number_of_bytes // partitions
    for i in range(partitions):
        start_bytes = i * bytes_per_partition + 1
        end_bytes = number_of_bytes if i == partitions - 1 else (i + 1) * bytes_per_partition
        allocations.append(f"{start_bytes}-{end_bytes}")
    return allocations


if __name__ == "__main__":
    from doctest import testmod

    testmod()

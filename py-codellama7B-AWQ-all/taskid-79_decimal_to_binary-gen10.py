def decimal_to_binary(decimal: int) -> str:
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    """

    # convert the decimal to a binary integer
    binary = bin(decimal)[2:]

    # create a list of the binary string
    binary_list = list(binary)

    # add the 'db' characters to the beginning and end of the list
    binary_list.insert(0, 'd')
    binary_list.insert(0, 'b')
    binary_list.append('d')
    binary_list.append('b')

    # convert the list back to a string
    binary = ''.join(binary_list)

    return binary

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # This line creates a dictionary, where each key is a number
    # and each value is the number's corresponding string.
    numbers_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    # This line creates a list of tuples from the numbers_dict dictionary.
    # The list is created by getting each key-value pair from the dictionary.
    # Each tuple has the form (key, value).
    numbers_list = [(key, value) for key, value in numbers_dict.items()]

    # This line creates a list of integers from the string argument.
    # The integers are created by getting the first character of each string in the list of tuples.
    # The integers are converted to strings and then converted to integers using the int() function.
    numbers = [int(str(int(x[0]))[0]) for x in numbers_list]

    # This line sorts the list of integers.
    sorted_numbers = sorted(numbers)

    # This line creates a string with the sorted numbers separated by spaces.
    # The string is created by getting each integer from the sorted_numbers list
    # and then getting the corresponding value from the numbers_dict dictionary.
    sorted_string = ' '.join([numbers_dict[x] for x in sorted_numbers])

    return sorted_string

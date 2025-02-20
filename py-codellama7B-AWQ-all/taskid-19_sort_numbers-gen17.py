def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """


    # Convert input string to a list of numberals.
    numbers = numbers.split()

    # Convert numberals to integer values.
    numbers = [int(number) for number in numbers]

    # Sort list of numberals.
    numbers.sort()

    # Convert list of numberals back to a string.
    numbers = ' '.join([str(number) for number in numbers])

    return numbers

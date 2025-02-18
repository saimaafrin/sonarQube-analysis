def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # convert numbers to ints
    numbers = [int(x) for x in numbers.split()]
    # sort the numbers
    numbers.sort()
    # convert back to string
    return ' '.join(map(str, numbers))

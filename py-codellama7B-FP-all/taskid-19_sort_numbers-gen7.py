def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Initialize empty list
    list_numbers = []
    # Fill list with numbers from 'one' to 'nine'
    for i in range(1, 10):
        list_numbers.append(str(i))
    # Remove numbers from input
    for num in numbers.split():
        if num in list_numbers:
            list_numbers.remove(num)
    # Sort list
    list_numbers.sort()
    # Return sorted list
    return ' '.join(list_numbers)

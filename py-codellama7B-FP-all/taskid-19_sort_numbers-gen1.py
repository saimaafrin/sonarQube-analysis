def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Step 1: Convert numbers to a list
    numbers = numbers.split(' ')

    # Step 2: Sort numbers
    numbers.sort()

    # Step 3: Return sorted numbers
    return ' '.join(numbers)

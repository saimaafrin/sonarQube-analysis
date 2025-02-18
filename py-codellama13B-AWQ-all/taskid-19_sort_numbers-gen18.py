def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers = numbers.split(' ')
    sorted_numbers = sorted(numbers, key=lambda x: int(x.replace('o', '0').replace('e', '0')))
    return ' '.join(sorted_numbers)

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # split the string into a list of individual words
    words = numbers.split()
    # sort the list of words, case insensitively
    words.sort(key=lambda x: x.lower(), reverse=False)
    # join the sorted words back into a string
    return " ".join(words)

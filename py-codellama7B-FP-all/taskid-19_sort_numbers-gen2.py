def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """


    # list of words
    lst = numbers.split(" ")

    # sort list of words
    lst = sorted(lst)

    # return list of words as string with space delimiters
    return " ".join(lst)

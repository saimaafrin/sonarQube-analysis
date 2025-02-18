def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    num_dict = {}
    for i in numbers:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    for i in num_dict:
        print(i)
    return ""

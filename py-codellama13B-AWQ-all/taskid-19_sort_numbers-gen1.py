def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """


    # 1. Get numbers from input
    numbers = numbers.split(' ')

    # 2. Convert input strings to ints and sort them
    numbers = [int(i) for i in numbers]
    numbers.sort()

    # 3. Convert numbers to string
    numbers = [str(i) for i in numbers]

    # 4. Return sorted numbers
    return ' '.join(numbers)

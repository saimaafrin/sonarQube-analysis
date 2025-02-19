def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    output = ''
    number_list = []
    numbers_list = numbers.split()
    for number in numbers_list:
        if number == 'zero':
            number_list.append(0)
        elif number == 'one':
            number_list.append(1)
        elif number == 'two':
            number_list.append(2)
        elif number == 'three':
            number_list.append(3)
        elif number == 'four':
            number_list.append(4)
        elif number == 'five':
            number_list.append(5)
        elif number == 'six':
            number_list.append(6)
        elif number == 'seven':
            number_list.append(7)
        elif number == 'eight':
            number_list.append(8)
        elif number == 'nine':
            number_list.append(9)
    number_list.sort()
    for number in number_list:
        if number == 0:
            output += 'zero '
        elif number == 1:
            output += 'one '
        elif number == 2:
            output += 'two '
        elif number == 3:
            output += 'three '
        elif number == 4:
            output += 'four '
        elif number == 5:
            output += 'five '
        elif number == 6:
            output += 'six '
        elif number == 7:
            output += 'seven '
        elif number == 8:
            output += 'eight '
        elif number == 9:
            output += 'nine '
    return output.strip()

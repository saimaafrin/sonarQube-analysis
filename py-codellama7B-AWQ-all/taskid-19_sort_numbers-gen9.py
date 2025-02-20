def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split string by whitespace
    numbers_list = numbers.split(" ")
    # Create an empty list to store the final output
    final_list = []
    # For each string in numbers_list
    for number in numbers_list:
        # Convert string to number
        number = int(number)
        # If number is less than the smallest number in final_list, add to final_list
        if len(final_list) == 0:
            final_list.append(number)
        else:
            if number < final_list[-1]:
                final_list.append(number)
            else:
                final_list.insert(0, number)
    # Join the list with spaces and return as string
    return " ".join(final_list)

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Split the input string into a list of words.
    numbers_list = numbers.split(' ')

    # Setup an empty list to store the sorted numbers.
    sorted_numbers = []

    # Iterate through the list of numbers
    for number in numbers_list:
        # Check if the number is a valid choice
        if number not in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
            raise ValueError(f"Invalid number {number}")
        else:
            # Add the number to the sorted list
            sorted_numbers.append(number)

    # Sort the list of numbers
    sorted_numbers.sort()

    # Join the sorted numbers back into a string
    sorted_numbers_string = ' '.join(sorted_numbers)

    # Return the sorted string
    return sorted_numbers_string

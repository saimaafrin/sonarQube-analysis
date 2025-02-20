def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Initialize an empty list
    sort_numbers_list = []
    # Split the string into individual words
    number_list = numbers.split()
    # Iterate through each word and append it to the empty list
    for i in number_list:
        # Check if the word is a valid number from zero to nine
        if i == 'zero' or i == 'one' or i == 'two' or i == 'three' or i == 'four' or i == 'five' or i == 'six' or i == 'seven' or i == 'eight' or i == 'nine':
            # Append each valid word to the list
            sort_numbers_list.append(i)
            # Check if the list is not empty
            if sort_numbers_list != []:
                # Sort the list from smallest to largest
                sort_numbers_list.sort()
                # Join the list into a string with space delimiting each word
                sort_numbers_string = ' '.join(sort_numbers_list)
                # Return the sorted string
                return sort_numbers_string
        # If the word is not a valid number, raise a TypeError
        else:
            raise TypeError('Invalid input')

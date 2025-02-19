def file_name_check(file_name: str) -> str:
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    >>> file_name_check('example.txt')
    'Yes'
    >>> file_name_check('1example.dll')
    'No'
    """

    # Create a list of numbers from 0 to 9
    numbers = [str(num) for num in range(0, 10)]
    # Create a list of letters from the latin alphabet
    letters = [chr(num) for num in range(97, 123)]
    letters.extend([chr(num) for num in range(65, 91)])
    # Create a list of file types
    file_types = ['txt', 'exe', 'dll']
    # Create a list of the characters in the file name
    file_name_chars = list(file_name)
    # Create a list of the digits in the file name
    digits = [char for char in file_name_chars if char in numbers]
    # Check if the length of the digits list is greater than 3
    if len(digits) > 3:
        return 'No'
    # Check if the file name contains a dot
    if file_name.count('.') != 1:
        return 'No'
    # Check if the character before the dot is a letter
    if file_name_chars[file_name.find('.') - 1] not in letters:
        return 'No'
    # Check if the character after the dot is a letter
    if file_name_chars[file_name.find('.') + 1] not in letters:
        return 'No'
    # Check if the file type is valid
    if file_name.split('.')[1] not in file_types:
        return 'No'
    # If all conditions are met, the file name is valid
    return 'Yes'

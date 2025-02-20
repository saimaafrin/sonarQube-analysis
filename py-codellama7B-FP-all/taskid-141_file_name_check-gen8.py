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

    # 2. Find the number of digits in the file_name
    digits_num = sum([1 for char in file_name if char.isdigit()])

    # 3. Check that there is no more than 3 digits
    if digits_num > 3:
        return 'No'

    # 4. Check that there is one and only one dot in the file_name
    if file_name.count('.') != 1:
        return 'No'

    # 5. Split the file_name at the dot
    split_file_name = file_name.split('.')

    # 6. Check that the first part of the file_name starts with a letter
    if not split_file_name[0][0].isalpha():
        return 'No'

    # 7. Check that the second part of the file_name is one of the three extensions
    if split_file_name[1] not in ('txt', 'exe', 'dll'):
        return 'No'

    # 8. If all the conditions are met return 'Yes'
    return 'Yes'

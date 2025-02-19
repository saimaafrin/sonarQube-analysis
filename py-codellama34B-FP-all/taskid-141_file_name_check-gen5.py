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

    def _file_name_check(name):
        name = name.strip()
        if name == '':
            return 'No'
        if not name[0].isalpha():
            return 'No'
        try:
            if name[-4:] != '.txt' and name[-4:] != '.exe' and name[-4:] != '.dll':
                return 'No'
        except IndexError:
            return 'No'
        num_count = 0
        for char in name:
            if char.isdigit():
                num_count += 1
                if num_count > 3:
                    return 'No'
        if '.' in name:
            dot_count = 0
            for char in name:
                if char == '.':
                    dot_count += 1
            if dot_count != 1:
                return 'No'
        return 'Yes'
    return _file_name_check(file_name)

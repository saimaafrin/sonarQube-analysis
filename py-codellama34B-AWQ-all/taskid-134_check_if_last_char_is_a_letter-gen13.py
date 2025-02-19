def check_if_last_char_is_a_letter(txt: str) -> bool:
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    >>> check_if_last_char_is_a_letter('apple pie')
    False
    >>> check_if_last_char_is_a_letter('apple pi e')
    True
    >>> check_if_last_char_is_a_letter('apple pi e ')
    False
    >>> check_if_last_char_is_a_letter('')
    False
    """

    if len(txt) == 0:
        return False

    # get the last character of the string
    last_char = txt[-1]
    # get the index of the last space character
    last_space_index = txt.rfind(' ')
    # check if the last character is a letter
    return last_char.isalpha() and last_space_index + 1 == len(txt)

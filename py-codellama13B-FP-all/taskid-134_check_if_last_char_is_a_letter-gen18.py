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


    # Step 1. If the input string is empty, return False
    if txt == "":
        return False

    # Step 2. Find the index of the last character
    last_char_index = len(txt) - 1

    # Step 3. Find the last character
    last_char = txt[last_char_index]

    # Step 4. Check if the last character is a letter
    if last_char.isalpha():

        # Step 5. If the last character is a letter, check if it is not part of a word
        if not txt[last_char_index - 1].isspace():
            return True

    # Step 6. If the last character is not a letter, or is part of a word, return False
    return False

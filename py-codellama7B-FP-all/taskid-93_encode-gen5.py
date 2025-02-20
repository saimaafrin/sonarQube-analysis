def encode(message: str) -> str:
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    # Use a dictionary to map lowercase characters to uppercase.
    lower_to_upper = dict((k, v) for k, v in zip(ascii_lowercase, ascii_uppercase))

    # Create a list of vowels to map to 2 letters ahead.
    vowels = 'aeiou'
    vowel_list = list(vowels)

    # Create a list of characters to be replaced with vowels.
    replace_list = lower_to_upper.values()

    # Create a new string with uppercase characters.
    new_string = message.swapcase()

    # Replace all vowels with characters 2 places ahead of them.
    for char in replace_list:
        # Find the index of the current vowel.
        vowel_index = vowel_list.index(char)

        # Determine the index of the new vowel.
        new_vowel_index = vowel_index + 2

        # Check if the new vowel index is less than 26.
        if new_vowel_index < 26:
            new_char = replace_list[new_vowel_index]
        else:
            new_char = replace_list[new_vowel_index - 26]

        # Replace the current vowel with the new vowel.
        new_string = new_string.replace(char, new_char)

    return new_string

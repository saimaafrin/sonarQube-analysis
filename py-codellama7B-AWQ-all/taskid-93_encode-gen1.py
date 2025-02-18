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

    # Your code here
    # Use a list to keep track of which characters you've seen
    # and where the character will go in the new string
    new_string = ''
    char_list = [' '] * 26
    # Go through each character of the input string
    for c in message:
        if c.isupper():
            # Uppercase, so look up the index of the character in char_list
            char_index = char_list.index(c)
            # Where is the next character?
            next_index = (char_index + 1) % 26
            # Get the character from the list at that index
            next_char = char_list[next_index]
            # Set the current character in the list to the next character
            char_list[char_index] = next_char
            new_string += next_char
        else:
            # Lowercase, so just uppercase the letter
            new_string += c.upper()
    return new_string

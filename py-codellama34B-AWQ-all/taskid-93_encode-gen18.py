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

    vowels = ['a', 'e', 'i', 'o', 'u']
    # Create a dictionary with a vowel as key and the letter that 
    # appears 2 places ahead as the value.
    vowel_dict = {}
    for vowel in vowels:
        vowel_dict[vowel] = chr(ord(vowel) + 2)
    vowel_dict['A'] = 'C'
    vowel_dict['E'] = 'G'
    vowel_dict['I'] = 'K'
    vowel_dict['O'] = 'M'
    vowel_dict['U'] = 'O'
    
    # Swap cases and then replace vowels.
    swapped_cases = swap_cases(message)
    encoded_message = ''
    for char in swapped_cases:
        if char in vowel_dict:
            encoded_message += vowel_dict[char]
        else:
            encoded_message += char
    return encoded_message

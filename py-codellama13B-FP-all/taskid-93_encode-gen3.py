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

    # Initialize vowels
    vowels = 'aeiou'
    # Initialize result
    result = ''
    # Iterate over message
    for char in message:
        # Check if char is a letter
        if char.isalpha():
            # Check if char is uppercase
            if char.isupper():
                # Find position of char in lowercase alphabet
                lower_pos = ord(char.lower()) - ord('a') + 1
                # Find position of char in uppercase alphabet
                upper_pos = ord(char.upper()) - ord('A') + 1
                # Check if char is a vowel
                if char.lower() in vowels:
                    # Get letter 2 places ahead of char
                    vowel_shift = lower_pos + 2
                    # Check if letter is in uppercase alphabet
                    if vowel_shift > upper_pos:
                        # If not, wrap around to the beginning of the alphabet
                        vowel_shift = vowel_shift - upper_pos
                    else:
                        # If yes, set letter to uppercase
                        result += chr(ord('A') + vowel_shift - 1)
                        continue
                else:
                    # If not a vowel, set letter to uppercase
                    result += chr(ord('A') + lower_pos - 1)
            else:
                # Check if char is a vowel
                if char in vowels:
                    # Get letter 2 places ahead of char
                    vowel_shift = ord(char) - ord('a') + 2
                    # Check if letter is in uppercase alphabet
                    if vowel_shift > 26:
                        # If not, wrap around to the beginning of the alphabet
                        vowel_shift = vowel_shift - 26
                    else:
                        # If yes, set letter to lowercase
                        result += chr(ord('a') + vowel_shift - 1)
                        continue
                else:
                    # If not a vowel, set letter to lowercase
                    result += chr(ord('a') + ord(char) - ord('A'))
        else:
            # If char is not a letter, add it to result
            result += char
    # Return result
    return result

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


    encoded_message = ''
    vowels = 'aeiou'
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                if letter in vowels:
                    new_letter = chr((ord(letter) + 2 - ord('a')) % 26 + ord('a'))
                else:
                    new_letter = letter.upper()
            else:
                if letter in vowels:
                    new_letter = letter.lower()
                else:
                    new_letter = chr((ord(letter) - 2 - ord('A')) % 26 + ord('A'))
            encoded_message += new_letter
        else:
            encoded_message += letter

    return encoded_message

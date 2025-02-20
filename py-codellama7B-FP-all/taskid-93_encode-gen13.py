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

    # This is the vowel list in english alphabet
    vowels = ["A", "E", "I", "O", "U"]
    # This is the 2 places ahead list in english alphabet
    # [A,B,C,D,E] -> [C,D,E,F,G]
    vowels_two_places_ahead = ["C", "D", "E", "F", "G"]
    
    encoded = ""
    for character in message:
        # If letter is lowercase, then change to uppercase
        if character.islower():
            encoded += character.upper()
        # If letter is uppercase, then change to lowercase
        else:
            encoded += character.lower()
        
        # Check if character is a vowel
        if character in vowels:
            # Get the vowel two places ahead
            encoded += vowels_two_places_ahead[vowels.index(character)]
        
    return encoded

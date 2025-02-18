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

    import string
    # Create a list of all the letters in the alphabet
    letters = string.ascii_letters
    # Create a list of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Create a list of all consonants
    consonants = [letter for letter in letters if letter.lower() not in vowels]
    
    # Replace all consonants with their upper case equivalent
    encoded_message = message.translate(str.maketrans({
        letter: letter.upper() for letter in consonants
    }))
    
    # Replace all vowels with their equivalent 2 positions ahead
    # of themselves in the alphabet
    for index, vowel in enumerate(vowels):
        # Get the 2 positions ahead of the current vowel
        new_vowel = letters[index + 2]
        
        # Replace all instances of the vowel with the new vowel
        encoded_message = encoded_message.replace(
            vowel, new_vowel
        )
    
    return encoded_message

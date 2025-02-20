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
    # Initialize a variable to hold the encoded message
    encoded_message = ''

    # Iterate over each character of the message
    for character in message:
        # If the character is a vowel, encode it
        if character.lower() in 'aeiou':
            # Replace the character with the character 2 places ahead of it
            # in the alphabet. Wrap around to the beginning of the alphabet
            # if necessary
            index = (ord(character.lower()) - ord('a') + 2) % 26 + ord('a')
            encoded_message += chr(index)
        # Otherwise, encode it by swapping its case
        else:
            if character.islower():
                encoded_message += character.upper()
            else:
                encoded_message += character.lower()

    return encoded_message

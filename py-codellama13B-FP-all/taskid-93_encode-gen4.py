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

    # Create a list of the letters in the message, and a new empty list to store the encoded message
    message_list = list(message)
    encoded_message = []

    # Create a dictionary that maps vowels to the letter 2 places ahead of them in the alphabet
    vowels_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'm', 'u': 's', 'y': 'z'}

    # Iterate through each letter in the message
    for letter in message_list:
        # If the letter is a vowel, find the letter that is 2 places ahead of it in the alphabet
        if letter.lower() in vowels_map:
            encoded_message.append(vowels_map[letter.lower()])
        # If the letter is a consonant, just swap its case
        elif letter.isalpha():
            # Check if the letter is uppercase or lowercase and append the appropriate case to the encoded message
            if letter.isupper():
                encoded_message.append(letter.lower())
            else:
                encoded_message.append(letter.upper())
    return ''.join(encoded_message)

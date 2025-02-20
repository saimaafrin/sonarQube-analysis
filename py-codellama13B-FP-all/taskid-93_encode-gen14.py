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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    message = message.lower()
    encoded_message = []

    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + 2
            if new_index > 25:
                new_index -= 26
            encoded_message.append(alphabet[new_index])
        else:
            encoded_message.append(char)

    return "".join(encoded_message)

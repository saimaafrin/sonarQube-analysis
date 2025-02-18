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

    # your code here
    message = message.swapcase()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(message)):
        if message[i] in vowels:
            message = message[:i] + chr((ord(message[i]) + 2 - ord('a')) % 26 + ord('a')) + message[i+1:]
    return message

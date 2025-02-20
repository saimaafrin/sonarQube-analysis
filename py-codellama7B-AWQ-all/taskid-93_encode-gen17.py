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
    result = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in message:
        if i.islower():
            result += vowel[vowel.index(i) % 5].upper()
        elif i.isupper():
            result += vowel[vowel.index(i) % 5].lower()
        else:
            result += i
    return result

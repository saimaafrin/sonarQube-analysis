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
    result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    for i in range(len(result)):
        if result[i].lower() in vowels:
            idx = vowels.index(result[i].lower())
            if idx == 4:
                idx = -1
            result = f'{result[:i]}{vowels[idx+2]}{result[i+1:]}'
    return result

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

    def swap_case(letter):
        if letter.isupper():
            return letter.lower()
        return letter.upper()
    
    def vowel_replace(letter):
        if letter.lower() in 'aeiou':
            return chr((ord(letter) + 2) % 26 + ord('A'))
        return letter

    return ''.join(map(lambda l: swap_case(vowel_replace(l)), message))

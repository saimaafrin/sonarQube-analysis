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

    vowels = 'aeiou'
    vowels_idx = {v: i for i, v in enumerate(vowels)}
    new_vowels = {i: v for i, v in enumerate(vowels)}

    encoded_msg = ''
    for ch in message:
        ch_idx = vowels_idx.get(ch)
        if ch_idx is not None:
            new_idx = (ch_idx + 2) % len(vowels)
            encoded_msg += new_vowels[new_idx]
        else:
            encoded_msg += ch.swapcase()
    return encoded_msg

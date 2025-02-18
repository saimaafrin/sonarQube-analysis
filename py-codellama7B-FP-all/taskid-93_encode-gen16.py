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

    def swap_case(char):
        if char.islower():
            return char.upper()
        else:
            return char.lower()
    
    def vowel_swap(char, vowel_list):
        if char.isalpha():
            if char.lower() in vowel_list:
                char_index = vowel_list.index(char.lower())
                return vowel_list[char_index+2]
            else:
                return char
        else:
            return char
    
    vowel_list = ['a','e','i','o','u']
    message = message.lower()
    result = ''.join(map(swap_case, message))
    result = ''.join(map(vowel_swap, result, vowel_list))
    return result

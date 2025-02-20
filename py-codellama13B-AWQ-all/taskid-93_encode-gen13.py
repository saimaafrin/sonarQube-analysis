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


    # 26 letters in the English alphabet.
    offset = 26

    # Convert message to upper case and get its length.
    msg_len = len(message.upper())

    # Create a list to store the encoded message.
    encoded_msg = []

    # Iterate through the message and encode each letter.
    for i in range(msg_len):
        # Check if the character at index i is a vowel.
        if message[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            # Calculate the index of the letter two places ahead of the vowel.
            index = ord(message[i].lower()) + offset
            # Convert the calculated index to a character.
            new_char = chr(index)
            # Append the encoded character to the encoded message.
            encoded_msg.append(new_char)
        else:
            # Check if the character at index i is a consonant.
            if message[i].isalpha() and message[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
                # Calculate the index of the letter two places ahead of the consonant.
                index = ord(message[i]) + offset
                # Convert the calculated index to a character.
                new_char = chr(index)
                # Append the encoded character to the encoded message.
                encoded_msg.append(new_char)
            # If the character at index i is not a letter, append it to the encoded message.
            else:
                encoded_msg.append(message[i])

    # Join the encoded message into a single string.
    encoded_message = "".join(encoded_msg)

    return encoded_message

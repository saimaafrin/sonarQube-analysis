def is_bored(S: str) -> int:
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored('Hello world')
    0
    >>> is_bored('The sky is blue. The sun is shining. I love this weather')
    1
    """

    # Initialize a counter for the number of boredoms
    count = 0

    # Initialize a list to store the sentences
    sentences = []

    # Split the input string into a list of words
    words = S.split(' ')

    # Initialize a temporary variable to hold the current sentence
    temp = ''

    # Iterate over the list of words
    for word in words:
        # Check if the word is a full stop, question mark or exclamation mark
        if word in ['.', '?', '!']:
            # If the temporary variable is not empty, add it to the list of
            # sentences
            if temp != '':
                sentences.append(temp)

            # Reset the temporary variable to an empty string
            temp = ''

        # If the word is not a sentence delimiter, add it to the temporary
        # variable
        else:
            temp += word + ' '

    # Add the last sentence to the list of sentences
    sentences.append(temp)

    # Iterate over the list of sentences
    for sentence in sentences:
        # Check if the sentence starts with the word "I"
        if sentence.startswith('I'):
            count += 1

    # Return the count of boredoms
    return count

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

    # split string into array of words
    words = S.split()

    # start counting
    boredom_count = 0

    # check each word
    for word in words:
        # if the word is "I"
        if word == "I":
            # add 1 to boredom count
            boredom_count += 1

    # return boredom count
    return boredom_count

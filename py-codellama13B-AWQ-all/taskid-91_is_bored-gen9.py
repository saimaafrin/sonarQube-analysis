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

    sentence = S.split()
    i = 0
    for i in range(len(sentence)):
        if sentence[i] == 'I':
            return 1
        else:
            return 0
        if sentence[i] == '.':
            i = i + 1
        elif sentence[i] == '?':
            i = i + 1
        elif sentence[i] == '!':
            i = i + 1
    return 0

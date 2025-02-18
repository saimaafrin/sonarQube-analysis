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

    # +++your code here+++
    # If you get an error on the following line it means you are using a version of Python later than
    # 3.5. In that case you should change the word 'yield' to 'yield from'
    return sum(1 for x in sentence.split() if x == 'I' for sentence in S.split('.'))
    # +++your code here+++

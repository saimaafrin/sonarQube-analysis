import random
import re
def task_func(text, seed=None):
    """
    Scramble the letters in each word of a given text, keeping the first and last letters of each word intact.
    Notes:
        - Words are determined by regex word boundaries.
        - The scrambling only affects words longer than three characters, leaving shorter words unchanged.
    Args:
        text (str): The text to scramble.
        seed (int, optional): The random seed to use. Defaults to None.
    Returns:
        str: The scrambled text.
    """
    if seed is not None:
        random.seed(seed)
    words = re.findall(r'\b\w+\b', text)
    scrambled_words = []
    for word in words:
        if len(word) > 3:
            scrambled_word = ''.join(random.sample(word, len(word)))
            scrambled_words.append(scrambled_word)
        else:
            scrambled_words.append(word)
    return ' '.join(scrambled_words)
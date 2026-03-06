import nltk
from collections import Counter
def task_func(content):
    """
    Count the Part-of-Speech (POS) tags in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count POS tags from.

    Returns:
    - dict: A dictionary with POS tags as keys and their count as values.

    Requirements:
    - nltk
    - collections.Counter

    Example:
    >>> task_func('this is an example content')
    {'DT': 2, 'VBZ': 1, 'NN': 1}
    """
    # Split the sentence into words and POS tags
    words = nltk.word_tokenize(content)
    pos_tags = nltk.pos_tag(words)

    # Count the POS tags
    pos_tag_counts = Counter(pos_tag[1] for pos_tag in pos_tags[:-1])

    # Return the counts as a dictionary
    return pos_tag_counts
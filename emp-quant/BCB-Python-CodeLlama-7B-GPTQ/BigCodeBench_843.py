import random
import re
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]
def task_func(n_sentences):
    """
    Generate a string of random sentences using a predefined word list.
    Each sentence is guaranteed to have one period at the end, and no period within the sentence.
    The generated sentences will be concatenated into a single string, with all letters in lowercase and all non-alphanumeric characters except spaces removed.
    Note that:
    The actual output will vary due to the randomness of sentence generation.
    The function should output with:
        str: A string containing the generated sentences in lowercase
        with non-alphanumeric characters removed (except for single periods ending sentences).
    """
    sentences = []
    for _ in range(n_sentences):
        sentence = ""
        for _ in range(random.randint(1, 5)):
            sentence += random.choice(WORD_LIST) + " "
        sentence += "."
        sentences.append(sentence)
    return " ".join(sentences)
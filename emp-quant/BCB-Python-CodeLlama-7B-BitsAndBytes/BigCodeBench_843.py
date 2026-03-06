
import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    sentences = []
    for _ in range(n_sentences):
        sentence = []
        for _ in range(random.randint(1, 5)):
            word = random.choice(WORD_LIST)
            sentence.append(word)
        sentence.append(".")
        sentences.append(" ".join(sentence))
    return " ".join(sentences).lower()

import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    sentences = []
    for _ in range(n_sentences):
        sentence = random.choice(WORD_LIST)
        while True:
            word = random.choice(WORD_LIST)
            if word != sentence and word[-1] != ".":
                sentence += " " + word
                break
        sentences.append(sentence)
    return " ".join(sentences).lower().replace("[^a-zA-Z]", "")
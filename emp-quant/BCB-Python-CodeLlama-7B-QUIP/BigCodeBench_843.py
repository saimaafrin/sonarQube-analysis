
import random
import re
# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]
def task_func(n_sentences):
    sentences = []
    for i in range(n_sentences):
        sentence = ""
        for j in range(random.randint(1, 5)):
            sentence += WORD_LIST[random.randint(0, len(WORD_LIST) - 1)] + " "
        sentence += "."
        sentences.append(sentence)
    return " ".join(sentences)
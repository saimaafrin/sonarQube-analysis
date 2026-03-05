
import random
import re

def task_func(target_words, n_sentences, vocabulary):
    if n_sentences < 0:
        raise ValueError("n_sentences must be non-negative")
    if not vocabulary:
        raise ValueError("vocabulary must not be empty")
    sentences = []
    for _ in range(n_sentences):
        sentence = " ".join(random.choice(vocabulary) for _ in range(10))
        for word in target_words:
            sentence = re.sub(r"(\b" + word + r"\b)", "_", sentence)
        sentences.append(sentence)
    return sentences
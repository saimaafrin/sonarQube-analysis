
import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    sentences = []
    for _ in range(n_sentences):
        sentence = ' '.join(random.choices(WORD_LIST, k=random.randint(3, 10)))
        sentences.append(sentence.capitalize() + '.')
    result = ' '.join(sentences).lower()
    result = re.sub(r'[^a-z\s.]', '', result)
    return result
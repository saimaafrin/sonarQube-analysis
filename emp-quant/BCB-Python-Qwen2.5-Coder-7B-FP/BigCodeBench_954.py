import random
import re
def task_func(target_words, n_sentences, vocabulary):
    if n_sentences < 0 or not vocabulary:
        raise ValueError("Invalid input: n_sentences must be non-negative and vocabulary must not be empty.")
    
    target_words = [word.lower() for word in target_words]
    sentences = []
    
    for _ in range(n_sentences):
        sentence = ' '.join(random.choices(vocabulary, k=10))
        for word in target_words:
            sentence = re.sub(r'\b' + re.escape(word) + r'\b', word.replace(' ', '_'), sentence, flags=re.IGNORECASE)
        sentences.append(sentence.lower())
    
    return sentences
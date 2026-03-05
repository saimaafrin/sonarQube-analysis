import random
import re
def task_func(target_words, n_sentences, vocabulary):
    if n_sentences < 0 or not vocabulary:
        raise ValueError("n_sentences must be non-negative and vocabulary must not be empty")
    
    target_words = [word.lower() for word in target_words]
    sentences = []
    
    for _ in range(n_sentences):
        sentence = []
        for _ in range(10):
            word = random.choice(vocabulary)
            if word.lower() in target_words:
                word = re.sub(r'\b(' + '|'.join(target_words) + r')\b', lambda m: m.group(1).replace(' ', '_'), word, flags=re.IGNORECASE)
            sentence.append(word)
        sentences.append(' '.join(sentence).lower())
    
    return sentences
import random
import re
def task_func(target_words, n_sentences, vocabulary):
    if n_sentences < 0 or not vocabulary:
        raise ValueError("Invalid input: n_sentences must be non-negative and vocabulary must not be empty.")
    
    sentences = []
    target_words_lower = [word.lower() for word in target_words]
    
    for _ in range(n_sentences):
        sentence = ' '.join(random.choice(vocabulary) for _ in range(10))
        for target_word in target_words_lower:
            sentence = re.sub(r'\b' + re.escape(target_word) + r'\b', target_word.replace(' ', '_'), sentence, flags=re.IGNORECASE)
        sentences.append(sentence.lower())
    
    return sentences
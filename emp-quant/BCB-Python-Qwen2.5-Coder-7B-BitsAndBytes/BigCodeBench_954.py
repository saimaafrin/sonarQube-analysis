
import random
import re

def task_func(target_words, n_sentences, vocabulary):
    if n_sentences < 0 or not vocabulary:
        raise ValueError("Invalid input: n_sentences must be non-negative and vocabulary cannot be empty.")
    
    def generate_sentence():
        sentence = ' '.join(random.choice(vocabulary) for _ in range(10))
        return sentence
    
    def underscore_target_words(sentence):
        for word in target_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            sentence = pattern.sub(lambda m: m.group().replace(' ', '_'), sentence)
        return sentence.lower()
    
    sentences = []
    while len(sentences) < n_sentences:
        sentence = generate_sentence()
        underscored_sentence = underscore_target_words(sentence)
        sentences.append(underscored_sentence)
    
    return sentences
import random
import re
def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def scramble_word(word):
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + ''.join(middle) + word[-1]
        return word
    
    words = re.findall(r'\b\w+\b', text)
    scrambled_words = [scramble_word(word) for word in words]
    scrambled_text = re.sub(r'\b\w+\b', lambda match: scrambled_words.pop(0), text)
    
    return scrambled_text
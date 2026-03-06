
import re
import string
import random

def task_func(text: str, seed=None) -> str:
    if seed is not None:
        random.seed(seed)
    
    # Remove special characters
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    
    # Normalize whitespace
    text = text.replace(' ', '_').replace('\t', '__').replace('\n', '___')
    
    # Randomize character casing
    result = []
    for char in text:
        if char.isalpha():
            if random.choice([True, False]):
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)
    
    return ''.join(result)

import re
import string
import random

def task_func(text: str, seed=None) -> str:
    if seed is not None:
        random.seed(seed)
    
    # Normalize whitespace
    text = re.sub(r'\s+', '_', text)
    text = re.sub(r'\t', '__', text)
    text = re.sub(r'\n', '___', text)
    
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Randomize character casing
    text = ''.join(random.choice([char.upper(), char.lower()]) for char in text)
    
    return text
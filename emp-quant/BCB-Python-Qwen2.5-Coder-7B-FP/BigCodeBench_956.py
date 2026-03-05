import re
import string
import random
def task_func(text: str, seed=None) -> str:
    if seed is not None:
        random.seed(seed)
    
    # Replace special characters with underscores
    text = re.sub(f'[{string.punctuation}]', '_', text)
    
    # Replace spaces, tabs, and newlines with _, __, and ___ respectively
    text = re.sub(r'\s+', lambda m: '_' * len(m.group()), text)
    
    # Randomize character casing
    text = ''.join(random.choice([char.upper(), char.lower()]) for char in text)
    
    return text
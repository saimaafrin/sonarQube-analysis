
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    tokenizer = RegexpTokenizer('[a-zA-Z0-9]+')
    tokens = tokenizer.tokenize(text)
    dollar_tokens = [token for token in tokens if token.startswith('$')]
    dollar_counts = Counter(dollar_tokens)
    dollar_counts = dollar_counts.most_common(5)
    return dollar_counts
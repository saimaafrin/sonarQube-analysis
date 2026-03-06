
import re
import nltk
from string import punctuation

def task_func(df):
    if df.empty or 'Title' not in df.columns or 'Content' not in df.columns:
        raise ValueError("DataFrame is empty or does not contain the necessary columns 'Title' and 'Content'")

    # Extract articles with keywords
    articles = df[df['Title'].str.contains('like|what', case=False)]

    # Tokenize and remove punctuation
    tokens = nltk.word_tokenize(articles['Content'])
    tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]

    # Count frequency of each word
    word_freq = {}
    for token in tokens:
        if token not in word_freq:
            word_freq[token] = 1
        else:
            word_freq[token] += 1

    return word_freq
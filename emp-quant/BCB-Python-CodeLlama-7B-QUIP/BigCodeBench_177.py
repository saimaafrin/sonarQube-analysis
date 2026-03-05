
import re
import nltk
from string import punctuation

def task_func(df):
    if df.empty or df['Title'].empty or df['Content'].empty:
        raise ValueError("The DataFrame is empty or does not contain the necessary columns 'Title' and 'Content'.")

    # Tokenize the text and remove punctuation
    def tokenize(text):
        return re.sub(r"[%s]" % punctuation, "", text.lower())

    # Create a dictionary of word frequencies
    word_freq = {}
    for text in df['Content']:
        for word in tokenize(text):
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words('english')
    for word in word_freq:
        if word in stop_words:
            del word_freq[word]

    return word_freq
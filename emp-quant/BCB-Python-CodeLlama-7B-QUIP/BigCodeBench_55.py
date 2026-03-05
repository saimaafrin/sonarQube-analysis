
import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]
def task_func(text):
    sentences = re.split(r"[.!?]", text)
    sentences = [s for s in sentences if s.strip()]
    sentences_with_words = [s for s in sentences if s.split()]
    sentences_with_words_without_stopwords = [s for s in sentences_with_words if s.split() - set(STOPWORDS)]
    return pd.Series(sentences_with_words_without_stopwords, index=["Sentence 1", "Sentence 2", "Sentence 3", "Sentence 4", "Sentence 5"])
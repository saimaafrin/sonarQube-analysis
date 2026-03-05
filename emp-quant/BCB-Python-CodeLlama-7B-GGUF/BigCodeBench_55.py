
import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]
def task_func(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z])(?<=\.|\?|\!)\s', text)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    sentences = [sentence for sentence in sentences if not any(word in STOPWORDS for word in sentence.split())]
    sentence_counts = {f"Sentence {i+1}": len(sentence.split()) for i, sentence in enumerate(sentences)}
    return pd.Series(sentence_counts)
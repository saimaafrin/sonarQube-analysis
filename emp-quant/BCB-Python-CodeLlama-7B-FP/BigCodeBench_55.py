import re
import pandas as pd
STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]
def task_func(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    sentences = [sentence for sentence in sentences if sentence.split()]
    sentences = [sentence for sentence in sentences if sentence.split() and sentence.split()[0] not in STOPWORDS]
    sentences = {f"Sentence {i+1}": sentence for i, sentence in enumerate(sentences)}
    return pd.Series(sentences)
text = "This is a sample text. Those are the words to ignore. This is another sentence."
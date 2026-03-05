
import pandas as pd
from collections import Counter

def task_func(text_dict, word_keys, top_k=2):
    if top_k < 0:
        raise ValueError("top_k must be a positive integer")
    word_freqs = Counter(word_keys)
    for word in word_keys:
        if word in text_dict:
            word_freqs[word] += text_dict[word]
    top_k_words = sorted(word_freqs.items(), key=lambda x: x[1], reverse=True)[:top_k]
    fig, ax = plt.subplots()
    ax.bar(x=range(top_k), height=top_k_words)
    ax.set_xlabel("Word")
    ax.set_ylabel("Frequency")
    ax.set_title("Top {} Most Common Words".format(top_k))
    return ax, {word: freq for word, freq in top_k_words}
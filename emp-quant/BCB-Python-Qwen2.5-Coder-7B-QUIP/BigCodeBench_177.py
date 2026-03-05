
import re
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

def task_func(df):
    # Check if the DataFrame is empty or does not contain the necessary columns
    if df.empty or 'Title' not in df or 'Content' not in df:
        raise ValueError("DataFrame is empty or missing necessary columns 'Title' and 'Content'")

    # Define the keywords to search for
    keywords = ['like', 'what']

    # Initialize an empty list to store the content of articles with matching titles
    matching_content = []

    # Iterate through the DataFrame to find articles with titles containing the keywords
    for index, row in df.iterrows():
        if any(keyword in row['Title'].lower() for keyword in keywords):
            matching_content.append(row['Content'])

    # Tokenize the content and count the frequency of each word, excluding punctuation
    all_words = []
    for content in matching_content:
        words = word_tokenize(content)
        words = [word.lower() for word in words if word.lower() not in set(punctuation) and word.lower() not in set(stopwords.words('english'))]
        all_words.extend(words)

    word_freq = Counter(all_words)

    return dict(word_freq)
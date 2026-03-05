
import re
import nltk
from string import punctuation
from collections import Counter

def task_func(df):
    # Check if the DataFrame is empty or does not contain the necessary columns
    if df.empty or 'Title' not in df.columns or 'Content' not in df.columns:
        raise ValueError("DataFrame is empty or does not contain the necessary columns 'Title' and 'Content'.")

    # Define the case-insensitive keywords
    keywords = ['like', 'what']

    # Initialize an empty list to store the content of articles with the specified keywords
    content_list = []

    # Iterate over the DataFrame rows
    for index, row in df.iterrows():
        # Check if the title contains any of the keywords
        if any(keyword.lower() in row['Title'].lower() for keyword in keywords):
            # Append the content to the list
            content_list.append(row['Content'])

    # Join all the content into a single string
    all_content = ' '.join(content_list)

    # Remove punctuation from the content
    all_content = re.sub(f'[{re.escape(punctuation)}]', '', all_content)

    # Tokenize the content into words
    words = nltk.word_tokenize(all_content)

    # Count the frequency of each word
    word_frequency = Counter(words)

    # Return the word frequency dictionary
    return word_frequency
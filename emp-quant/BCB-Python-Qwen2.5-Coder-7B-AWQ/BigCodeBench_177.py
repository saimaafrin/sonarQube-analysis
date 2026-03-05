import re
import nltk
from string import punctuation
from collections import Counter
def task_func(df):
    # Ensure the DataFrame is not empty and contains the necessary columns
    if df.empty or 'Title' not in df.columns or 'Content' not in df.columns:
        raise ValueError("DataFrame is empty or does not contain the necessary columns 'Title' and 'Content'.")

    # Define the keywords to search for in the titles
    keywords = ['like', 'what']

    # Initialize an empty list to store the content of articles that match the criteria
    matching_content = []

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        # Check if the title contains any of the keywords (case-insensitive)
        if any(keyword in row['Title'].lower() for keyword in keywords):
            # Append the content of the article to the list
            matching_content.append(row['Content'])

    # Join all the content into a single string
    all_content = ' '.join(matching_content)

    # Remove punctuation from the content
    all_content = re.sub(f"[{re.escape(punctuation)}]", "", all_content)

    # Tokenize the content into words
    words = nltk.word_tokenize(all_content)

    # Count the frequency of each word
    word_frequency = Counter(words)

    # Return the dictionary of word frequencies
    return dict(word_frequency)
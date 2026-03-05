
import re
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

def task_func(df):
    if df.empty or 'Title' not in df.columns or 'Content' not in df.columns:
        raise ValueError("DataFrame is empty or does not contain the necessary columns 'Title' and 'Content'.")

    # Filter articles containing 'like' or 'what' in the title, case-insensitive
    filtered_df = df[df['Title'].str.contains('like|what', case=False, na=False)]

    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Iterate over the filtered articles
    for content in filtered_df['Content']:
        # Tokenize the content into words
        words = word_tokenize(content)
        # Remove punctuation and convert to lowercase
        words = [word.lower() for word in words if word.isalnum()]
        # Remove stopwords
        words = [word for word in words if word not in stopwords.words('english')]
        # Update the word frequency dictionary
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq
import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation
def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    """
    Analyze the sentiment of a text using the provided SentimentIntensityAnalyzer.
    The text is first cleaned by:
    - Removing all non-alphanumeric characters except spaces.
    - Converting to lowercase.
    - Removing punctuation.
    The function should output with:
        dict: A dictionary with sentiment scores. The dictionary contains four scores:
        'compound': The overall sentiment score.
        'neg': Negative sentiment score.
        'neu': Neutral sentiment score.
        'pos': Positive sentiment score.
    """
    # Clean the text
    text = re.sub(ALPHANUMERIC, ' ', text.lower())
    text = re.sub(PUNCTUATIONS, '', text)

    # Analyze the sentiment
    sentiment = sia.polarity_scores(text)

    # Return the sentiment scores
    return sentiment
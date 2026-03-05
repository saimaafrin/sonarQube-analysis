
import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation

def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    # Clean the text
    text = re.sub(ALPHANUMERIC, '', text)  # Remove non-alphanumeric characters
    text = text.lower()  # Convert to lowercase
    text = re.sub(PUNCTUATIONS, '', text)  # Remove punctuation

    # Analyze the sentiment
    sentiment_scores = sia.polarity_scores(text)

    return sentiment_scores

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
    text = re.sub(ALPHANUMERIC, ' ', text).lower()
    text = re.sub(PUNCTUATIONS, '', text)
    # Analyze the sentiment
    scores = sia.polarity_scores(text)
    return {
        'compound': scores['compound'],
        'neg': scores['neg'],
        'neu': scores['neu'],
        'pos': scores['pos']
    }

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
    cleaned_text = ALPHANUMERIC.sub(' ', text).lower()
    cleaned_text = cleaned_text.translate(str.maketrans('', '', PUNCTUATIONS))
    
    # Analyze the sentiment
    sentiment_scores = sia.polarity_scores(cleaned_text)
    
    return sentiment_scores
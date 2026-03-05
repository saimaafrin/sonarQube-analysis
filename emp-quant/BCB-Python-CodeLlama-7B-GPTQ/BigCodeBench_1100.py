import re
from sklearn.feature_extraction.text import TfidfVectorizer
def task_func(texts):
    # Remove URLs from the text documents
    texts = [re.sub(r'https?://\S+', '', text) for text in texts]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the texts
    vectorizer.fit(texts)

    # Transform the texts into TF-IDF scores
    scores = vectorizer.transform(texts)

    # Extract the unique words (features) from the texts
    features = vectorizer.get_feature_names()

    # Convert the scores to a list of tuples
    scores_list = scores.tolist()

    # Convert the features to a list of strings
    features_list = features.tolist()

    # Return the TF-IDF scores and unique words as a tuple
    return (scores_list, features_list)
texts = [
    'This is a sample text.',
    'This is another sample text.',
    'This is a third sample text.',
]
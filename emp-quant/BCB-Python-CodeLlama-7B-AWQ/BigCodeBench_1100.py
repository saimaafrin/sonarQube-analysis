import re
from sklearn.feature_extraction.text import TfidfVectorizer
def task_func(texts):
    """
    Processes a collection of text documents to compute the TF-IDF (Term Frequency-Inverse Document Frequency) scores for each word, excluding any URLs present in the texts. The TF-IDF scores help to identify the importance of a word within a document relative to a collection of documents.
    Notes:
        - URLs in the text documents are removed before calculating TF-IDF scores to ensure they do not affect the analysis.
        - The TF-IDF scores are rounded to 8 decimal places for precision.
    Args:
        texts (list of str): A list of text documents.
    Returns:
        tuple of (list of tuples, list of str):
            The first element is a list of tuples, each tuple representing a document with its words' TF-IDF scores in a dense matrix format. Each score in the tuple corresponds to a word's TF-IDF score in the document.
            The second element is a list of strings, representing the unique words (features) across all documents for which TF-IDF scores have been calculated. The order of words in this list matches the order of scores in the tuples of the first element.
    """
    # Remove URLs from the text documents
    texts = [re.sub(r'https?://\S+|www\.\S+', '', text) for text in texts]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the TfidfVectorizer object to the text documents
    X = vectorizer.fit_transform(texts)

    # Get the TF-IDF scores for each word in each document
    scores = X.toarray()

    # Get the unique words (features) across all documents
    features = vectorizer.get_feature_names()

    # Round the TF-IDF scores to 8 decimal places for precision
    scores = [round(score, 8) for score in scores]

    # Return the TF-IDF scores and unique words as a tuple
    return (scores, features)
texts = ['This is a sample text document.', 'This is another sample text document.', 'This is a third sample text document.']
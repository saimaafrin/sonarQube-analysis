
import re
import nltk
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
# Ensure nltk's stopwords are downloaded
nltk.download('stopwords')
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(texts, num_topics):
    # Preprocess texts
    texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    texts = [word for text in texts for word in text.split() if word not in STOPWORDS]
    # Vectorize texts
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    # Apply NMF
    nmf = NMF(n_components=num_topics)
    W = nmf.fit_transform(X)
    # Extract topics
    topics = []
    for topic_idx in range(num_topics):
        topic_words = []
        for word_idx in range(X.shape[1]):
            if W[topic_idx, word_idx] > 0:
                topic_words.append(vectorizer.get_feature_names()[word_idx])
        topics.append(topic_words)
    return topics
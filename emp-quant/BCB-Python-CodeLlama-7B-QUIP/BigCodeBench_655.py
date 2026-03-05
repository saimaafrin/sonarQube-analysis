
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
    # Preprocess the texts
    texts = [re.sub(ALPHANUMERIC, ' ', text).lower() for text in texts]
    # Remove stopwords
    texts = [[word for word in nltk.word_tokenize(text) if word not in STOPWORDS] for text in texts]
    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=10000, stop_words=STOPWORDS)
    vectors = vectorizer.fit_transform(texts)
    # Apply NMF to the vectorized texts
    nmf = NMF(n_components=num_topics, random_state=42)
    nmf.fit(vectors)
    # Extract the topics
    topics = [[' '.join(word for word in nltk.word_tokenize(word) for word in topic) for topic in nmf.components_] for topic in nmf.components_]
    return topics
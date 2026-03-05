
import re
import nltk
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
# Ensure nltk's stopwords are downloaded
nltk.download('stopwords')
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')

def preprocess_text(text):
    # Remove non-alphanumeric characters, convert to lowercase, and remove stopwords
    return [word for word in re.findall(ALPHANUMERIC, text.lower()) if word not in STOPWORDS]

def task_func(texts, num_topics):
    # Preprocess the texts
    processed_texts = [preprocess_text(text) for text in texts]
    
    # Vectorize the processed texts using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    
    # Apply NMF to extract the specified number of topics
    nmf = NMF(n_components=num_topics, random_state=42)
    W = nmf.fit_transform(X)
    
    # Get the most significant words for each topic
    topic_words = []
    for i in range(num_topics):
        topic_words.append([word for word, _ in zip(vectorizer.get_feature_names_out(), W[i]) if word not in STOPWORDS and W[i, vectorizer.get_feature_names_out().index(word)] > 0])
    
    return topic_words
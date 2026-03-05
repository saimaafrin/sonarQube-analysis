import re
import nltk
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(texts, num_topics):
    # Preprocess the texts
    processed_texts = []
    for text in texts:
        # Remove non-alphanumeric characters (excluding spaces)
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        # Remove stopwords
        words = [word for word in text.split() if word not in STOPWORDS]
        processed_texts.append(' '.join(words))
    
    # Vectorize the processed texts using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(processed_texts)
    
    # Apply NMF to extract the specified number of topics
    nmf = NMF(n_components=num_topics, random_state=42)
    W = nmf.fit_transform(X)
    H = nmf.components_
    
    # Get the most significant words for each topic
    topics = []
    for component in H:
        topic_words = [vectorizer.get_feature_names_out()[i] for i in component.argsort()[:-11:-1]]
        topics.append(topic_words)
    
    return topics
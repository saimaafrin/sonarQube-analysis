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
    
    # Apply NMF to extract topics
    nmf = NMF(n_components=num_topics, random_state=42)
    nmf.fit(X)
    
    # Get the feature names (words) from the vectorizer
    feature_names = vectorizer.get_feature_names_out()
    
    # Extract the top words for each topic
    topics = []
    for topic_idx in range(num_topics):
        top_words = [feature_names[i] for i in nmf.components_[topic_idx].argsort()[:-11:-1]]
        topics.append(top_words)
    
    return topics

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
    tfidf_matrix = vectorizer.fit_transform(processed_texts)
    
    # Apply NMF to extract the specified number of topics
    nmf = NMF(n_components=num_topics, random_state=42)
    nmf.fit(tfidf_matrix)
    
    # Extract the most significant words for each topic
    topics = []
    for topic_idx in range(num_topics):
        topic_words = nmf.components_[topic_idx]
        top_words_indices = topic_words.argsort()[:-11:-1]  # Get top 10 words
        top_words = [vectorizer.get_feature_names_out()[i] for i in top_words_indices]
        topics.append(top_words)
    
    return topics
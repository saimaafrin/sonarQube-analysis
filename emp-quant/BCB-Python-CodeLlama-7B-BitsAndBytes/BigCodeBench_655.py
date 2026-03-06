
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
    # Preprocess the input texts
    texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    texts = [word for word in texts if word not in STOPWORDS]

    # Vectorize the processed texts using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Apply NMF to extract the specified number of topics
    nmf = NMF(n_components=num_topics)
    W = nmf.fit_transform(X)

    # Get the most significant words for each topic
    topic_words = []
    for topic_idx in range(num_topics):
        topic_words.append([vectorizer.get_feature_names()[i] for i in W.get_indices()[topic_idx]])

    return topic_words

# Call the function
topic_words = task_func(texts, num_topics)

# Print the topics
print(topic_words)
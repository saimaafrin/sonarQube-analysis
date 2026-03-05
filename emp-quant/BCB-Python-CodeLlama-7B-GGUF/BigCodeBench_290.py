
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(directory_path):
    # Initialize the counter
    word_count = Counter()
    # Iterate over all files in the directory
    for file in os.listdir(directory_path):
        # Open the file and read its contents
        with open(os.path.join(directory_path, file), 'r') as f:
            contents = f.read()
        # Tokenize the contents and remove stopwords
        tokens = nltk.word_tokenize(contents)
        tokens = [word for word in tokens if word.lower() not in STOPWORDS]
        # Increment the counter for each unique word
        word_count.update(tokens)
    # Return the total count of unique non-stop words
    return len(word_count)
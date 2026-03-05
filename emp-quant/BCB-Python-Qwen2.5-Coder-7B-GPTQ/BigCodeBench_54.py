import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer
def task_func(text):
    # Split the text into sentences using regex to handle multiple periods
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence]
    
    # Initialize CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the sentences to create the document-term matrix
    dtm = vectorizer.fit_transform(sentences)
    
    # Convert the document-term matrix to a pandas DataFrame
    df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return df
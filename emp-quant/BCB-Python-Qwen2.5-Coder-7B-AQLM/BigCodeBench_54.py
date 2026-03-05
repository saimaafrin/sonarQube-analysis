
import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Split the text into sentences using regex to handle multiple periods
    sentences = re.split(r'(?<=\.)\s*', text)
    
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]
    
    # Initialize CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the sentences to create the document-term matrix
    dtm = vectorizer.fit_transform(sentences)
    
    # Create a DataFrame from the document-term matrix
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return dtm_df
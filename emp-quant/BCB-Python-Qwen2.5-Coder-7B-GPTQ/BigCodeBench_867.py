import re
import string
def task_func(text1, text2):
    # Define a regular expression pattern to match ASCII punctuation
    pattern = re.compile('[%s]' % re.escape(string.punctuation))
    
    # Remove punctuation from both texts
    cleaned_text1 = pattern.sub('', text1)
    cleaned_text2 = pattern.sub('', text2)
    
    # Return the cleaned texts as a tuple
    return (cleaned_text1, cleaned_text2)
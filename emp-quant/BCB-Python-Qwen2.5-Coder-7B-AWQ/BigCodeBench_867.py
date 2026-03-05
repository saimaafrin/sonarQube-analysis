import re
import string
def task_func(text1, text2):
    # Define a translation table to remove ASCII punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation from both texts
    cleaned_text1 = text1.translate(translator)
    cleaned_text2 = text2.translate(translator)
    
    # Return the cleaned texts as a tuple
    return (cleaned_text1, cleaned_text2)
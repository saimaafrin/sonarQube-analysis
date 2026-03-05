
import re
import string

def task_func(text1, text2):
    # Define a pattern to match ASCII punctuation
    pattern = f"[{re.escape(string.punctuation)}]"
    
    # Remove ASCII punctuation from both texts
    cleaned_text1 = re.sub(pattern, "", text1)
    cleaned_text2 = re.sub(pattern, "", text2)
    
    # Return the cleaned texts as a tuple
    return (cleaned_text1, cleaned_text2)
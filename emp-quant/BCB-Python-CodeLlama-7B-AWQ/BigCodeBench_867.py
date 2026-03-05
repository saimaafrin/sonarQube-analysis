import re
import string
def task_func(text1, text2):
    """
    This function takes two strings, removes any ASCII punctuation using regular expressions, and returns the cleaned strings as a tuple.
    It targets punctuation characters defined in `string.punctuation`, which includes the following characters: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    """
    # Remove punctuation from text1
    cleaned_text1 = re.sub(r'[^\w\s]', '', text1)

    # Remove punctuation from text2
    cleaned_text2 = re.sub(r'[^\w\s]', '', text2)

    return (cleaned_text1, cleaned_text2)
text1 = "test (with parenthesis []!!)"
text2 = "And, other; stuff ^_`"
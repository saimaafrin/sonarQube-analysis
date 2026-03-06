import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
STEMMER = PorterStemmer()
def task_func(content):
    """
    Stem every word in a sentence, except the last, and count the frequency of each stem.

    Parameters:
    content (str): The sentence to stem and count.

    Returns:
    dict: A dictionary with stemmed words as keys and their frequency as values.

    Requirements:
    - re
    - string
    - nltk.stem
    - collections.Counter

    Example:
    >>> task_func('running runner run')
    {'run': 1, 'runner': 1}
    """
    words = re.findall(r'\w+', content)
    words = [STEMMER.stem(word) for word in words]
    words = [word for word in words if word not in string.punctuation]
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word.islower()]
    words = [word for word in words if word != 'i']
    words = [word for word in words if word != 'me']
    words = [word for word in words if word != 'my']
    words = [word for word in words if word != 'myself']
    words = [word for word in words if word != 'we']
    words = [word for word in words if word != 'us']
    words = [word for word in words if word != 'our']
    words = [word for word in words if word != 'ours']
    words = [word for word in words if word != 'ourselves']
    words = [word for word in words if word != 'you']
    words = [word for word in words if word != 'your']
    words = [word for word in words if word != 'yours']
    words = [word for word in words if word != 'yourself']
    words = [word for word in words if word != 'yourselves']
    words = [word for word in words if word != 'he']
    words = [word for word in words if word != 'him']
    words = [word for word in words if word != 'his']
    words = [word for word in words if word != 'himself']
    words = [word for word in words if word != 'she']
    words = [word for word in words if word != 'her']
    words = [word for word in words if word != 'hers']
    words = [word for word in words if word != 'herself']
    words = [word for word in words if word != 'it']
    words = [word for word in words if word != 'its']
    words = [word for word in words if word != 'itself']
    words = [word for word in words if word != 'they']
    words = [word for word in words if word != 'them']
    words = [word for word in words if word != 'their']
    words = [word for word in words if word != 'theirs']
    words = [word for word in words if word != 'themselves']
    words = [word for word in words if word != 'what']
    words = [word for word in words if word != 'which']
    words = [word for word in words if word != 'who']
    words = [word for word in words if word != 'whom']
    words = [word for word in words if word != 'this']
    words = [word for word in words if word != 'that']
    words = [word for word in words if word != 'these']
    words = [word for word in words if word != 'those']
    words = [word for word in words if word != 'am']
    words = [word for word in words if word != 'is']
    words = [word for word in words if word != 'are']
    words = [word for word in words if word != 'was']
    words = [word for word in words if word != 'were']
    words = [word for word in words if word != 'be']
    words = [word for word in words if word != 'been']
    words = [word for word in words if word != 'being']
    words = [word for word in words if word != 'have']
    words = [word for word in words if word != 'has']
    words = [word for word in words if word != 'had']
    words = [word for word in words if word != 'do']
    words = [word for word in words if word != 'does']
    words = [word for word in words if word != 'did']
    words = [word for word in words if word != 'doing']
    words = [word for word in words if word != 'will']
    words = [word for word in words if word != 'would']
    words = [word for word in words if word != 'shall']
    words = [word for word in words if word != 'should']
    words = [word for word in words if word != 'can']
    words = [word for word in words if word != 'could']
    words = [word for word in words if word != 'ought']
    words = [word for word in words if word != 'must']
    words = [word for word in words if word != 'will']
    words = [word for word in words if word != 'would']
    words = [word for word in words if word != 'shall']
    words = [word for word in words if word != 'should']
    words = [word for word in words if word != 'can']
    words = [word for word in words if word != 'could']
    words = [word for word in words if word != 'ought']
    words = [word for word in words if word != 'must']
    words = [word for word in words if word != 'will']
    words = [word for word in words if word != 'would']
    words = [word for word in words if word != 'shall']
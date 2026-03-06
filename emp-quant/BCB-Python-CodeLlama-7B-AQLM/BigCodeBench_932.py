from collections import Counter
import re
def task_func(word: str) -> list:
    """
    Finds the most common two-letter combination in a given, cleaned word (lowercased and alphabetic characters only) 
    and returns its frequency. The search is case-insensitive and ignores non-alphabetic characters.
    
    Requirements:
    - collections.Counter
    - re
    
    Parameters:
    - word (str): The input string containing the word to analyze. The word should have a length of at least 2 to form pairs.
    
    Returns:
    - list: A list containing a single tuple. The tuple consists of the most frequent two-letter combination (str) 
      and its frequency (int). Returns an empty list if the word has fewer than 2 letters, or after cleaning, 
      the word has fewer than 2 alphabetic characters.
    
    Examples:
    >>> task_func("aaBBcc")
    [('aa', 1)]
    >>> task_func("abc!abc")
    [('ab', 2)]
    >>> task_func("a")
    []
    >>> task_func("abcd")
    [('ab', 1)]
    >>> task_func("a1b2c3")
    [('ab', 1)]
    """
    # Clean the word
    word = re.sub(r'[^a-zA-Z]', '', word.lower())
    # If the word has fewer than 2 letters, return an empty list
    if len(word) < 2:
        return []
    # If the word has fewer than 2 alphabetic characters, return an empty list
    if len(re.sub(r'[^a-zA-Z]', '', word)) < 2:
        return []
    # Create a Counter object from the word
    counter = Counter(word)
    # Find the most common two-letter combination
    most_common = counter.most_common(1)
    # Return a list containing a single tuple
    return [most_common[0]]
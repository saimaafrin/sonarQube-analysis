import re
import string
def task_func(content):
    # Define a set of common stop words
    stop_words = set(["the", "and", "is", "in", "of", "that", "it", "to", "with", "for", "on", "at", "as", "by", "from", "this", "that", "which", "where", "when", "how", "why", "who", "what", "or", "but", "not", "all", "any", "one", "some", "no", "not", "up", "down", "left", "right", "in", "out", "on", "off", "over", "under", "for", "with", "without", "about", "above", "below", "around", "behind", "between", "beyond", "during", "inside", "outside", "through", "underneath", "upside-down", "around", "behind", "between", "beyond", "during", "inside", "outside", "through", "underneath", "upside-down"])

    # Remove punctuation from the content
    content = content.translate(str.maketrans('', '', string.punctuation))

    # Split the content into words
    words = content.split()

    # Remove the last word
    words = words[:-1]

    # Count the non-stop words
    count = sum(1 for word in words if word.lower() not in stop_words)

    return count
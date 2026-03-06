
import re
import string

# Define a set of stop words for English
stop_words = {
    "a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "from",
    "by", "about", "as", "like", "into", "with", "without", "up", "down", "in",
    "out", "over", "under", "between", "among", "through", "across", "against",
    "along", "around", "behind", "below", "beneath", "beside", "between", "beyond",
    "during", "except", "inside", "near", "past", "since", "toward", "underneath",
    "upon", "within", "without"
}

def task_func(content):
    # Remove punctuation from the content
    content = re.sub(f"[{string.punctuation}]", "", content)
    
    # Split the content into words
    words = content.split()
    
    # Exclude the last word
    if len(words) > 0:
        words = words[:-1]
    
    # Count non-stop words
    non_stop_word_count = sum(1 for word in words if word.lower() not in stop_words)
    
    return non_stop_word_count
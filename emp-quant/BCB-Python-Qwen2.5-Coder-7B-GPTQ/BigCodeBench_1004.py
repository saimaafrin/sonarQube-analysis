import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt
def task_func(url):
    # Download the text file from the specified URL
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    
    # Use a regular expression to find words and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the ten most common words
    most_common_words = word_counts.most_common(10)
    
    # Extract words and their counts for plotting
    words, counts = zip(*most_common_words)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(words, counts)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Frequent Words')
    
    return word_counts, ax
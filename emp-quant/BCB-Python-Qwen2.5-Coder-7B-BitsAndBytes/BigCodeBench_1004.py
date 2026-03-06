
import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(url):
    # Download the text file from the specified URL
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    
    # Use regex to find words and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Get the ten most common words
    top_words = word_count.most_common(10)
    
    # Prepare data for plotting
    labels, counts = zip(*top_words)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, counts)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')
    
    return word_count, ax

import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(text):
    # Remove URLs from the text
    url_pattern = re.compile(r'http[s]?://\S+|www\.\S+')
    text = re.sub(url_pattern, '', text)
    
    # Check if there are any words left after removing URLs
    words = re.findall(r'\b\w+\b', text)
    if not words:
        raise ValueError("No words available to generate a word cloud after removing URLs.")
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
    # Return the WordCloud object
    return wordcloud
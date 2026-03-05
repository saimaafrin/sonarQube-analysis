
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(text):
    # Remove URLs from text
    text = re.sub(r'http\S+', '', text)
    # Check if there are any words left
    if not text.strip():
        raise ValueError("No words available to generate a word cloud after removing URLs.")
    # Create a word cloud
    wordcloud = WordCloud(width=800, height=400).generate(text)
    # Plot the word cloud
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
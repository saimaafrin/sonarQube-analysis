import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def task_func(text):
    """
    Create a word cloud from text after removing URLs and plot it.
    """
    # Remove URLs from text
    text = re.sub(r"http\S+", "", text)

    # Check if there are any words left
    if not text.split():
        raise ValueError("No words available to generate a word cloud after removing URLs.")

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400).generate(text)

    # Plot word cloud
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
text = "This is a sample text with a URL: https://www.example.com"
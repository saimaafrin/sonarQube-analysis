
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(text):
    # Remove URLs from the text
    text = re.sub(r'http\S+', '', text)

    # Create a word cloud from the remaining text
    wordcloud = WordCloud(width=800, height=500, margin=2, random_state=42).generate(text)

    # Plot the word cloud
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
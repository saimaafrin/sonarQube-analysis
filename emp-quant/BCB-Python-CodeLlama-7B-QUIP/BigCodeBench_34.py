
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(text):
    # Remove URLs from the text
    text = re.sub(r"http\S+", "", text)

    # Create a WordCloud object
    wordcloud = WordCloud(
        font_path="path/to/font/file",
        width=800,
        height=600,
        max_font_size=100,
        background_color="white"
    )

    # Add the text to the WordCloud object
    wordcloud.add_text(text)

    # Generate the word cloud
    wordcloud.generate_word_cloud()

    # Plot the word cloud
    plt.imshow(wordcloud.get_word_cloud())
    plt.show()

    # Check if there are any words available to generate a word cloud
    if not wordcloud.has_words():
        raise ValueError("No words available to generate a word cloud after removing URLs.")

    return wordcloud
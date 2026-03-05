
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    # Get the text of the Wikipedia page
    try:
        page = wikipedia.page(page_title)
        text = page.content
    except wikipedia.PageError:
        return None

    # Create a word cloud
    wordcloud = WordCloud(
        font_family="Comic Sans MS",
        font_size=10,
        max_font_size=30,
        width=1000,
        height=1000,
        background_color="white",
        stop_words=["a", "an", "the", "of", "and", "in", "to", "is", "with", "on", "at", "as", "for", "the", "be", "by", "have", "had", "is", "it", "its", "its", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my", "my",
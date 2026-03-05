import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def task_func(page_title):
    """
    Create a word cloud from the text of a Wikipedia page.

    Args:
        page_title (str): The title of the Wikipedia page to be used as input.

    Returns:
        matplotlib.axes.Axes: The Axes object of the plotted data. Is None if there is no Wikipedia page with the title given as input.
    """
    try:
        page = wikipedia.page(page_title)
        text = page.content
        wordcloud = WordCloud().generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud)
        ax.set_title(f"Word Cloud of {page_title}")
        return ax
    except wikipedia.exceptions.PageError:
        return None
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def task_func(page_title):
    """
    Create a word cloud from the text of a Wikipedia page.

    Parameters:
    page_title (str): The title of the Wikipedia page.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted data. Is None if there is no wikipedia page with the title given as input.

    Requirements:
    - wikipedia
    - wordcloud.WordCloud
    - matplotlib.pyplot

    Example:
    >>> ax = task_func('Python (programming language)')
    """
    try:
        page = wikipedia.page(page_title)
        text = page.content
        wordcloud = WordCloud().generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        return plt.gca()
    except wikipedia.exceptions.PageError:
        return None
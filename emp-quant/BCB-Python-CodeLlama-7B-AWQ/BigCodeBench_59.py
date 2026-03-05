import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def task_func(page_title):
    """
    Create a word cloud from the text of a Wikipedia page.

    Args:
        page_title (str): The title of the Wikipedia page to be analyzed.

    Returns:
        matplotlib.axes.Axes: The Axes object of the plotted data. Is None if there is no Wikipedia page with the title given as input.
    """
    try:
        # Get the text of the Wikipedia page
        page = wikipedia.page(page_title)
        text = page.content

        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, margin=2, random_state=42).generate(text)

        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot the word cloud
        ax.imshow(wordcloud, interpolation='bilinear')

        # Set the title and labels
        ax.set_title(f'Word Cloud of {page_title}')
        ax.set_xlabel('Word')
        ax.set_ylabel('Frequency')

        # Return the Axes object
        return ax
    except wikipedia.exceptions.PageError:
        # If the page does not exist, return None
        return None
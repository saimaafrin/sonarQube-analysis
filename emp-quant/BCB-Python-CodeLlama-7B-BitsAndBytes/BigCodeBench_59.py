
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    # Get the text of the Wikipedia page
    try:
        page = wikipedia.page(page_title)
        text = page.content
    except wikipedia.exceptions.DisambiguationError:
        print("DisambiguationError: More than one page with this title. Please provide a more specific title.")
        return None
    except wikipedia.exceptions.PageError:
        print("PageError: No page with this title found.")
        return None

    # Create a word cloud from the text
    wordcloud = WordCloud(width=800, height=500, margin=2, random_state=42).generate(text)

    # Plot the word cloud
    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.set_title(f"Word Cloud of {page_title}")
    ax.axis("off")

    return ax
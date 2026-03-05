
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    try:
        page = wikipedia.page(page_title)
    except wikipedia.DisambiguationError:
        return None
    text = page.content
    wordcloud = WordCloud().generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.set_title(page_title)
    return ax
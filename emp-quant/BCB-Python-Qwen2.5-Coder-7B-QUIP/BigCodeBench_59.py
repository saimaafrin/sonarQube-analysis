
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    try:
        # Fetch the Wikipedia page content
        page = wikipedia.page(page_title)
        text = page.content
        
        # Create a WordCloud object
        wc = WordCloud(width=800, height=400, background_color='white')
        wordcloud = wc.generate(text)
        
        # Plot the WordCloud
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        
        return ax
    except wikipedia.exceptions.WikipediaError:
        return None
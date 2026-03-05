
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    try:
        # Fetch the Wikipedia page
        page = wikipedia.page(page_title)
        
        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(page.content)
        
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Display the word cloud on the axis
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        
        # Return the Axes object
        return ax
    except wikipedia.exceptions.PageError:
        # Return None if the page does not exist
        return None
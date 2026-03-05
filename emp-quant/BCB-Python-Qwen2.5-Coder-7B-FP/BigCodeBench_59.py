import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def task_func(page_title):
    try:
        # Fetch the Wikipedia page content
        page = wikipedia.page(page_title)
        text = page.content
        
        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Display the word cloud on the axis
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        
        return ax
    except wikipedia.exceptions.PageError:
        # Return None if the Wikipedia page does not exist
        return None
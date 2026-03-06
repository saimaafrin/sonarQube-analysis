
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
        
        # Create a figure and axis to display the word cloud
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')  # Turn off axis for cleaner look
        
        return ax
    
    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found with the title: {page_title}")
        return None
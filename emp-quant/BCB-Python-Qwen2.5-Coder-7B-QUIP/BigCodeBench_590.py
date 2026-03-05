
import urllib.request
from pyquery import PyQuery as pq
from datetime import datetime
import pandas as pd

def task_func(url):
    if not url:
        raise ValueError("Invalid URL")
    
    try:
        # Fetch HTML content from the URL
        with urllib.request.urlopen(url) as response:
            html = response.read()
        
        # Parse the HTML content using PyQuery
        doc = pq(html)
        
        # Extract anchor tags
        anchor_tags = doc('a')
        
        # Extract text and href attributes
        data = []
        for tag in anchor_tags:
            text = tag.text.strip()
            href = tag.get('href', '')
            data.append((text, href))
        
        # Create a DataFrame
        df = pd.DataFrame(data, columns=['text', 'href'])
        
        # Add fetch time column
        df['fetch_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return df
    except urllib.error.URLError as e:
        raise e
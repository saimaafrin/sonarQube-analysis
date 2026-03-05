import urllib.request
from pyquery import PyQuery as pq
from datetime import datetime
import pandas as pd
def task_func(url):
    if not url:
        raise ValueError("URL cannot be empty")
    
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read()
    except urllib.error.URLError as e:
        raise URLError("Failed to fetch URL: " + str(e.reason))
    
    doc = pq(html_content)
    anchor_tags = doc('a')
    
    data = []
    for tag in anchor_tags:
        text = pq(tag).text()
        href = pq(tag).attr('href')
        data.append({'text': text, 'href': href})
    
    fetch_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df = pd.DataFrame(data)
    df['fetch_time'] = fetch_time
    
    return df
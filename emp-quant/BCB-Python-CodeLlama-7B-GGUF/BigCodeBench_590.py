
import urllib.request
from pyquery import PyQuery as pq
from datetime import datetime
import pandas as pd

def task_func(url):
    if not url:
        raise ValueError("Invalid URL")

    try:
        response = urllib.request.urlopen(url)
    except URLError as e:
        raise URLError("Error fetching HTML content: {}".format(e))

    html = response.read()
    doc = pq(html)
    anchors = doc("a")

    data = []
    for anchor in anchors:
        text = anchor.text
        href = anchor.attr("href")
        data.append({"text": text, "href": href})

    df = pd.DataFrame(data)
    df["fetch_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df
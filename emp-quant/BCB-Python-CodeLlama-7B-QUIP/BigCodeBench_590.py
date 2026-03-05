
import urllib.request
from pyquery import PyQuery as pq
from datetime import datetime
import pandas as pd

def task_func(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        doc = pq(html)
        anchors = doc.find("a")
        df = pd.DataFrame(columns=["text", "href", "fetch_time"])
        for anchor in anchors:
            df = df.append({"text": anchor.text, "href": anchor.attr("href"), "fetch_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
                           ignore_index=True)
        return df
    except ValueError:
        raise ValueError("Invalid URL or empty response")
    except URLError:
        raise URLError("Network connectivity or server issue")
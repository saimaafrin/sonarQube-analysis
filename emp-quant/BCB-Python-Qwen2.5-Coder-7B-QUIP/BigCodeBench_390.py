
import pandas as pd
import requests
from io import StringIO

def task_func(csv_url_dict, sort_by_column="title"):
    if not csv_url_dict or "URL" not in csv_url_dict:
        raise ValueError("Invalid input: dictionary is empty or 'URL' key is missing")

    csv_url = csv_url_dict["URL"]
    response = requests.get(csv_url)
    data = StringIO(response.text)
    df = pd.read_csv(data)

    return df.sort_values(by=sort_by_column)
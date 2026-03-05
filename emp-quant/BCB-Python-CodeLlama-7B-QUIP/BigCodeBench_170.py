
import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    # Fetch the data from the given CSV URL
    response = requests.get(csv_url)
    if response.status_code != 200:
        raise Exception("Invalid response status code")
    # Convert the response to a StringIO object
    csv_string = StringIO(response.content.decode("utf-8"))
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_string)
    # Sort the DataFrame based on the specified column
    df = df.sort_values(by=sort_by_column)
    return df
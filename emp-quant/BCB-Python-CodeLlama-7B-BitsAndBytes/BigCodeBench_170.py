
import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    # Fetch data from the given CSV URL
    response = requests.get(csv_url)

    # Check the response status code
    if response.status_code != 200:
        raise Exception("Invalid response status code: {}".format(response.status_code))

    # Convert the response content to a pandas DataFrame
    df = pd.read_csv(StringIO(response.content.decode("utf-8")))

    # Sort the DataFrame based on the specified column
    df = df.sort_values(by=sort_by_column)

    # Return the sorted DataFrame
    return df
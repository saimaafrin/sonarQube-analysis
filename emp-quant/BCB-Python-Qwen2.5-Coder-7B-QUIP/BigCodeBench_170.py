
import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    response = requests.get(csv_url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data. Status code: {}".format(response.status_code))
    
    # Read the CSV data from the response
    csv_data = StringIO(response.text)
    
    # Load the data into a pandas DataFrame
    df = pd.read_csv(csv_data)
    
    # Sort the DataFrame based on the specified column
    df = df.sort_values(by=sort_by_column)
    
    # Return the sorted DataFrame
    return df
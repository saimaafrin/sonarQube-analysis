import pandas as pd
import requests
from io import StringIO
def task_func(csv_url, sort_by_column="title"):
    # Send a GET request to the CSV URL
    response = requests.get(csv_url)
    
    # Check if the response status code is 200
    if response.status_code != 200:
        raise Exception("Failed to fetch data. Status code: {}".format(response.status_code))
    
    # Read the CSV data from the response content
    csv_data = StringIO(response.content.decode('utf-8'))
    
    # Create a pandas DataFrame from the CSV data
    df = pd.read_csv(csv_data)
    
    # Sort the DataFrame based on the specified column
    df_sorted = df.sort_values(by=sort_by_column)
    
    return df_sorted
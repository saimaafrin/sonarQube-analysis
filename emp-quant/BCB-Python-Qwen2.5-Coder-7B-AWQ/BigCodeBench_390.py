import pandas as pd
import requests
from io import StringIO
def task_func(csv_url_dict, sort_by_column="title"):
    # Check if the dictionary is empty
    if not csv_url_dict:
        raise ValueError("The dictionary is empty.")
    
    # Check if the key "URL" exists in the dictionary
    if "URL" not in csv_url_dict:
        raise ValueError("The key 'URL' does not exist in the dictionary.")
    
    # Fetch the CSV data from the URL
    csv_url = csv_url_dict["URL"]
    response = requests.get(csv_url)
    csv_data = response.text
    
    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(StringIO(csv_data))
    
    # Sort the DataFrame based on the specified column
    df_sorted = df.sort_values(by=sort_by_column)
    
    return df_sorted
csv_url_dict = {"URL": "http://example.com/test.csv"}
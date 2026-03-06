
import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    try:
        response = requests.get(csv_url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
        
        # Read the CSV data into a pandas DataFrame
        df = pd.read_csv(StringIO(response.text))
        
        # Sort the DataFrame by the specified column
        sorted_df = df.sort_values(by=sort_by_column)
        
        return sorted_df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
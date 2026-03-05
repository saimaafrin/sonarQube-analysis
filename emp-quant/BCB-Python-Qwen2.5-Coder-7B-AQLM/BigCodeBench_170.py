
import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    try:
        response = requests.get(csv_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Read the CSV data from the response
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        # Sort the DataFrame by the specified column
        sorted_df = df.sort_values(by=sort_by_column)

        return sorted_df

    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP error occurred: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
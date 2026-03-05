
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
HEADERS = {
    'accept': 'application/json'
}

def task_func(url, parameters):
    try:
        response = requests.get(url, headers=HEADERS, params=parameters)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        data = response.json()

        # Convert the data to a pandas DataFrame
        df = pd.DataFrame(data)

        # Check if the DataFrame is empty
        if df.empty:
            raise ValueError("Empty data")

        # Calculate the correlation matrix
        correlation_matrix = df.corr()

        # Draw the heatmap
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

        # Display the heatmap
        plt.show()

        return df, heatmap

    except requests.exceptions.RequestException as e:
        raise Exception(f"URL cannot be accessed: {e}")
    except (ValueError, json.JSONDecodeError) as e:
        raise Exception(f"Invalid data: {e}")
    except Exception as e:
        raise Exception(f"General error: {e}")
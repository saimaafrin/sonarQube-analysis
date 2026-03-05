
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
        # Validate URL
        if not url:
            raise Exception("URL is invalid or empty")
        
        # Make the API request
        response = requests.get(url, headers=HEADERS, params=parameters)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Parse the JSON data
        data = response.json()
        
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Check if DataFrame is empty
        if df.empty:
            raise Exception("Empty data received from the API")
        
        # Check if DataFrame contains only non-numeric data
        if not df.select_dtypes(include=[np.number]).columns.any():
            raise Exception("Invalid data: No numeric columns found")
        
        # Draw a heatmap to show the correlation between numerical characteristics
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()
        
        return df, heatmap
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"URL cannot be accessed: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
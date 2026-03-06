
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
        # Send GET request to the API endpoint
        response = requests.get(url, headers=HEADERS, params=parameters)
        
        # Check if the URL is valid and accessible
        if response.status_code != 200:
            raise Exception(f"URL cannot be accessed. Status code: {response.status_code}")
        
        # Convert the response content to JSON
        data = response.json()
        
        # Check if the data is empty
        if not data:
            raise Exception("Empty data received.")
        
        # Convert the JSON data to a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Check if the DataFrame contains only numerical columns
        if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
            raise Exception("Invalid data. DataFrame does not contain only numerical characteristics.")
        
        # Draw a heatmap to show the correlation between numerical characteristics
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        
        # Display the heatmap
        plt.show()
        
        # Return the DataFrame and the Axes object of the heatmap
        return df, heatmap
        
    except Exception as e:
        raise Exception(f"This function will raise an Exception: {e}")
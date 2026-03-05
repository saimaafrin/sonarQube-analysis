import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
HEADERS = {
    'accept': 'application/json'
}
def task_func(url, parameters):
    """
    Retrieve data from a specific API endpoint with the provided parameters, convert the data into a pandas dataframe,
    and draw a heatmap to show the correlation between numerical characteristics.
    
    Parameters:
    url (str): The API endpoint URL.
    parameters (dict): The parameters to be sent with the request.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The pandas DataFrame containing the data.
        Axes: The matplotlib Axes object of the heatmap.
    """
    try:
        # Validate URL
        if not url:
            raise Exception("Invalid URL")
        
        # Send GET request
        response = requests.get(url, headers=HEADERS, params=parameters)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON data
        data = response.json()
        
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Check if DataFrame is empty
        if df.empty:
            raise Exception("Empty data")
        
        # Check if DataFrame contains only numerical data
        if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
            raise Exception("Invalid data")
        
        # Draw heatmap
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        
        # Return DataFrame and Axes
        return df, heatmap
        
    except Exception as e:
        raise Exception(f"Error: {e}")
url = "https://api.example.com/data"
parameters = {"key": "value"}
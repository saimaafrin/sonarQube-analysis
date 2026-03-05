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
    
    Args:
    url (str): The API endpoint URL.
    parameters (dict): The parameters to be sent with the request.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The pandas DataFrame containing the data.
        Axes: The matplotlib Axes object of the heatmap.
    
    Raises:
    Exception: If the url is invalid, empty data, invalid data, or url cannot be accessed.
    """
    # Validate URL
    if not url:
        raise Exception("Invalid URL")
    
    try:
        # Send GET request
        response = requests.get(url, headers=HEADERS, params=parameters)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        raise Exception(f"URL cannot be accessed: {e}")
    
    # Parse JSON response
    try:
        data = response.json()
    except json.JSONDecodeError:
        raise Exception("Invalid data")
    
    # Convert data to DataFrame
    try:
        df = pd.DataFrame(data)
    except ValueError:
        raise Exception("Empty data")
    
    # Draw heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()
    
    return df, heatmap
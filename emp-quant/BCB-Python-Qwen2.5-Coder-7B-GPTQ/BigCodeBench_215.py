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
    url (str): The URL of the API endpoint.
    parameters (dict): The parameters to be sent with the request.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: The pandas DataFrame containing the data.
        Axes: The matplotlib Axes object of the heatmap.
    
    Raises:
    Exception: If the URL is invalid, empty data, invalid data, or the URL cannot be accessed.
    """
    try:
        # Send a GET request to the API endpoint
        response = requests.get(url, headers=HEADERS, params=parameters)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Convert the data into a pandas DataFrame
        df = pd.DataFrame(data)

        # Check if the DataFrame is empty
        if df.empty:
            raise Exception("Empty data")

        # Calculate the correlation matrix
        correlation_matrix = df.corr()

        # Draw a heatmap to show the correlation between numerical characteristics
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap')

        # Return the DataFrame and the Axes object of the heatmap
        return df, heatmap

    except requests.exceptions.RequestException as e:
        raise Exception(f"URL cannot be accessed: {e}")
    except json.JSONDecodeError:
        raise Exception("Invalid data")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
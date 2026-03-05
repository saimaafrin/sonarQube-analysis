
import requests
import json
import pandas as pd
import seaborn as sns
# Constants
HEADERS = {
    'accept': 'application/json'
}
def task_func(url, parameters):
    # Check if the URL is valid
    if not url:
        raise Exception('Invalid URL')
    # Send a GET request to the API endpoint
    response = requests.get(url, headers=HEADERS)
    # Check if the response is valid
    if response.status_code != 200:
        raise Exception('Invalid response')
    # Convert the JSON data to a pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)
    # Check if the data is valid
    if not df.empty:
        raise Exception('Invalid data')
    # Create a heatmap of the correlation between numerical characteristics
    sns.heatmap(df.corr())
    # Return the DataFrame and the Axes object
    return df, sns.heatmap(df.corr())
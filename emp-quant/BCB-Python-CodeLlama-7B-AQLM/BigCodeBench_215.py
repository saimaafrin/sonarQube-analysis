import requests
import json
import pandas as pd
import seaborn as sns
HEADERS = {
    'accept': 'application/json'
}
def task_func(url, parameters):
    """
    Retrieve data from a specific API endpoint with the provided parameters, 
    convert the data into a pandas dataframe, and draw a heatmap to show 
    the correlation between numerical characteristics. The heatmap is 
    displayed and also returned for further use or testing.

    Parameters:
    url (str): The API endpoint URL.
    parameters (dict): The parameters to be sent with the GET request.

    Returns:
    tuple: A tuple containing:
        - DataFrame: The pandas DataFrame containing the data.
        - Axes: The matplotlib Axes object of the heatmap.

    Raises:
    - This function will raise a general Expection if the url is invalid, empty data, invalid data, and url cannot be accessed.

    Requirements:
    - requests
    - json
    - pandas
    - seaborn

    Example:
    >>> df, ax = task_func('https://api.example.com/data', {'param1': 'value1'})
    >>> df.iloc[0]['data']
    1
    """
    # Check if the url is valid
    if not url:
        raise Exception('Invalid url')

    # Send the GET request
    response = requests.get(url, headers=HEADERS, params=parameters)

    # Check if the response is valid
    if not response.ok:
        raise Exception('Invalid response')

    # Convert the response into a DataFrame
    df = pd.DataFrame(response.json())

    # Check if the DataFrame is valid
    if not df.empty:
        raise Exception('Invalid data')

    # Draw the heatmap
    ax = sns.heatmap(df.corr())

    # Return the DataFrame and the Axes
    return df, ax
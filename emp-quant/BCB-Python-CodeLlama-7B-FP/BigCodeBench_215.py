import requests
import json
import pandas as pd
import seaborn as sns
HEADERS = {
    'accept': 'application/json'
}
def task_func(url, parameters):
    """
    Retrieve data from a specific API endpoint with the provided parameters, convert the data into a pandas dataframe, and draw a heatmap to show the correlation between numerical characteristics.
    The heatmap is displayed and also returned for further use or testing.
    The function should raise the exception for:
        - This function will raise a general Expection if the url is invalid, empty data, invalid data, and url cannot be accessed.
    The function should output with:
        - tuple: A tuple containing:
            - DataFrame: The pandas DataFrame containing the data.
            - Axes: The matplotlib Axes object of the heatmap.
    """
    # Check if the url is valid
    if not url:
        raise Exception('Invalid URL')
    # Retrieve data from the API endpoint
    response = requests.get(url, headers=HEADERS, params=parameters)
    # Check if the response is valid
    if not response.ok:
        raise Exception('Invalid response')
    # Convert the response data into a pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)
    # Check if the data is valid
    if not df.empty:
        raise Exception('Invalid data')
    # Draw a heatmap to show the correlation between numerical characteristics
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    # Display the heatmap
    plt.show()
    # Return the heatmap and the DataFrame
    return (df, ax)
url = 'https://api.example.com/data'
parameters = {'param1': 'value1', 'param2': 'value2'}